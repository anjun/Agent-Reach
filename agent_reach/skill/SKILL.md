# Agent Reach for Surfin Claw

给你的 AI Agent 一键装上互联网能力 —— 支持抓取 Twitter/X、Reddit、YouTube、GitHub、B站、小红书等 16+ 平台。

## 功能

- 🌐 **网页** - 阅读任意网页内容
- 📺 **YouTube/B站** - 提取视频字幕和元数据
- 🐦 **Twitter/X** - 读取推文、搜索、浏览时间线
- 📖 **Reddit** - 搜索和阅读帖子
- 📦 **GitHub** - 搜索仓库、查看 Issue/PR
- 📕 **小红书** - 搜索笔记、查看详情
- 🎵 **抖音** - 解析视频信息
- 💬 **微信公众号** - 搜索和阅读文章
- 🎙️ **小宇宙播客** - 音频转文字
- 💼 **LinkedIn** - 查看个人资料
- 📰 **微博/V2EX/RSS** - 社交媒体和订阅源

## 命令

```bash
# 检测所有渠道状态
agent-reach doctor

# 配置特定平台
agent-reach configure twitter      # 配置 Twitter
agent-reach configure xiaohongshu  # 配置小红书
agent-reach configure proxy        # 配置代理

# 安装/更新工具
agent-reach install
agent-reach update
```

## 使用示例

直接告诉 Agent 你的需求，它会自动调用合适的工具：

- "帮我看看这个 YouTube 视频讲了什么"
- "搜一下 Twitter 上关于 AI 的讨论"
- "看看这个 GitHub 仓库是做什么的"
- "小红书上有哪些关于旅游的笔记"
- "这个网页的主要内容是什么"

## 技术实现

Agent Reach 是一个脚手架工具，实际调用以下上游工具：

| 平台 | 工具 | 说明 |
|------|------|------|
| 网页 | Jina Reader | 免费，无需 API Key |
| YouTube/B站 | yt-dlp | 148K Star，支持 1800+ 站点 |
| Twitter/X | xreach | Cookie 登录，免费 |
| Reddit | Exa/直接 API | 搜索免费，读取需代理 |
| GitHub | gh CLI | 官方工具 |
| 小红书/抖音/LinkedIn | mcporter (MCP) | 通过 MCP 服务调用 |
| 微信公众号 | miku_ai + Camoufox | 搜索+全文阅读 |
| 小宇宙播客 | groq-whisper | 音频转录 |
| V2EX | 公开 API | 无需认证 |

## 安装

```bash
pip install agent-reach
```

或从源码安装：

```bash
git clone https://github.com/anjun/Agent-Reach.git
cd Agent-Reach
pip install -e .
```

## 依赖

- Python 3.10+
- Node.js（用于 xreach、mcporter）
- yt-dlp（视频下载）
- gh CLI（GitHub 操作）

## 配置

配置文件位于 `~/.agent-reach/config.yaml`

```yaml
# Twitter 认证（可选）
twitter_auth_token: your_token
twitter_ct0: your_ct0

# 代理配置（服务器部署时需要）
proxy: http://your-proxy:port

# Groq API Key（小宇宙播客转录需要）
groq_api_key: your_key
```

## 隐私与安全

- Cookie 和 Token 只存储在本地 `~/.agent-reach/`，文件权限 600
- 代码完全开源，可审查
- 支持安全模式安装：`agent-reach install --safe`

## Surfin Claw 适配说明

本项目是 Agent Reach 的 Surfin Claw 适配版本，主要修改：
- 移除了 OpenClaw 特有的配置检测
- 适配 Surfin Claw 技能目录结构
- 使用内置 bash/webfetch 工具调用

原项目：https://github.com/Panniantong/Agent-Reach
