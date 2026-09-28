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

- 笔记空间：持久新建、自动保存、分组与回收站、可配置存储位置；支持多个独立进程共享空间、自动同步目录及同笔记保存冲突保护；会话与笔记独立折叠，工具栏统一主题气泡样式。见 [使用示例](docs/note-space/EXAMPLES.md) 和 [验收状态](docs/note-space/TESTING.md)（macOS 本地验收通过，Windows/Linux 由用户人工验收）。

#### 连接与工作区

- SSH2 远程终端，支持密码、托管凭据、私钥和跳板代理
- SSH 终端支持主题背景、背景图片、透明玻璃三选一背景；透明度实时调整，文字可跟随主题、增强字重或自定义颜色（保留 ANSI 色）；Windows/Linux 原生效果待对应平台验证，操作见 [透明玻璃示例](docs/ssh-terminal-glass/EXAMPLES.md)
- 可搜索的会话树、多标签工作区和 SSH 分屏
- SSH 快速连接支持会话名称和归属目录，留空自动命名；见 [使用示例](docs/ssh-session-identity/EXAMPLES.md)
- 精简 SSH 标签菜单：连接与标签操作留在右键；记录、传输、布局和终端旁编辑按功能归入顶部菜单，见 [菜单入口指南](docs/terminal-menu-organization/EXAMPLES.md)
- 清晰的连接、失败、断开与原标签重连状态
- 本地终端、最近文件和文本文件编辑；编辑器支持按内容类型提供离线词汇、关键词、字段和片段补全。见 [补全示例](docs/local-file-editor-floating-workspace/EXAMPLES.md#内容感知自动补全fr-26) 与 [平台验收状态](docs/local-file-editor-floating-workspace/TESTING.md)。
- 本地 HTML 可静态预览并显式运行页面脚本，普通 JavaScript 可显式运行并查看页面及控制台；预览引擎随运行包交付，无需用户另装浏览器、Node 或 Qt。Markdown 继续使用原有预览。见 [网页预览样例](examples/file-editor-web-preview/README.md)；Windows/Linux 安装包原生验收待用户完成，详情见 [验收记录](docs/local-file-editor-floating-workspace/TESTING.md#fr-27-用户手动平台验收最新授权)。
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
- **Kubernetes / Cilium：** [新建 K8s 连接与托管凭据](docs/K8S_CONNECTION_CREDENTIAL_EXAMPLES.md)，支持 Token、证书、OIDC、Exec、kubeconfig 导入和单跳 SSH；实际能力取决于运行包版本、集群组件和 RBAC 权限。平台验收状态见 [测试记录](docs/K8S_CONNECTION_CREDENTIAL_TESTING.md)。
- **AI 助手：** 需要用户自行配置兼容的模型服务及访问凭据
- **Agent / iChat：** 取决于运行包版本、服务端部署、账号权限和功能开关
- **终端录制与云同步：** 取决于运行包是否包含相应组件及服务配置

### 近期更新 · 2026-09-23—2026-09-27

本轮更新覆盖 9 月 22 日之后已提交的功能、体验优化与问题修复：把连接管理、编辑、记录和集群巡检串联到同一个工作区。以下为实现进展，平台验收范围见本节末尾。

#### 笔记空间与编辑器：边操作，边积累

- **持久笔记空间**：新建、自动保存、分组、回收站、导入导出及存储位置切换；多个独立进程可共享空间，同一笔记发生保存冲突时保留编辑内容，避免静默覆盖。
- **更清晰的文件导航**：已打开文件集中在笔记空间中，固定在回收站上方；修复默认分组选中、树移动后新建位置及保存失败恢复问题。
- **离线内容补全**：按内容类型提供本地词汇、关键词、字段和片段建议；支持普通与悬浮编辑器，修复自动保存打断补全、HTML 分隔符插入和弹层位置问题。
- **HTML / JavaScript 预览**：HTML 可静态预览，页面脚本与独立 JavaScript 需显式运行；可查看页面及控制台，Markdown 保持原有预览流程，运行包携带预览引擎。

![最新构建的笔记空间与 Markdown 编辑器](docs/readme-updates-20260927/assets/latest-notes-editor.png)

*最新源码构建的英文界面，使用本次新建的公开示例文件；显示笔记导航、文件标签与语法高亮。*

使用与验证：[笔记空间](docs/note-space/EXAMPLES.md) · [编辑器补全](docs/local-file-editor-floating-workspace/EXAMPLES.md#内容感知自动补全fr-26) · [网页预览样例](examples/file-editor-web-preview/README.md)。

#### Kubernetes：受管连接与一键巡检

- **保存与复用集群连接**：从文件菜单创建 K8s 连接，在会话树打开、重连和定位已连接工作台；支持 kubeconfig 导入、上下文选择和 SSH 引用。
- **统一凭据管理**：支持 Token、客户端证书、OIDC 及经批准的 exec 认证；显示已保存凭据状态与证书摘要，完善 Minikube 扩展兼容及粘贴外部证书路径时的操作提示。
- **一键只读巡检**：已实现 21 项检查模块（默认启用 16 项），覆盖节点、工作负载、Pod、网络、存储和名称空间治理，支持进度与取消。
- **可留存的巡检报告**：生成中英文离线 HTML，展示异常、风险、建议及未知判断，提供资源明细和对应证据；报告自动归档到笔记空间，文件名包含集群名称和日期。

![最新 Kubernetes 连接配置界面](docs/readme-updates-20260927/assets/latest-k8s-connection.png)

*本次重新打开的新建连接界面，使用保留示例域名；未填写凭据、保存连接或访问集群。巡检报告本轮未重新截图。*

使用与验证：[连接与凭据](docs/K8S_CONNECTION_CREDENTIAL_EXAMPLES.md) · [连接验收](docs/K8S_CONNECTION_CREDENTIAL_TESTING.md) · [巡检进度](docs/k8s-utils/TASKS.md) · [巡检验证](docs/k8s-utils/TESTING.md)。

#### SSH 与文件传输：减少重复操作

- **多会话命令目标**：在助手的 SSH 会话模式中通过 `@` 添加多个目标，发送前可逐个移除；发送后清空选择，并分别反馈提交结果。命令执行结果仍以各终端输出为准。
- **快捷连接与排序**：快速连接可填写会话名称和目录；保存连接按协议和名称排序，文件夹优先，已连接入口保留在末尾，并高亮当前连接。
- **自动启动接收端**：在支持的 POSIX shell 和 lrzsz 环境中，发送 X/Y/ZMODEM 文件时自动启动匹配接收程序；取消传输时保留终端连接，并区分握手等待与实际传输。
- **大文件转交 SFTP**：超出 ZMODEM 引擎边界的文件经明确确认转交 SFTP，支持进度、取消与续传相关处理。1 TiB 稀疏高偏移测试已覆盖，完整 1 TiB 上传与全文件校验未执行。
- **菜单更聚焦**：标签右键保留连接和标签操作，记录、传输、布局及终端旁编辑归入对应顶部菜单。

![最新 SSH 快捷连接界面，包含会话名称与目录](docs/readme-updates-20260927/assets/latest-ssh-connection.png)

使用与验证：[多目标命令](docs/ssh-session-mention/EXAMPLES.md) · [自动发送](docs/terminal-auto-send/EXAMPLES.md) · [大文件传输验证](docs/terminal-large-file-transfer/TESTING.md) · [菜单指南](docs/terminal-menu-organization/EXAMPLES.md)。

#### 主题与桌面体验：让外观跟随工作方式

- **22 套主题的应用图标适配**：本轮为现有主题补齐对应应用图标；22 套主题本身并非全部在本轮新增。
- **SSH 透明玻璃背景**：主题背景、背景图片与透明玻璃三选一，透明度实时调整；支持跟随主题或自定义前景色，并保留 ANSI 颜色。
- **细节与稳定性修复**：改善下拉菜单边框与屏幕边缘定位、工具提示透明圆角、会话菜单图标；修复 macOS Dock 重新激活窗口、托盘通知图片崩溃及透明标题栏拖动问题。

![最新外观设置与主题预览](docs/readme-updates-20260927/assets/latest-appearance.png)

*本次从最新构建打开外观设置后直接截图；未复用旧图标拼图或玻璃测试背景。*

使用与验证：[透明背景](docs/ssh-terminal-glass/EXAMPLES.md) · [透明背景验证](docs/ssh-terminal-glass/TESTING.md)。

#### 当前验证范围

上述功能已有对应的 macOS 构建、定向测试或原生验收记录，具体范围以链接文档为准。Windows/Linux 原生效果与安装包验收仍按各功能计划推进；Kubernetes 巡检整体仍为 **In Progress**，尚有认证组合、版本及平台矩阵待验收。本节截图均为本次从最新源码构建重新采集的 macOS 英文界面，使用隔离示例数据；不代表生产集群、全平台或最终发布验收通过。开发构建标题显示 1.0.0，是当前 CMake 默认版本值，并非已发布版本号。

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
- SSH terminals support mutually exclusive solid, image, and transparent-glass backgrounds, configurable opacity, and text-legibility protection; native Windows/Linux effects await platform validation. See the [glass background example](docs/ssh-terminal-glass/EXAMPLES.md)
- Searchable session tree, tabbed workspace, and split SSH views
- Quick SSH connections support a session name and folder, with automatic naming; see the [example](docs/ssh-session-identity/EXAMPLES.md)
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
- **Kubernetes / Cilium:** [manual connections and managed credentials](docs/K8S_CONNECTION_CREDENTIAL_EXAMPLES.md) support Token, certificates, OIDC, Exec and a single SSH jump. Availability depends on package version, cluster components and RBAC; see [validation status](docs/K8S_CONNECTION_CREDENTIAL_TESTING.md).
- **AI assistant:** requires a compatible model service and user-supplied credentials
- **Agent / iChat:** depends on the package version, server deployment, account permissions, and feature flags
- **Recording and cloud sync:** depend on the components and service configuration included with the package

### Recent updates · September 23–27, 2026

These committed updates after September 22 bring connection management, editing, notes, and cluster inspection into a more connected workspace. Implementation progress and platform acceptance are distinguished below.

#### Notes and editing: keep knowledge alongside your work

- **Persistent note spaces:** create, autosave, group, recover from trash, import/export, and switch storage locations. Independent processes can share a space; conflicting edits are retained rather than silently overwritten.
- **Clearer file navigation:** opened files now live in the note space immediately above Trash. Fixes cover default-group selection, new-note destinations after tree moves, and recovery from failed saves.
- **Offline content-aware completion:** local words, keywords, fields, and snippets in regular and floating editors. Fixes preserve suggestions across autosave, retain HTML delimiters, and improve popup positioning.
- **HTML / JavaScript preview:** preview static HTML, explicitly run page scripts or standalone JavaScript, and inspect the page and console. Markdown keeps its existing workflow; the preview engine ships with the package.

![Current note space and Markdown editor](docs/readme-updates-20260927/assets/latest-notes-editor.png)

*Fresh capture of the current source build in English, with a newly created public sample file, note navigation, file tabs, and syntax highlighting.*

Guides and evidence: [Note spaces](docs/note-space/EXAMPLES.md) · [Editor](docs/local-file-editor-floating-workspace/EXAMPLES.md) · [Web preview examples](examples/file-editor-web-preview/README.md).

#### Kubernetes: managed connections and one-click inspection

- **Reusable cluster connections:** create K8s connections from the File menu, open and reconnect from the session tree, and locate connected workbenches. Includes kubeconfig import, context selection, and SSH references.
- **Managed credentials:** Token, client certificates, OIDC, and approved exec authentication, with saved-credential status and certificate summaries. Improvements cover Minikube extensions and guidance for pasted external certificate paths.
- **Read-only inspection:** 21 implemented modules, with 16 enabled by default, covering nodes, workloads, Pods, networking, storage, and namespace governance, with progress and cancellation.
- **Reports you can retain:** localized, offline HTML reports distinguish faults, risks, recommendations, and unknown assessments, with inventory tables and supporting evidence. Reports are archived to the note space with cluster names and dates in filenames.

![Current Kubernetes connection configuration](docs/readme-updates-20260927/assets/latest-k8s-connection.png)

*Fresh capture of the connection form using a reserved example domain. No credentials were entered, no connection was saved, and no cluster was accessed. An inspection report was not recaptured in this session.*

Guides and evidence: [Connections and credentials](docs/K8S_CONNECTION_CREDENTIAL_EXAMPLES.md) · [Connection acceptance](docs/K8S_CONNECTION_CREDENTIAL_TESTING.md) · [Inspection progress](docs/k8s-utils/TASKS.md) · [Inspection validation](docs/k8s-utils/TESTING.md).

#### SSH and transfers: fewer repeated steps

- **Multiple command targets:** use `@` in the assistant's SSH session mode to add targets and remove individual selections before sending. Targets clear after submission, with a result for each connection; remote execution results remain in the respective terminals.
- **Quick connect and ordering:** specify a session name and folder during quick connect. Saved connections sort by protocol and name, folders remain first, Connected remains last, and the active connection is highlighted.
- **Automatic receiver startup:** start the matching X/Y/ZMODEM receiver in supported POSIX shell and lrzsz environments. Cancellation preserves the terminal connection; handshake waiting is distinguished from payload transfer.
- **Large-file SFTP handoff:** files beyond the ZMODEM engine limit can explicitly switch to SFTP, with progress, cancellation, and resume handling. Sparse high-offset tests cover 1 TiB; a complete 1 TiB upload and full-file verification have not been performed.
- **Focused menus:** tab context menus retain connection and tab actions, while recording, transfers, layout, and adjacent editing live in their respective top menus.

![Current SSH quick-connect form with session name and folder](docs/readme-updates-20260927/assets/latest-ssh-connection.png)

Guides and evidence: [Multiple targets](docs/ssh-session-mention/EXAMPLES.md) · [Automatic sending](docs/terminal-auto-send/EXAMPLES.md) · [Large-file validation](docs/terminal-large-file-transfer/TESTING.md) · [Menu guide](docs/terminal-menu-organization/EXAMPLES.md).

#### Themes and desktop experience

- **Application icons for all 22 themes:** this update adds matching icons to the existing theme collection; it does not introduce 22 new themes.
- **Transparent SSH backgrounds:** choose a theme background, an image, or transparent glass with live opacity adjustment. Text can follow the theme or use a custom foreground while preserving ANSI colors.
- **Polish and stability:** improved combo popup borders and screen positioning, transparent tooltip corners, and session-menu icons. Fixes address macOS Dock reactivation, tray notification image crashes, and glass-titlebar dragging.

![Current appearance settings and theme preview](docs/readme-updates-20260927/assets/latest-appearance.png)

*Fresh capture of Appearance Settings in the current build, replacing the historical icon montage and glass-test backdrop.*

Guides and evidence: [Glass backgrounds](docs/ssh-terminal-glass/EXAMPLES.md) · [Glass validation](docs/ssh-terminal-glass/TESTING.md).

#### Validation scope

Linked records describe the applicable macOS builds, focused tests, and native checks. Windows/Linux native behavior and package acceptance remain subject to each feature's plan. Kubernetes inspection remains **In Progress**, with authentication combinations, versions, and platform coverage still pending. All screenshots in this section were freshly captured from the current macOS source build in English with isolated sample data. They do not establish production-cluster, cross-platform, or final release acceptance. The title shows 1.0.0, the current CMake development-build default, not a published release number.

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
