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
- SSH 可见文本记录（默认关闭，支持会话设置、手动启停、分片与异常恢复辅助文件）；操作与验证见 [终端增强示例](docs/terminal-enhancements/EXAMPLES.md#te-07-ssh-文本记录)
- 文本记录历史查看与查找（只读分页、跨分片搜索、异常尾行提示）；操作与验证见 [历史查看示例](docs/terminal-enhancements/EXAMPLES.md#te-08-历史查看与查找)
- SSH 终端截图（当前可见区域或全部保留缓存、逐页 PNG、七字段水印）；操作与验证见 [截图示例](docs/terminal-enhancements/EXAMPLES.md#te-10-ssh-终端截图)
- Serial 串口连接（枚举/手输端口、参数校验、会话树重开、可见文本记录与截图）；模拟设备示例见 [终端增强示例](docs/terminal-enhancements/EXAMPLES.md#te-11-模拟串口连接macoslinux)
- Windows 本地 Named Pipe 连接（已有双向 byte-mode 管道、保存会话、可见文本记录与截图）；非 Windows 明确禁用，Windows 原生验收待对应平台执行。
- XMODEM 文件发送与接收（SSH、Serial，以及 Windows 本地 Named Pipe；128/1024 B 数据块、进度/取消和安全接收）；接收末块填充按协议保留，使用方式见 [XMODEM 示例](docs/terminal-enhancements/EXAMPLES.md#te-14-xmodem-文件收发)。Windows/Linux 原生验收待对应平台执行。
- YMODEM 批量文件发送与接收（逐文件状态、中文 UTF-8 名称、按对端声明的长度落盘、同名跳过/改名/覆盖）；使用方式见 [YMODEM 示例](docs/terminal-enhancements/EXAMPLES.md#te-15-ymodem-批量文件收发)。Windows/Linux 原生验收待对应平台执行。
- ZMODEM 批量发送与接收（独立开关、对端发起时先确认再接收、有界探测、逐文件队列与失败重连）；使用方式见 [ZMODEM 示例](docs/terminal-enhancements/EXAMPLES.md#te-16-zmodem-批量文件收发)。Windows/Linux 原生验收待对应平台执行。
- 本地配置导出、预览、恢复及存储位置管理

#### 可选与预览能力

- **RDP 远程桌面：** 支持直接连接和 SSH 隧道场景，当前仍属于开发测试能力
- **Kubernetes / Cilium：** 实际能力取决于运行包版本、集群组件和 RBAC 权限
- **AI 助手：** 需要用户自行配置兼容的模型服务及访问凭据
- **Agent / iChat：** 取决于运行包版本、服务端部署、账号权限和功能开关
- **终端录制与云同步：** 取决于运行包是否包含相应组件及服务配置

### 近期更新（2026-09-20—2026-09-21）

以下说明汇总本仓库近期已提交的功能与修复；不代表所有平台均已验收或对应安装包已经发布。具体使用方式、测试范围与未完成项见各功能文档。

#### 功能迭代

- **SSH 连接控制：** 展示实际连接阶段和重试倒计时，支持超时、初次连接重试与取消；首次连接需要明确确认主机密钥，初连重试与已建立会话的断线恢复分别处理。
- **记录、历史与截图：** 新增可见文本记录、分片历史查看与跨分片查找；支持当前可见区域或保留缓存的分页 PNG 截图及水印。记录默认关闭，可按会话配置和手动启停。
- **Serial 与 Named Pipe：** 串口支持端口枚举、手动输入、参数设置、保存会话、记录和截图；Windows 本地 Named Pipe 支持连接已有双向 byte-mode 管道，其他平台禁用该入口。
- **终端文件传输：** 新增 XMODEM、YMODEM、ZMODEM 收发能力，支持进度、取消和接收文件保护；YMODEM/ZMODEM 支持批量传输。远端执行 `rz` 时可识别上传请求并打开本地文件选择，执行 `sz` 时先确认再接收。
- **SFTP 本地导航：** 路径栏增加主题化目录选择器，路径、目录树与文件列表同步更新；Windows 增加盘符导航。

操作入口与配置示例见 [终端增强使用示例](docs/terminal-enhancements/EXAMPLES.md)。

#### 问题修复与性能改进

- **SSH 生命周期：** 修复失败连接的资源释放及对相邻标签的影响；优化大量失败标签关闭时的重复刷新，并缓存标签标题测量结果。
- **会话树与串口：** 修复切换标签时运行中会话行被重建、选择状态重置的问题，以及 macOS 模拟串口对端退出的识别。
- **macOS 弹窗稳定性：** 为配置管理和会话日志窗口补充 Cocoa 辅助功能兼容保护，修复对应入口的崩溃问题。
- **macOS 授权保留：** 改进签名和安装场景下的设备绑定兼容，保留已有许可证及试用身份、到期时间；修复构建时 OpenSSL 工具架构不匹配导致的公钥校验失败。
- **iChat 断线恢复：** 增加断开后的重试和关闭入口，合并重复重试、忽略过期回调，同步完成后恢复聊天；关闭聊天窗口不影响共享身份和终端会话。此次修复不代表此前反馈的进程退出根因已确认。

#### UI 优化

- 统一主题化胶囊页签，优化选中、悬停、焦点、禁用及溢出状态。
- 修复 SSH 连接状态卡片内容裁切，调整截图范围弹窗的紧凑布局和说明换行。
- 截图结果、功能授权限制提示、终端复制反馈及会话日志详情跟随应用主题。
- 修复弹出层残留矩形边框、文本选区对比度，以及徽标、箭头、脚本、分屏和辅助区域的主题刷新。
- macOS 原生标题栏与窗口配色同步更新；设备页面支持运行时语言切换。

#### 主题更新

内置主题扩展至 **22 套**，在现有主题基础上增加两批柔和与自然风格配色：

- **首批六套：** 薄荷、海盐、日落、樱桃奶油、雾紫、玫瑰可可。
- **新增八套：** 桃桃、晴紫、燕麦、夜鸢、草莓牛奶、奶油布丁、山岚、星湖。

在外观设置中可预览、应用或取消主题，并保存选择供重启后恢复。主题统一覆盖控件、页签和选区；应用 UI 主题与终端配色方案分别管理。预览及说明见 [主题使用示例](docs/theme-refresh/EXAMPLES.md)。

#### 验证范围与待跟进项

- **已有验证记录：** macOS 构建与相关专项测试、22 套主题的 Cocoa 检查、真实 SSH `rz`/`sz` 文件往返，以及 100 路独立模拟串口的轻量收发和生命周期验证。模拟串口结果不代表实物设备、高吞吐或长期稳定性验收。
- **待对应平台验证：** Windows/Linux 原生终端增强、主题和 SFTP 导航；Windows Named Pipe 仍需 Windows 原生验收。
- **仍在推进：** 终端增强父功能、完整逐项 UI 点击验收及更高档位 SSH 容量验证尚未全部完成；不把局部修复或压力抽查等同于完整验收。

详细证据与限制见 [终端增强测试记录](docs/terminal-enhancements/TESTING.md)、[终端增强任务状态](docs/terminal-enhancements/TASKS.md)、[主题测试记录](docs/theme-refresh/TESTING.md)、[授权测试记录](docs/activation-license-v2/TESTING.md)及 [iChat 断线恢复测试记录](docs/ichat-disconnect-recovery/TESTING.md)。

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
- Visible SSH text recording (off by default, with per-session settings, manual start/stop, file rotation, and crash-recovery sidecars); see the [terminal enhancement example](docs/terminal-enhancements/EXAMPLES.md#te-07-ssh-文本记录)
- Text recording history viewer (read-only paging, search across parts, and recovered-tail display); see the [history viewer example](docs/terminal-enhancements/EXAMPLES.md#te-08-历史查看与查找)
- SSH terminal captures (visible area or retained history, paged PNG files and seven watermark fields); see the [capture example](docs/terminal-enhancements/EXAMPLES.md#te-10-ssh-终端截图)
- Serial connections (port discovery/manual entry, checked settings, saved sessions, text recording, and screenshots); see the [simulated-device example](docs/terminal-enhancements/EXAMPLES.md#te-11-模拟串口连接macoslinux)
- Local Windows Named Pipe connections to existing duplex byte-mode pipes, with saved sessions, text recording, and screenshots; other platforms disable the entry, and native Windows validation is pending.
- Local configuration export, preview, restore, and storage-location management

#### Optional and preview capabilities

- **RDP remote desktop:** direct and SSH-tunnel scenarios; currently a development-preview capability
- **Kubernetes / Cilium:** availability depends on the package version, cluster components, and RBAC permissions
- **AI assistant:** requires a compatible model service and user-supplied credentials
- **Agent / iChat:** depends on the package version, server deployment, account permissions, and feature flags
- **Recording and cloud sync:** depend on the components and service configuration included with the package

### Recent updates (September 20–21, 2026)

This summary covers recently committed changes in this repository. It does not imply acceptance on every platform or availability in a published package. Feature documents contain usage instructions, evidence, and remaining work.

#### Feature updates

- **SSH connection controls:** observed connection phases, retry countdowns, timeout settings, initial retries, and cancellation. First-use host keys require explicit trust; initial retries remain separate from established-session recovery.
- **Recording, history, and captures:** visible-text recording, paged history with search across parts, and watermarked PNG captures of the visible area or retained history. Recording is off by default, with per-session settings and manual controls.
- **Serial and Named Pipe:** serial port discovery/manual entry, connection settings, saved sessions, recording, and captures. Local Windows Named Pipe sessions connect to existing duplex byte-mode pipes; the entry is disabled on other platforms.
- **Terminal file transfers:** XMODEM, YMODEM, and ZMODEM sending/receiving with progress, cancellation, and protected file reception; YMODEM/ZMODEM support batches. Remote `rz` requests can open the local upload picker, while `sz` reception requires confirmation.
- **SFTP local navigation:** a themed directory picker keeps the path, tree, and file list synchronized; Windows gains drive navigation.

See the [terminal enhancement examples](docs/terminal-enhancements/EXAMPLES.md) for controls and configuration.

#### Fixes and performance

- **SSH lifecycle:** release failed-connection resources and preserve neighboring tabs; reduce repeated refreshes during bulk failure-tab closure and cache tab-title measurements.
- **Session tree and serial:** preserve runtime rows and selection when switching tabs; detect simulated serial peer hangup on macOS.
- **macOS dialog stability:** add Cocoa accessibility compatibility guards for crashes in configuration-management and session-log dialogs.
- **macOS activation:** improve device-binding compatibility across signing and installation while preserving existing licenses, trial identity, and expiration; fix public-key validation failures caused by a build-time OpenSSL architecture mismatch.
- **iChat recovery:** add retry/close controls after disconnection, coalesce retries, reject stale callbacks, and restore chat after synchronization. Closing chat preserves shared identity and terminal sessions. The previously reported process-exit root cause remains unconfirmed.

#### UI improvements

- Shared themed capsule tabs with consistent selected, hover, focus, disabled, and overflow states.
- Fix clipped SSH status cards and make capture-scope dialogs compact with wrapping descriptions.
- Apply the current theme to capture results, license-restriction prompts, terminal copy feedback, and session-log details.
- Remove residual rectangular popup frames, improve text-selection contrast, and refresh badges, arrows, scripts, split panes, and assistant surfaces with theme changes.
- Synchronize macOS native titlebars/window colors and update device pages when the language changes at runtime.

#### Theme updates

The built-in collection now contains **22 themes**, including two recent groups of softer and nature-inspired palettes:

- **First six additions:** Mint, Sea Salt, Sunset, Cherry Cream, Lavender, and Rose Cocoa.
- **Eight further additions:** Peach Blush, Lilac Sky, Oat Linen, Plum Night, Strawberry Milk, Vanilla Pudding, Mountain Mist, and Starlit Lake.

Appearance settings support preview, apply, cancel, and persistence across restarts. Controls, tabs, and selection surfaces share theme styling; application themes and terminal color schemes remain separate. See the [theme examples](docs/theme-refresh/EXAMPLES.md).

#### Validation and remaining work

- **Recorded evidence:** macOS builds and focused tests, Cocoa checks for all 22 themes, real SSH `rz`/`sz` round trips, and lightweight traffic/lifecycle checks across 100 independent simulated serial connections. These serial results do not cover physical hardware, high throughput, or long-duration operation.
- **Pending native platform checks:** Windows/Linux terminal enhancements, themes, and SFTP navigation; Named Pipe still requires native Windows acceptance.
- **Still in progress:** the terminal-enhancement parent feature, exhaustive UI interaction acceptance, and higher-tier SSH capacity validation. Focused fixes and sampled load checks do not establish complete acceptance.

See [terminal testing](docs/terminal-enhancements/TESTING.md), [terminal task status](docs/terminal-enhancements/TASKS.md), [theme testing](docs/theme-refresh/TESTING.md), [activation testing](docs/activation-license-v2/TESTING.md), and [iChat recovery testing](docs/ichat-disconnect-recovery/TESTING.md) for evidence and limitations.

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
