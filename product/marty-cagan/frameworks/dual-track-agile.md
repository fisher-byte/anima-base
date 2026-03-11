---
framework: Dual-Track Agile
creator: Marty Cagan (概念来自Jeff Patton)
source: SVPG Articles, Inspired Book
verification_status: verified
verification_date: 2026-03-11
content_type: curated_framework
tags: [product-discovery, agile, continuous-discovery, delivery]
---

# 双轨敏捷 (Dual-Track Agile)

## 框架概述

双轨敏捷（也称 Dual-Track Scrum）是 Marty Cagan 推广的产品开发框架，核心是将**发现（Discovery）**和**交付（Delivery）**作为两条并行运行的轨道。这一概念最早由 Jeff Patton 提出，Marty Cagan 将其系统化并广泛传播。

**注意**: Marty Cagan 后来停止使用"双轨敏捷"这个术语，改用**持续发现 (Continuous Discovery)** 和**持续交付 (Continuous Delivery)**，因为"双轨"让人过度关注流程而非原则。

## 核心理念

> "Our higher order objective is to validate our ideas the fastest, cheapest way possible. Actually building and launching a product idea is generally the slowest, most expensive way to validate the idea."

传统敏捷团队的问题：
- Sprint计划会议冗长低效
- Backlog项目定义不清
- 开发过程中仍在敲定细节
- 大量浪费和返工
- 交付速度慢，设计质量差

## 双轨模型

```
┌─────────────────────────────────────────────────────────────┐
│                     产品团队工作流                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  发现轨道 (Discovery Track)                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • 快速生成经过验证的Backlog项目                        │   │
│  │ • 原型设计和用户测试                                  │   │
│  │ • 降低四大风险                                       │   │
│  │ • 协作式工作（PM + Designer + Engineer）              │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↓                                  │
│                   验证过的Backlog                            │
│                          ↓                                  │
│  交付轨道 (Delivery Track)                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • 生成可发布的软件                                    │   │
│  │ • Sprint开发                                         │   │
│  │ • 持续集成和部署                                      │   │
│  │ • 质量保证                                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 发现轨道 (Discovery Track)

**目标**: 快速生成经过验证的产品Backlog项目

**核心活动**:
- 用户研究和访谈
- 原型设计
- 可用性测试
- 技术可行性评估
- 商业可行性验证

**输出**: 经过验证、定义清晰的Backlog项目

**参与者**: 产品经理、产品设计师、技术负责人（产品三人组）

### 交付轨道 (Delivery Track)

**目标**: 生成可发布的、高质量的软件

**核心活动**:
- Sprint开发
- 代码编写和审查
- 测试
- 持续集成/部署
- 运维

**输出**: 可发布的软件

**参与者**: 整个工程团队

## 关键原则

### 1. 并行而非串行

- 发现和交付同时进行
- 不是"先发现完再交付"
- 持续不断的循环

### 2. 协作而非交接

> "The work flow is not characterized by each role delivering artifacts on to the next step; rather it is collaborative – the product manager, designer and lead engineer are working together, side-by-side."

- PM、设计师、工程师并肩工作
- 不是生成文档然后交接
- 原型就是规格说明

### 3. 验证在构建之前

> "Unlike a Waterfall process where the validation happens after release, in Dual-Track Agile, we are validating during Discovery."

- 发现阶段就完成验证
- 不等到发布后才知道结果
- "Fake it before we make it"

### 4. 最快最便宜地验证

- 优先使用原型
- 优先使用定性研究
- 生产代码是最后手段

## 与传统敏捷的区别

| 维度 | 传统敏捷 | 双轨敏捷 |
|-----|---------|---------|
| **验证时机** | 发布后 | 构建前 |
| **Backlog来源** | 利益相关者需求 | 发现轨道验证 |
| **PM角色** | 管理Backlog | 主导发现 |
| **设计角色** | 交付设计稿 | 原型验证 |
| **工程师参与** | 实现阶段 | 发现就参与 |
| **风险管理** | 反应式 | 前置式 |

## 实施要点

### 发现轨道最佳实践

1. **原型先行**
   - 使用原型而非需求文档
   - 原型是沟通和验证工具
   - 原型精度根据验证目的调整

2. **持续用户测试**
   - 每周至少一次用户测试
   - 定性优先于定量
   - 快速迭代原型

3. **三人组协作**
   - PM、设计师、工程师一起工作
   - 共同参与用户访谈
   - 共同决定解决方案

4. **精益UX**
   - 关注学习而非交付物
   - 假设驱动设计
   - 最小化文档

### 交付轨道最佳实践

1. **只交付验证过的项目**
   - 不接受未验证的需求
   - Backlog项目定义清晰
   - 减少开发中的变更

2. **持续交付**
   - 小批量发布
   - 自动化测试和部署
   - 快速反馈循环

## 常见问题

### Q: 两条轨道如何同步？

A: 通过验证过的Backlog同步。发现轨道产出定义清晰的Backlog项目，交付轨道从中提取工作。

### Q: 工程师如何分配时间？

A: 技术负责人主要参与发现，其他工程师主要负责交付。但所有工程师都应该了解发现的进展。

### Q: 发现轨道需要多少时间？

A: 不是固定时间。一个想法可能几小时就能验证，也可能需要几周。关键是够快、够便宜。

## Marty Cagan 原话

> "If your product team is frustrated by the amount of waste and the slow pace in achieving actual business results, consider trying out Dual-Track Agile."

> "Much of the time we can in fact do our validation before we write any production code, in the spirit of 'fake it before we make it.'"

## 演进说明

Marty Cagan 后来更倾向于使用以下术语：

- **持续发现 (Continuous Discovery)** 替代"发现轨道"
- **持续交付 (Continuous Delivery)** 替代"交付轨道"

这样做是为了强调：
1. 这是持续的过程，而非阶段
2. 关注原则而非流程
3. 避免过度形式化

## 延伸阅读

- **原文**: [Dual-Track Agile](https://www.svpg.com/dual-track-agile/)
- **更新**: [Process vs Model](https://www.svpg.com/process-vs-model/)
- **相关**: [Continuous Discovery](https://www.svpg.com/continuous-discovery/)
- **书籍**: 《Inspired》第2版 - 产品发现部分
- **深入**: Teresa Torres《Continuous Discovery Habits》

---
*Framework curated from SVPG articles and Jeff Patton's original concept*
*Last updated: 2026-03-11*
