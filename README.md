# XTermPro

> 一站式跨平台桌面运维工作台
>
> One cross-platform desktop workspace for everyday operations

[简体中文](#简体中文) · [English](#english)

## 简体中文

### 产品简介

XTermPro 面向开发者、系统管理员和平台工程师，将远程连接、终端操作、文件传输、笔记、脚本与网络诊断集中到一个多标签桌面工作区。产品支持 Windows、macOS 与 Linux；本目录提供 Windows 和 macOS 的 **3.2.18** 运行包。

### 下载与版本

选择与操作系统和 CPU 架构匹配的安装包：

| 平台 | 安装包 | 使用方式 |
| --- | --- | --- |
| Windows x64 | [3.2.18 安装版](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-windows-x64-installer.zip) | 解压后运行安装程序 |
| Windows x64 | [3.2.18 便携版](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-windows-x64.zip) | 完整解压后启动 |
| macOS Apple Silicon | [3.2.18 arm64](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-arm64.dmg) | 打开 DMG，拖入应用程序目录 |
| macOS Intel | [3.2.18 amd64](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-amd64.dmg) | 打开 DMG，拖入应用程序目录 |

Linux 运行包未包含在本目录中，请通过产品发布方获取。升级前请关闭应用并备份重要配置；安装包的存在不代表所有平台和功能均已完成验收。

### 功能概览

- **连接与工作区**：SSH 密码、私钥与托管凭据，跳板与隧道，会话树搜索、多标签、分屏和重连；提供本地终端、Serial 串口与 Windows Named Pipe 连接。
- **文件传输**：SFTP 双栏浏览、上传下载和命令模式；X/Y/ZMODEM 终端文件传输，具体支持以当前平台和连接类型为准。
- **S3 对象存储**：连接配置、对象浏览、上传下载及目录同步；支持已有 INI 配置导入和 SSH 路由。AWS S3、腾讯云 COS、阿里云 OSS 等服务的参数和兼容边界见配置指南。
- **笔记与文件编辑**：笔记自动保存、分组、回收站、导入导出与存储位置管理；文本编辑、内容补全、Markdown 预览及显式运行的 HTML / JavaScript 预览。
- **运维工具**：脚本库、多目标命令、终端文本记录、录像与截图、会话日志、网络计算、网络监控和运行资源查看。
- **Kubernetes / Cilium**：集群连接与凭据管理、资源浏览、日志、Exec、端口转发、监控和巡检报告；实际能力取决于集群组件与 RBAC 权限。
- **外观与设置**：中文与英文、主题与终端背景、快捷键、凭据与密钥管理、命令拦截、配置备份与恢复。
- **可选能力**：AI 助手、Agent / iChat 与云同步依赖对应服务、账号和配置。RDP 当前仍为开发测试能力。

### 使用文档

| 文档 | 内容 |
| --- | --- |
| [图文用户手册（HTML）](xtermpro-user-manual.html) | 安装、连接、终端、文件、笔记、Kubernetes、设置与故障排查，可下载后离线打开 |
| [S3 配置指南（HTML）](S3配置指南.html) | 云服务参数、连接配置、SSH 路由、同步预览与传输验证 |
| [S3 配置指南（Word）](S3配置指南.docx) | 可下载的 Word 版本 |
| [用户手册（PDF）](XTermPro用户手册.pdf) · [Word](XTermPro用户手册.docx) | 较早版本的补充资料，界面与功能以当前运行包为准 |

图文用户手册的更新记录截至 2026-09-28，未覆盖 3.2.18 的全部变更；S3 功能请结合专项指南使用。HTML 文档建议下载后用浏览器打开。

### 工作区布局

- **左侧**：会话树、目录、搜索及笔记空间。
- **中间**：终端、文件传输、编辑器与工具标签。
- **右侧**：按需启用的 AI 与协作区域。
- **底部**：当前连接、路径、网络出口和代理等状态。

### 安装与启动

#### Windows 安装

1. 安装版：运行安装程序并按向导完成安装。
2. 便携版：将 ZIP 完整解压到可写目录，不要直接在压缩包内运行。
3. 启动 XTermPro，并在首次连接前完成必要的语言、外观和安全设置。

#### macOS 安装

1. 打开与当前 Mac 架构匹配的 DMG。
2. 将 XTermPro 拖入 `Applications`。
3. 从“应用程序”启动。若系统阻止启动，请先核对安装包来源和签名，不要在来源不明时绕过系统安全检查。

#### Linux 安装

按照发布方针对目标发行版提供的说明安装或解压运行包。桌面环境、系统库及权限要求可能因发行版而异。

### 快速开始

1. 启动 XTermPro，在左侧会话区域创建目录或连接。
2. 新建 SSH 连接，填写目标主机、端口、用户名和认证方式。
3. 首次连接时核对目标地址及主机指纹。
4. 连接成功后，可在同一工作区打开终端、SFTP、文件或运维工具。
5. 关闭程序前确认文件传输、脚本执行和远程任务已经完成。

### 使用与安全建议

- 不要把密码、私钥、Token 或云密钥写入脚本、截图、日志和公开文档。
- 批量发送命令或执行脚本前，逐项核对目标会话和命令内容。
- 导入配置或恢复备份前，先预览变更并保留现有配置副本。
- RDP、集群写操作、代理转发和云同步应先在测试环境验证。
- 不要使用来源不明、签名异常或校验值不一致的运行包。
- 升级前关闭活动连接并备份重要配置；不要直接覆盖仍在运行的旧版本文件。

### 功能边界

- 功能可用性可能因平台、运行包版本、授权状态、服务端部署和账号权限而不同。
- RDP 当前属于开发测试能力，不应在未验证的关键业务场景中替代专业远程桌面方案。
- Kubernetes、Cilium、AI、Agent、iChat、录屏和云同步需要相应环境、权限或外部服务。
- 实际功能、限制和错误提示以当前运行包中的界面为准。

### 支持与问题反馈

反馈问题时，请提供 XTermPro 版本、操作系统、CPU 架构、复现步骤和已脱敏的错误信息。请勿提交密码、私钥、Token、完整认证头、云密钥或包含敏感信息的配置文件。

请通过产品发布方提供的支持渠道获取更新、授权和技术支持。

### 版权与授权

XTermPro 是专有软件，不是开源项目。本发布内容仅包含产品说明和可执行运行包，不提供源代码。

软件的安装、使用、复制和分发受随运行包提供的授权协议约束。除非获得版权所有者明确书面许可或适用法律允许，不得擅自复制、转售、再分发、修改、反向工程或将运行包用于未授权用途。

XTermPro 使用的第三方组件分别受其自身许可证约束；第三方组件许可证不改变 XTermPro 产品及运行包的专有属性。

---

## English

### Overview

XTermPro brings remote connections, terminals, file transfers, notes, scripts, and network diagnostics into one tabbed desktop workspace for developers, system administrators, and platform engineers. The product supports Windows, macOS, and Linux. This directory contains **3.2.18** packages for Windows and macOS.

### Downloads

| Platform | Package | Usage |
| --- | --- | --- |
| Windows x64 | [3.2.18 installer](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-windows-x64-installer.zip) | Extract and run the installer |
| Windows x64 | [3.2.18 portable](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-windows-x64.zip) | Extract the entire archive before launching |
| macOS Apple Silicon | [3.2.18 arm64](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-arm64.dmg) | Open the DMG and drag the app into Applications |
| macOS Intel | [3.2.18 amd64](https://github.com/jackm1688/xtermpro/releases/download/v3.2.18/xtermpro-3.2.18-amd64.dmg) | Open the DMG and drag the app into Applications |

Linux packages are available separately from the publisher. Close the app and back up important configuration before upgrading. Package availability does not establish complete platform or feature acceptance.

### Key features

- **Connections and workspace:** SSH password, key and managed-credential authentication, jump hosts, tunnels, searchable sessions, tabs, split panes and reconnect; local terminals, Serial and Windows Named Pipe connections.
- **File transfers:** dual-pane SFTP browsing, uploads, downloads and command mode; X/Y/ZMODEM transfers subject to platform and connection support.
- **S3 object storage:** connection setup, object browsing, uploads, downloads and directory synchronization, with INI configuration import and SSH routing. See the dedicated guide for AWS S3, Tencent COS, Alibaba OSS and compatibility boundaries.
- **Notes and editing:** autosave, groups, trash, import/export and storage settings; text editing, content completion, Markdown preview, and explicitly executed HTML / JavaScript previews.
- **Operations tools:** scripts, multiple command targets, terminal text recording, video recording, screenshots, session logs, network calculations, network monitoring and process/resource views.
- **Kubernetes / Cilium:** managed connections and credentials, resource browsing, logs, Exec, port forwarding, monitoring and inspection reports. Availability depends on cluster components and RBAC.
- **Appearance and settings:** Chinese and English, themes and terminal backgrounds, shortcuts, credentials and keys, command interception, configuration backup and restore.
- **Optional capabilities:** AI, Agent / iChat and cloud sync require the corresponding services, accounts and configuration. RDP remains a development-preview capability.

### Documentation

The following documents are in Chinese. Download HTML files and open them in a browser for offline reading.

| Document | Contents |
| --- | --- |
| [Illustrated user manual (HTML)](xtermpro-user-manual.html) | Installation, connections, terminals, files, notes, Kubernetes, settings and troubleshooting |
| [S3 configuration guide (HTML)](S3配置指南.html) | Provider settings, connection setup, SSH routing, sync preview and transfer verification |
| [S3 configuration guide (Word)](S3配置指南.docx) | Downloadable Word edition |
| [Earlier user manual (PDF)](XTermPro用户手册.pdf) · [Word](XTermPro用户手册.docx) | Supplementary older documentation; the installed package determines current behavior |

The illustrated manual's change history ends on September 28, 2026 and does not cover every 3.2.18 change. Refer to the dedicated S3 guide for object storage.

### Workspace layout

- **Left:** saved sessions, folders, search and note spaces.
- **Center:** terminals, file transfers, editors and tools in tabs.
- **Right:** optional AI and collaboration area.
- **Bottom:** connection, path, network outlet and proxy status.

### Install and launch

#### Install on Windows

1. Installer: run the installer and follow the setup wizard.
2. Portable package: extract the entire ZIP to a writable directory. Do not run it from inside the archive.
3. Start XTermPro and review the language, appearance, and security settings before the first connection.

#### Install on macOS

1. Open the DMG matching the Mac architecture.
2. Drag XTermPro into `Applications`.
3. Launch it from Applications. If macOS blocks the application, verify the package source and signature before changing any system security setting.

#### Install on Linux

Install or extract the runtime package according to the instructions supplied for the target distribution. Desktop-environment, system-library, and permission requirements may vary.

### Quick start

1. Start XTermPro and create a folder or connection in the session area.
2. Create an SSH connection and enter the target host, port, user name, and authentication method.
3. Verify the target address and host fingerprint on the first connection.
4. After connecting, open terminal, SFTP, file, and operations tools in the same workspace.
5. Before exiting, confirm that transfers, scripts, and remote tasks have completed.

### Safe usage

- Never place passwords, private keys, tokens, or cloud secrets in scripts, screenshots, logs, or public documentation.
- Review every target session and command before batch dispatch or script execution.
- Preview changes and preserve the current configuration before importing or restoring a backup.
- Validate RDP, cluster write operations, proxy forwarding, and cloud sync in a test environment first.
- Do not use packages from unknown sources or packages with invalid signatures or mismatched checksums.
- Close active connections and back up important configuration before upgrading. Do not overwrite files belonging to a running version.

### Feature boundaries

- Feature availability may vary by platform, package version, activation state, server deployment, and account permissions.
- RDP is currently a development-preview capability and should not replace a dedicated remote-desktop solution in unverified critical workflows.
- Kubernetes, Cilium, AI, Agent, iChat, recording, and cloud sync require the corresponding environment, permissions, or external services.
- The interface, limitations, and error messages in the installed package are authoritative for that release.

### Support and issue reports

When reporting an issue, include the XTermPro version, operating system, CPU architecture, reproduction steps, and redacted error details. Never submit passwords, private keys, tokens, full authorization headers, cloud secrets, or configuration files containing sensitive data.

Use the support channel provided by the product publisher for updates, licensing, and technical assistance.

### Copyright and licensing

XTermPro is proprietary software and is not an open-source project. This release contains product documentation and executable runtime packages only; source code is not provided.

Installation, use, copying, and distribution are governed by the license agreement supplied with the runtime package. Unless expressly authorized in writing by the copyright owner or permitted by applicable law, you may not copy, resell, redistribute, modify, reverse engineer, or use the package for an unauthorized purpose.

Third-party components used by XTermPro remain subject to their respective licenses. Those licenses do not change the proprietary status of the XTermPro product or runtime package.
