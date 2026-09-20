# XTermPro

> 一站式跨平台桌面运维工作台
>
> One cross-platform desktop workspace for everyday operations

[简体中文](#简体中文) · [English](#english)

---

## 简体中文

### 产品简介

XTermPro 是一款面向开发者、系统管理员和平台工程师的跨平台桌面运维工作台，支持 Windows、macOS 与 Linux。它将远程连接、终端操作、文件传输、脚本复用、网络诊断和运行监控集中到一个多标签工作区，帮助用户减少工具切换并统一日常运维流程。

XTermPro 不只是终端模拟器。它以会话树管理连接，以标签和分屏承载任务，并提供 SSH、SFTP、本地终端、文件编辑、RDP 预览以及可选的 Kubernetes、AI 和协作能力。

### 核心功能

#### 连接与工作区

- SSH2 远程终端，支持密码、托管凭据、私钥和跳板代理
- 可搜索的会话树、多标签工作区和 SSH 分屏
- 清晰的连接、失败、断开与原标签重连状态
- 本地终端、最近文件和文本文件编辑
- 浅色、深色与高对比度主题
- 简体中文、英文及自动语言选择

#### SFTP 文件操作

- 图形化本地/远端双栏文件浏览器
- `sftp>` 命令模式，支持目录浏览、上传、下载和文件维护
- 异步传输、进度显示与取消操作

部分“代理 + SFTP”组合当前有意保持禁用。请以客户端界面显示的可用入口和提示为准。

#### 运维效率工具

- 脚本库：保存、分类、搜索、预览和发送常用脚本
- IPv4、IPv6、CIDR、聚合与扣减计算
- 系统网卡与活动会话网络监控
- 进程与运行资源查看
- 命令拦截规则与会话操作日志
- 凭据、SSH 私钥、云访问密钥和网络出口管理
- 终端录屏、快捷键指南及工具站点管理
- 本地配置导出、预览、恢复及存储位置管理

#### 可选与预览能力

- **RDP 远程桌面：** 支持直接连接和 SSH 隧道场景，当前仍属于开发测试能力
- **Kubernetes / Cilium：** 实际能力取决于运行包版本、集群组件和 RBAC 权限
- **AI 助手：** 需要用户自行配置兼容的模型服务及访问凭据
- **Agent / iChat：** 取决于运行包版本、服务端部署、账号权限和功能开关
- **终端录制与云同步：** 取决于运行包是否包含相应组件及服务配置

### 工作区布局

- **左侧：** 保存的会话、目录、搜索结果和当前连接
- **中间：** SSH、本地终端、SFTP、RDP、文件和工具标签
- **右侧：** 可显示或隐藏的 AI / 协作辅助区域
- **底部：** 当前目标、会话路径、连接状态、网络出口和代理信息

### 运行包选择

请只从产品发布方提供的渠道获取 XTermPro，并根据操作系统和 CPU 架构选择运行包：

- **Windows：** 安装程序或 portable ZIP
- **macOS：** Apple Silicon (`arm64`) 或 Intel (`amd64`) DMG
- **Linux：** 与目标发行版及系统架构匹配的运行包

安装前请核对文件名、产品版本、操作系统、CPU 架构和发布来源。如发布方同时提供 SHA-256 校验值，请在运行安装包前完成完整性校验。

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

XTermPro is a cross-platform desktop operations workspace for developers, system administrators, and platform engineers. Available for Windows, macOS, and Linux, it brings remote connections, terminal operations, file transfer, reusable scripts, network diagnostics, and runtime monitoring into one tabbed application.

XTermPro is more than a terminal emulator. It organizes connections in a session tree, runs tasks in tabs and split panes, and combines SSH, SFTP, local terminals, file editing, an RDP preview, and optional Kubernetes, AI, and collaboration capabilities.

### Key features

#### Connections and workspace

- SSH2 terminal sessions with password, managed-credential, private-key, and jump-host options
- Searchable session tree, tabbed workspace, and split SSH views
- Clear connecting, failure, disconnected, and in-place reconnect states
- Local terminals, recent files, and text-file editing
- Light, dark, and high-contrast themes
- Simplified Chinese, English, and automatic language selection

#### SFTP file operations

- Graphical two-pane local and remote file browser
- Local `sftp>` command mode for navigation, upload, download, and file operations
- Asynchronous transfers with progress and cancellation

Some proxy-plus-SFTP combinations are intentionally disabled. Follow the availability and guidance shown by the client.

#### Operations toolkit

- Script library for storing, categorizing, searching, reviewing, and sending common scripts
- IPv4, IPv6, CIDR, aggregation, and subtraction calculator
- System-interface and active-session network monitoring
- Process and runtime-resource inspection
- Command interception rules and session operation logs
- Credential, SSH key, cloud access-key, and network-outlet management
- Terminal recording, shortcut guide, and tool-site manager
- Local configuration export, preview, restore, and storage-location management

#### Optional and preview capabilities

- **RDP remote desktop:** direct and SSH-tunnel scenarios; currently a development-preview capability
- **Kubernetes / Cilium:** availability depends on the package version, cluster components, and RBAC permissions
- **AI assistant:** requires a compatible model service and user-supplied credentials
- **Agent / iChat:** depends on the package version, server deployment, account permissions, and feature flags
- **Recording and cloud sync:** depend on the components and service configuration included with the package

### Workspace layout

- **Left:** saved sessions, folders, search results, and active connections
- **Center:** SSH, local terminal, SFTP, RDP, file, and tool tabs
- **Right:** optional AI and collaboration assistant area
- **Bottom:** current target, session path, connection state, network outlet, and proxy context

### Choose a package

Obtain XTermPro only through a distribution channel provided by the product publisher. Choose the package matching the operating system and CPU architecture:

- **Windows:** installer or portable ZIP
- **macOS:** Apple Silicon (`arm64`) or Intel (`amd64`) DMG
- **Linux:** runtime package matching the target distribution and system architecture

Before installation, verify the file name, product version, operating system, CPU architecture, and package source. If the publisher supplies a SHA-256 checksum, verify the package before running it.

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
