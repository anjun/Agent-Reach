# Agent Reach for Surfin Claw

<p align="center">
  <strong>给你的 AI Agent 一键装上互联网能力</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/anjun/Agent-Reach/stargazers"><img src="https://img.shields.io/github/stars/anjun/Agent-Reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

---

## 📝 项目说明

本项目是 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) 的 **Surfin Claw 适配版**。

原项目是一个开源的 AI Agent 互联网数据获取工具，支持 OpenClaw 等平台。本 fork 针对 **Surfin Claw** 进行了适配和优化。

### 与原项目的区别

| 特性 | 原项目 (OpenClaw) | 本 fork (Surfin Claw) |
|------|-------------------|----------------------|
| 技能目录 | `~/.openclaw/skills/` | `~/.surfin-claw/skills/` |
| 工具调用 | `messaging`/`coding` profile | 内置 `bash`/`webfetch`/`websearch` |
| 配置检测 | `openclaw` 命令 | `~/.surfin-claw/` 目录 |
| SKILL.md 格式 | OpenClaw YAML 头部 | Surfin Claw Markdown 格式 |

---

## 🚀 快速开始

### Surfin Claw 用户（推荐）

直接告诉你的 AI Agent：

```
帮我安装技能：https://github.com/anjun/Agent-Reach
```

或手动安装：

```bash
mkdir -p ~/.surfin-claw/skills/agent-reach
curl -o ~/.surfin-claw/skills/agent-reach/SKILL.md \
  https://raw.githubusercontent.com/anjun/Agent-Reach/main/agent_reach/skill/SKILL.md
```

### 其他平台用户

```bash
pip install agent-reach
```

或从源码安装：

```bash
git clone https://github.com/anjun/Agent-Reach.git
cd Agent-Reach
pip install -e .
```

---

## 📦 安装依赖

```bash
# Node.js（用于 xreach、mcporter）
brew install node  # macOS

# 安装 Node 工具
npm install -g xreach-cli mcporter

# yt-dlp（视频下载）
pip install yt-dlp

# gh CLI（GitHub 操作）
brew install gh  # macOS
```

---

## 🎯 支持的平台

| 平台 | 状态 | 工具 | 说明 |
|------|------|------|------|
| 🌐 网页 | ✅ 可用 | Jina Reader | 免费，无需 API Key |
| 📺 YouTube | ✅ 可用 | yt-dlp | 视频字幕提取 |
| 📺 B站 | ✅ 可用 | yt-dlp | 视频字幕提取 |
| 🐦 Twitter/X | ✅ 可用 | xreach | 需配置 Cookie |
| 📖 Reddit | ✅ 可用 | Exa/API | 搜索免费 |
| 📦 GitHub | ✅ 可用 | gh CLI | 官方工具 |
| 📕 小红书 | ⚙️ 需配置 | mcporter | 需 Docker 部署 |
| 🎵 抖音 | ⚙️ 需配置 | mcporter | 需配置服务 |
| 💬 微信公众号 | ✅ 可用 | miku_ai | 搜索+阅读 |
| 🎙️ 小宇宙播客 | ⚙️ 需配置 | groq-whisper | 需 ffmpeg |
| 💼 LinkedIn | ⚙️ 需配置 | mcporter | 需配置服务 |
| 📰 微博 | ✅ 可用 | 公开 API | 无需认证 |
| 📰 V2EX | ✅ 可用 | 公开 API | 无需认证 |
| 📡 RSS | ✅ 可用 | feedparser | 订阅源读取 |

---

## 🛠️ 配置指南

### Twitter/X

1. 浏览器登录 Twitter
2. 安装 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor) 插件
3. 导出 Cookie 为 JSON
4. 告诉 Agent："帮我配置 Twitter"

```bash
agent-reach configure twitter
```

### 小红书

```bash
# 部署小红书 MCP 服务
docker run -d --name xiaohongshu-mcp -p 18060:18060 \
  --platform linux/amd64 xpzouying/xiaohongshu-mcp

# 配置连接
mcporter config add xiaohongshu http://localhost:18060/mcp
```

### 代理（服务器部署）

```bash
agent-reach configure proxy http://your-proxy:port
```

---

## 📖 使用示例

安装完成后，直接告诉 Agent 你的需求：

```
"帮我看看这个 YouTube 视频讲了什么"
"搜一下 Twitter 上关于 AI 的讨论"
"看看这个 GitHub 仓库是做什么的"
"小红书上有哪些关于旅游的笔记"
"这个网页的主要内容是什么"
```

---

## 🔧 故障排查

### 检查所有渠道状态

```bash
agent-reach doctor
```

### 常见问题

| 问题 | 解决方案 |
|------|----------|
| xreach 未安装 | `npm install -g xreach-cli` |
| YouTube 403 | 配置代理：`agent-reach configure proxy` |
| Twitter 403 | 导出 Cookie 配置认证 |
| 微信公众号失败 | 使用 Camoufox 工具读取 |

---

## 🏗️ 技术架构

Agent Reach 是一个脚手架工具，Agent 直接调用上游工具完成实际工作：

```
Agent Request
    ↓
SKILL.md (Surfin Claw 格式)
    ↓
bash/webfetch/websearch 工具
    ↓
上游工具 (xreach/yt-dlp/gh/mcporter/...)
    ↓
目标平台 (Twitter/YouTube/GitHub/...)
```

---

## 🔒 安全性

- Cookie 和 Token 只存储在本地 `~/.agent-reach/`
- 配置文件权限 600（仅所有者可读写）
- 代码完全开源，可随时审查
- 所有依赖工具也是开源项目

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

- 原项目：https://github.com/Panniantong/Agent-Reach
- 本 fork：https://github.com/anjun/Agent-Reach

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

感谢 [Panniantong](https://github.com/Panniantong) 创建原项目 Agent Reach！
