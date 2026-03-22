#!/usr/bin/env python3
"""
Agent Reach 技能执行脚本

用法:
    python3 scripts/run.py <command> [args...]

示例:
    python3 scripts/run.py doctor
    python3 scripts/run.py read --url https://example.com
    python3 scripts/run.py search --query "python tutorial"
"""

import sys
import os
import subprocess
import argparse

# 虚拟环境路径
VENV_PATH = os.path.expanduser("~/.agent-reach-venv/bin/activate")

def activate_venv():
    """激活虚拟环境并返回完整的命令前缀"""
    if not os.path.exists(VENV_PATH):
        print(f"错误：虚拟环境不存在：{VENV_PATH}", file=sys.stderr)
        print("请先安装 agent-reach: pip3 install agent-reach", file=sys.stderr)
        sys.exit(1)
    return f"source {VENV_PATH} && "

def run_command(cmd):
    """执行 shell 命令"""
    full_cmd = activate_venv() + cmd
    result = subprocess.run(
        full_cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

def read_url(url):
    """读取网页内容"""
    cmd = f'curl -s "https://r.jina.ai/{url}"'
    return run_command(cmd)

def search_web(query):
    """全网语义搜索"""
    # 使用 agent-reach 的搜索功能（如果有）或回退到 Jina
    cmd = f'curl -s "https://s.jina.ai/{query}"'
    return run_command(cmd)

def doctor():
    """检查环境状态"""
    return run_command("agent-reach doctor")

def configure(platform, value=None):
    """配置平台认证"""
    if value:
        return run_command(f"agent-reach configure {platform} \"{value}\"")
    else:
        return run_command(f"agent-reach configure {platform}")

def main():
    parser = argparse.ArgumentParser(
        description="Agent Reach 技能执行脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s doctor                          # 检查环境状态
  %(prog)s read --url https://example.com  # 读取网页内容
  %(prog)s search --query "python"         # 搜索内容
  %(prog)s configure twitter               # 配置 Twitter 认证
        """
    )
    
    parser.add_argument("command", nargs="?", default="doctor",
                       choices=["doctor", "read", "search", "configure", "install"],
                       help="要执行的命令")
    parser.add_argument("--url", "-u", help="要读取的 URL")
    parser.add_argument("--query", "-q", help="搜索关键词")
    parser.add_argument("--platform", "-p", help="配置的平台名称")
    parser.add_argument("--value", "-v", help="配置的值（如 Cookie）")
    parser.add_argument("--env", help="安装环境（local/server/auto）")
    
    args = parser.parse_args()
    
    if args.command == "doctor":
        sys.exit(doctor())
    
    elif args.command == "read":
        if not args.url:
            print("错误：--url 参数必填", file=sys.stderr)
            sys.exit(1)
        sys.exit(read_url(args.url))
    
    elif args.command == "search":
        if not args.query:
            print("错误：--query 参数必填", file=sys.stderr)
            sys.exit(1)
        sys.exit(search_web(args.query))
    
    elif args.command == "configure":
        if not args.platform:
            print("错误：--platform 参数必填", file=sys.stderr)
            sys.exit(1)
        sys.exit(configure(args.platform, args.value))
    
    elif args.command == "install":
        env = args.env or "auto"
        sys.exit(run_command(f"agent-reach install --env={env}"))
    
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
