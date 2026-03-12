# Retention Analysis Framework

---
type: framework
person: lenny-rachitsky
title: Retention Analysis Framework  
date: 2021-08-31
source: https://www.lennysnewsletter.com/p/how-to-increase-your-products-retention
original_urls:
  - https://www.lennysnewsletter.com/p/how-to-increase-your-products-retention
  - https://gopractice.io/product/retention-how-to-understand-calculate-and-improve-it/
status: published
verification_status: reviewed
tags:
  - retention
  - metrics
  - cohort-analysis
  - growth
---

## 概述

Retention Analysis Framework 是 Lenny Rachitsky 总结的用户留存分析方法论。这个框架帮助团队系统性地理解、测量和提升用户留存。

**Lenny 的名言：** "Retention is the king, queen, and jack of growth."（留存是增长的王、后和杰克）

## 为什么留存如此重要

### 1. 留存是增长的基础
- 没有留存,所有获客投入都会流失
- 留存好 = 增长容易
- 留存差 = 增长不可能

### 2. 留存预示 PMF
- 留存曲线趋平 = 找到了真正需要你的用户
- 持续下降 = 产品还未 PMF

### 3. 留存影响单位经济
- 高留存 = 高 LTV
- LTV 高 = 可承受更高 CAC
- 可承受高 CAC = 更多增长机会

## 留存的三种类型

### 1. Classic Retention（经典留存）
**定义:** 某个 cohort 在特定日期仍然活跃的百分比

**计算方式:**
```
Day N Retention = (Day N 活跃用户数) / (Day 0 获取用户数) × 100%
```

**优点:** 简单直观
**缺点:** 可能低估真实留存（用户可能跳过某天但仍活跃）

**适用:** 高频产品（每日/每周使用）

### 2. Unbounded Retention（无界留存）
**定义:** 某个 cohort 在特定日期或之后任何时间活跃过的百分比

**计算方式:**
```
Day N+ Retention = (Day N 及之后活跃过的用户数) / (Day 0 获取用户数) × 100%
```

**优点:** 更准确反映长期留存
**缺点:** 不能反映使用频率

**适用:** 低频产品（每月使用）

### 3. Rolling Retention（滚动留存）
**定义:** 在特定时间窗口内活跃的用户百分比

**计算方式:**
```
Week N Retention = (Week N 的7天内活跃的用户数) / (Week 0 获取用户数) × 100%
```

**优点:** 更灵活,适合不同使用频率
**缺点:** 计算复杂

**适用:** 使用频率不固定的产品

## 如何正确测量留存

### 步骤 1: 选择正确的留存类型
- 每日使用产品 → Classic Retention (Day 1, 7, 30)
- 每周使用产品 → Rolling Retention (Week 1, 4, 12)
- 每月使用产品 → Unbounded Retention (Month 1, 3, 6)

### 步骤 2: 定义"活跃"
**不同产品的"活跃"定义:**
- 社交应用: 发送消息 / 查看内容
- 电商: 浏览商品 / 购买
- SaaS 工具: 打开应用 / 完成核心动作
- 内容平台: 观看 / 阅读

**原则:**
✅ 选择反映核心价值的动作
✅ 不要定义过低（登录不等于活跃）
✅ 不要定义过高（发帖可能太高）

### 步骤 3: 绘制留存曲线
```
Cohort Retention Curve:
- X 轴: 时间（Day/Week/Month）
- Y 轴: 留存率 (%)
- 多条线: 不同时间的 cohort

关键观察:
1. 曲线是否趋平？
2. 平台期在哪里？
3. 新 cohort 是否比旧 cohort 好？
```

### 步骤 4: 找到留存拐点
**关键时间点:**
- Day 1 (24小时内)
- Day 7 (1周)
- Day 30 (1个月)
- Day 90 (3个月)

这些拐点的留存率最能预示长期留存。

## 留存基准参考

基于 Lenny 的研究：

### 消费社交产品
- Day 1: 50-60%
- Day 7: 30-40%
- Day 30: 20-30%

### SaaS 工具
- Week 1: 40-50%
- Week 4: 20-30%
- Month 3: 15-25%

### 电商平台
- Month 1: 25-35%
- Month 3: 15-25%
- Month 6: 10-20%

**重要:** 基准只是参考,最重要的是你的留存趋势是否在改善。

## 提升留存的七大策略

### 1. Improve Onboarding（优化引导）
**目标:** 让用户尽快体验到核心价值

**关键动作:**
- 识别 Aha Moment（价值顿悟时刻）
- 减少达到 Aha Moment 的步骤
- 提供个性化引导
- 设置早期里程碑

**案例:** Dropbox
- Aha Moment: 文件在多设备间同步
- 引导: 鼓励用户立即在第二台设备安装

### 2. Build Habits（培养习惯）
**目标:** 让产品成为用户日常习惯的一部分

**关键策略:**
- 触发器 (Triggers): 通知、邮件、外部事件
- 行动 (Action): 简化核心动作
- 奖励 (Reward): 即时反馈和满足感
- 投入 (Investment): 让用户在产品中积累价值

