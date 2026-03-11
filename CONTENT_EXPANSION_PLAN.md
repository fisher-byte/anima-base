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

### 内容类型
```
person-name/
├── profile.md                    # 人物档案（已有）
├── books/                        # 书籍核心观点
│   ├── book-title-summary.md
│   └── book-title-frameworks.md
├── articles/                     # 文章精华
│   ├── YYYY-MM-DD-article-title.md
│   └── topic-collection.md
├── podcasts/                     # 播客洞察（非完整转录）
│   ├── YYYY-MM-DD-podcast-name.md
│   └── key-insights.md
├── frameworks/                   # 方法论框架
│   ├── framework-name.md
│   └── toolkit.md
└── resources.md                  # 资源索引
```

---

## 🚀 实施计划

### Phase 1: 核心人物扩充 (5人)
优先级最高，创建完整内容：

1. **Lenny Rachitsky** (Product)
   - 来源: Lenny's Newsletter 320+ 文章
   - 来源: Lenny's Podcast 320+ 集
   - 书籍: 《The Product-Led Playbook》内容框架
   - 预计产出: 20+ 个主题框架文档

2. **Brian Chesky** (Product/Leadership)
   - 来源: Master of Scale 播客洞察
   - 来源: Lenny's Podcast 访谈
   - 框架: 11星级体验、产品化公司
   - 预计产出: 15+ 个框架文档

3. **Marty Cagan** (Product)
   - 书籍: 《Inspired》《Empowered》核心框架
   - 来源: SVPG 博客文章精选
   - 来源: 播客访谈洞察
   - 预计产出: 25+ 个方法论文档

4. **Shreyas Doshi** (Product)
   - 来源: Twitter 精华整理
   - 框架: LNO框架、产品思维模型
   - 来源: 播客访谈
   - 预计产出: 30+ 个框架文档

5. **Gokul Rajaram** (Product)
   - 来源: Lenny's Podcast 访谈
   - 框架: 招聘、产品开发流程
   - 来源: 投资洞察
   - 预计产出: 15+ 个框架文档

### Phase 2: 重要人物扩充 (10人)
中等优先级：

**Product领域**:
- Julie Zhuo (设计与产品)
- Teresa Torres (持续发现)
- John Cutler (产品运营)

**Growth领域**:
- Sean Ellis (增长黑客创始人)
- Brian Balfour (增长框架)
- Andrew Chen (网络效应)

**Marketing领域**:
- Seth Godin (现代营销)
- April Dunford (定位)

**Leadership领域**:
- Ben Horowitz (创业管理)
- Ray Dalio (原则)

### Phase 3: 补充人物 (12人)
基础扩充，重点框架：
- 其余 product/ marketing/ growth/ leadership/ 目录下的人物

---

## 📝 内容创建模板

### 1. 播客洞察文档 (podcasts/)

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
---

# [播客名称] - [嘉宾名称] 核心洞察

> 本文档提炼播客中的核心观点、框架和方法论，非完整转录。
> 原始播客: [链接]

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

### 2. 文章精华文档 (articles/)

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
---

# [文章标题] - 核心提炼

> 本文档提炼文章核心观点和可执行建议。
> 原文: [链接]

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

### 3. 框架文档 (frameworks/)

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
---

# [框架名称]

## 📋 框架概览

**创建者**: [人物名称](../profile.md)
**适用场景**: ...
**预期成果**: ...

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

**处理方式**:
- 提炼核心洞察（非完整转录）
- 结构化框架提取
- 交叉引用验证

### 2. 文章资源
**主要来源**:
- Lenny's Newsletter (Substack)
- First Round Review
- Andreessen Horowitz Blog
- Reforge Blog
- SVPG Blog
- 个人博客/Medium

**处理方式**:
- 核心观点提炼
- 可执行建议提取
- 框架图表化

### 3. 书籍资源
**处理方式**:
- 章节核心观点总结
- 关键框架提取
- 实用工具整理
- **不包含**完整章节或大段原文

### 4. 视频资源
**主要来源**:
- YouTube 访谈/演讲
- 线上课程公开内容
- 会议演讲

**处理方式**:
- 核心观点提炼
- 演示框架整理
- 视觉化内容重构

---

## ⚖️ 版权合规

### 合规原则
1. ✅ **转换性使用**: 提炼、总结、框架化
2. ✅ **归属标注**: 所有内容标注原始来源
3. ✅ **教育目的**: 用于学习和知识分享
4. ✅ **非商业**: 开源项目，非盈利性质
5. ❌ **不复制**: 不直接复制大段原文
6. ❌ **不替代**: 不替代原始内容消费

### 内容类型区分
| 类型 | 可以做 | 不可以做 |
|------|--------|----------|
| 播客 | 核心洞察提炼、框架总结 | 完整逐字转录 |
| 文章 | 要点归纳、观点提炼 | 整篇复制 |
| 书籍 | 章节概要、框架提取 | 完整章节 |
| 视频 | 核心观点、演示框架 | 完整字幕 |

---

## 📊 进度追踪

### 完成标准
每个人物至少包含:
- ✅ 1个完善的 profile.md
- ✅ 3-5个核心框架文档
- ✅ 5-10个播客/文章洞察
- ✅ 1个资源索引 resources.md
- ✅ 所有内容标注来源链接

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

### 数量指标
- 人物档案: 27个 (已有)
- 框架文档: 150+
- 播客洞察: 100+
- 文章精华: 200+
- 总文档数: 500+

### 质量指标
- 来源标注率: 100%
- 框架可执行性: 90%+
- 用户实用性评分: 4.5/5+

---

**制定日期**: 2026-03-11  
**版本**: 2.0  
**状态**: 执行中
