# Agent Reach for Surfin Claw

**给你的 AI Agent 一键装上互联网能力** —— 支持抓取 Twitter/X、Reddit、YouTube、GitHub、B站、小红书等 16+ 平台。

**版本**: 1.0.0  
**适配**: Surfin Claw  
**源码**: https://github.com/anjun/Agent-Reach

---

## 技能说明

Agent Reach 是一个互联网数据获取工具，让你的 AI Agent 能够读取和搜索各种平台的内容，无需 API Key 或付费。

### 支持的平台

- 🌐 **网页** - 阅读任意网页内容 (Jina Reader)
- 📺 **YouTube/B站** - 提取视频字幕和元数据 (yt-dlp)
- 🐦 **Twitter/X** - 读取推文、搜索、浏览时间线 (xreach)
- 📖 **Reddit** - 搜索和阅读帖子 (Exa/直接 API)
- 📦 **GitHub** - 搜索仓库、查看 Issue/PR (gh CLI)
- 📕 **小红书** - 搜索笔记、查看详情 (mcporter)
- 🎵 **抖音** - 解析视频信息 (mcporter)
- 💬 **微信公众号** - 搜索和阅读文章 (miku_ai)
- 🎙️ **小宇宙播客** - 音频转文字 (groq-whisper)
- 💼 **LinkedIn** - 查看个人资料 (mcporter)
- 📰 **微博/V2EX/RSS** - 社交媒体和订阅源

---

## 触发词 (Triggers)

当用户说以下关键词时，Agent 应自动调用 Agent Reach：

- **搜索类**: "搜一下", "搜索", "上网搜", "帮我查", "查一下", "web search", "search", "research"
- **视频类**: "看视频", "YouTube", "B站", "bilibili", "抖音", "douyin", "视频字幕"
- **社交类**: "推特", "Twitter", "X", "小红书", "微博", "Reddit", "V2EX"
- **开发类**: "GitHub", "看仓库", "搜代码", "issue"
- **文章类**: "公众号", "微信文章", "知乎", "网页内容", "read this link"
- **播客类**: "小宇宙", "播客", "podcast", "音频转录"

---

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

---

## 使用示例

直接告诉 Agent 你的需求，它会自动调用合适的工具：

- "帮我看看这个 YouTube 视频讲了什么"
- "搜一下 Twitter 上关于 AI 的讨论"
- "看看这个 GitHub 仓库是做什么的"
- "小红书上有哪些关于旅游的笔记"
- "这个网页的主要内容是什么"
- "把这篇公众号文章转成 Markdown"

---

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

---

## 安装

### Surfin Claw 用户

```
帮我安装技能：https://github.com/anjun/Agent-Reach
```

或手动安装：

```bash
mkdir -p ~/.surfin-claw/skills/agent-reach
curl -o ~/.surfin-claw/skills/agent-reach/SKILL.md \
  https://raw.githubusercontent.com/anjun/Agent-Reach/main/agent_reach/skill/SKILL.md
```

### 其他平台

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

## 依赖

- Python 3.10+
- Node.js（用于 xreach、mcporter）
- yt-dlp（视频下载）
- gh CLI（GitHub 操作）

---

## 配置

配置文件位于 `~/.agent-reach/config.yaml`

```yaml
# Twitter 认证
auth:
  twitter_auth_token: your_token
  twitter_ct0: your_ct0

# 代理（服务器部署时需要）
proxy: http://your-proxy:port

# Groq API Key（小宇宙播客转录用）
groq_api_key: your_key
```

---

## 故障排查 (Troubleshooting)

### agent-reach doctor 显示某个渠道不可用

| 问题 | 解决方案 |
|------|----------|
| xreach 未安装 | `npm install -g xreach-cli` |
| mcporter 未安装 | `npm install -g mcporter` |
| yt-dlp 未安装 | `pip install yt-dlp` |
| gh CLI 未安装 | `brew install gh` 或从官网下载 |

### YouTube/B站 403 错误

服务器 IP 可能被屏蔽，解决方案：
- 本地电脑无需额外配置
- 服务器部署时配置代理：`agent-reach configure proxy`

### Twitter 403/无法读取

需要配置认证信息：
1. 浏览器登录 Twitter
2. 使用 Cookie-Editor 插件导出 Cookie
3. 告诉 Agent "帮我配置 Twitter"

### 小红书无法访问

同 Twitter，需要导出 Cookie 配置

### 微信公众号读取失败

微信公众号有反爬机制，请使用：
```bash
cd ~/.agent-reach/tools/wechat-article-for-ai && python3 main.py "文章URL"
```

---

## 安全说明

- Cookie 和 Token 只存储在本地 `~/.agent-reach/`，不上传
- 配置文件权限设置为 600（仅所有者可读写）
- 代码完全开源，可随时审查

---

## Surfin Claw 适配说明

本版本针对 Surfin Claw 进行了适配：
- ✅ 使用 Surfin Claw 内置工具（bash/webfetch/websearch）
- ✅ 技能目录自动识别 `~/.surfin-claw/skills/`
- ✅ 移除 OpenClaw 专属配置依赖

---

## 项目来源

本项目 Fork 自：[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

原项目是一个开源的 AI Agent 互联网数据获取工具，支持 OpenClaw 等平台。

---

## 反馈与支持

- **问题反馈**: https://github.com/anjun/Agent-Reach/issues
- **原项目**: https://github.com/Panniantong/Agent-Reach