**案例:** Instagram
- 触发器: Push 通知（有人点赞）
- 行动: 快速打开查看
- 奖励: 看到互动
- 投入: 发布内容,关注朋友

### 3. Improve Core Value（提升核心价值）
**目标:** 让产品更好地解决用户问题

**方法:**
- 持续用户访谈
- 分析流失用户反馈
- A/B 测试核心功能
- 移除干扰功能

### 4. Add New Use Cases（增加使用场景）
**目标:** 给用户更多回来的理由

**策略:**
- 从主要场景扩展到次要场景
- 从个人使用扩展到团队使用
- 从单一功能扩展到工作流

**案例:** Notion
- 从笔记 → 知识库 → 项目管理 → 协作工具

### 5. Reactivation Campaigns（重新激活）
**目标:** 召回流失用户

**策略:**
- Email 序列
- Push 通知
- 产品内消息
- 特殊优惠

**最佳实践:**
- 个性化消息（基于用户历史）
- 突出新功能
- 提供明确行动号召
- 测试不同时间和频率

### 6. Build Network Effects（建立网络效应）
**目标:** 用户越多,产品越有价值

**类型:**
- 直接网络效应（朋友越多越有用）
- 间接网络效应（内容越多越有价值）
- 双边网络效应（买家卖家互相促进）

### 7. Gamification & Incentives（游戏化和激励）
**目标:** 通过外部激励提升参与度

**策略:**
- 积分系统
- 等级勋章
- 排行榜
- 成就系统

**警告:** 不要过度依赖,核心价值最重要

## 留存分析深度方法

### 1. Cohort Segmentation（分群分析）
**按不同维度分析留存:**
- 获取渠道（Organic vs Paid）
- 用户特征（年龄、地区、职业）
- 使用行为（重度 vs 轻度）
- 产品版本（A/B test 不同版本）

**目的:** 找出留存最好的用户群,专注获取类似用户

### 2. Correlation Analysis（相关性分析）
**分析哪些行为与高留存相关:**

例子：
```
高留存用户的共同特征:
- 前7天内添加了 3+ 个朋友
- 完成了首次核心动作
- 使用了关键功能 X

低留存用户的特征:
- 只完成注册
- 未完成引导流程
- 未体验核心价值
```

### 3. Leading Indicators（前置指标）
**识别能预测长期留存的早期信号:**

Lenny 的建议:
- D1 行为预测 D30 留存
- W1 行为预测 M3 留存
- 前置指标让你能更快迭代

**案例:** Facebook
- 前置指标: "在10天内添加7个朋友"
- 达成这个指标的用户长期留存显著更高

## 提升留存的实验框架

### Step 1: 假设
```
我们相信 [某个改动]
会让 [某类用户]
更多地 [某个行为]
从而提升 [留存指标]
```

### Step 2: 测量基线
- 当前留存率是多少？
- 目标提升多少？
- 最小可检测效果（MDE）是多少？

### Step 3: 设计实验
- A/B test 设计
- 样本量计算
- 时间长度（至少 2-4 周）

### Step 4: 分析结果
- 统计显著性
- 实际业务影响
- 是否有负面影响

### Step 5: 迭代
- 成功 → 全量发布 → 下一个实验
- 失败 → 分析原因 → 新假设

## 常见陷阱

### 1. 过早优化留存
❌ PMF 之前就过度优化留存
✅ 先找到 PMF,再系统优化留存

### 2. 忽视新用户留存
❌ 只关注整体留存,不关注 cohort 趋势
✅ 每个新 cohort 留存都应该改善

### 3. 用错误的指标
❌ 把登录当作活跃
✅ 用核心价值动作定义活跃

### 4. 只看短期留存
❌ 只优化 D1,忽视 D30/D90
✅ 平衡短期和长期留存

### 5. 忽视流失原因
❌ 不分析为什么流失
✅ 定期访谈流失用户

## 检查清单

优化留存前问自己:

- [ ] 我们的留存曲线趋平了吗？
- [ ] 新 cohort 留存是否在改善？
- [ ] 我们知道 Aha Moment 是什么吗？
- [ ] 用户能快速体验到核心价值吗？
- [ ] 我们有有效的 onboarding 吗？
- [ ] 我们有重新激活流失用户的策略吗？
- [ ] 我们定期分析流失用户吗？
- [ ] 我们知道高留存用户的共同特征吗？

## 参考资源

- [How to increase your product's retention](https://www.lennysnewsletter.com/p/how-to-increase-your-products-retention) - Lenny's Newsletter
- [Retention: how to understand, calculate, and improve it](https://gopractice.io/product/retention-how-to-understand-calculate-and-improve-it/) - GoPractice
- [Brian Balfour on Retention](https://brianbalfour.com/essays/retention) - Reforge

---

**最后更新:** 2026-03-12  
**验证状态:** 已审核,内容基于 Lenny Rachitsky 和 Brian Balfour 的研究
