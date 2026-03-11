# Anima Base 自动化执行计划

## 📊 当前状态（2026-03-11）

### ✅ 已完成
- "原文优先+双语支持"架构重构
- 核心文档更新至 v3.0（STRUCTURE.md、CONTENT_EXPANSION_PLAN.md）
- 原文存储和翻译策略文档（FILE_STORAGE_POLICY.md、TRANSLATION_POLICY.md）
- 5位核心专家完整档案（Gokul/Brian/Shreyas/Marty/Lenny）
- Git同步自动化（每15分钟）

### ⚠️ 严重缺失
- **原文文件几乎为空**：media/ 和 files/ 目录
- 翻译工作未启动
- 定时任务未配置cron
- 新建脚本未添加到定时调度

---

## 🎯 新执行计划

### Phase 1: 原文文件收集（最高优先级）

#### 1.1 安装依赖工具
```bash
# 安装 yt-dlp（YouTube下载）
pip install yt-dlp

# 安装 feedparser（RSS解析）
pip install feedparser

# 安装 beautifulsoup4（HTML解析）
pip install beautifulsoup4
```

#### 1.2 配置环境变量
创建 `.env` 文件（可选，用于API配置）：
```env
# OpenAI API（用于翻译）
OPENAI_API_KEY=your_key_here

# Twitter API（可选）
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_key
TWITTER_BEARER_TOKEN=your_key
```

#### 1.3 初始化原文收集

**Day 1 - YouTube字幕下载**
```bash
# 下载核心5位专家的YouTube字幕
cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/scripts
python youtube_subtitle_downloader.py

# 查看结果
ls -la ../media/audio/youtube/
```

**Day 2 - RSS文章下载**
```bash
# 下载产品领域文章
python rss_article_downloader.py product

# 下载营销领域文章
python rss_article_downloader.py marketing

# 下载增长领域文章
python rss_article_downloader.py growth
```

**Day 3 - 播客音频下载**
```bash
# 下载Lenny's Podcast
python podcast_audio_downloader.py lennys-podcast

# 下载Masters of Scale（Brian Chesky）
python podcast_audio_downloader.py masters-of-scale
```

---

### Phase 2: 翻译自动化

#### 2.1 配置翻译API

**选项A：使用OpenAI API（推荐）**
1. 获取OpenAI API Key
2. 在 `scripts/auto_translator.py` 中配置：
```python
# 在translate_text方法中添加OpenAI API调用
import openai
openai.api_key = "your_api_key"

def translate_text(text, file_context=""):
    # 调用GPT-4进行翻译
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "你是一个专业翻译，将英文翻译为中文，保持Markdown格式。"},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
```

**选项B：使用本地模型（离线）**
```bash
# 安装Hugging Face模型
pip install transformers torch

# 下载中文翻译模型
python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-zh')"
```

#### 2.2 执行翻译

```bash
# 翻译高优先级文档（干运行模式）
python auto_translator.py high --dry-run

# 确认无误后执行翻译
python auto_translator.py high

# 翻译中优先级文档
python auto_translator.py medium
```

---

### Phase 3: 定时任务配置

#### 3.1 测试所有脚本

```bash
cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/scripts

# 测试调度器
python scheduler.py list

# 测试单个任务
python scheduler.py run daily_rss_collect
```

#### 3.2 配置Cron定时任务

```bash
# 编辑crontab
crontab -e

# 添加以下配置（替换路径为实际路径）
# 每天8点 - RSS采集
0 8 * * * cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/scripts && python3 rss_article_downloader.py >> logs/daily_rss.log 2>&1

# 每天9点 - YouTube字幕采集
0 9 * * * cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/scripts && python3 youtube_subtitle_downloader.py >> logs/daily_youtube.log 2>&1

# 周日下午2点 - 播客采集
0 14 * * 0 cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/scripts && python3 podcast_audio_downloader.py >> logs/weekly_podcast.log 2>&1

# 周日晚上8点 - 文档翻译
0 20 * * 0 cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/scripts && python3 auto_translator.py high >> logs/weekly_translation.log 2>&1

# 每15分钟 - GitHub同步
*/15 * * * * cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled && bash scripts/sync-github.sh >> logs/github_sync.log 2>&1
```

#### 3.3 使用调度器（简化管理）

```bash
# 生成cron配置
python scheduler.py cron

# 复制输出到crontab
crontab -e
```

---

### Phase 4: 监控和维护

#### 4.1 查看执行日志

```bash
# 查看最新日志
ls -lt /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/scripts/logs/

# 查看RSS采集日志
tail -f logs/daily_rss.log

# 查看YouTube采集日志
tail -f logs/daily_youtube.log

# 查看翻译日志
tail -f logs/weekly_translation.log
```

#### 4.2 检查采集进度

