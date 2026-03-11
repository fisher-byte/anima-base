# Anima Base 双语翻译策略

## 🌐 双语架构设计

### 目录结构

```
anima-base/
├── README.md                    # 中文说明
├── README.en.md                 # 英文说明
├── ROADMAP.md                   # 中文路线图
├── ROADMAP.en.md                # 英文路线图
│
├── people/                      # 人物内容库（英文原文为主）
│   ├── {category}/
│   │   └── {person-name}/
│   │       ├── profile.md       # 人物档案（英文原文）
│   │       ├── quotes.md        # 语录合集（英文原文）
│   │       ├── frameworks/      # 框架方法论（英文原文）
│   │       ├── podcasts/        # 播客索引（英文）
│   │       ├── articles/        # 文章索引（英文）
│   │       ├── books/           # 书籍索引（英文）
│   │       └── sources.md       # 原文文件索引（英文）
│
├── translations/                # 翻译内容（中文为主）
│   ├── zh-cn/                   # 中文翻译
│   │   ├── README.md            # 翻译说明
│   │   ├── {category}/
│   │   │   └── {person-name}/
│   │   │       ├── profile.zh-cn.md      # 人物档案（中文）
│   │   │       ├── quotes.zh-cn.md       # 语录合集（中文）
│   │   │       ├── frameworks/             # 框架翻译
│   │   │       │   ├── framework-name.zh-cn.md
│   │   │       ├── podcasts/              # 播客翻译
│   │   │       │   ├── index.zh-cn.md      # 播客索引（中文）
│   │   │       │   └── 2024-03-10-show.zh-cn.md
│   │   │       ├── articles/              # 文章翻译
│   │   │       │   ├── index.zh-cn.md
│   │   │       │   └── 2024-03-05-title.zh-cn.md
│   │   │       ├── books/                 # 书籍翻译
│   │   │       │   └── index.zh-cn.md
│   │   │       └── sources.zh-cn.md
│   │   │
│   │   └── topics/                 # 主题翻译
│   │       └── {topic-name}/
│   │           └── index.zh-cn.md
│   │
│   └── en/                       # 英文（作为备份/补充）
│       └── {category}/
│
├── media/                       # 多媒体原始文件（语言无关）
│   ├── audio/                   # 音频（原语言）
│   ├── video/                   # 视频（原语言）
│   └── ebook/                   # 电子书（原语言）
│
├── files/                       # 文档原始文件（语言无关）
│   ├── pdf/                     # PDF（原语言）
│   └── articles/                # HTML（原语言）
│
└── scripts/                     # 脚本（语言无关）
    ├── translator.py            # 翻译工具
    ├── sync_translations.py     # 同步翻译文件
    └── check_translation.py     # 检查翻译完整性
```

## 🎯 翻译原则

### 1. 语言分层

| 层级 | 内容 | 语言 | 说明 |
|------|------|------|------|
| 原材料 | MP3/PDF/EPUB/HTML视频字幕 | 原始语言 | 保留原文 |
| 核心内容 | profile.md / frameworks/ | 英文原文 | 主要内容 |
| 翻译内容 | translations/zh-cn/ | 中文 | 完整翻译 |
| 交叉引用 | 所有文件 | 双语链接 | 中英文互链 |

### 2. 翻译优先级

