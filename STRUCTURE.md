# Anima Base - 完整知识库系统

## 目录结构规范

```
anima-base/
├── README.md                    # 项目主文档（中文）
├── README.en.md                 # 项目主文档（英文）
├── ROADMAP.md                   # 路线图与计划（中文）
├── ROADMAP.en.md                # 路线图与计划（英文）
├── SOURCES.md                   # 来源清单与追踪
├── STRUCTURE.md                 # 本文件 - 目录结构说明
├── CONTENT_EXPANSION_PLAN.md   # 内容扩充计划（中文）
├── CONTENT_EXPANSION_PLAN.en.md # 内容扩充计划（英文）
├── CONTENT_QUALITY.md           # 内容质量标准
├── FILE_STORAGE_POLICY.md       # 原文文件存储规范
├── TRANSLATION_POLICY.md         # 双语翻译策略
│
├── people/                      # 核心人物内容库（英文原文为主）
│   ├── product/                 # 产品管理专家
│   ├── growth/                  # 增长领域专家
│   ├── marketing/               # 营销领域专家
│   ├── leadership/              # 领导力专家
│   └── startup/                 # 创业专家
│
├── translations/                # 翻译内容（中文为主）
│   ├── zh-cn/                   # 中文翻译
│   │   ├── README.md            # 翻译说明
│   │   ├── {category}/          # product/growth/marketing/leadership/startup
│   │   │   └── {person-name}/
│   │   │       ├── profile.zh-cn.md
│   │   │       ├── quotes.zh-cn.md
│   │   │       ├── frameworks/
│   │   │       ├── podcasts/
│   │   │       ├── articles/
│   │   │       ├── books/
│   │   │       └── sources.zh-cn.md
│   │   └── topics/              # 主题翻译
│   └── en/                       # 英文（作为备份）
│       └── {category}/
│
├── media/                       # 多媒体原始文件（语言无关）
│   ├── audio/                   # 音频（原语言）
│   ├── video/                   # 视频（原语言）
│   └── ebook/                   # 电子书（原语言）
│
├── files/                       # 文档原始文件（语言无关）
│   ├── pdf/                     # PDF文档（原语言）
│   └── articles/                # 网页文章HTML（原语言）
│
├── topics/                      # 按主题聚合的内容（英文）
├── index/                       # 主题索引（英文）
├── sources/                     # 来源追踪
│
├── scripts/                     # 自动化脚本
│   ├── translator.py           # 翻译工具
│   ├── sync_translations.py    # 同步翻译文件
│   ├── check_translation.py    # 检查翻译完整性
│   ├── index_generator.py
│   ├── content_collector.py
│   ├── content_miner.py
│   ├── media_downloader.py
│   ├── document_collector.py
│   ├── rss_collector.py
│   ├── sync-github.sh
│   ├── collect-and-sync.sh
│   └── monitor-and-fix.sh
│
└── output/                      # 输出目录（临时文件）
    └── {session-id}/
```

## 人物内容目录规范

每个人物目录包含以下标准结构：

```
{person-name}/
├── profile.md              # 人物档案（必需）
├── quotes.md               # 语录合集（必需）
├── frameworks/             # 框架方法论（10-20个，可保留摘要）
├── podcasts/               # 播客索引+摘要（链接到原始MP3/TXT）
│   ├── index.md           # 播客列表（含原始文件链接）
│   └── YYYY-MM-DD-show.md  # 单个播客摘要+洞察
├── articles/               # 文章索引+摘要（链接到原始PDF/HTML）
│   ├── index.md           # 文章列表（含原始文件链接）
│   └── YYYY-MM-DD-title.md # 单篇文章摘要+核心观点
├── talks/                  # 演讲/访谈索引+摘要（链接到原始视频）
│   └── index.md
├── books/                  # 书籍索引+摘要（链接到原始EPUB/PDF）
│   └── index.md
└── sources.md              # 原文文件统计索引（必需）
```

### 双轨制说明

