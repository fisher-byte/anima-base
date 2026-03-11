---
type: framework
person: teresa-torres
title: Assumption Testing Framework
date: 2026-03-12
source: https://www.producttalk.org/assumption-testing/
status: published
verification_status: reviewed
tags: [product-discovery, experimentation, validation, risk-reduction]
language: en
---

# Assumption Testing Framework

**Assumption Testing** 是 Teresa Torres 持续发现方法的核心组成部分，帮助产品团队快速验证想法的可行性，在投入大量资源前降低风险。

## 框架概述

### 为什么要测试假设？

> "Every idea we have is really just a collection of assumptions. The faster we can test those assumptions, the faster we can learn which ideas will work and which won't."
> — Teresa Torres

产品开发中的大多数失败来自于未经验证的假设。Assumption Testing 帮助团队：
- 在构建前发现问题
- 避免投入大量资源到注定失败的方向
- 做出基于证据的决策

## 假设类型

Teresa Torres 将产品假设分为五类：

### 1. Desirability（可欲性）
用户是否想要这个解决方案？

```markdown
示例假设：
- 用户愿意为这个功能付费
- 用户会每天使用这个功能
- 这个解决方案比他们现有的方案更好
```

### 2. Viability（可行性 - 商业）
这对我们的业务有意义吗？

```markdown
示例假设：
- 这个功能能带来足够的收入
- 获客成本是可持续的
- 不会与现有收入模式冲突
```

### 3. Feasibility（可行性 - 技术）
我们能够构建它吗？

```markdown
示例假设：
- 现有技术能够支持这个功能
- 我们有足够的工程资源
- 性能可以满足要求
```

### 4. Usability（可用性）
用户能够使用它吗？

```markdown
示例假设：
- 用户能理解如何使用
- 用户能独立完成任务
- 错误率在可接受范围内
```

### 5. Ethical（道德性）
我们应该构建它吗？

```markdown
示例假设：
- 不会对用户造成伤害
- 符合隐私和合规要求
- 不会产生负面社会影响
```

## 假设测试方法

### 测试类型光谱

```
低保真 ←————————————————————→ 高保真
  |         |         |         |
调研    原型测试   实验    MVP
  ↓         ↓         ↓         ↓
快速/便宜   中等      较多      最多投入
```

### 常用测试方法

| 方法 | 适用场景 | 时间 | 成本 |
|------|----------|------|------|
| **用户访谈** | 早期验证可欲性 | 1-2天 | 低 |
| **纸面原型** | 快速测试概念 | 1天 | 最低 |
| **点击原型** | 测试可用性 | 2-3天 | 低 |
| **烟雾测试** | 验证需求强度 | 1周 | 中 |
| **Wizard of Oz** | 模拟功能 | 1-2周 | 中 |
| **A/B测试** | 验证假设 | 2-4周 | 高 |

## 假设测试流程

### Step 1: 识别假设

从解决方案中提取所有假设：

```markdown
解决方案：为用户提供自动化报告功能

假设：
□ 用户目前手动创建报告很痛苦（可欲性）
□ 用户愿意为自动化报告付费（可行性-商业）
□ 我们可以准确提取所需数据（可行性-技术）
□ 用户能理解报告的格式（可用性）
```

### Step 2: 评估风险

使用风险矩阵优先排序：

```
          高不确定性
              ↑
    [高优先级] | [最高优先级]
              |
   ←——————————+——————————→ 高影响
              |
    [低优先级] | [中优先级]
              ↓
          低不确定性
```

### Step 3: 设计测试

```markdown
假设测试计划模板：

假设：[具体假设陈述]
类型：[可欲性/可行性/可用性/道德性]
风险等级：[高/中/低]

测试方法：[具体方法]
成功标准：[可衡量的标准]
所需时间：[预估时间]
所需资源：[人员/工具]

预期结果：
- 如果验证成功：[下一步行动]
- 如果验证失败：[下一步行动]
```

### Step 4: 执行并学习

- 快速执行测试
- 收集数据
- 与团队分享发现
- 更新 Opportunity Solution Tree

## 比较与对比决策

### Compare and Contrast 原则

> "Good product decisions are compare and contrast decisions, not whether or not decisions."
> — Teresa Torres

**错误方式**: 逐个评估想法
```
想法A → 要不要做？→ 做 ✓
```

**正确方式**: 同时比较多个想法
```
想法A ┐
想法B ├→ 哪个更有希望？→ A > B > C
想法C ┘
```

### 如何比较

1. 为每个想法测试相同的关键假设
2. 使用统一的成功标准
3. 根据证据选择最优选项

## 假设测试 vs 实验

| | 假设测试 | 实验 |
|---|----------|------|
| **阶段** | 发现阶段 | 交付后 |
| **目的** | 决定要构建什么 | 衡量构建的影响 |
| **时间** | 1-2天 | 数周 |
| **规模** | 小样本 | 大规模 |
| **问题** | "这个想法有希望吗？" | "这个功能有效果吗？" |

## 实施建议

### 建立节奏

```markdown
推荐频率：
- 每周至少 1 个假设测试
- 同时测试 2-3 个解决方案的假设
- 与用户访谈结合进行
```

### 团队协作

- Product Trio 共同设计测试
- 共同分析结果
- 共同做出决策

### 避免常见错误

1. **测试过大**
   - 不需要测试整个解决方案
   - 聚焦于最高风险的假设

2. **等待完美数据**
   - 足够好的数据就可以决策
   - 更多测试比完美测试重要

3. **忽视负面结果**
   - 失败的测试也是有价值的
   - 记录学习并调整方向

## 来源

- **原文**: [Assumption Testing - Product Talk](https://www.producttalk.org/assumption-testing/)
- **书籍**: Continuous Discovery Habits, Chapter 8
- **课程**: [Discovering Solutions - Product Talk Academy](https://learn.producttalk.org/discovering-solutions)

---
*Framework documented based on Teresa Torres's official Product Talk materials*
