# Surfin Claw 安装指南

## 快速安装

### 1. 安装 agent-reach CLI

```bash
pip install agent-reach
```

或从源码安装：

```bash
git clone https://github.com/anjun/Agent-Reach.git
cd Agent-Reach
pip install -e .
```

### 2. 安装系统依赖

```bash
# Node.js（用于 xreach、mcporter）
brew install node  # macOS
# 或从 https://nodejs.org 下载

# yt-dlp（视频下载）
pip install yt-dlp

# gh CLI（GitHub 操作）
brew install gh  # macOS
# 或从 https://cli.github.com 下载
```

### 3. 配置 Surfin Claw 技能

```bash
# 创建技能目录
mkdir -p ~/.surfin-claw/skills/agent-reach

# 复制 SKILL.md
cp agent_reach/skill/SKILL.md ~/.surfin-claw/skills/agent-reach/
```

### 4. 验证安装

```bash
agent-reach doctor
```

## 配置各平台

### Twitter/X

1. 浏览器登录 Twitter
2. 使用 Cookie-Editor 插件导出 Cookie
3. 告诉 Agent "帮我配置 Twitter"，粘贴 Cookie

### 小红书

1. 浏览器登录小红书
2. 使用 Cookie-Editor 插件导出 Cookie
3. 告诉 Agent "帮我配置小红书"，粘贴 Cookie

### 代理（服务器部署时需要）

```bash
agent-reach configure proxy http://your-proxy:port
```

## 使用

安装完成后，直接告诉 Agent 你的需求：

- "帮我看看这个 YouTube 视频讲了什么"
- "搜一下 Twitter 上关于 AI 的讨论"
- "看看这个 GitHub 仓库是做什么的"

Agent 会自动调用合适的工具。

## 更新

```bash
pip install --upgrade agent-reach
```

或从源码更新：

```bash
cd Agent-Reach
git pull
pip install -e .
```
