# COLLECTION_STATUS — 收集进度追踪

> **Agent 执行入口**：每次开始新一轮收集任务前，先读取本文件了解当前状态；任务完成后更新对应字段。
>
> 最后更新：2026-03-11 | 版本：1.0

---

## 外部数据源

本库与以下外部仓库联动，作为内容来源和参考：

| 外部仓库 | 内容 | 规模 | 关系 |
|----------|------|:----:|------|
| [ChatPRD/lennys-podcast-transcripts](https://github.com/ChatPRD/lennys-podcast-transcripts) | Lenny's Podcast 完整转录 | 290 集 | 已全量导入至 `people/product/lenny-rachitsky/podcasts/`；Anima AI Lenny Space 的数据基础 |

---

## 全局统计

| 指标 | 当前值 | 目标值 | 完成度 |
|------|:------:|:------:|:------:|
| 人物目录（已建立） | 28 | 30 | 93% |
| 有完整 Profile | 22 | 28 | 79% |
| 播客文档——本库策展版 | 58 | 350 | 17% |
| Lenny 播客——完整转录（已导入） | 290 集 | 290 | 100% |
| 文章文档 | 42 | 920 | 5% |
| 框架文档 | 45 | 350 | 13% |
| 书籍摘要 | 0 | 23 | 0% |
| 语录集 | 1 | 28 | 4% |
| 中文翻译 | — | 全量 | — |

---

## 逐人进度表

### Product（产品管理）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Lenny Rachitsky | ✅ | ✅ | 290 | 0 | 1 | 1 | 0 | 0 | P0 | 290集转录已导入（ChatPRD来源）；需从中提炼框架文档至20+篇 |
| Brian Chesky | ✅ | ✅ | 10 | 1 | 15 | 0 | 0 | 0 | P0 | 框架最丰富，需补 quotes |
| Marty Cagan | ✅ | ✅ | 6 | 1 | 12 | 0 | 0 | 0 | P0 | 需补充 Inspired/Empowered 书籍摘要 |
| Shreyas Doshi | ✅ | ✅ | 2 | 1 | 8 | 1 | 0 | 0 | P0 | Twitter精华(100+条)需API设置(待处理) |
| Gokul Rajaram | ✅ | ✅ | 4 | 1 | 9 | 0 | 0 | 0 | P1 | 框架已较全，需补播客 |
| Julie Zhuo | ✅ | ✅ | 12 | 0 | 5 | 0 | 0 | 0 | P1 | ✅ 播客(12)+框架(5) 完成 |
| Teresa Torres | ✅ | ✅ | 11 | 0 | 5 | 0 | 0 | 0 | P1 | ✅ 框架完成 (OST/Interview Snapshot/Assumption Testing/CDH/Experience Map) |
| Jackie Bavaro | ✅ | — | 1 | 0 | 0 | 0 | 0 | 0 | P2 | 无 profile，需补充 |
| John Cutler | ✅ | — | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 空目录，待启动 |
| Brandon Chu | ✅ | — | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 空目录，待启动 |

### Growth（增长）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Sean Ellis | ✅ | ✅ | 1 | 0 | 0 | 0 | 0 | 0 | P1 | 需补 Hacking Growth 书籍摘要 |
| Brian Balfour | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P1 | 仅有 profile |
| Andrew Chen | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P1 | 仅有 profile，需补 a16z 文章 |
| Casey Winters | ✅ | ✅ | 1 | 0 | 0 | 0 | 0 | 0 | P2 | |
| Elena Verna | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 有 profile，需补充内容 |
| Chamath Palihapitiya | ✅ | — | 0 | 0 | 0 | 0 | 0 | 0 | P3 | 空目录 |

### Marketing（营销）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Seth Godin | ✅ | ✅ | 0 | 3 | 0 | 0 | 0 | 0 | P1 | 有文章，需补框架和播客 |
| April Dunford | ✅ | ✅ | 0 | 1 | 5 | 0 | 0 | 0 | P1 | ✅ Obviously Awesome 框架已完成 (5篇) |
| Ann Handley | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P2 | |
| David Ogilvy | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 经典人物，需补书籍摘要 |
| Dave Gerhardt | ✅ | — | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 空目录 |
| Rand Fishkin | ✅ | — | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 空目录 |

### Leadership（领导力）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Ben Horowitz | ✅ | ✅ | 1 | 0 | 0 | 0 | 0 | 0 | P1 | 需补 Hard Thing 书籍摘要 |
| Ray Dalio | ✅ | ✅ | 0 | 0 | 5 | 0 | 0 | 0 | P1 | ✅ Principles 核心框架完成 (5篇) |
| Satya Nadella | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 有 profile，需补充内容 |
| Reed Hastings | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 有 profile，需补充内容 |
| Andy Grove | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P3 | 有 profile，需补充内容 |

### Startup（创业）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Paul Graham | ✅ | ✅ | 0 | 32 | 0 | 0 | 0 | 0 | P1 | ✅ Essays已补充至32篇精选 |

---

## 缺口分析

### 最高优先级缺口（P0）

1. **Lenny Rachitsky 播客扩充**
   - 当前：3 集模板
   - 缺口：317+ 集完整转录
   - 方法：YouTube 字幕下载 → `yt-dlp` + Whisper 转录
   - 路径：`people/product/lenny-rachitsky/podcasts/`

2. **Brian Chesky 语录集**
   - 当前：0 条
   - 缺口：50+ 条核心语录
   - 方法：从已有 10 集播客文档和框架中提炼
   - 路径：`people/product/brian-chesky/quotes/`

3. **Marty Cagan 书籍摘要**
   - 当前：0 本
   - 缺口：Inspired、Empowered、Transformed 三本书
   - 方法：获取 EPUB → 生成章节摘要
   - 路径：`people/product/marty-cagan/books/`

4. **Shreyas Doshi Twitter 精华**
   - 当前：0 条
   - 缺口：100+ 条精华推文
   - 方法：Twitter API v2 采集
   - 路径：`people/product/shreyas-doshi/twitter/`

### 空档案（有目录无内容）

以下 10 人目录为空，需要建立 profile 并开始内容采集：

| 人物 | 分类 | 建议第一步 |
|------|------|-----------|
| Jackie Bavaro | product | 建 profile.md |
| John Cutler | product | 建 profile.md |
| Brandon Chu | product | 建 profile.md |
| Elena Verna | growth | 建 profile.md |
| Chamath Palihapitiya | growth | 建 profile.md |
| Dave Gerhardt | marketing | 建 profile.md |
| Rand Fishkin | marketing | 建 profile.md |
| Satya Nadella | leadership | 建 profile.md |
| Reed Hastings | leadership | 建 profile.md |
| Andy Grove | leadership | 建 profile.md |

---

## 待收录人物

以下人物已在 ROADMAP 中列出但尚未建立目录：

| 人物 | 分类 | 来源 |
|------|------|------|
| Naval Ravikant | startup | ROADMAP Phase 2 |
| Gustaf Alströmer | growth | ROADMAP Phase 2 |
| Amanda Natividad | marketing | ROADMAP Phase 2 |
| Katelyn Bourgoin | marketing | ROADMAP Phase 2 |
| Patrick Lencioni | leadership | ROADMAP Phase 2 |

---

## Agent 执行指南

### 每次启动前

```
1. 读取本文件（COLLECTION_STATUS.md）了解当前进度
2. 确认要处理的人物和内容类型
3. 按优先级（P0 → P1 → P2 → P3）执行
4. 完成后更新本文件对应人物的数字
5. 提交 commit，格式：feat(collection): add {人物名} {内容类型} ({数量})
```

### 优先执行队列（按顺序）

```
P0 - 核心人物深度扩充：
  [ ] lenny-rachitsky: 基于外部281集转录，提炼框架文档至20篇（当前1篇）
      参考源：https://github.com/ChatPRD/lennys-podcast-transcripts
  [ ] brian-chesky: 补充 quotes.md (50+ 条)
  [ ] marty-cagan: 补充 books/ (Inspired 摘要)
  [ ] shreyas-doshi: 补充 twitter/ 精华

P1 - 有 profile 但内容稀薄的人物：
  [ ] julie-zhuo: 补充 podcasts + frameworks
  [ ] teresa-torres: 补充 podcasts + frameworks
  [x] paul-graham: ✅ 已完成 profile.md + 22篇essays (2026-03-11)
  [ ] april-dunford: 补充 frameworks (Obviously Awesome)
  [ ] ben-horowitz: 补充 books/ (The Hard Thing)
  [ ] ray-dalio: 补充 frameworks (Principles)

P2 - 空目录人物（建立 profile）：
  [ ] jackie-bavaro, john-cutler, brandon-chu
  [ ] elena-verna, dave-gerhardt, rand-fishkin
  [ ] satya-nadella, reed-hastings, andy-grove

P3 - 新增人物：
  [ ] naval-ravikant（建目录 + profile）
  [ ] gustaf-alstromer, amanda-natividad 等
```

### 内容类型说明

| 内容类型 | 存储路径 | 文件命名 | 最低标准 |
|----------|----------|----------|----------|
| 人物档案 | `{person}/profile.md` | `profile.md` | 2000+ 字，含来源链接 |
| 播客文档 | `{person}/podcasts/YYYY-MM-DD-title.md` | 日期前缀 | 核心洞察提炼，含 5+ 要点 |
| 文章文档 | `{person}/articles/YYYY-MM-DD-title.md` | 日期前缀 | 摘要 + 核心框架 |
| 框架文档 | `{person}/frameworks/framework-name.md` | kebab-case | 框架说明 + 应用场景 |
| 语录集 | `{person}/quotes/quotes.md` | `quotes.md` | 50+ 条，含来源 |
| 书籍摘要 | `{person}/books/book-title.md` | kebab-case | 章节摘要 + 核心观点 |
| Twitter 精华 | `{person}/twitter/twitter-threads.md` | 月度文件 | 精华推文 + 上下文 |

### 质量检查清单（每个文件提交前）

```
□ YAML frontmatter 完整（type, person, title, date, source, status）
□ 关键框架/数字有来源链接
□ verification_status 已设置（reviewed / needs-review）
□ 文件名符合命名规范（lowercase-with-hyphens）
□ 无 AI 幻觉内容（框架/数字经过搜索验证）
```

---

## 自动化脚本状态

| 脚本 | 文件 | 功能 | 状态 |
|------|------|------|------|
| RSS 采集 | `scripts/rss_collector.py` | 订阅 Lenny/SVPG/Reforge 等 | 已部署 |
| 内容挖掘 | `scripts/content_miner.py` | 抓取文章内容 | 已部署 |
| GitHub 同步 | `scripts/sync-github.sh` | 自动推送 | 每 15 分钟 |
| 监控修复 | `scripts/monitor-and-fix.sh` | 质量监控 | 运行中 |
| 索引生成 | `scripts/index_generator.py` | 更新主题索引 | 已部署 |
| yt-dlp 转录 | — | YouTube 字幕下载 | **待安装** |
| Whisper 转录 | — | 音频转文字 | **待配置** |
| Twitter 采集 | — | Twitter API v2 | **待配置** |

---

## 更新日志

| 日期 | 操作 | 操作人 |
|------|------|--------|
| 2026-03-11 | 初始化 COLLECTION_STATUS.md，记录当前实际进度 | system |

---

> **注意**：本文件由人工和 Agent 协同维护。每次 Agent 完成一批收集任务后，必须更新对应人物的数字统计，并在更新日志中记录操作。

| 2026-03-11 | 完成P0缺口: Brian Chesky语录集(50+条) | ✅ 已完成 |
| 2026-03-11 | 完成P0缺口: Marty Cagan书籍摘要(Inspired/Empowered/Transformed) | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Jackie Bavaro | ✅ 已完成 |
| 2026-03-11 | 创建空档案: John Cutler | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Brandon Chu | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Elena Verna | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Chamath Palihapitiya | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Dave Gerhardt | ✅ 已完成 |
| 2026-03-11 | 完成P1: April Dunford frameworks (5篇 + 原文) | ✅ 已完成 |
| 2026-03-11 | 完成P1: Ben Horowitz book summary (The Hard Thing) | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Rand Fishkin | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Satya Nadella | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Reed Hastings | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Andy Grove |                                                                                