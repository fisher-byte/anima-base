# Anima Base 原文文件存储规范

## 📁 目录结构

```
anima-base/
├── media/                           # 多媒体原始文件
│   ├── audio/                       # 音频文件
│   │   ├── {person-name}/           # 按人物分类
│   │   │   ├── podcast/             # 播客音频
│   │   │   │   ├── {date}-show-name.mp3
│   │   │   │   └── {date}-show-name-transcript.md
│   │   │   └── interview/           # 访谈音频
│   │   └── youtube/                 # YouTube视频音频
│   │       └── {video-id}.mp3
│   ├── video/                       # 视频文件
│   │   ├── {person-name}/
│   │   │   ├── ted-talks/           # TED演讲
│   │   │   ├── conference/          # 会议演讲
│   │   │   └── interviews/          # 视频访谈
│   └── ebook/                       # 电子书（EPUB, MOBI等）
│       └── {isbn-or-title}.{epub|mobi}
│
├── files/                           # 文档原始文件
│   ├── pdf/                         # PDF文档
│   │   ├── {person-name}/
│   │   │   ├── articles/            # PDF文章
│   │   │   │   └── {date}-title.pdf
│   │   │   ├── whitepapers/         # 白皮书
│   │   │   ├── presentations/        # 演示文稿（PDF格式）
│   │   │   └── books/               # PDF书籍
│   │   │       └── {title}-{year}.pdf
│   └── articles/                    # 网页文章原始HTML
│       └── {person-name}/
│           └── {date}-title.html
│
└── people/                          # 人物内容库
    └── {category}/                  # product/growth/marketing/leadership/startup
        └── {person-name}/
            ├── profile.md           # 人物档案
            ├── quotes.md            # 语录合集
            ├── frameworks/          # 方法论框架（可保留摘要）
            ├── articles/            # 文章索引+摘要
            │   ├── YYYY-MM-DD-title.md
            │   └── index.md        # 文章列表
            ├── podcasts/            # 播客索引+摘要
            │   ├── YYYY-MM-DD-show.md
            │   └── index.md
            ├── talks/               # 演讲索引+摘要
            ├── books/               # 书籍索引+摘要
            └── sources.md           # 原文文件索引
```

## 🎯 存储原则

### 1. 优先保留原始文件
| 类型 | 原始格式 | 存储位置 | 对应索引 |
|------|---------|---------|---------|
| 播客 | MP3/WAV | `media/audio/{person}/podcast/` | `people/.../podcasts/index.md` |
| 转录 | TXT/MD | `media/audio/{person}/podcast/` | - |
| 文章 | PDF/HTML | `files/pdf/{person}/articles/` | `people/.../articles/index.md` |
| 书籍 | EPUB/PDF | `media/ebook/` 或 `files/pdf/{person}/books/` | `people/.../books/index.md` |
| 视频 | MP4 | `media/video/{person}/` | `people/.../talks/index.md` |
| 演示文稿 | PDF/PPTX | `files/pdf/{person}/presentations/` | - |

### 2. 双轨制：原文 + 索引 + 翻译
**原文文件**：存储在 `media/` 或 `files/`，保留完整原貌
**索引文件**：存储在 `people/{category}/{person}/`，提供元数据和快速访问（英文）
**翻译文件**：存储在 `translations/zh-cn/{category}/{person}/`，提供中文翻译

示例：
```
# 原文文件
media/audio/gokul-rajaram/podcast/2024-03-10-lennys-podcast.mp3
media/audio/gokul-rajaram/podcast/2024-03-10-lennys-podcast-transcript.txt

# 索引文件（英文）
people/product/gokul-rajaram/podcasts/index.md
people/product/gokul-rajaram/podcasts/2024-03-10-lennys-podcast.md

# 翻译文件（中文）
translations/zh-cn/product/gokul-rajaram/podcasts/index.zh-cn.md
translations/zh-cn/product/gokul-rajaram/podcasts/2024-03-10-lennys-podcast.zh-cn.md
```

**双语链接**：
- 英文文件 → 中文：`[中文版](../../translations/zh-cn/product/gokul-rajaram/podcasts/2024-03-10-lennys-podcast.zh-cn.md)`
- 中文文件 → 英文：`[English Version](../../../people/product/gokul-rajaram/podcasts/2024-03-10-lennys-podcast.md)`

详见：[TRANSLATION_POLICY.md](./TRANSLATION_POLICY.md)

### 3. 文件命名规范

#### 音频文件
```
{YYYY-MM-DD}-{show-name}-{speaker}.{mp3|wav|m4a}
{YYYY-MM-DD}-{show-name}-transcript.{txt|md}
```

