---
framework: Pre-mortem Framework
creator: Shreyas Doshi
source: Medium Article, Stripe Practice, Coda Template
verification_status: verified
verification_date: 2026-03-11
content_type: curated_framework
tags: [risk-management, project-planning, prevention, launch]
---

# Pre-mortem Framework

## 框架概述

Pre-mortem 是 Shreyas Doshi 在 Stripe 开发并推广的风险预防框架。与传统的 Post-mortem（项目失败后分析）不同，Pre-mortem 是在项目开始或发布前进行，目的是提前识别和预防可能导致失败的问题。

## 核心理念

> "The best way to deal with problems is to prevent them from happening in the first place."

传统问题管理的悖论：
- 领导者经常被赞扬"救火"
- 但火原本可以预防
- Pre-mortem 将重点从"解决问题"转向"预防问题"

## Pre-mortem vs Post-mortem

| 维度 | Post-mortem | Pre-mortem |
|-----|-------------|------------|
| **时机** | 项目失败后 | 项目开始/发布前 |
| **目的** | 分析失败原因 | 预防失败发生 |
| **态度** | 反应式 | 主动式 |
| **价值** | 学习教训 | 避免损失 |
| **心态** | 回顾过去 | 预判未来 |

## Tigers, Paper Tigers, Elephants 框架

Shreyas 创造了一个独特的分类方法来处理Pre-mortem中识别的问题：

### 🐯 Tigers (老虎)
**真正的威胁，需要立即行动**

**特征**:
- 真实存在的重大风险
- 不处理会导致项目失败
- 需要投入资源解决
- 无法忽视

**处理方式**:
- 优先分配资源
- 制定具体解决方案
- 指定负责人
- 设定截止日期

### 📄 Paper Tigers (纸老虎)
**看起来可怕但实际可控**

**特征**:
- 表面上看起来严重
- 实际上有解决方案
- 团队可能过度担心
- 需要澄清而非行动

**处理方式**:
- 分析为什么看起来可怕
- 展示已有的缓解措施
- 降低团队焦虑
- 监控但不过度投入

### 🐘 Elephants (房间里的大象)
**被忽视的重大问题**

**特征**:
- 大家都知道但不愿讨论
- 可能涉及敏感话题
- 忽视会导致严重后果
- 需要勇气来提出

**处理方式**:
- 创造安全的讨论环境
- 明确提出来讨论
- 不回避难题
- 制定解决计划

## Pre-mortem 执行流程

### Phase 1: 准备 (Before Meeting)

1. **确定范围**
   - 明确项目/发布的边界
   - 确定时间范围

2. **邀请参与者**
   - 跨职能代表
   - 不同视角的人
   - 包括怀疑者

3. **准备问题**
   > "假设现在是[未来某日期]，这个项目彻底失败了。是什么导致了失败？"

### Phase 2: 执行 (During Meeting)

1. **设定场景** (5分钟)
   - 描述假设的失败情景
   - 强调是"假设已经失败"

2. **独立思考** (10分钟)
   - 每人独立写下可能的失败原因
   - 不讨论，避免群体思维

3. **分享整合** (20分钟)
   - 轮流分享
   - 整合相似的问题
   - 不评判，只记录

4. **分类** (15分钟)
   - 将问题分为 Tigers, Paper Tigers, Elephants
   - 讨论分类理由

5. **制定行动** (20分钟)
   - 为每个Tiger制定解决方案
   - 指定负责人和截止日期
   - 确定监控机制

### Phase 3: 跟进 (After Meeting)

1. **文档记录**
   - 记录所有识别的问题
   - 记录分类和行动计划

2. **持续跟踪**
   - 定期检查Tiger的解决进度
   - 监控Paper Tigers是否变化
   - 重新评估Elephants

## Pre-mortem 模板

```markdown
# Pre-mortem: [项目名称]

## 基本信息
- 日期: 
- 参与者:
- 项目发布日期:

## 假设场景
"现在是[发布后1个月]，[项目名称]彻底失败了..."

## 识别的问题

### 🐯 Tigers (需立即行动)
| 问题 | 负责人 | 截止日期 | 状态 |
|-----|--------|---------|------|
| | | | |

### 📄 Paper Tigers (需要澄清)
| 问题 | 为什么是纸老虎 | 监控方式 |
|-----|--------------|---------|
| | | |

### 🐘 Elephants (需要讨论)
| 问题 | 讨论计划 | 决策日期 |
|-----|---------|---------|
| | | |

## 行动计划
[具体行动和时间表]

## 下次检查
[日期和方式]
```

## 最佳实践

### Do ✅

1. **提前做，不要太晚**
   - 在还有时间修正时做
   - 不要等到发布前一天

2. **创造安全环境**
   - 鼓励提出担忧
   - 不批评"负面"想法

3. **包含多样视角**
   - 工程、设计、销售、支持
   - 不只是核心团队

4. **落实到行动**
   - 没有行动的Pre-mortem是浪费时间
   - 明确负责人和截止日期

### Don't ❌

1. **不要变成抱怨会**
   - 聚焦可行动的问题
   - 不是发泄情绪

2. **不要只做一次**
   - 定期重新评估
   - 情况会变化

3. **不要忽视Elephants**
   - 最危险的往往是被忽视的
   - 需要勇气去讨论

## Shreyas Doshi 原话

> "Pre-mortems are one of the most powerful tools I've seen for preventing problems before they happen."

> "The key insight of pre-mortems is that it's much easier to think about why something might fail than to think about what might go wrong."

> "Most teams are good at post-mortems. Very few are good at pre-mortems. That's a massive missed opportunity."

## 延伸阅读

- **原文**: [How to Use Pre-mortems](https://medium.com/@shreyashere/how-to-use-pre-mortems-to-prevent-problems-blunders-and-disasters-6ecc6df6e22a)
- **模板**: [Coda Pre-mortem Template](https://coda.io/@shreyas/pre-mortems)
- **视频**: [How to use my pre-mortem doc](https://www.youtube.com/watch?v=Pwh0RFqL2Sk)

---
*Framework curated from Medium article and Stripe practices*
*Last updated: 2026-03-11*
