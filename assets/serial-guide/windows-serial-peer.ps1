# 作者：FanZhen Meng(Ivan)  mail: yzmeng1688@gmail.com
# 代码功能：打开 Windows 虚拟 COM 对端，手工复验连接及重连后的双向文本收发。
# 开发时间：2026-11-22
# 更新时间：2026-11-22
param(
    [ValidatePattern('^COM[1-9][0-9]*$')][string]$Port = 'COM74',
    [ValidateRange(1, 2147483647)][int]$BaudRate = 38400
)

$ErrorActionPreference = 'Stop'
$peer = [System.IO.Ports.SerialPort]::new($Port, $BaudRate, 'None', 8, 'One')
$peer.Handshake = 'None'
$peer.WriteTimeout = 3000

try {
    $peer.Open()
    $null = Read-Host 'Type app-to-peer in XTermPro, then press Enter here'
    $received = $peer.ReadExisting()
    if ($received -notlike '*app-to-peer*') {
        throw "Expected app-to-peer on ${Port}; received: '$received'"
    }
    Write-Host "Received: $received"
    $peer.Write("peer-to-app`r`n")

    # 保留对端句柄，仅重开应用一侧，随后复查两个方向。
    $null = Read-Host 'Verify peer-to-app, reconnect in XTermPro, type app-reconnected, then press Enter here'
    $received = $peer.ReadExisting()
    if ($received -notlike '*app-reconnected*') {
        throw "Expected app-reconnected on ${Port}; received: '$received'"
    }
    Write-Host "Received: $received"
    $peer.Write("peer-reconnected`r`n")
    $null = Read-Host 'Verify peer-reconnected in XTermPro, then press Enter to close'
} finally {
    $peer.Dispose()
}
