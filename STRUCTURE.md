# Anima Base - 完整知识库系统

## 目录结构规范

```
anima-base/
├── README.md                    # 项目主文档
├── ROADMAP.md                   # 路线图与计划
├── SOURCES.md                   # 来源清单与追踪
├── COLLECTION_LOG.md            # 采集日志
│
├── product/                     # 产品领域
│   ├── {person-name}/
│   │   ├── README.md            # 人物导航页
│   │   ├── profile.md           # 人物档案
│   │   ├── quotes/              # 语录合集
│   │   │   ├── README.md
│   │   │   ├── from-twitter.md
│   │   │   ├── from-podcasts.md
│   │   │   └── from-books.md
│   │   ├── podcasts/            # 播客转录
│   │   │   ├── README.md
│   │   │   ├── lennys-podcast-2024-01-15.md
│   │   │   └── how-i-built-this-2023-08-20.md
│   │   ├── books/               # 书籍内容
│   │   │   ├── README.md
│   │   │   ├── inspired-chapter-summary.md
│   │   │   └── empowered-chapter-summary.md
│   │   ├── articles/            # 文章归档
│   │   │   ├── README.md
│   │   │   ├── from-newsletter-2024-03.md
│   │   │   └── from-blog-2024-02.md
│   │   └── talks/               # 演讲/访谈
│   │       ├── README.md
│   │       └── ted-talk-2024.md
│   └── ...
│
├── marketing/                   # 营销领域
├── growth/                      # 增长领域
├── leadership/                  # 领导力领域
│
├── index/                       # 主题索引
│   ├── README.md
│   ├── product-management.md
│   ├── growth-strategy.md
│   └── ...
│
├── sources/                     # 来源追踪
│   ├── README.md
│   ├── rss-feeds.md
│   ├── podcasts.md
│   ├── newsletters.md
│   └── websites.md
│
└── scripts/                     # 自动化脚本
    ├── rss_collector.py
    ├── podcast_downloader.py
    ├── content_indexer.py
    └── sync_github.sh
```

## 文件格式规范

### 每个内容文件必须包含：

```yaml
---
type: profile|quotes|podcast|book|article|talk
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
