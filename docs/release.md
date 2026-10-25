# XTermPro Release 包发布操作

本仓库用于分发已构建的 Windows/macOS 安装包。`scripts/release.py` 负责整理附件、校验、上传草稿、正式发布及发布后验证；源码编译、签名和公证在产品源码工程中完成。

## 1. 环境与发布前准备

- Python 3.8+、GitHub CLI `gh`、`curl`，macOS/Linux 终端；Windows 可在 WSL 中运行。
- 执行 `gh auth login --hostname github.com`，使用对 `jackm1688/xtermpro` 有 Release 写权限的账号；不要在脚本内写 Token。
- 查看 `git status --short`、`git remote -v`，核对仓库及本次发布版本；保留已有未提交文件。
- 在对应系统上验证安装、启动、升级和关键功能。macOS 核对 DMG 内应用版本、CPU 架构、签名及公证结果；Windows 核对安装版和便携版版本、签名及启动结果。脚本只检查文件结构和传输一致性，不能替代这些验收。
- 手动更新 README 下载链接和 CHANGELOG；将本次要发布的说明写入单独 UTF-8 文件。不要未经筛选将全部历史日志作为本次说明。

目录需包含以下文件（以 `3.2.18` 为例）：

```text
xtermpro-3.2.18-arm64.dmg
xtermpro-3.2.18-amd64.dmg
xtermpro-3.2.18-windows-x64-installer.zip
xtermpro-3.2.18-windows-x64.zip
xtermpro-user-manual.html
S3配置指南.html
S3配置指南.docx
```

四个包必须同一版本；脚本校验命名、ZIP CRC、DMG UDIF 尾标和 LFS 指针，但不读取包内应用版本。若 Git checkout 只得到 LFS 指针，先执行 `git lfs pull` 获取实体文件。

## 2. 整理发布目录（仅本地）

以下命令均从本仓库根目录运行，示例说明文件 `/tmp/xtermpro-3.2.18-notes.md` 需先自行编写。

```bash
python3 scripts/release.py prepare --version 3.2.18 \
  --source . --bundle ../release-v3.2.18 \
  --notes /tmp/xtermpro-3.2.18-notes.md
```

需额外预留约 2 GB 空间。输出目录必须不存在，失败不会覆盖源包。脚本复制四个包及三份文档，生成四个包的 `SHA256SUMS`、全部八个附件的 `manifest.json` 和本地 `release-notes.md`。S3 文档上传名固定为 `S3.html`、`S3.docx`，避免重复副本混入。

`manifest.json` 和 `release-notes.md` 仅用于本地流程，不作为 Release 附件。保存整个发布目录用于后续复核，不要手工修改其中的附件或清单。仓库根目录原有 `SHA256SUMS` 不会被改写。

## 3. 确定发布提交

README、CHANGELOG、脚本与文档确认后，按本次实际路径提交并推送。安装包可直接通过 Release 上传，无需为上传而提交大文件。不要使用 `git add .` 混入其他工作。

```bash
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

核对目标提交已在远端，记录完整 40 位 SHA；下一步用它替换 `FULL_COMMIT_SHA`。脚本不会自动提交、推送、删除旧版本或移动已有 tag。

## 4. 创建草稿并上传

此步骤会写入 GitHub，但保持 Release 为草稿。

```bash
python3 scripts/release.py draft --version 3.2.18 \
  --bundle ../release-v3.2.18 --target FULL_COMMIT_SHA
```

脚本核对远端提交、已有 tag 及草稿目标，逐个上传缺失附件，核对八个附件的大小、SHA-256、上传状态及说明内容。上传中断后可用相同命令重试；已匹配附件自动跳过。已有公开 Release、同名但内容不同的附件、额外附件均会报错，不自动覆盖。

若提示附件摘要不可用或不一致，停止发布，检查 GitHub API、上传状态及本地文件；不要绕过校验。若上传留下 `starter` 附件，先在 GitHub 草稿页核实并删除该失败附件，再重试。说明不一致时在草稿页修正为本地说明后重试。草稿 target 不一致时需人工核实处理。

打开 GitHub Releases 页面检查草稿说明和八个附件。`verify` 可独立重复运行：

```bash
python3 scripts/release.py verify --version 3.2.18 --bundle ../release-v3.2.18
```

## 5. 正式发布

下面命令会将草稿公开，设为正式版本及 Latest。确认内容和平台验收完成后再执行。

```bash
python3 scripts/release.py publish --version 3.2.18 --bundle ../release-v3.2.18
```

发布前重新校验附件与说明；发布后检查公开状态、非 prerelease、Latest 及每个附件 URL 的 HTTP 可达性。网络失败时命令返回非零，但 Release 可能已经公开；先执行 `verify` 确认现状，勿盲目删除重建。

公开后复核：

```bash
python3 scripts/release.py verify --version 3.2.18 --bundle ../release-v3.2.18
```

成功标准为八个附件齐全、远端 API 摘要及大小与本地一致、说明一致、公开正式版本、Latest 和下载链接可达。HEAD 请求只验证链接可访问；如需完整下载证据，应下载到独立目录，再运行 `shasum -a 256 -c SHA256SUMS`（Linux 可用 `sha256sum -c SHA256SUMS`）。最后在对应操作系统安装下载后的包，记录结果。

## 6. 故障及回退

- 登录或权限失败：检查 `gh auth status`，修复账号权限后重试。
- 文件缺失、LFS 指针、ZIP 损坏、DMG 尾标异常：回到构建产物来源修复，重新生成新的发布目录。
- 本地清单校验失败：文件已变更，重新准备目录并人工核对变更，不要手改摘要。
- 公开版本内容出错：停止推广并人工决定撤回或发布修复版本；脚本不删除 Release/tag，也不使用 `--clobber`。
- 已发布版本再次执行 `draft` 会拒绝操作；`publish` 可重新执行验证并设为 Latest，历史版本仅复核时应使用 `verify`。

参考：[gh release create](https://cli.github.com/manual/gh_release_create)、[upload](https://cli.github.com/manual/gh_release_upload)、[edit](https://cli.github.com/manual/gh_release_edit)。
