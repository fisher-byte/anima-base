---
type: framework
person: gustaf-alstromer
title: Growth Metrics for Early-Stage Startups
date: 2018-10-29
source: https://www.ycombinator.com/blog/growth-ama-with-yc-partner-gustaf-alstromer
status: published
verification_status: reviewed
tags: [metrics, kpi, early-stage, retention, growth-rate]
---

# Growth Metrics for Early-Stage Startups

**Gustaf Alströmer 的早期增长指标选择框架**

---

## 核心观点

> "The two metrics I think make sense for early-stage startups are Weekly Growth and Retention."
> — Gustaf Alströmer

早期创业公司往往会被各种指标淹没，但实际上只需要关注两个核心指标。

---

## 为什么只需要两个指标？

### 问题：指标过多导致迷失方向

**常见错误**:
- 追踪几十个指标
- 关注虚荣指标 (总用户数、下载量)
- 忽视真正重要的健康指标
- 团队对优先级产生混淆

**Gustaf 的解决方案**:
- **简化到 2 个核心指标**
- 让整个团队聚焦于同一目标
- 更快发现问题和机会

---

## Metric 1: Weekly Growth Rate (周增长率)

### 定义

```
Weekly Growth Rate = (本周活跃用户 - 上周活跃用户) / 上周活跃用户 × 100%
```

### 为什么是"周"增长？

**相比月增长的优势**:
1. ✅ **更快的反馈循环**: 每周都能看到结果
2. ✅ **更快的学习速度**: 可以每周调整策略
3. ✅ **更早发现问题**: 不用等一个月才知道问题
4. ✅ **适合早期快速迭代**: 早期公司需要速度

**Gustaf 的建议**:
> "Measure weekly, not monthly. You need fast feedback loops in the early days."

### 计算示例

**场景**: SaaS 产品
- 上周活跃用户：1,000 人
- 本周活跃用户：1,050 人
- Weekly Growth Rate = (1,050 - 1,000) / 1,000 = **5%**

**健康增长率标准**:
- ✅ **Excellent**: 每周增长 > 10%
- ✅ **Good**: 每周增长 5-10%
- ⚠️ **Need Improvement**: 每周增长 < 5%
- ❌ **Red Flag**: 负增长

### 如何使用这个指标

**1. 设定每周增长目标**
```
如果目标是 6 个月增长 10 倍:
需要的平均周增长率 = 10%
(1.10)^26 ≈ 11.9 倍
```

**2. 每周回顾和调整**
- 每周一回顾上周增长
- 分析增长来源
- 调整本周策略
- 快速实验新想法

**3. 分解增长驱动因素**
- 自然增长 (Organic)
- 付费获取 (Paid)
- 病毒传播 (Viral)
- 内容/SEO (Content)

### 常见陷阱

❌ **陷阱 1: 混淆注册用户和活跃用户**
- 错误：计算总注册用户增长
- 正确：计算活跃用户增长 (MAU 或 WAU)

❌ **陷阱 2: 忽视 Cohort 差异**
- 错误：只看总体增长数字
- 正确：按 cohort 分析留存和增长

❌ **陷阱 3: 虚假增长**
- 错误：通过一次性活动制造短期增长
- 正确：关注可持续、可重复的增长

---

## Metric 2: Retention Rate (留存率)

### 定义

留存率衡量用户在一段时间后是否还在使用产品。

**关键时间节点**:
- **Day 1 Retention** (次日留存)
- **Day 7 Retention** (周留存)
- **Day 30 Retention** (月留存)
- **Cohort Retention Curve** (队列留存曲线)

### 计算公式

```
Day N Retention = 第 N 天回来的用户 / 第 0 天注册的用户 × 100%
```

### 示例计算

**场景**: 移动应用
- 第 1 天注册：1,000 人
- 第 2 天回来：400 人
- **Day 1 Retention = 40%**

---

**继续追踪同一批用户**:
- 第 7 天回来：250 人
- **Day 7 Retention = 25%**

- 第 30 天回来：150 人
- **Day 30 Retention = 15%**

### 健康留存率基准

#### B2C 产品
- **Day 1**: > 40% (优秀), 20-40% (一般), < 20% (需改进)
- **Day 7**: > 20% (优秀), 10-20% (一般), < 10% (需改进)
- **Day 30**: > 10% (优秀), 5-10% (一般), < 5% (需改进)

#### B2B SaaS
- **Week 1**: > 70% (优秀), 50-70% (一般), < 50% (需改进)
- **Month 1**: > 60% (优秀), 40-60% (一般), < 40% (需改进)
- **Month 3**: > 50% (优秀), 30-50% (一般), < 30% (需改进)

**Gustaf 的警告**:
> "If you can't retain users, growth doesn't matter. Fix retention first."

### 为什么留存比增长更重要？

**漏桶效应 (Leaky Bucket)**:

```
如果留存率低:
  获取 100 新用户
  - 第 7 天只剩 10 人 (90% 流失)
  - 本质上是在浪费获客成本

如果留存率高:
  获取 100 新用户
  - 第 7 天还有 70 人 (30% 流失)
  - 获客投入有持续价值
```

**数学真相**:
- 低留存 + 高增长 = **不可持续** (最终失败)
- 高留存 + 低增长 = **有机会** (可以优化获客)
- 高留存 + 高增长 = **快速成功**

