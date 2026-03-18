# COLLECTION_STATUS — 收集进度追踪

> **Agent 执行入口**：每次开始新一轮收集任务前，先读取本文件了解当前状态；任务完成后更新对应字段。
>
> 最后更新：2026-03-18 19:00 | 版本：1.4

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
| 人物目录（已建立） | 31 | 30 | 103% |
| 有完整 Profile | 26 | 31 | 84% |
| 播客文档——本库策展版 | 74 | 350 | 21% |
| Lenny 播客——完整转录（已导入） | 290 集 | 290 | 100% |
| 文章文档 | 51 | 920 | 6% |
| 框架文档 | 60 | 350 | 17% |
| 书籍摘要 | 0 | 23 | 0% |
| 语录集 | 1 | 28 | 4% |
| 中文翻译 | — | 全量 | — |

---

## 逐人进度表

### Product（产品管理）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Lenny Rachitsky | ✅ | ✅ | 290 | 9 | 21 | 1 | 0 | 0 | P0 | ✅ 290集转录已导入（ChatPRD来源）；✅ Phase 3完成：21个核心框架（新增PM招聘面试/SaaS定价策略/客户访谈最佳实践/功能发布/高绩效团队建设）；✅ 2026-03-17新增9篇决策相关核心文章（决策框架/优先级/PMF/不确定性/SaaS定价/增长渠道/职业路径/Annie Duke/Shreyas Doshi访谈） |
| Brian Chesky | ✅ | ✅ | 10 | 1 | 15 | 1 | 0 | 0 | P0 | ✅ 语录集完成(50+条)；框架最丰富 |
| Marty Cagan | ✅ | ✅ | 6 | 1 | 12 | 0 | 3 | 0 | P0 | ✅ 三本书摘要完成(Inspired/Empowered/Transformed) |
| Shreyas Doshi | ✅ | ✅ | 2 | 1 | 8 | 1 | 0 | 1 | P0 | ✅ 决策案例库启动（Case-01: Stripe Pre-mortem）；Twitter精华(100+条)需API设置(待处理) |
| Gokul Rajaram | ✅ | ✅ | 10 | 1 | 9 | 0 | 0 | 0 | P1 | ✅ 播客扩充完成(10集)；框架已较全 |
| Julie Zhuo | ✅ | ✅ | 17 | 0 | 5 | 0 | 0 | 0 | P1 | ✅ 播客(17)+框架(5) 完成 |
| Teresa Torres | ✅ | ✅ | 11 | 0 | 5 | 0 | 0 | 0 | P1 | ✅ 框架完成 (OST/Interview Snapshot/Assumption Testing/CDH/Experience Map) |
| Jackie Bavaro | ✅ | ✅ | 5 | 0 | 3 | 0 | 0 | 0 | P1 | ✅ profile完整 + 5播客 + 3框架 (Strategy/PEARL/Seniority) |
| John Cutler | ✅ | ✅ | 4 | 0 | 4 | 0 | 0 | 0 | P2 | ✅ Phase 2 完成：完整profile+4框架+4播客 |
| Brandon Chu | ✅ | ✅ | 4 | 0 | 6 | 0 | 0 | 0 | P2 | ✅ Phase 2 轮次11完成：完整profile + 6框架 + 4播客 |