```bash
# 检查原文文件
find /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/media -type f | wc -l
find /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/files -type f | wc -l

# 检查翻译文件
find /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/translations -type f | wc -l

# 查看集合日志
tail -f /Users/zhiyangyu/.box/Workspace/anima-base-scheduled/collection.log
```

#### 4.3 故障排查

**YouTube下载失败**
```bash
# 检查yt-dlp版本
yt-dlp --version

# 更新yt-dlp
pip install --upgrade yt-dlp

# 检查网络连接
ping youtube.com
```

**RSS采集失败**
```bash
# 手动测试RSS源
python3 -c "import feedparser; print(feedparser.parse('https://www.lennysnewsletter.com/feed').entries[:1])"
```

**翻译失败**
```bash
# 测试OpenAI API
python3 -c "import openai; print(openai.api_key)"
```

---

## 📋 执行检查清单

### Week 1: 原文收集
- [ ] 安装 yt-dlp
- [ ] 安装 feedparser 和 beautifulsoup4
- [ ] 下载Lenny Rachitsky YouTube字幕
- [ ] 下载Brian Chesky YouTube字幕
- [ ] 下载Shreyas Doshi YouTube字幕
- [ ] 下载Marty Cagan YouTube字幕
- [ ] 下载Gokul Rajaram YouTube字幕
- [ ] 下载产品领域RSS文章（3个源）
- [ ] 下载营销领域RSS文章（3个源）
- [ ] 下载增长领域RSS文章（3个源）

### Week 2: 播客与翻译
- [ ] 下载Lenny's Podcast（10集）
- [ ] 下载Masters of Scale（5集）
- [ ] 配置OpenAI API Key
- [ ] 测试翻译脚本（干运行）
- [ ] 翻译高优先级文档（5个profile + quotes）
- [ ] 翻译核心框架文档（SPADE等）

### Week 3: 自动化
- [ ] 配置cron定时任务
- [ ] 测试每日RSS采集
- [ ] 测试每日YouTube采集
- [ ] 测试周播客采集
- [ ] 测试周翻译任务
- [ ] 验证GitHub同步

### Week 4: 验证与优化
- [ ] 统计原文文件数量
- [ ] 统计翻译文件数量
- [ ] 检查采集日志错误
- [ ] 优化采集参数
- [ ] 生成执行报告

---

## 🎯 目标指标

### 短期目标（4周）
- **原文文件**：200+ 文件（字幕、文章、音频）
- **翻译文件**：50+ 文件（核心文档）
- **自动化率**：80%（每日任务自动执行）
- **错误率**：<5%（采集失败率）

### 中期目标（3个月）
- **原文文件**：1000+ 文件
- **翻译文件**：300+ 文件
- **人物覆盖**：10人（核心5位 + 其他5位）
- **自动化率**：90%

### 长期目标（1年）
- **原文文件**：5000+ 文件
- **翻译文件**：2000+ 文件
- **人物覆盖**：30+ 人
- **自动化率**：95%

---

## 🛠️ 脚本使用说明

### YouTube字幕下载器
```bash
# 下载所有核心专家
python youtube_subtitle_downloader.py

# 下载指定专家
python youtube_subtitle_downloader.py lenny-rachitsky,brian-chesky
```

### RSS文章下载器
```bash
# 下载所有RSS源
python rss_article_downloader.py

# 下载指定类别
python rss_article_downloader.py product

# 下载指定源
python rss_article_downloader.py product "Lenny's Newsletter"
```

### 播客音频下载器
```bash
# 下载所有播客
python podcast_audio_downloader.py

# 下载指定播客
python podcast_audio_downloader.py lennys-podcast,masters-of-scale
```

### 自动翻译器
```bash
# 翻译高优先级（干运行）
python auto_translator.py high --dry-run

# 翻译高优先级
python auto_translator.py high

# 翻译中优先级
python auto_translator.py medium
```

### 任务调度器
```bash
# 列出所有任务
python scheduler.py list

# 运行指定任务
python scheduler.py run daily_rss_collect

# 运行所有任务
python scheduler.py run-all

# 生成cron配置
python scheduler.py cron
```

---

## 📞 故障支持

### 常见问题

**Q: YouTube下载速度慢？**
A: 使用代理或更换下载时间（如凌晨）

**Q: RSS采集失败率高？**
A: 检查RSS源是否有效，部分网站可能有反爬限制

**Q: 翻译成本高？**
A: 可以批量翻译，或使用更便宜的API（如Claude、本地模型）

**Q: 磁盘空间不足？**
A: 定期清理旧日志，或使用压缩存储音频文件

**Q: 定时任务不执行？**
A: 检查cron服务状态：`sudo systemctl status cron` (Linux) 或检查系统设置（macOS）

---

**创建日期**: 2026-03-11
**版本**: 1.0
**维护者**: Anima Base Team
