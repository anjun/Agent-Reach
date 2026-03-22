---
name: agent-reach
description: 给 AI Agent 装上互联网能力，支持抓取 Twitter/X、Reddit、YouTube、GitHub、B 站、小红书、微信公众号等 16+ 平台的内容
---

# Agent Reach 技能

## ⚠️ 重要说明

**本技能为全局安装模式**，需要先安装 `agent-reach` Python 包，并在调用时激活虚拟环境。

### 前置条件

1. **安装 agent-reach**（首次使用）：
   ```bash
   pip3 install agent-reach
   ```

2. **虚拟环境位置**：`~/.agent-reach-venv`

3. **激活方式**：
   ```bash
   source ~/.agent-reach-venv/bin/activate
   ```

## 适用场景

当用户需要读取或搜索互联网内容时使用，包括：
- 查看视频字幕（YouTube、B 站）
- 搜索社交媒体（Twitter、小红书、微博）
- 查看 GitHub 仓库、Issue、PR
- 阅读网页内容、公众号文章
- 搜索 Reddit、V2EX 等社区

## 支持的平台

| 平台 | 状态 | 工具 |
|------|------|------|
| 网页 | ✅ 可用 | Jina Reader |
| YouTube | ✅ 可用 | yt-dlp |
| B 站 | ✅ 可用 | yt-dlp |
| Twitter/X | ✅ 可用 | xreach |
| Reddit | ✅ 可用 | Exa/API |
| GitHub | ✅ 可用 | gh CLI |
| 微信公众号 | ✅ 可用 | miku_ai |
| 微博 | ✅ 可用 | 公开 API |
| V2EX | ✅ 可用 | 公开 API |
| RSS | ✅ 可用 | feedparser |
| 小红书 | ⚙️ 需配置 | mcporter |
| 抖音 | ⚙️ 需配置 | mcporter |
| LinkedIn | ⚙️ 需配置 | mcporter |
| 小宇宙播客 | ⚙️ 需配置 | groq-whisper |

## 在 Surfin Claw 中的调用方式

### 方式 1：使用 bash 命令（推荐）

```bash
# 激活虚拟环境后执行
source ~/.agent-reach-venv/bin/activate && agent-reach doctor
```

### 方式 2：使用技能脚本

```bash
# 通过 scripts/run.py 调用
bash({skill: "agent-reach", program: "python3", script: "scripts/run.py", args: "doctor"})
```

### 方式 3：直接使用完整路径

```bash
~/.agent-reach-venv/bin/agent-reach doctor
```

## 操作步骤

### 1. 检测环境

首先运行 doctor 检查所有渠道状态：

```bash
source ~/.agent-reach-venv/bin/activate && agent-reach doctor
```

### 2. 根据用户需求选择工具

**读取网页内容：**
```bash
curl -s "https://r.jina.ai/URL"
```

**YouTube/B 站 视频字幕：**
```bash
yt-dlp --dump-json "URL"
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --skip-download -o "/tmp/%(id)s" "URL"
```

**Twitter/X：**
```bash
xreach tweet "URL_OR_ID" --json
xreach search "query" -n 10 --json
```

**GitHub：**
```bash
gh repo view owner/repo
gh search repos "query" --sort stars --limit 10
gh issue list -R owner/repo --state open
```

**Reddit：**
```bash
curl -s "https://www.reddit.com/r/SUBREDDIT/hot.json?limit=10" -H "User-Agent: agent-reach/1.0"
```

**微信公众号：**
```bash
source ~/.agent-reach-venv/bin/activate && python3 -c "import asyncio; from miku_ai import get_wexin_article; result = asyncio.run(get_wexin_article('URL')); print(result)"
```

### 3. 配置认证（如需要）

对于需要登录的平台（Twitter、小红书等）：

1. 浏览器登录目标平台
2. 使用 Cookie-Editor 插件导出 Cookie
3. 运行配置命令：
   ```bash
   source ~/.agent-reach-venv/bin/activate && agent-reach configure twitter
   source ~/.agent-reach-venv/bin/activate && agent-reach configure xiaohongshu
   ```

### 4. 处理结果

- 提取关键信息并总结
- 如遇到 403 错误，建议配置代理
- 如工具未安装，提示用户安装对应依赖

## 输出格式

根据平台类型输出结构化内容：

**视频内容：**
- 标题
- 作者
- 发布时间
- 字幕摘要（关键内容）

**社交媒体：**
- 帖子内容
- 作者信息
- 互动数据（点赞、评论、转发）
- 热门评论（如有）

**GitHub：**
- 仓库描述
- Star/Fork 数
- 最近更新
- Issue/PR 状态

**网页文章：**
- 标题
- 作者/来源
- 发布时间
- 内容摘要

## 注意事项

1. **隐私安全**：Cookie 只存储在本地 `~/.agent-reach/`，不上传
2. **代理配置**：服务器部署时可能需要配置代理
3. **错误处理**：
   - 403 错误：建议配置代理或检查认证
   - 工具未安装：提示用户安装对应命令
   - 超时：重试或建议用户检查网络
4. **内容长度**：长内容自动分段，保留关键信息
5. **虚拟环境**：所有 agent-reach 命令都需要先激活虚拟环境

## 故障排查

| 问题 | 解决方案 |
|------|----------|
| xreach 未安装 | `source ~/.agent-reach-venv/bin/activate && pip install xreach-cli` |
| mcporter 未安装 | `source ~/.agent-reach-venv/bin/activate && pip install mcporter` |
| yt-dlp 未安装 | `source ~/.agent-reach-venv/bin/activate && pip install yt-dlp` |
| gh CLI 未安装 | `brew install gh` |
| YouTube 403 | 配置代理：`agent-reach configure proxy` |
| Twitter 403 | 导出 Cookie 配置认证 |
| ModuleNotFoundError | 确认已激活虚拟环境：`source ~/.agent-reach-venv/bin/activate` |

## 技术实现

Agent Reach 是一个脚手架工具，实际调用上游工具完成工作：
- Jina Reader：网页内容
- yt-dlp：视频字幕
- xreach：Twitter/X
- gh CLI：GitHub
- mcporter：小红书、抖音、LinkedIn（MCP）
- miku_ai：微信公众号

## 项目来源

本技能 Fork 自 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
适配 Surfin Claw 平台使用。

## 反馈与支持

- **问题反馈**: https://github.com/anjun/Agent-Reach/issues
- **原项目**: https://github.com/Panniantong/Agent-Reach