### Retention Curve Analysis (留存曲线分析)

#### 1. 理想的留存曲线

```
100% |●
     |  ●●●
     |      ●●●●
 50% |          ●●●●●●●
     |                ●●●●●●●●
  0% |________________________
     0  7  14  21  28  35  42 (天)
```

**特征**:
- 初期有下降
- 然后趋于平稳
- 形成"留存底部" (Retention Floor)

#### 2. 糟糕的留存曲线

```
100% |●
     |  ●●
     |     ●●
 50% |       ●●
     |         ●●
  0% |           ●●●
     0  7  14  21  28  35  42 (天)
```

**问题**:
- 持续下降，没有平稳
- 最终趋近于 0
- **说明产品没有 PMF**

**Gustaf 的建议**:
> "Look for the retention curve to flatten out. That's your signal of product-market fit."

---

## 两个指标的关系

### 先留存，后增长

```
阶段 1: 优化留存
  目标: 建立健康的留存曲线
  行动: 产品迭代，用户访谈，改善核心价值

阶段 2: 增长加速
  目标: 在高留存基础上规模化增长
  行动: 投放广告，优化渠道，扩大团队
```

**关键原则**:
> "Don't pour gasoline on a fire that's not burning." — Gustaf Alströmer

意思是：不要在产品还没有 PMF (留存不好) 的情况下，大规模投入增长。

---

## 如何提升留存率

### 方法 1: 深度用户访谈

**访谈流失用户**:
- 为什么停止使用？
- 期望产品做什么？
- 有什么替代方案？

**访谈留存用户**:
- 为什么持续使用？
- 产品解决了什么问题？
- 什么让你回来？

### 方法 2: Cohort Analysis (队列分析)

**按不同维度分析**:
- 获客渠道 (Organic vs Paid)
- 用户属性 (地理位置、年龄)
- 首次体验 (完成 onboarding vs 未完成)

**找出高留存 Cohort 的特征**:
- 他们有什么共同点？
- 如何获取更多类似用户？

### 方法 3: 优化 Onboarding

**关键时刻 (Aha Moment)**:
- 用户体验核心价值的时刻
- 例如：Facebook 添加 7 个好友，Twitter 关注 30 个账号

**优化策略**:
1. 缩短用户到达 Aha Moment 的时间
2. 降低 Onboarding 摩擦
3. 提供清晰的价值展示

### 方法 4: 建立使用习惯

**习惯养成循环**:
1. **Trigger** (触发): 推送通知、邮件提醒
2. **Action** (行动): 降低使用门槛
3. **Reward** (奖励): 提供即时价值
4. **Investment** (投入): 让用户投入时间/数据

---

## 实施指南

### Week 1-2: 建立基础测量

**步骤**:
1. 设置 Analytics (Mixpanel / Amplitude)
2. 定义"活跃用户"标准
3. 设置 Cohort Retention 报表
4. 计算当前 Weekly Growth 和 Retention

### Week 3-4: 诊断问题

**问题排查**:
- Retention 曲线是否平稳？
- 哪个时间点流失最多？
- 不同 cohort 的差异？
- 用户为什么流失？

### Month 2: 优化留存

**行动计划**:
1. 进行 10+ 用户访谈
2. 优化 Onboarding 流程
3. 改进核心产品功能
4. 每周测量留存改善

### Month 3+: 加速增长

**前提条件**:
- ✅ Retention 曲线已经平稳
- ✅ Day 7 Retention > 目标基准
- ✅ 用户反馈积极

**增长行动**:
- 开始小规模付费测试
- 优化产品增长循环
- 扩大有效渠道预算

---

## 常见问题 Q&A

### Q1: 我的产品是低频使用，如何测量留存？

**A**: 调整时间窗口
- 不要用 Day 1, Day 7
- 使用 Week 1, Week 4, Week 12
- 或者测量"回购率" (Repeat Purchase Rate)

### Q2: 初期用户很少，数据不够怎么办？

**A**: 定性 > 定量
- 进行深度用户访谈
- 观察用户实际使用行为
- 小样本也有价值 (100 人足够看趋势)

### Q3: 留存一直上不去怎么办？

**A**: 可能还没找到 PMF
- 回到用户访谈
- 重新验证问题假设
- 可能需要 pivot

### Q4: 应该按周计算还是按天计算增长？

**A**: 取决于产品节奏
- 高频产品 (社交、工具) → 按周
- 低频产品 (B2B SaaS) → 按月
- 关键是保持一致性

---

## 关键要点总结

1. ✅ **只关注两个指标**: Weekly Growth + Retention
2. ✅ **留存优先于增长**: 先修好"漏桶"
3. ✅ **按周测量**: 更快的反馈循环
4. ✅ **Cohort Analysis**: 深入理解用户行为
5. ✅ **避免虚荣指标**: 总用户数不代表健康
6. ✅ **PMF 信号**: 留存曲线趋于平稳

---

**适用场景**:
- Pre-Seed 到 Series A 阶段
- 产品刚上线，需要建立指标体系
- 团队需要聚焦核心目标

**相关框架**:
- [[how-to-get-users-and-grow]] - 系统化增长策略
- [[product-market-fit-validation]] - PMF 验证方法

---

**来源**: [Growth AMA with YC Partner Gustaf Alströmer](https://www.ycombinator.com/blog/growth-ama-with-yc-partner-gustaf-alstromer)
