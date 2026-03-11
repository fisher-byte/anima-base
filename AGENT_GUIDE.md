# AGENT_GUIDE — Anima Base Agent 执行手册

> **用法**：把本文件完整喂给任何 agent，它即可无缝接手 anima-base 项目，了解当前状态、知道下一步干什么、按规范执行并提交。
>
> 最后更新：2026-03-11

---

## 项目是什么

**anima-base** 是一个结构化知识库，收录产品、增长、营销、领导力领域顶尖人物的核心洞察和框架。

它服务于两个目的：
1. 供人类直接浏览学习
2. 为 [Anima AI](https://github.com/fisher-byte/anima-ai) 提供内容——用户可以把任意人物的内容导入 Anima，作为自己的记忆空间使用

**仓库地址**：https://github.com/fisher-byte/anima-base

---

## 仓库结构

```
anima-base/
├── people/                        # 核心内容，按分类 > 人物组织
│   ├── product/
│   │   ├── lenny-rachitsky/       # 最完整，包含 290 集播客转录
│   │   │   ├── profile.md
│   │   │   ├── podcasts/          # YYYY-MM-DD-{guest-slug}.md
│   │   │   ├── frameworks/        # {framework-name}.md
│   │   │   ├── quotes/
│   │   │   ├── books/
│   │   │   ├── talks/
│   │   │   └── twitter/
│   │   ├── brian-chesky/          # 10播客 + 1文章 + 15框架
│   │   ├── marty-cagan/           # 6播客 + 1文章 + 12框架
│   │   ├── shreyas-doshi/         # 2播客 + 1文章 + 8框架
│   │   ├── gokul-rajaram/         # 4播客 + 1文章 + 9框架
│   │   └── ...（另5人）
│   ├── growth/                    # 6人
│   ├── marketing/                 # 6人
│   ├── leadership/                # 5人
│   └── startup/                   # 1人（paul-graham）
│
├── translations/zh-cn/            # 中文翻译（结构镜像 people/）
├── topics/                        # 主题内容（product/marketing/ai）
├── index/                         # 跨人物主题索引
├── scripts/                       # 自动化采集脚本
├── sources/                       # 来源记录
│
├── AGENT_GUIDE.md                 # 本文件
├── COLLECTION_STATUS.md           # 进度追踪（每次任务后必须更新）
├── EXECUTION_PLAN.md              # 详细任务清单
├── CONTENT_QUALITY.md             # 质量标准
├── STRUCTURE.md                   # 文件规范
└── README.md                      # 项目主页（中英双语）
```

---

## 当前进度（2026-03-11）

| 指标 | 状态 |
|------|------|
| 人物目录 | 28 个已建立 |
| 有完整 Profile | 18 人 |
| **Lenny 播客转录** | **290 集**（完整，来自 ChatPRD/lennys-podcast-transcripts） |
| 其他人物播客 | 43 集策展摘要 |
| 文章文档 | 11 篇 |
| 框架文档 | 45 篇 |
| 书籍摘要 | 0 本 |
| 语录集 | 1 份（Lenny） |
| 中文翻译 | 尚未开始 |

**最需要推进的方向**（按优先级）：

```
P0 — 框架提炼（基于已有内容生成，不需要新采集）
  · lenny-rachitsky: 290集转录已有，需从中提炼框架文档（当前仅1篇）
  · brian-chesky: 15框架已有，需补 quotes.md（50+ 条）
  · marty-cagan: 需补书籍摘要（Inspired / Empowered / Transformed）

P1 — 内容补全（有 profile 但几乎没有内容）
  · julie-zhuo, teresa-torres, sean-ellis, brian-balfour, andrew-chen
  · april-dunford（需补 Obviously Awesome 框架）
  · ben-horowitz（需补 The Hard Thing About Hard Things 摘要）
  · paul-graham（需补 profile.md 和更多 essays）

P2 — 空目录启动（有目录无任何文件）
  · john-cutler, brandon-chu, elena-verna, dave-gerhardt,
    rand-fishkin, satya-nadella, reed-hastings, andy-grove

P3 — 新增人物
  · naval-ravikant（在 ROADMAP 中列出，尚未建目录）
```

详细进度见 [COLLECTION_STATUS.md](./COLLECTION_STATUS.md)。

---

## 文件规范

### 目录命名

```
people/{category}/{person-slug}/
  category: product | growth | marketing | leadership | startup
  person-slug: lowercase-with-hyphens（如 brian-chesky）
```

### 文件命名

| 类型 | 命名规则 | 示例 |
|------|----------|------|
| 人物档案 | `profile.md` | `people/product/brian-chesky/profile.md` |
| 播客 | `YYYY-MM-DD-{guest-slug}.md` | `2023-11-12-brian-chesky.md` |
| 文章 | `YYYY-MM-DD-{title-slug}.md` | `2024-01-15-why-product-roadmaps-lie.md` |
| 框架 | `{framework-name}.md` | `11-star-framework.md` |
| 语录集 | `quotes.md` | |
| 书籍摘要 | `{book-title-slug}.md` | `inspired-summary.md` |

### YAML Frontmatter 规范

每个文件必须有完整的 frontmatter：

```yaml
---
type: profile | podcast | article | framework | quotes | book
person: Brian Chesky
title: "文件标题"
date: 2023-11-12          # 内容发布日期
date_collected: 2026-03-11 # 采集日期
source: "https://..."      # 原始来源链接
collection_method: manual | rss | script | chatprd-import
tags: [product, leadership, airbnb]
status: needs-review | reviewed
verification_status: needs-review | reviewed
---
```

**最低要求**：`type`、`person`、`title`、`date`、`source`、`status` 必填。

### profile.md 标准结构

```markdown
---
（frontmatter）
---

# {人物全名}

## 简介
（2-3句核心介绍，含当前职位和最知名的贡献）

## 核心理念
（3-5条最重要的观点，每条有来源支撑）

## 代表性框架
（列出该人物最著名的1-3个框架，简要说明）

## 主要作品
（书籍/播客/文章，含链接）

## 来源
（核心来源列表）
```

字数要求：≥ 1500 字。

---

## 内容质量标准

参考 [CONTENT_QUALITY.md](./CONTENT_QUALITY.md)，核心原则：

1. **每个核心观点必须有来源链接**——没有来源的具体数字、框架名称不能写
2. **不编造内容**——宁可留空，不写未经验证的信息
3. **策展而非复制**——提炼核心洞察，不逐字粘贴原文
4. 写完后设 `status: needs-review`，人工审查后改为 `reviewed`

---

## 执行流程

### 开始新任务前

```
1. 读取 COLLECTION_STATUS.md，了解当前进度
2. 确认本次要处理的人物和内容类型
3. 按优先级（P0 → P1 → P2 → P3）选择任务
4. 若处理 lenny-rachitsky，播客转录已在 people/product/lenny-rachitsky/podcasts/（290集）
```

### 执行中

```
5. 按文件命名规范创建文件
6. 填写完整 frontmatter
7. 内容基于原始来源或现有播客转录提炼，不凭空生成
8. 质量检查：关键数字/框架是否有来源？
```

### 完成后

```
9. 更新 COLLECTION_STATUS.md 对应人物的数字
10. 在更新日志区块添加一行记录（日期 | 操作 | 操作人）
11. git add + git commit，格式：
    feat(collection): add {人物名} {内容类型} ({数量})
    示例：feat(collection): add lenny-rachitsky frameworks (5 docs)
12. git push
```

### Commit 格式

```
feat(collection): add {person} {type} ({count})    # 新增内容
fix(collection): fix {person} {issue}               # 修正问题
docs: update COLLECTION_STATUS                      # 更新进度文件
chore: {other}                                      # 其他维护
```

---

## 常用操作参考

### 从 Lenny 播客转录提炼框架

Lenny 播客转录位于：`people/product/lenny-rachitsky/podcasts/*.md`

每集格式：
```yaml
---
guest: Brian Chesky
title: "..."
youtube_url: "..."
publish_date: 2023-11-12
duration: "1:13:28"
keywords: [growth, metrics, ...]
---

# 标题

## Transcript

SpeakerName (00:00:00):
[对话内容...]
```

**提炼框架的方法**：
1. 读取某集转录
2. 识别嘉宾提出的具体框架/方法论/观点
3. 在该嘉宾的 `frameworks/` 目录下创建对应框架文件
4. 如果嘉宾不在 anima-base 人物目录内，在 lenny-rachitsky 的 `frameworks/` 下创建以嘉宾命名的框架文件

### 新建人物 profile

```bash
mkdir -p people/{category}/{person-slug}/{podcasts,articles,frameworks,quotes,books,talks,twitter}
touch people/{category}/{person-slug}/profile.md
```

然后按 profile.md 标准结构填写内容。

### 查看当前进度

```bash
# 统计某人物各类文件数
person="brian-chesky"
category="product"
base="people/$category/$person"
echo "profile: $(ls $base/profile.md 2>/dev/null | wc -l)"
echo "podcasts: $(find $base/podcasts -name '*.md' 2>/dev/null | wc -l)"
echo "frameworks: $(find $base/frameworks -name '*.md' 2>/dev/null | wc -l)"
echo "articles: $(find $base/articles -name '*.md' 2>/dev/null | wc -l)"
```

---

## 相关仓库

| 仓库 | 说明 |
|------|------|
| [fisher-byte/anima-ai](https://github.com/fisher-byte/anima-ai) | Anima AI 应用，本库内容的消费方 |
| [fisher-byte/anima-base](https://github.com/fisher-byte/anima-base) | 本仓库 |
| [ChatPRD/lennys-podcast-transcripts](https://github.com/ChatPRD/lennys-podcast-transcripts) | Lenny 播客完整转录原始来源（已导入本库） |

---

## 注意事项

- **不要修改已有的手写策展文件**（`20230910-*`、`20231120-*`、`20240115-*` 开头的三个文件是人工策展版本，质量高于自动导入的转录）
- **COLLECTION_STATUS.md 必须在每次任务后更新**，这是进度的唯一真相来源
- **不要提交 media/ 或 files/ 中的大文件**到 git，只提交 markdown 索引文件
- **translations/zh-cn/ 目前为空**，翻译任务是独立的低优先级工作流
