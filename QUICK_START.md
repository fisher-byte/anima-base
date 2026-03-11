# 快速开始指南

## 🚀 一键启动

### 1. 安装依赖

```bash
cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled

# 安装Python依赖
pip install yt-dlp feedparser beautifulsoup4 requests
```

### 2. 运行一键采集

```bash
cd scripts
bash run_collection.sh
```

### 3. 配置定时任务

```bash
# 生成cron配置
python scheduler.py cron

# 添加到crontab
crontab -e
# 粘贴生成的配置
```

---

## 📋 每日任务

### 自动执行（通过Cron）
- **08:00** - RSS文章采集
- **09:00** - YouTube字幕采集
- **20:00** - 文档翻译（周日）
- **14:00** - 播客音频采集（周日）
- **每15分钟** - GitHub同步

### 手动执行

```bash
# YouTube字幕
python youtube_subtitle_downloader.py

# RSS文章
python rss_article_downloader.py

# 播客音频
python podcast_audio_downloader.py

# 文档翻译
python auto_translator.py high
```

---

## 📊 监控执行

### 查看日志

```bash
# 所有日志
ls -lt scripts/logs/

# RSS采集日志
tail -f scripts/logs/daily_rss.log

# YouTube采集日志
tail -f scripts/logs/daily_youtube.log

# 翻译日志
tail -f scripts/logs/weekly_translation.log

# 集合日志
tail -f collection.log
```

### 检查状态

```bash
# 系统健康检查
python maintenance.py --health

# 文件统计
python maintenance.py --stats

# 生成报告
python maintenance.py --report
```

---

## 🎯 关键指标

### 原文文件
```bash
# 媒体文件
find media -type f | wc -l

# 文档文件
find files -type f | wc -l
```

### 翻译文件
```bash
# 中文翻译
find translations/zh-cn -type f | wc -l
```

---

## 🛠️ 故障排查

### YouTube下载失败
```bash
# 检查yt-dlp版本
yt-dlp --version

# 更新yt-dlp
pip install --upgrade yt-dlp
```

### RSS采集失败
```bash
# 测试RSS源
python3 -c "import feedparser; print(feedparser.parse('https://www.lennysnewsletter.com/feed').entries[:1])"
```

### 翻译失败
```bash
# 检查API配置
python3 -c "import os; print(os.getenv('OPENAI_API_KEY'))"
```

---

## 📞 获取帮助

- 详细文档：`README.md`
- 执行计划：`AUTO_EXECUTION_PLAN.md`
- 架构设计：`STRUCTURE.md`
- 存储策略：`FILE_STORAGE_POLICY.md`
- 翻译策略：`TRANSLATION_POLICY.md`

---

**更新日期**: 2026-03-11
