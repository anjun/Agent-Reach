# Surfin Claw 安装指南

**版本**: 1.0.0  
**更新日期**: 2026-03-22

---

## 快速安装

### 1. 安装 agent-reach CLI

```bash
pip install agent-reach
```

或从源码安装（推荐，获取最新适配）：

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

# 安装 Node 工具
npm install -g xreach-cli mcporter

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

或使用 Surfin Claw 命令安装：
```
帮我安装技能：https://github.com/anjun/Agent-Reach
```

### 4. 验证安装

```bash
agent-reach doctor
```

预期输出示例：
```
✓ web        - Jina Reader (可用)
✓ youtube    - yt-dlp (可用)
✓ twitter    - xreach (可用)
✓ github     - gh CLI (可用)
✓ bilibili   - yt-dlp (可用)
? reddit     - 需要配置代理
? xiaohongshu - 需要登录
```

---

## 配置各平台

### Twitter/X

1. 浏览器登录 Twitter
2. 安装 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor) 插件
3. 导出 Cookie 为 JSON
4. 告诉 Agent："帮我配置 Twitter"，粘贴 Cookie

```bash
agent-reach configure twitter
```

### 小红书

1. 浏览器登录小红书
2. 使用 Cookie-Editor 导出 Cookie
3. 告诉 Agent："帮我配置小红书"，粘贴 Cookie

```bash
agent-reach configure xiaohongshu
```

### 代理（服务器部署时需要）

```bash
agent-reach configure proxy http://your-proxy:port
```

### Groq API Key（小宇宙播客转录用）

```bash
agent-reach configure groq-key YOUR_GROQ_API_KEY
```

---

## 使用

安装完成后，直接告诉 Agent 你的需求：

| 需求 | 示例指令 |
|------|----------|
| 看视频 | "帮我看看这个 YouTube 视频讲了什么" |
| 搜推特 | "搜一下 Twitter 上关于 AI 的讨论" |
| 看仓库 | "看看这个 GitHub 仓库是做什么的" |
| 搜小红书 | "小红书上有哪些关于旅游的笔记" |
| 读网页 | "这个网页的主要内容是什么" |
| 读公众号 | "把这篇公众号文章转成 Markdown" |
| 搜 Reddit | "Reddit 上怎么评价这个产品" |

Agent 会自动调用合适的工具，无需记忆具体命令。

---

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

---

## 故障排查

### Q: doctor 显示某些工具未安装？

```bash
# 重新安装 Node 工具
npm install -g xreach-cli mcporter

# 重新安装 Python 包
pip install --force-reinstall agent-reach yt-dlp
```

### Q: YouTube/B站 报错 403？

- 本地电脑：通常无需配置
- 服务器：配置代理 `agent-reach configure proxy`

### Q: 如何清除配置？

```bash
rm ~/.agent-reach/config.yaml
```

### Q: Cookie 安全吗？

- 只存储在本地 `~/.agent-reach/`
- 文件权限 600（仅所有者可读写）
- 不上传到任何服务器

---

## 反馈与支持

- **问题反馈**: https://github.com/anjun/Agent-Reach/issues
- **原项目**: https://github.com/Panniantong/Agent-Reach
- **Surfin Claw**: 内部项目

---

**祝你使用愉快！**