#### 第一优先级（完整翻译）
- ✅ **profile.md** → `profile.zh-cn.md` - 人物档案
- ✅ **quotes.md** → `quotes.zh-cn.md` - 语录合集
- ✅ **frameworks/** - 核心框架文档
- ✅ **podcasts/index.md** → `index.zh-cn.md` - 播客索引
- ✅ **articles/index.md** → `index.zh-cn.md` - 文章索引
- ✅ **books/index.md** → `index.zh-cn.md` - 书籍索引

#### 第二优先级（选择性翻译）
- 🔄 **podcasts/2024-03-10-show.md** - 高质量播客访谈
- 🔄 **articles/2024-03-05-title.md** - 核心文章
- 🔄 **books/book-summary.md** - 重要书籍摘要

#### 第三优先级（按需翻译）
- 📝 **topics/** - 主题聚合内容
- 📝 **index/** - 全局索引

### 3. 翻译质量标准

#### 准确性
- ✅ 术语统一：专业术语建立glossary
- ✅ 含义准确：不改变原意
- ✅ 上下文一致：同一概念翻译一致

#### 可读性
- ✅ 中文表达自然：避免"翻译腔"
- ✅ 逻辑清晰：保持原文结构
- ✅ 格式规范：保留markdown格式

#### 完整性
- ✅ 不删减：保留所有内容
- ✅ 链接保留：原文链接保持有效
- ✅ 元数据完整：frontmatter完整翻译

### 4. 翻译文件命名

**规则**：`原文件名.zh-cn.md`

示例：
```markdown
# 英文原文
people/product/gokul-rajaram/profile.md

# 中文翻译
translations/zh-cn/product/gokul-rajaram/profile.zh-cn.md

# 框架文档
people/product/gokul-rajaram/frameworks/hiring-framework.md
translations/zh-cn/product/gokul-rajaram/frameworks/hiring-framework.zh-cn.md

# 播客文档
people/product/gokul-rajaram/podcasts/2024-03-10-lennys-podcast.md
translations/zh-cn/product/gokul-rajaram/podcasts/2024-03-10-lennys-podcast.zh-cn.md
```

## 🔗 交叉引用策略

### 1. 英文文件引用中文翻译

在英文文件顶部添加：

```markdown
---
language: en
translation: ../../translations/zh-cn/product/gokul-rajaram/profile.zh-cn.md
---

**中文翻译** → [中文版](../../translations/zh-cn/product/gokul-rajaram/profile.zh-cn.md)
```

### 2. 中文文件引用英文原文

在中文文件顶部添加：

```markdown
---
language: zh-cn
original: ../../people/product/gokul-rajaram/profile.md
---

**英文原文** → [English Version](../../people/product/gokul-rajaram/profile.md)
```

### 3. 索引文件双语链接

```markdown
| 人物 | 英文 | 中文 | 状态 |
|------|------|------|------|
| Gokul Rajaram | [Profile](../../people/product/gokul-rajaram/profile.md) | [简介](../../translations/zh-cn/product/gokul-rajaram/profile.zh-cn.md) | ✅ 已翻译 |
| Brian Chesky | [Profile](../../people/product/brian-chesky/profile.md) | [简介](../../translations/zh-cn/product/brian-chesky/profile.zh-cn.md) | 🔄 翻译中 |
```

## 📚 翻译模板

### 1. 人物档案翻译模板

```markdown
---
language: zh-cn
original: ../../../people/product/{person-name}/profile.md
person: 人物名称
category: product
translation_date: YYYY-MM-DD
---

# 人物名称 - 人物档案

**英文原文** → [English Version](../../../people/product/{person-name}/profile.md)

> 本文档是英文原文的中文翻译版本，请与原文对照阅读。

## 📌 人物简介

[翻译内容...]

## 🎯 核心专长

[翻译内容...]

## 📚 主要著作

[翻译内容...]

## 🔗 相关链接

- [英文原文](../../../people/product/{person-name}/profile.md)
- [英文播客列表](../../../people/product/{person-name}/podcasts/index.md)
- [中文播客列表](./index.zh-cn.md)
```

### 2. 框架文档翻译模板

```markdown
---
language: zh-cn
original: ../../../people/product/{person-name}/frameworks/{framework-name}.md
framework: 框架名称
creator: 创建者
translation_date: YYYY-MM-DD
---

# [框架名称]

**英文原文** → [English Version](../../../people/product/{person-name}/frameworks/{framework-name}.md)

> 本文档翻译自英文原文，包含完整框架说明和案例。

## 📋 框架概览

**创建者**: [人物名称](../profile.zh-cn.md)
**适用场景**: [翻译...]
**预期成果**: [翻译...]

**原文来源**:
- [英文原文](../../../people/product/{person-name}/frameworks/{framework-name}.md)
- [原始播客](../../../media/audio/{person-name}/podcast/20240310-mp3-file.mp3)

---

## 🎯 框架详解

### 核心概念
[翻译...]

### 操作步骤
1. **步骤1**: [翻译...]
2. **步骤2**: [翻译...]
```

### 3. 播客翻译模板

```markdown
---
language: zh-cn
original: ../../../people/product/{person-name}/podcasts/2024-03-10-show.md
title: 播客标题
source: 播客名称
publish_date: YYYY-MM-DD
translation_date: YYYY-MM-DD
---

# [播客名称] - 核心洞察

**英文原文** → [English Version](../../../people/product/{person-name}/podcasts/2024-03-10-show.md)
**原始音频**: [MP3](../../../media/audio/{person-name}/podcast/20240310-mp3-file.mp3)
**完整转录**: [TXT](../../../media/audio/{person-name}/podcast/20240310-mp3-file-transcript.txt)

> 本文档提炼播客中的核心观点、框架和方法论

## 📌 核心要点

### 1. [主题一]
**核心观点**: [翻译...]

**实用建议**:
- [翻译...]

**相关框架**: [框架名称](../frameworks/framework-name.zh-cn.md)
```

## 🔧 翻译工具

### 1. translator.py

功能：
- 批量翻译Markdown文件
- 保留原文格式
- 生成翻译文件
- 检查翻译完整性

使用：
```bash
python scripts/translator.py --source people/product/gokul-rajaram --target translations/zh-cn/product/gokul-rajaram
```

### 2. sync_translations.py

功能：
- 同步英文文件到翻译目录
- 检查哪些文件未翻译
- 生成翻译任务列表

使用：
```bash
python scripts/sync_translations.py --check
```

### 3. check_translation.py

功能：
- 检查翻译完整性
- 验证链接有效性
- 检查术语一致性

使用：
```bash
python scripts/check_translation.py --person gokul-rajaram
```

## 📊 翻译进度追踪

### 翻译状态标签

| 状态 | 说明 | 标签 |
|------|------|------|
| 未开始 | 未开始翻译 | 📅 待翻译 |
| 进行中 | 正在翻译 | 🔄 翻译中 |
| 已完成 | 翻译完成 | ✅ 已翻译 |
| 已审核 | 通过审核 | ✅✅ 已审核 |

### 进度统计

每个人物目录包含 `translation_progress.md`：

```markdown
# 人物名称 - 翻译进度

## 统计信息

| 文件类型 | 总数 | 已翻译 | 完成率 |
|---------|------|--------|--------|
| profile.md | 1 | 1 | 100% |
| frameworks/ | 20 | 15 | 75% |
| podcasts/ | 25 | 10 | 40% |
| articles/ | 50 | 5 | 10% |
| books/ | 3 | 2 | 67% |

## 待翻译列表

### 优先级1 - 核心
- [ ] frameworks/framework-1.md
- [ ] frameworks/framework-2.md

### 优先级2 - 重要
- [ ] podcasts/2024-03-10-show.md
- [ ] articles/2024-03-05-title.md
```

## 🎯 术语库

### 专业术语对照表

| 英文 | 中文 | 说明 |
|------|------|------|
| Product Management | 产品管理 | - |
| Product-Market Fit | 产品市场契合度 | 简称PMF |
| Product-Led Growth | 产品驱动增长 | 简称PLG |
| User Experience | 用户体验 | 简称UX |
| Customer Development | 客户开发 | - |
| A/B Testing | A/B测试 | - |
| Conversion Rate | 转化率 | - |
| Churn Rate | 流失率 | - |
| Customer Lifetime Value | 客户生命周期价值 | 简称CLV |
| Net Promoter Score | 净推荐值 | 简称NPS |

## 📝 翻译工作流

### 1. 翻译新文件

```bash
# 1. 创建翻译文件
cp people/product/gokul-rajaram/profile.md translations/zh-cn/product/gokul-rajaram/profile.zh-cn.md

# 2. 翻译内容（手动或使用工具）
python scripts/translator.py --input profile.zh-cn.md

# 3. 添加语言标记和原文链接
# 在frontmatter添加language和original字段

# 4. 更新进度追踪
# 编辑translation_progress.md
```

### 2. 同步英文更新

```bash
# 1. 检查英文文件更新
python scripts/sync_translations.py --check

# 2. 更新已翻译文件
python scripts/translator.py --update profile.zh-cn.md

# 3. 验证翻译
python scripts/check_translation.py --file profile.zh-cn.md
```

### 3. 质量检查

```bash
# 检查翻译完整性
python scripts/check_translation.py --completeness

# 检查术语一致性
python scripts/check_translation.py --terminology

# 检查链接有效性
python scripts/check_translation.py --links
```

## 🌍 多语言扩展

未来支持更多语言：
- `translations/ja/` - 日语
- `translations/ko/` - 韩语
- `translations/es/` - 西班牙语
- `translations/fr/` - 法语

---

**版本**: 1.0
**更新日期**: 2026-03-11
