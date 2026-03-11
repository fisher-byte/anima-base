# Anima Base 内容扩充计划 v2.0

## 📋 扩充目标

参考 [ChatPRD/lennys-podcast-transcripts](https://github.com/ChatPRD/lennys-podcast-transcripts) 的高质量标准，为项目中的每位人物创建全面、结构化的知识资源库。

---

## 🎯 内容标准

### 质量原则
1. **原创策展** - 不直接复制转录，而是提炼核心洞察
2. **多源验证** - 交叉验证多个来源的信息
3. **实用导向** - 聚焦可执行的框架和方法论
4. **完整引用** - 每个观点都标注来源链接
5. **原文优先** - 优先保留原始文件（MP3/PDF/EPUB/HTML），摘要为辅
6. **双语支持** - 英文原文为主，提供中文翻译版本

### 双轨制：原文 + 索引 + 翻译

**原文文件存储**（语言无关）：
- 播客音频：`media/audio/{person}/podcast/` → MP3/WAV + 转录TXT
- 文章原文：`files/pdf/{person}/articles/` → PDF / `files/articles/{person}/` → HTML
- 书籍原文：`media/ebook/` → EPUB/MOBI / `files/pdf/{person}/books/` → PDF
- 视频文件：`media/video/{person}/` → MP4

**索引与摘要**（英文原文）：
- `people/.../podcasts/index.md` - 播客列表（链接到原始MP3/TXT）
- `people/.../podcasts/2024-03-10-show.md` - 单个播客摘要+洞察
- `people/.../articles/index.md` - 文章列表（链接到原始PDF/HTML）
- `people/.../books/index.md` - 书籍列表（链接到原始EPUB/PDF）

**翻译内容**（中文）：
- `translations/zh-cn/.../podcasts/index.zh-cn.md` - 播客列表（中文）
- `translations/zh-cn/.../podcasts/2024-03-10-show.zh-cn.md` - 播客摘要（中文）
- `translations/zh-cn/.../articles/index.zh-cn.md` - 文章列表（中文）
- `translations/zh-cn/.../books/index.zh-cn.md` - 书籍列表（中文）

**双语链接**：
- 英文文件顶部：`**中文版** → [中文翻译](../../translations/zh-cn/...)`
- 中文文件顶部：`**英文原文** → [English Version](../../../people/...)`

详见：
- [FILE_STORAGE_POLICY.md](./FILE_STORAGE_POLICY.md) - 原文存储
- [TRANSLATION_POLICY.md](./TRANSLATION_POLICY.md) - 双语翻译

### 内容结构
```
{person-name}/
├── profile.md                    # 人物档案
├── quotes.md                     # 语录合集
├── frameworks/                    # 方法论框架（可保留摘要）
├── podcasts/                      # 播客索引+摘要
│   ├── index.md                  # 播客列表（含原始文件链接）
│   └── 2024-03-10-lennys-podcast.md
├── articles/                      # 文章索引+摘要
│   ├── index.md                  # 文章列表（含原始文件链接）
│   └── 2024-03-05-title.md
├── talks/                         # 演讲/访谈索引+摘要
├── books/                         # 书籍索引+摘要
│   └── index.md
└── sources.md                     # 原文文件统计索引
```

### 原文文件命名规范
- 播客：`{YYYY-MM-DD}-{show-name}.{mp3|wav|m4a}`
- 转录：`{YYYY-MM-DD}-{show-name}-transcript.{txt|md}`
- PDF文章：`{YYYY-MM-DD}-{title-slug}.pdf`
- 电子书：`{isbn}.{epub|mobi}`
- 网页：`{YYYY-MM-DD}-{title-slug}.html`

详见：[FILE_STORAGE_POLICY.md](./FILE_STORAGE_POLICY.md)

---

## 🚀 实施计划

### Phase 1: 核心人物扩充 (5人)
优先级最高，创建完整内容（原文优先）：

1. **Lenny Rachitsky** (Product)
   - 原文收集：
     - Newsletter文章：保存HTML到 `files/articles/lenny-rachitsky/`
     - 播客音频：下载MP3到 `media/audio/lenny-rachitsky/podcast/`
     - 转录文本：保存TXT到 `media/audio/lenny-rachitsky/podcast/`
   - 索引创建（英文）：
     - `articles/index.md` - 320+篇文章列表（链接到HTML）
     - `podcasts/index.md` - 320+集播客列表（链接到MP3/TXT）
     - `books/index.md` - 《The Product-Led Playbook》框架提取
   - 翻译内容（中文）：
     - `translations/zh-cn/.../articles/index.zh-cn.md`
     - `translations/zh-cn/.../podcasts/index.zh-cn.md`
     - 核心框架文档翻译
   - 预计产出: 20+ 个主题框架文档（从播客中提炼）+ 中文翻译

2. **Brian Chesky** (Product/Leadership)
   - 原文收集：
     - Master of Scale播客：下载MP3+转录
     - Lenny's Podcast访谈：下载MP3+转录
   - 索引创建（英文）：
     - `podcasts/index.md` - 播客列表（链接到MP3/TXT）
     - 框架文档：11星级体验、产品化公司等15+个
   - 翻译内容（中文）：
     - 播客列表和核心框架文档翻译

3. **Marty Cagan** (Product)
   - 原文收集：
     - 书籍《Inspired》《Empowered》：获取EPUB/PDF
     - SVPG博客文章：保存HTML
     - 播客访谈：下载MP3+转录
   - 索引创建（英文）：
     - `books/index.md` - 书籍索引（链接到EPUB/PDF）
     - `articles/index.md` - 博客文章列表（链接到HTML）
     - 框架文档：25+个方法论文档（从书中提炼）
   - 翻译内容（中文）：
     - 书籍索引和核心框架文档翻译

4. **Shreyas Doshi** (Product)
   - 原文收集：
     - Twitter精华：保存HTML到 `files/articles/shreyas-doshi/`
     - 播客访谈：下载MP3+转录
   - 索引创建（英文）：
     - `articles/index.md` - Twitter文章列表
     - 框架文档：LNO框架、产品思维模型等30+个
   - 翻译内容（中文）：
     - 核心框架文档翻译

5. **Gokul Rajaram** (Product) ✅ 已完成
   - 9个框架已创建
   - 需补充原文文件（MP3/PDF）
   - 需补充中文翻译

### Phase 2: 重要人物扩充 (10人)
中等优先级（原文优先 + 翻译）：

**Product领域**:
- Julie Zhuo (设计与产品)
  - 原文收集：播客访谈MP3+转录，Substack文章HTML
  - 索引创建：播客列表+文章列表（英文）
  - 框架提取：设计+产品框架
  - 翻译内容：核心框架文档（中文）

- Teresa Torres (持续发现)
  - 原文收集：播客访谈MP3+转录，《Continuous Discovery Habits》PDF/EPUB
  - 索引创建：播客列表+书籍索引（英文）
  - 框架提取：持续发现框架
  - 翻译内容：书籍摘要+核心框架（中文）

- John Cutler (产品运营)
  - 原文收集：博客文章HTML，播客访谈MP3+转录
  - 索引创建：文章列表+播客列表（英文）
  - 框架提取：产品运营框架
  - 翻译内容：核心框架（中文）

**Growth领域**:
- Sean Ellis (增长黑客创始人)
  - 原文收集：播客访谈MP3+转录，《Hacking Growth》PDF/EPUB
  - 索引创建：播客列表+书籍索引（英文）
  - 框架提取：增长黑客框架
  - 翻译内容：核心框架（中文）

- Brian Balfour (增长框架)
  - 原文收集：Reforge课程材料（如有），博客文章HTML
  - 索引创建：文章列表（英文）
  - 框架提取：增长循环框架
  - 翻译内容：核心框架（中文）

- Andrew Chen (网络效应)
  - 原文收集：博客文章HTML，播客访谈MP3+转录
  - 索引创建：文章列表+播客列表（英文）
  - 框架提取：网络效应框架
  - 翻译内容：核心框架（中文）

**Marketing领域**:
- Seth Godin (现代营销)
  - 原文收集：博客文章HTML，播客访谈MP3+转录
  - 索引创建：文章列表（英文，已收集部分HTML）
  - 框架提取：营销框架
  - 翻译内容：核心框架（中文）

- April Dunford (定位)
  - 原文收集：《Obviously Awesome》PDF/EPUB，博客文章HTML
  - 索引创建：书籍索引+文章列表（英文）
  - 框架提取：定位框架
  - 翻译内容：书籍摘要+核心框架（中文）

**Leadership领域**:
- Ben Horowitz (创业管理)
  - 原文收集：《Hard Thing About Hard Things》PDF/EPUB，播客访谈MP3+转录
  - 索引创建：书籍索引+播客列表（英文）
  - 框架提取：创业管理框架
  - 翻译内容：书籍摘要+核心框架（中文）

- Ray Dalio (原则)
  - 原文收集：《Principles》PDF/EPUB，视频转录TXT
  - 索引创建：书籍索引（英文）
  - 框架提取：原则框架
  - 翻译内容：核心原则（中文）

### Phase 3: 补充人物 (12人)
基础扩充，重点框架+原文收集+选择性翻译：
- 其余 product/ marketing/ growth/ leadership/ startup/ 目录下的人物
- 优先翻译核心框架文档（中英双语）

---

## 📝 内容创建模板

### 1. 播客索引文档 (podcasts/index.md)

```markdown
---
type: index
person: 人物名称
category: product
last_updated: 2026-03-11
total_podcasts: XX
total_duration: XX hours
---

# 人物名称 - 播客索引

## 2024

| 日期 | 节目名称 | 时长 | 原始文件 | 转录 | 洞察文档 |
|------|---------|------|---------|------|---------|
| 2024-03-10 | Lenny's Podcast #320 | 45:23 | [MP3](../../media/audio/人物名/podcast/20240310-lennys-podcast.mp3) | [TXT](../../media/audio/人物名/podcast/20240310-lennys-podcast-transcript.txt) | [详情](./2024-03-10-lennys-podcast.md) |

## 统计

- 总播客数: XX
- 总时长: XX小时
- 存储空间: XX MB
```

### 2. 播客洞察文档 (podcasts/YYYY-MM-DD-show.md)

```markdown
---
guest: 人物名称
title: 播客标题
source: 播客名称
source_url: 原始链接
publish_date: YYYY-MM-DD
episode_number: EP123
duration: 60 min
topics: [product, growth, leadership]
verification_status: reviewed
verification_date: YYYY-MM-DD
content_type: curated_insights
original_audio: ../../media/audio/人物名/podcast/20240310-mp3-file.mp3
original_transcript: ../../media/audio/人物名/podcast/20240310-mp3-file-transcript.txt
---

# [播客名称] - [嘉宾名称] 核心洞察

> 本文档提炼播客中的核心观点、框架和方法论
>
> **原始播客**: [MP3](../../media/audio/人物名/podcast/20240310-mp3-file.mp3) | [完整转录](../../media/audio/人物名/podcast/20240310-mp3-file-transcript.txt)
> **来源**: [原始链接](source_url)

## 📌 核心要点

### 1. [主题一]
**核心观点**:
...

**实用建议**:
- 建议1
- 建议2

**相关框架**: [框架名称](../frameworks/framework.md)

---

## 🎯 可执行框架

### [框架名称]
**适用场景**: ...
**操作步骤**:
1. 步骤1
2. 步骤2

**案例**: ...

---

## 💡 金句摘录

> "引用内容"
> — 人物名称, [来源](链接)

---

## 📚 延伸阅读

- 相关书籍: [书名](../books/book.md)
- 相关文章: [文章](../articles/article.md)
- 相关框架: [框架](../frameworks/framework.md)
```

### 2. 文章索引文档 (articles/index.md)

```markdown
---
type: index
person: 人物名称
category: product
last_updated: 2026-03-11
total_articles: XX
---

# 人物名称 - 文章索引

## 按来源分类

### Newsletter
| 日期 | 标题 | 来源 | 原始文件 | 摘要文档 |
|------|------|------|---------|---------|
| 2024-03-05 | Product Leadership | Substack | [HTML](../../files/articles/人物名/20240305-title.html) | [详情](./2024-03-05-title.md) |

### 博客文章
| 日期 | 标题 | 来源 | 原始文件 | 摘要文档 |
|------|------|------|---------|---------|
| 2024-02-15 | Growth Framework | Personal Blog | [HTML](../../files/articles/人物名/20240215-growth.html) | [详情](./2024-02-15-growth.md) |
```

### 3. 文章精华文档 (articles/YYYY-MM-DD-title.md)

```markdown
---
title: 文章标题
author: 作者名称
source: 发布平台
source_url: 原文链接
publish_date: YYYY-MM-DD
reading_time: 15 min
topics: [topic1, topic2]
verification_status: reviewed
verification_date: YYYY-MM-DD
content_type: curated_summary
original_html: ../../files/articles/人物名/20240305-title.html
original_pdf: ../../files/pdf/人物名/articles/20240305-title.pdf (可选)
---

# [文章标题] - 核心提炼

> 本文档提炼文章核心观点和可执行建议
>
> **原文**: [HTML](../../files/articles/人物名/20240305-title.html) | [原始链接](source_url)

## 📝 文章概览

**主题**: ...
**核心观点**: ...
**目标读者**: ...

---

## 🔑 关键洞察

### 1. [洞察点一]
**要点**: ...
**为什么重要**: ...
**如何应用**: ...

---

## 🛠️ 实用工具

### [工具/框架名称]
...

---

## 📊 数据/案例

...

---

## 🎬 行动建议

1. 立即可做: ...
2. 本周实施: ...
3. 长期计划: ...
```

### 4. 书籍索引文档 (books/index.md)

```markdown
---
type: index
person: 人物名称
category: product
last_updated: 2026-03-11
total_books: XX
---

# 人物名称 - 书籍索引

| 书名 | 作者 | 出版年 | 原始文件 | 摘要 | 框架提取 |
|------|------|-------|---------|------|---------|
| The Product Manager's Handbook | - | 2023 | [EPUB](../../media/ebook/pm-handbook-2023.epub) | [详情](./pm-handbook-summary.md) | [框架](./pm-handbook-frameworks.md) |
| Inspired | Marty Cagan | 2017 | [PDF](../../files/pdf/marty-cagan/books/inspired-2017.pdf) | [详情](./inspired-summary.md) | [框架](./inspired-frameworks.md) |
```

### 5. 框架文档 (frameworks/framework-name.md)

```markdown
---
framework: 框架名称
creator: 创建者
category: product/growth/marketing/leadership
difficulty: beginner/intermediate/advanced
time_to_implement: 时间估计
source: 来源
source_url: 链接
verification_status: reviewed
verification_date: YYYY-MM-DD
related_sources:
  - type: podcast
    file: ../../media/audio/人物名/podcast/20240310-mp3-file.mp3
    transcript: ../../media/audio/人物名/podcast/20240310-mp3-file-transcript.txt
  - type: article
    file: ../../files/articles/人物名/20240305-title.html
---

# [框架名称]

## 📋 框架概览

**创建者**: [人物名称](../profile.md)
**适用场景**: ...
**预期成果**: ...

**来源**: 
- [播客 #320](../../media/audio/人物名/podcast/20240310-mp3-file.mp3)
- [文章标题](../../files/articles/人物名/20240305-title.html)

---

## 🎯 框架详解

### 核心概念
...

### 操作步骤
1. **步骤1**: ...
2. **步骤2**: ...

---

## 💼 实际案例

### 案例1: [公司名称]
**背景**: ...
**应用**: ...
**结果**: ...

---

## ⚠️ 常见误区

1. 误区1: ...
   - 正确做法: ...

---

## 🔗 相关资源

- 原始来源: [链接]
- 深入阅读: [文章](../articles/article.md)
- 配套工具: [工具链接]
```

---

## 🔍 资源收集策略

### 1. 播客资源
**主要来源**:
- Lenny's Podcast (320+ 集)
- Master of Scale
- How I Built This
- The Product Podcast
- My First Million

**原文收集**:
- 下载MP3音频 → `media/audio/{person}/podcast/`
- 获取转录文本 → `media/audio/{person}/podcast/`
- 保存元数据（时长、日期等）

**索引创建**:
- 创建 `podcasts/index.md` - 播客列表（含原始文件链接）
- 创建 `podcasts/2024-03-10-show.md` - 单个播客摘要+洞察
- 提炼框架并链接到原始MP3/TXT

### 2. 文章资源
**主要来源**:
- Lenny's Newsletter (Substack)
- First Round Review
- Andreessen Horowitz Blog
- Reforge Blog
- SVPG Blog
- 个人博客/Medium

**原文收集**:
- 保存原始HTML → `files/articles/{person}/`
- 如有PDF版本 → `files/pdf/{person}/articles/`
- 提取元数据（标题、日期、作者）

**索引创建**:
- 创建 `articles/index.md` - 文章列表（含原始文件链接）
- 创建 `articles/2024-03-05-title.md` - 单篇文章摘要
- 提炼框架并链接到原始HTML/PDF

### 3. 书籍资源
**原文收集**:
- 获取EPUB/MOBI → `media/ebook/`
- 获取PDF版本 → `files/pdf/{person}/books/`
- 提取元数据（ISBN、出版年、作者）

**索引创建**:
- 创建 `books/index.md` - 书籍列表（含原始文件链接）
- 创建 `books/book-title-summary.md` - 书籍摘要
- 提炼框架并链接到原始EPUB/PDF

### 4. 视频资源
**主要来源**:
- YouTube 访谈/演讲
- 线上课程公开内容
- 会议演讲

**原文收集**:
- 下载视频MP4 → `media/video/{person}/`
- 提取音频 → `media/audio/{person}/interview/`
- 获取字幕/转录 → `media/audio/{person}/interview/transcript.txt`

**索引创建**:
- 创建 `talks/index.md` - 演讲列表（含原始文件链接）
- 创建 `talks/YYYY-MM-DD-talk.md` - 单个演讲摘要
- 提炼框架并链接到原始MP4/TXT

---

## ⚖️ 版权合规

### 合规原则
1. ✅ **保留原文**: 存储公开可用的原始文件（MP3/PDF/EPUB/HTML）
2. ✅ **归属标注**: 所有内容标注原始来源和链接
3. ✅ **教育目的**: 用于学习和知识分享
4. ✅ **非商业**: 开源项目，非盈利性质
5. ✅ **公开资源**: 仅收集公开可用的资源
6. ❌ **不分享**: 原始文件仅用于本地学习，不重新分发

### 内容类型区分
| 类型 | 原文存储 | 索引创建 | 摘要提炼 |
|------|---------|---------|---------|
| 播客 | ✅ MP3 + 转录TXT | ✅ 列表 + 链接 | ✅ 核心洞察 |
| 文章 | ✅ HTML + PDF | ✅ 列表 + 链接 | ✅ 要点归纳 |
| 书籍 | ✅ EPUB + PDF | ✅ 列表 + 链接 | ✅ 框架提取 |
| 视频 | ✅ MP4 | ✅ 列表 + 链接 | ✅ 核心观点 |

---

## 📊 进度追踪

### 完成标准
每个人物至少包含:
- ✅ 1个完善的 profile.md
- ✅ 3-5个核心框架文档
- ✅ 5-10个播客/文章洞察
- ✅ 播客/文章/书籍的index.md索引
- ✅ 原始文件（MP3/PDF/EPUB/HTML）
- ✅ 所有内容标注来源链接

### 预期产出（按Phase）

**Phase 1 (5人)**:
- Lenny Rachitsky: 320+播客MP3+转录, 320+文章HTML, 20+框架
- Brian Chesky: 10+播客MP3+转录, 15+框架
- Marty Cagan: 2本书EPUB+PDF, 10+播客MP3+转录, 25+框架
- Shreyas Doshi: 100+Twitter HTML, 5+播客MP3+转录, 30+框架
- Gokul Rajaram: ✅ 9框架已创建, 需补充MP3/PDF

**总预期**:
- 播客MP3: 345+集
- 文章HTML: 420+篇
- 书籍EPUB/PDF: 10+本
- 框架文档: 100+个

### 质量检查
- [ ] 所有文档包含 YAML frontmatter
- [ ] 所有观点标注来源
- [ ] 框架可执行性验证
- [ ] 交叉引用完整
- [ ] 符合 CONTENT_QUALITY.md 标准

---

## 🚀 执行时间表

### Week 1: 基础建设
- 完成内容模板
- 建立收集流程
- Phase 1 前2人（Lenny, Brian）

### Week 2-3: 核心扩充
- 完成 Phase 1 剩余3人
- 开始 Phase 2 前5人

### Week 4-5: 深度扩充
- 完成 Phase 2 全部10人
- 开始 Phase 3

### Week 6: 完善优化
- 完成 Phase 3
- 全面质量检查
- 优化交叉引用

---

## 📈 预期成果

### 数量指标（原文+索引）

| 指标 | Phase 1 | Phase 2 | Phase 3 | 总计 |
|------|---------|---------|---------|------|
| 人物 | 5 | 10 | 12 | 27 |
| 播客MP3 | 345+ | 200+ | 150+ | 695+ |
| 转录TXT | 345+ | 200+ | 150+ | 695+ |
| 文章HTML | 420+ | 300+ | 200+ | 920+ |
| 文章PDF | 100+ | 80+ | 50+ | 230+ |
| 书籍EPUB | 5 | 8 | 10 | 23 |
| 书籍PDF | 5 | 8 | 10 | 23 |
| 视频MP4 | 20+ | 30+ | 20+ | 70+ |
| 框架文档 | 100+ | 150+ | 100+ | 350+ |

### 存储空间估算
- 音频（MP3）: 695集 × 50MB ≈ 35GB
- 转录（TXT）: 695集 × 50KB ≈ 35MB
- 文章HTML: 920篇 × 200KB ≈ 184MB
- 文章PDF: 230篇 × 500KB ≈ 115MB
- 书籍EPUB/PDF: 23本 × 5MB ≈ 115MB
- 视频MP4: 70集 × 500MB ≈ 35GB
- **总计**: 约 **70GB**

### 质量指标
- 原始文件保存率: 100%（所有内容均有原文存储）
- 来源标注率: 100%（链接到原始文件）
- 框架可执行性: 90%+
- 用户实用性评分: 4.5/5+
- 索引完整性: 100%（每个人物都有podcasts/articles/books/index.md）

### 文件完整性检查
每个人物目录包含：
```
people/{category}/{person}/
├── podcasts/index.md          ✅ 播客列表（链接到原始MP3/TXT）
├── articles/index.md          ✅ 文章列表（链接到原始HTML/PDF）
├── books/index.md             ✅ 书籍列表（链接到原始EPUB/PDF）
└── sources.md                 ✅ 原文文件统计索引

media/audio/{person}/
├── podcast/                   ✅ 播客MP3 + 转录TXT
└── interview/                 ✅ 访谈音频 + 转录

files/articles/{person}/       ✅ 文章HTML
files/pdf/{person}/articles/   ✅ 文章PDF
media/ebook/                   ✅ 书籍EPUB
files/pdf/{person}/books/     ✅ 书籍PDF
media/video/{person}/          ✅ 视频MP4
```

---

**制定日期**: 2026-03-11
**版本**: 3.0（原文优先）
**状态**: 执行中