#### PDF文件
```
{YYYY-MM-DD}-{title-slug}.{pdf}
{title}-{year}.{pdf}
```

#### HTML文件
```
{YYYY-MM-DD}-{title-slug}.html
```

#### 电子书
```
{isbn}.{epub|mobi}
{title-slug}-{year}.{epub|mobi}
```

## 📝 索引文件格式

### podcasts/index.md
```markdown
---
type: index
person: Gokul Rajaram
category: product
last_updated: 2026-03-11
total_podcasts: 25
---

# Gokul Rajaram - 播客索引

## 2024

| 日期 | 节目名称 | 时长 | 原始文件 | 转录 | 洞察文档 |
|------|---------|------|---------|------|---------|
| 2024-03-10 | Lenny's Podcast #320 | 45:23 | [MP3](../../media/audio/gokul-rajaram/podcast/20240310-lennys-podcast.mp3) | [TXT](../../media/audio/gokul-rajaram/podcast/20240310-lennys-podcast-transcript.txt) | [详情](./2024-03-10-lennys-podcast.md) |
| 2024-01-15 | How I Built This | 52:10 | [MP3](../../media/audio/gokul-rajaram/podcast/20240115-how-i-built-this.mp3) | [TXT](...) | [详情](./2024-01-15-how-i-built-this.md) |
```

### articles/index.md
```markdown
---
type: index
person: Gokul Rajaram
category: product
last_updated: 2026-03-11
total_articles: 150
---

# Gokul Rajaram - 文章索引

## 按来源分类

### Substack
| 日期 | 标题 | 来源 | 原始文件 | 摘要文档 |
|------|------|------|---------|---------|
| 2024-03-05 | Product Leadership Lessons | Substack | [HTML](../../files/articles/gokul-rajaram/20240305-product-leadership-lessons.html) | [详情](./2024-03-05-product-leadership-lessons.md) |
```

### books/index.md
```markdown
---
type: index
person: Gokul Rajaram
category: product
---

# Gokul Rajaram - 书籍索引

| 书名 | 作者 | 出版年 | 原始文件 | 摘要 | 框架提取 |
|------|------|-------|---------|------|---------|
| The Product Manager's Handbook | - | 2023 | [EPUB](../../media/ebook/pm-handbook-2023.epub) | [详情](./pm-handbook-summary.md) | [框架](./pm-handbook-frameworks.md) |
```

## 🔍 查找与引用

### 在人物内容中引用原文
```markdown
## Framework: Product Development Process

**来源**: [Lenny's Podcast #320](../podcasts/2024-03-10-lennys-podcast.md)
**原始音频**: [下载MP3](../../media/audio/gokul-rajaram/podcast/20240310-lennys-podcast.mp3)
**完整转录**: [查看TXT](../../media/audio/gokul-rajaram/podcast/20240310-lennys-podcast-transcript.txt)
```

### 在索引中跨引用
```markdown
**相关音频**: [查看完整播客库](../../media/audio/gokul-rajaram/podcast/)
**相关PDF**: [查看所有文章PDF](../../files/pdf/gokul-rajaram/articles/)
```

## 📥 采集流程

### 播客采集
1. 下载MP3到 `media/audio/{person}/podcast/`
2. 下载/生成转录文件到同目录
3. 在 `people/.../podcasts/` 创建索引+摘要文档

### 文章采集
1. 保存原始HTML到 `files/articles/{person}/`
2. 如有PDF版本，保存到 `files/pdf/{person}/articles/`
3. 在 `people/.../articles/` 创建索引+摘要文档

### 书籍采集
1. 获取EPUB/MOBI到 `media/ebook/`
2. 如有PDF，保存到 `files/pdf/{person}/books/`
3. 在 `people/.../books/` 创建摘要+框架提取

## ⚙️ 自动化工具

### 媒体下载器 (media_downloader.py)
- 下载YouTube视频音频
- 下载播客MP3
- 获取转录文本

### 文档采集器 (document_collector.py)
- 保存网页原始HTML
- 下载PDF
- 提取元数据

### 索引生成器 (index_generator.py)
- 扫描media/和files/目录
- 自动生成index.md文件
- 更新交叉引用

## 📊 存储统计

每个人物目录包含 `sources.md` 文档，统计：
- 音频文件数量及总大小
- PDF文件数量及总大小
- 电子书数量
- HTML文章数量

## 🔐 版权说明

- 仅收集公开可用的资源
- 保留原始来源信息
- 不用于商业用途
- 尊重作者版权

---

**版本**: 1.0
**更新日期**: 2026-03-11
