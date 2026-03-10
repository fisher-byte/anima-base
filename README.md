# Anima Base - 知识与智慧宝库

一个持续收集、整理和归档全球各领域精华内容的知识库。涵盖产品、营销、增长、领导力等领域的名人语录、播客精华和书籍内容。

## 项目结构

```
anima-base/
├── product/          # 产品领域
│   └── {人物名称}/
│       ├── profile.md      # 人物简介
│       ├── quotes.md       # 经典语录
│       ├── podcast/        # 播客内容
│       ├── books/          # 书籍摘要
│       └── articles/       # 文章精华
├── marketing/        # 营销领域
├── growth/           # 增长领域
├── leadership/       # 领导力领域
├── index/            # 主题索引
│   ├── product-management.md
│   ├── growth-strategy.md
│   ├── marketing-tactics.md
│   ├── leadership.md
│   └── ...
├── scripts/          # 自动化脚本
│   ├── collect-content.sh
│   ├── update-index.sh
│   └── sync-github.sh
└── README.md
```

## 内容格式

### 人物目录结构
每个领域的人物按以下格式组织：

```yaml
├── brian-chesky/
│   ├── profile.md          # 人物档案（YAML frontmatter）
│   ├── quotes.md           # 语录合集
│   ├── podcast/
│   │   ├── lennys-podcast-2024.md
│   │   └── how-i-built-this.md
│   ├── books/
│   │   └── book-summary.md
│   └── articles/
│       └── blog-posts.md
```

### Markdown 文件格式

每个文件包含 YAML frontmatter：

```yaml
---
type: profile|quotes|podcast|book|article
person: 人物名称
title: 标题
date: YYYY-MM-DD
source: 来源URL
tags: [tag1, tag2, tag3]
language: zh|en
---
```

## 第一阶段：种子人物清单

### 产品领域 (Product)
- [ ] Brian Chesky (Airbnb CEO)
- [ ] Lenny Rachitsky (Lenny's Podcast)
- [ ] Shreyas Doshi
- [ ] Julie Zhuo
- [ ] John Cutler
- [ ] Marty Cagan
- [ ] Teresa Torres
- [ ] Gibson Biddle
- [ ] Jackie Bavaro
- [ ] Brandon Chu (Shopify)

### 营销领域 (Marketing)
- [ ] Seth Godin
- [ ] April Dunford
- [ ] David Ogilvy
- [ ] Ann Handley
- [ ] Gary Vaynerchuk
- [ ] Neil Patel
- [ ] Rand Fishkin
- [ ] Contently团队
- [ ] HubSpot团队
- [ ] Mailchimp团队

### 增长领域 (Growth)
- [ ] Sean Ellis
- [ ] Brian Balfour
- [ ] Andrew Chen
- [ ] Casey Winters
- [ ] Elena Verna
- [ ] Chamath Palihapitiya
- [ ] Reforge团队
- [ ] GrowthHackers团队

### 领导力领域 (Leadership)
- [ ] Ben Horowitz
- [ ] Andy Grove
- [ ] Satya Nadella
- [ ] Jeff Bezos
- [ ] Reed Hastings
- [ ] Ray Dalio
- [ ] Jim Collins
- [ ] Patrick Lencioni

## 内容来源渠道

### 播客 (Podcasts)
- Lenny's Podcast
- How I Built This
- The Tim Ferriss Show
- Masters of Scale
- 20VC
- The Knowledge Project
- Rework Podcast
- Product Thinking

### 博客/新闻稿 (Newsletters)
- Lenny's Newsletter
- First Round Review
- Reforge Blog
- Growth.design Case Studies
- Shreyas Doshi's Newsletter
- Julie Zhuo's Blog

### 书籍 (Books)
- Inspired (Marty Cagan)
- Continuous Discovery Habits (Teresa Torres)
- The Lean Startup (Eric Ries)
- Zero to One (Peter Thiel)
- The Hard Thing About Hard Things (Ben Horowitz)
- High Growth Handbook (Elad Gil)
- Obviously Awesome (April Dunford)
- Crossing the Chasm (Geoffrey Moore)

### 社交媒体
- Twitter/X 精华推文
- LinkedIn 长文
- YouTube 演讲/访谈

## 自动化计划

### Phase 1: 基础搭建 ✅
- [x] GitHub 仓库连接
- [x] 参考项目分析
- [x] 目录结构设计
- [x] 文档模板创建

### Phase 2: 内容采集系统
- [ ] RSS 订阅收集器
- [ ] 播客转录脚本
- [ ] YouTube 字幕提取
- [ ] Twitter 精华抓取
- [ ] 书籍摘要生成

### Phase 3: 内容处理流水线
- [ ] 自动分类标签
- [ ] 内容质量评估
- [ ] 多语言翻译
- [ ] 索引自动生成

### Phase 4: 持续更新机制
- [ ] 每日定时采集
- [ ] 每周内容审查
- [ ] 月度质量报告

## 贡献指南

1. 所有内容必须注明来源
2. 保持原始内容的完整性
3. 添加适当的标签便于检索
4. 遵循统一的文件命名规范

## License

仅供学习和研究使用。所有内容版权归原作者所有。

---
*Last Updated: 2026-03-10*
