#!/usr/bin/env python3
# Author: FanZhen Meng(Ivan)  mail: yzmeng1688@gmail.com
# 代码功能：提供一次性 POSIX 伪串口对端，供桌面串口会话验证。
# 开发时间：未知（历史记录不足）
# 更新时间：2026-11-21
"""Run a disposable POSIX pseudo-serial peer for manual desktop verification."""

import os
import pty
import select
import signal
import sys
import tty


def main() -> int:
    if os.name != "posix":
        print("This fixture requires macOS or Linux; use a native Windows serial simulator on Windows.", file=sys.stderr)
        return 2
    master, slave = pty.openpty()
    tty.setraw(slave)
    print(os.ttyname(slave), flush=True)
    print("Keep this process running while the app is connected. Press Ctrl-C to disconnect.", flush=True)
    try:
        while True:
            ready, _, _ = select.select([master], [], [], 1)
            if master not in ready:
                continue
            try:
                payload = os.read(master, 4096)
            except OSError:
                break
            if not payload:
                break
            os.write(master, b"simulated> " + payload)
    except KeyboardInterrupt:
        pass
    finally:
        os.close(master)
        os.close(slave)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