### Growth（增长）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Sean Ellis | ✅ | ✅ | 1 | 0 | 0 | 0 | 1 | 0 | P1 | ✅ 完成：Hacking Growth 书籍摘要 + README |
| Brian Balfour | ✅ | ✅ | 2 | 0 | 6 | 0 | 0 | 0 | P1 | ✅ 完成：6框架(Four Fits/Retention/Loops/System/Experimentation/PLG) + 2播客 + 2 READMEs |
| Andrew Chen | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P1 | ✅ 完成扩充：5框架(Cold Start/Atomic Network/3 Effects/Law Shitty CTR/Tipping) + 4播客(Lenny/Tim Ferriss/Intercom x2) + 2 READMEs |
| Casey Winters | ✅ | ✅ | 3 | 0 | 4 | 0 | 0 | 0 | P2 | ✅ 完成：4框架(PMF Guide/Growth Loops/S-Curves/Acquisition Layering) + 3播客(Lenny系列) + 2 READMEs |
| Elena Verna | ✅ | ✅ | 4 | 0 | 6 | 0 | 0 | 0 | P2 | ✅ Phase 2 轮次12完成：6框架 + 4播客 |
| Chamath Palihapitiya | ✅ | ✅ | 5 | 0 | 7 | 0 | 0 | 0 | P2 | ✅ Phase 2 扩充完成：7框架 + 5播客 + 2 READMEs |
| Gustaf Alströmer | ✅ | ✅ | 2 | 0 | 5 | 0 | 0 | 0 | P3 | ✅ Phase 4 完成：profile + 5框架 + 2播客 + 3 READMEs |
|| Naval Ravikant | ✅ | ✅ | 3 | 0 | 5 | 0 | 0 | 0 | P4 | ✅ Phase 4 完成：完整profile + 5框架(Specific Knowledge/Happiness/Compound Interest/Long-Term/First Principles) + 3播客(JRE/TF #473/#136) + 3 READMEs |

### Marketing（营销）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Seth Godin | ✅ | ✅ | 6 | 3 | 5 | 0 | 0 | 0 | P1 | ✅ 核心框架完成 + 6播客(Lenny/Tim Ferriss x2/SPI/Guy Kawasaki/TED Radio Hour) |
| April Dunford | ✅ | ✅ | 3 | 1 | 10 | 0 | 0 | 0 | P1 | ✅ 10个frameworks + 3播客完成(Lenny/Knowledge Project/Everyone Hates Marketers)；新增Differentiated Value框架(Obviously Awesome 2nd Ed核心) |
| Ann Handley | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P2 | ✅ P4完成：5框架(Writing GPS/Everybody Writes/Content Rules/Post-Info Age/15min Marketing) + 4播客 + 2 READMEs |
| David Ogilvy | ✅ | ✅ | 0 | 0 | 0 | 0 | 0 | 0 | P2 | 经典人物，需补书籍摘要 |
| Dave Gerhardt | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P2 | ✅ Phase 2 轮次14完成：5框架 + 4播客 |
| Rand Fishkin | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P2 | ✅ Phase 2 轮次15完成：5框架 + 4播客 |
| Katelyn Bourgoin | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P4 | ✅ Phase 4 完成：完整profile + 5框架(Trigger Technique/Customer Whisperer System/5 F's/Switch Interview/JTBD Marketing) + 4播客 + 3 READMEs |

### Leadership（领导力）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Ben Horowitz | ✅ | ✅ | 1 | 0 | 0 | 0 | 2 | 0 | P1 | ✅ 书籍摘要完成 (The Hard Thing + What You Do) |
| Ray Dalio | ✅ | ✅ | 2 | 0 | 5 | 0 | 0 | 0 | P1 | ✅ Principles 核心框架完成 (5篇)；✅ 2026-03-17新增2个高质量播客(All-In 2025/Lex Fridman 2019) |
| Satya Nadella | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P2 | ✅ Phase 2 轮次16完成：5框架 + 4播客 |
| Reed Hastings | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P2 | ✅ Phase 2 轮次17完成：5框架 + 4播客 |
| Andy Grove | ✅ | ✅ | 3 | 0 | 5 | 0 | 0 | 0 | P3 | ✅ Phase 2 轮次18完成：5框架 + 3播客 |
| Patrick Lencioni | ✅ | ✅ | 4 | 0 | 5 | 0 | 0 | 0 | P4 | ✅ P4新增：profile + 5框架 + 4播客 + README |

### Startup（创业）

| 人物 | 目录 | profile | podcasts | articles | frameworks | quotes | books | talks | 优先级 | 备注 |
|------|:----:|:-------:|:--------:|:--------:|:----------:|:------:|:-----:|:-----:|:------:|------|
| Paul Graham | ✅ | ✅ | 0 | 48 | 0 | 0 | 0 | 0 | P1 | ✅ Essays已补充至48篇精选 |

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
| ~~John Cutler~~ | ~~product~~ | ✅ 已完成 |
| ~~Brandon Chu~~ | ~~product~~ | ✅ 已完成 |
| ~~Elena Verna~~ | ~~growth~~ | ✅ 已完成 |
| ~~Chamath Palihapitiya~~ | ~~growth~~ | ✅ 已完成 |
| ~~Dave Gerhardt~~ | ~~marketing~~ | ✅ 已完成 |
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

| Amanda Natividad | marketing | ROADMAP Phase 2 |

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
  [x] lenny-rachitsky: ✅ Phase 3完成 30个frameworks (2026-03-18) — 原有24个 + 新增6个（North Star Metric/User Activation/Product Intuition Development/User Onboarding/AI Evals/Product Velocity） | Phase 3轮次2完成：基于290集播客转录提炼2个高价值框架（AI Evals Framework完整方法论/Product Velocity Framework速度质量平衡），frameworks总数28→30个
      参考源：https://github.com/ChatPRD/lennys-podcast-transcripts
  [x] brian-chesky: ✅ 已完成 quotes.md (50+ 条) (2026-03-11)
  [x] marty-cagan: ✅ 已完成 3本书籍摘要 (Inspired, Empowered, Transformed) (2026-03-11)
  [ ] shreyas-doshi: 补充 twitter/ 精华 (需要Twitter API，暂时跳过) | ✅ **Phase 3轮次1完成**（2026-03-18 22:00）：决策案例库启动，新增 Case-01 Stripe Pre-mortem 决策案例（~11KB A级文档），完整记录 Shreyas 在 Stripe 使用改进版 Pre-mortem 方法的决策过程：背景/选项/理由/结果/启发式，包含 Tigers-Paper Tigers-Elephants 隐喻框架完整应用，5个核心启发式规则（预防优于治疗/心理安全词汇/系统化预警/结构化流程/权衡成本价值），多来源验证（Coda/Medium/Lenny's Podcast），为其他人物决策案例建立参考模板 | ✅ **Phase 3轮次2完成**（2026-03-19 00:00）：决策案例扩充，新增 Case-02 Google时期LNO框架的发现与应用（~13KB A级文档），完整记录 Shreyas 在 Google 前三年作为新任PM经历压力、发现任务价值差异、创造LNO（Leverage-Neutral-Overhead）框架的完整决策过程，包含三类任务定义/精力分配策略/实施方法/长期影响，6个核心启发式规则（任务价值幂律分布/精力匹配杠杆/完成≠影响/O任务机会成本/动态分类/说不的战略价值），多来源验证（Lenny's Podcast/Medium文章/Coda模板/Twitter），decision-cases总数1→2
  [x] zhang-xiaolong: ✅ 已完成 profile + 6 frameworks + 2 podcasts + 1 books + 18 articles + 1 quotes + 6 talks + 3 interviews + **22 decision cases** + **1 evolution timeline** + **1 controversies analysis** (2026-03-18) — Core Principles, Discovering Needs, Product Design, Great Product, Product Temperament, Product Details | 2017/2019公开课演讲、推荐10本好书、产品世界观、腾讯内刊专访、新华社采访、产品方法论、语录集、2016/2017/2018/2020/2021微信公开课演讲 | Phase 0轮次1完成第二批：新增2篇关键文章(2015年微信公开课PRO版八大理念+2012年微信背后的产品观演讲)，articles总数16→18篇，补充公众平台理念(去中心化/生态系统/动态系统)和产品设计哲学(简单之美/人性洞察/摇一摇案例) | **P0完成** 决策案例库22个案例(新增小程序战略决策)：10核心+12扩展，~265KB证据+73启发式 | **P1完成** 观点演化时间线(2000-2021)：五阶段轨迹+5大观点演化(工具/用户/社交/平台/克制)+3转折点+高频词统计+不变量提炼，8000字A级分析 | **P1完成** 反例与争议材料(2026-03-18 19:00)：~18KB系统性分析，覆盖张小龙承认的2个失误(短视频风口/公众号路径依赖)、3个用户强烈反对功能(已读/朋友圈广告/提现收费)、3个失败产品(漂流瓶/微信电话本/边缘化功能)、3个业界批评维度(过度克制/封闭生态/言论审查)、能力边界明确化(✅熟人社交⚠️陌生人社交⚠️内容平台)、8个反向启发式，A级证据多源验证，为Persona建立边界感 | **Phase 0轮次7完成**：综合查漏新增1篇内部分享（2016年WXG领导力大会：KPI是副产品/警惕复杂流程/敏捷团队/轮岗机制），talks总数5→6篇，补充管理哲学、组织效能、QQ邮箱敏捷转型完整经验
  [x] wang-huiwen: ✅ 已完成 profile + 4 frameworks + 1 podcasts + 16 articles + 4 talks + **6 decision cases** (2026-03-18) — Core Competencies, Following Rules, π-Talent, Latecomer Advantage | 连续创业传奇(校内网/淘房网/美团/AI)、清华课程、π型人才演讲、互联网AB面、AI时代崛起、决策方法论、2024回归美团顾问、AI英雄榜招募 | **Phase 0轮次10完成**（2026-03-18）：综合查漏新增1篇关键一手材料(2023年AI英雄榜招募帖原文)，articles总数8→16篇(发现实际已有16个文档)，补充75%股份给研发团队、个人不占股、打造中国OpenAI、5千万美元投资、人才招募策略完整一手证据，A级原始材料(即刻发布) | **Phase 0轮次9完成**（2026-03-18）：综合查漏新增1篇关键文章(2024年回归美团任顾问)，articles总数7→8篇，补充健康管理、职业规划灵活性、创始人价值延续、企业人才长期投资完整案例，A级新闻证据 | **Phase 0轮次8完成**：综合查漏新增1个关键演讲(2020年混沌大学完整决策课，~24000字)，talks总数3→4篇，补充战略决策完整方法论：规模效应/马太效应/产业链/先发后发优势/时机判断/存量市场策略/组织决策/需求本质/认知形成，结合美团千团大战/外卖密度经济/打车战略撤退三大实战案例，A级证据系统性阐述 | Phase 0轮次6完成：新增3个演讲(2020年清华"不设限的人生"/2020年混沌大学决策演讲/2019年战略与组织能力)，覆盖π型人才、快速学习、核心竞争力、战略决策、规模效应、马太效应、先发后发优势、组织能力建设完整体系 | Phase 0轮次2完成：新增2篇深度文章(2023年AGI创业访谈/2020年退休全记录)，articles总数5→7篇，补充AI创业决策、退休决策、工作生活平衡、知止不殆、运气归因完整框架 | **P1完成** 决策案例库扩充：新增4个案例(case-03美团外卖后发制人/case-04前三战略/case-05退休决策/case-06光年AI创业)，总计6个案例，涵盖战略时机选择、市场定位、职业规划、二次创业完整决策场景，12个新增启发式(后发思维盲区/三年试错/前三法则/知止不殆/技术周期窗口等)，~40KB A级证据

P1 - 有 profile 但内容稀薄的人物：
  [x] julie-zhuo: ✅ 已完成 10个podcasts + 5个frameworks (2026-03-18) — Punk Rock HR, Pivot, Hurry Slowly, Accidental Creative, Design Better, Growth Podcast, Founder Things, HBR Leadership, Let's Fix Work, FranklinCovey | Three Ps, Diagnose/Treat, Feedback, User Guide, Managing Up | **Phase 1轮次13完成**（2026-03-18 23:00）：新增6个高质量播客访谈(Design Better 2024 Rewind/The Growth Podcast AI Leadership 2025/Founder Things Interview 2023/HBR On Leadership 2024/Let's Fix Work 2019/FranklinCovey Caring Without Lowering the Bar 2026)，podcasts总数4→10，覆盖leadership vs management区分、三大管理桶(人员/流程/目标)、AI时代产品领导力、管理不确定性、反馈文化、高标准与同理心平衡、Facebook成长历程完整体系，~38KB A级文档，多来源验证(InVision/Aakash Gupta/Helena Price/HBR/Laurie Ruettimann/FranklinCovey)，目标10+播客达成
  [x] teresa-torres: ✅ 已完成 12个podcasts + 5个frameworks (2026-03-12) — Lenny, Boundaryless, It Shipped, AgileData, Product People, Product Rising, UX Research, Brave UX, Aakash Gupta, ITX, All Things Product, Just Now Possible | CDH, OST, Interview Snapshot, Experience Map, Assumption Testing
  [x] paul-graham: ✅ 已完成 profile.md + 74篇essays (2026-03-18) | **Phase 1轮次9完成**：新增13篇高质量精选文章(Superlinear Returns/How to Get New Ideas/Schlep Blindness/Black Swan Farming/Keep Your Identity Small/Maker's Schedule Manager's Schedule/Life is Short/Write Like You Talk/Frighteningly Ambitious Startup Ideas/How People Get Rich Now/Cities and Ambition/The Refragmentation/Having Kids)，覆盖超线性回报、创意产生、schlep盲区、黑天鹅投资、身份认同、时间管理、人生哲学、写作技巧、野心想法、财富创造、城市文化、社会分化、育儿反思完整体系，essays总数17→30篇(实际增加13篇，之前记录有误)
  [x] april-dunford: ✅ 已完成 10个frameworks + 3 podcasts (2026-03-18) — Positioning Canvas, 10-Step Process, 5 Components, Sales Pitch Framework, Market Category, Competitive Alternatives, Feature List Trap, Best Customers Exercise, Market Category Strategies, Differentiated Value | 新增Differentiated Value框架(Obviously Awesome第二版2026核心扩展章节)，涵盖差异化价值定义、识别流程、价值vs异议处理区分、无差异化幻觉破除、实战应用等完整方法论
  [x] ben-horowitz: ✅ 已完成 profile + 1 books (2026-03-18) — The Hard Thing About Hard Things完整摘要(~8500字A级文档，包含9章详细拆解、核心框架Peacetime vs Wartime CEO、Lead Bullets理念、招聘高管6大陷阱、裁员正确方式、决策金句集、适用场景与启发)，覆盖创业危机管理、领导力切换、团队建设、文化塑造完整体系 | **Phase 1轮次11完成**：创建完整profile(~12000字，职业生涯轨迹Netscape→Opsware→a16z、核心思想框架6个、投资哲学、450亿美元规模、100+独角兽、领导力风格、业界评价、争议与反思)，补充The Hard Thing About Hard Things书籍摘要，建立Ben Horowitz完整知识体系
  [x] ray-dalio: ✅ 已完成 9个frameworks (2026-03-18) — Pain+Reflection, 5-Step, Idea Meritocracy, Radical Transparency, Economic Machine, Believability-Weighted, Meaningful Work & Relationships, Two Biggest Barriers, Baseball Cards & Dot Collector

P2 - 空目录人物（建立 profile）：
  [x] jackie-bavaro: ✅ 已完成 profile + 3 frameworks + 4 podcasts (2026-03-12)
  [x] john-cutler: ✅ 已完成 profile + 4 frameworks + 4 podcasts (2026-03-12)
  [x] brandon-chu: ✅ 已完成 profile + 6 frameworks + 4 podcasts (2026-03-12)
  [x] elena-verna: ✅ 已完成 profile + 10 frameworks + 5 podcasts (2026-03-15) — Motions x Levers Model, Freemium vs Trial, Reverse Trial, Growth Squad Sequencing, 10 Growth Tactics That Never Work
  [x] chamath-palihapitiya: ✅ 已完成 profile + 5 frameworks + 4 podcasts (2026-03-12)
  [x] dave-gerhardt: ✅ 已完成 profile + 5 frameworks + 4 podcasts (2026-03-12)
  [x] rand-fishkin: ✅ 已完成 profile + 5 frameworks + 4 podcasts (2026-03-12)
  [x] satya-nadella: ✅ 已完成 profile + 5 frameworks + 4 podcasts (2026-03-12)
  [x] reed-hastings: ✅ 已完成 profile + 5 frameworks + 4 podcasts (2026-03-12)
  [x] andy-grove: ✅ 已完成 5 frameworks + 3 podcasts + 3 READMEs (2026-03-12)

P3 - 新增人物：
  [x] naval-ravikant: ✅ 已完成 profile + 6 frameworks + 4 podcasts (2026-03-12)
  [x] gustaf-alstromer: ✅ 已完成 profile + 5 frameworks + 2 podcasts + 3 READMEs (2026-03-12)

P4 - 经典人物补充：
  [x] david-ogilvy: ✅ 已完成 1 framework (7 Principles) + 60+ quotes + 2 books index + 2 READMEs (2026-03-14)
  [x] amanda-natividad: ✅ 已完成 profile + 5 frameworks + 4 podcasts + README (2026-03-12)
  [x] patrick-lencioni: ✅ 已完成 profile + 5 frameworks + 4 podcasts + README (2026-03-13)
  [x] ann-handley: ✅ 已完成 5 frameworks + 4 podcasts + 2 READMEs (2026-03-14)
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
| 2026-03-11 | 创建空档案: Andy Grove |                                                                                || 2026-03-14 | 张小龙完整档案 (profile + 6 frameworks + 1 article + 1 quotes) | ✅ 已完成 |
| 2026-03-14 | 王慧文完整档案 (profile + 4 frameworks + 1 article) | ✅ 已完成 |
| 2026-03-11 | 创建空档案: Andy Grove | ✅ 已完成 |
|| 2026-03-12 | Phase 4: Gustaf Alströmer 完整档案 (profile + 5 frameworks + 2 podcasts + 3 READMEs) | ✅ 已完成 |
| 2026-03-17 | Lenny 深度决策内容收集：7 篇决策框架文档 (PMF/定价/渠道选择/优先级/职业路径/不确定性/通用决策) | ✅ 已完成 |
| 2026-03-17 | Lenny 框架扩充 Phase 4：3 个核心框架 (Product Roadmap Planning/SaaS Metrics & KPI Dashboard/Product Operations) | ✅ 已完成 |
|| 2026-03-17 | Lenny 深度决策内容收集：7 篇决策框架文档 (PMF/定价/渠道选择/优先级/职业路径/不确定性/通用决策) | ✅ 已完成 |
|| 2026-03-17 | Lenny 框架扩充 Phase 4：3 个核心框架 (Product Roadmap Planning/SaaS Metrics & KPI Dashboard/Product Operations) | ✅ 已完成 |
|| 2026-03-17 | 张小龙决策案例库启动：2 个高质量决策案例 (视频号战略/公众号平台化)，含背景/选项/理由/结果/启发式，A级证据支撑 | ✅ 已完成 |
|| 2026-03-17 | Phase 0 轮次3：张小龙 interviews 启动，收集3篇深度访谈 (2013商业价值&极客公园/2013腾讯月刊/2021极客公园) | ✅ 已完成 |
|| 2026-03-17 | Lenny决策案例库启动：Superhuman PMF Survey决策 (Rahul Vohra, A级证据) | ✅ 已完成 |
|| 2026-03-18 00:35 | 张小龙决策案例库扩充：5个案例完成（50%） | ✅ 已完成 |
|| 2026-03-18 01:00 | 决策案例库持续扩充：张小龙6个+Lenny 2个，总计8个案例 | ✅ 已完成 |
|| 2026-03-17 | Lenny 决策案例库新增：Case-13 Netflix密码共享限制决策（Greg Peters/Reed Hastings，13K字深度案例，DHM框架分析） | ✅ 已完成 |
|| 2026-03-18 11:30 | 王慧文决策案例库扩充：新增4个案例（case-03美团外卖后发制人/case-04前三战略/case-05退休决策/case-06光年AI创业），总计6个案例，12个新增启发式，~40KB A级证据 | ✅ 已完成 |

|| 2026-03-18 [Current] | Lenny Rachitsky框架扩充：基于290集播客转录提炼2个高价值框架（AI Evals Framework完整方法论+Product Velocity Framework速度质量平衡），frameworks总数28→30个，Phase 3持续推进 | ✅ 已完成 |
|| 2026-03-18 19:00 | **战略P1任务完成**：张小龙反例与争议材料收集（~18KB系统性分析），覆盖承认的失误（短视频风口/公众号路径依赖）、用户强烈反对功能（已读/朋友圈广告/提现收费）、失败产品（漂流瓶/微信电话本）、业界批评（过度克制/封闭生态/言论审查）、能力边界明确化（✅熟人社交⚠️陌生人社交⚠️内容平台）、8个反向启发式，A级证据多源验证，为Persona建立边界感和真实感，补齐"决策证据库"关键拼图 | ✅ 已完成 |

|| 2026-03-18 [Current] | Phase 0轮次8完成：王慧文综合查漏新增1个关键演讲(2020年混沌大学完整决策课~24000字)，talks总数3→4篇，补充战略决策完整方法论体系：规模效应/马太效应/产业链/先发后发优势/时机判断/存量市场策略/组织决策/需求本质/认知形成，结合美团千团大战/外卖密度经济/打车战略撤退三大实战案例，A级证据系统性阐述 | ✅ 已完成 |

|| 2026-03-18 | Phase 0轮次9完成：王慧文综合查漏新增1篇关键文章(2024年回归美团任顾问职位)，articles总数7→8篇，补充健康管理与职业规划平衡、创始人价值灵活实现、企业人才长期投资策略完整案例，A级新闻报道证据(~6KB)，关键词：健康优先/顾问角色/价值延续/光年之外收购/战略连续性 | ✅ 已完成 |

|| 2026-03-18 12:00 | Phase 0轮次10完成：王慧文综合查漏新增1篇关键一手材料(2023年AI英雄榜招募帖原文，即刻平台发布)，articles实际统计16篇(之前未准确统计)，补充王慧文AI创业最重要的启动文档：75%股份给研发团队/个人肉身不占股/打造中国OpenAI/5千万美元投资/业界顶级人才标准/狂热信念筛选/造福人类价值观/杂事打理承诺完整一手证据，A级原始材料(~10KB)，标志性创业招募案例，Phase 0王慧文阶段全部完成 | ✅ 已完成 |

|| 2026-03-18 | Phase 0轮次7完成：张小龙综合查漏新增1篇内部分享（2016年WXG领导力大会：KPI是副产品/警惕复杂流程/敏捷团队/轮岗机制），talks总数5→6篇，补充管理哲学、组织效能、QQ邮箱敏捷转型完整经验，A级证据14000字 | ✅ 已完成 |

|| 2026-03-18 17:00 | Phase 1轮次10完成：April Dunford frameworks扩充，新增Differentiated Value Framework(Obviously Awesome第二版2026核心扩展章节)，frameworks总数9→10个，补充差异化价值完整方法论：价值定义/识别流程(三层模型)/价值vs异议处理区分/无差异化幻觉破除/四层价值体系/持续优化机制/实战应用指南，基于第二版新增章节和2024-2026年Substack文章，~10KB A级框架文档 | ✅ 已完成 |

|| 2026-03-18 22:00 | **Phase 3决策案例扩充**：Shreyas Doshi 决策案例库启动，新增 Case-01 Stripe Pre-mortem 决策（~11KB A级文档），完整记录 Shreyas 在 Stripe 使用改进版 Pre-mortem 方法预防产品发布问题的决策过程：情境背景/三个决策选项对比（继续现状/标准pre-mortem/改进版+隐喻）/决策理由（预防成本/心理安全词汇/持续性机制/结构化流程）/决策结果（平静发布/团队士气/方法传播）/5个启发式规则（预防优于治疗/心理安全词汇降低沟通成本/系统化预警需要持续机制/结构化流程确保质量/权衡流程成本和价值），包含 Tigers-Paper Tigers-Elephants 隐喻框架完整应用场景和1小时会议流程设计，多来源A级验证（Coda模板/Medium文章/Lenny's Podcast访谈），为其他产品专家决策案例建立参考模板，decision-cases总数 0→1 | ✅ 已完成 |