**原文文件**（存储在 `media/` 或 `files/`）：
- 播客音频：`media/audio/{person}/podcast/` (MP3/WAV)
- 转录文本：`media/audio/{person}/podcast/` (TXT/MD)
- 文章PDF：`files/pdf/{person}/articles/` (PDF)
- 网页HTML：`files/articles/{person}/` (HTML)
- 书籍EPUB：`media/ebook/` (EPUB/MOBI)
- 视频文件：`media/video/{person}/` (MP4)

**索引文件**（存储在 `people/.../`）：
- 提供元数据和快速访问
- 包含原始文件的相对路径链接
- 保留摘要和框架提取（可选）

**翻译文件**（存储在 `translations/zh-cn/.../`）：
- 人物档案：`profile.zh-cn.md`
- 语录合集：`quotes.zh-cn.md`
- 框架文档：`frameworks/*.zh-cn.md`
- 播客文档：`podcasts/*.zh-cn.md`
- 文章文档：`articles/*.zh-cn.md`
- 书籍索引：`books/index.zh-cn.md`

详见：
- [FILE_STORAGE_POLICY.md](./FILE_STORAGE_POLICY.md) - 原文存储
- [TRANSLATION_POLICY.md](./TRANSLATION_POLICY.md) - 双语翻译

## 文件格式规范

### 每个内容文件必须包含 Frontmatter：

```yaml
---
type: profile|quote|framework|podcast|article|talk|book
person: 人物名称
title: 内容标题
date: YYYY-MM-DD
date_collected: YYYY-MM-DD HH:MM:SS
source:
  name: 来源名称
  url: 来源URL
  type: rss|podcast|newsletter|twitter|youtube|website|book
  author: 原作者（如适用）
  published: 原始发布日期
  language: en|zh
collection_method: rss|api|manual|script
tags: [tag1, tag2, tag3]
related: [related-person-1, related-person-2]
status: raw|processed|summarized|verified
---
```

## 来源类型定义

| 类型 | 描述 | 采集方式 |
|------|------|----------|
| RSS | RSS订阅源 | 自动采集 |
| Podcast | 播客音频 | 转录+人工校对 |
| Newsletter | 邮件订阅 | RSS/API/手动 |
| Twitter/X | 社交媒体 | API抓取 |
| YouTube | 视频平台 | 字幕提取 |
| Website | 网站文章 | RSS/爬虫/手动 |
| Book | 书籍 | OCR/电子书/手动 |

## 采集状态追踪

每个来源必须有：
- 最后采集时间
- 采集频率
- 状态（活跃/暂停/失败）
- 失败次数
- 负责人

## 质量标准

1. **完整性**: 保留原始内容的完整性
2. **可追溯性**: 每个内容都能追溯到原始来源
3. **结构化**: 统一格式，便于检索
4. **可验证**: 保留原始URL和时间戳

## 人物分类规则

| 分类 | 标签 | 主要领域 |
|------|------|----------|
| product | 产品专家 | 产品管理、产品策略、用户研究 |
| growth | 增长专家 | 增长黑客、增长策略、用户增长 |
| marketing | 营销专家 | 品牌营销、内容营销、营销定位 |
| leadership | 领导力专家 | 组织管理、文化打造、领导力 |
| startup | 创业专家 | 创业方法论、融资、公司建设 |

## 索引系统

`index/` 目录提供按主题分类的内容索引，每个主题索引文件包含：
- 相关人物列表
- 核心框架/方法论链接
- 重要文章和播客
- 统计信息

## 脚本功能

### index_generator.py
- 扫描people/目录生成索引
- 按主题分类内容
- 统计内容数量

### content_collector.py
- 从RSS/Newsletter采集内容
- 自动归档到对应人物目录
- 标注来源信息

### content_miner.py
- 挖掘框架和方法论
- 提取核心洞察
- 生成结构化文档

## 版本历史

- v2.0 (2026-03-11): 统一people目录结构，消除重复
- v1.0: 初始版本，分离product/growth/marketing/leadership顶层目录
