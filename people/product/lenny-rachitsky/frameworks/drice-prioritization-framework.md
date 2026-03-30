---
type: framework
person: lenny-rachitsky
title: DRICE Prioritization Framework
source: https://www.lennysnewsletter.com/p/introducing-drice-a-modern-prioritization
date: 2023-11-07
verification_status: reviewed
tags: [prioritization, growth, experiments, product-development]
---

# DRICE Prioritization Framework

> 现代化的增长实验优先级框架,提升实验成功率

**来源**: Darius Contractor (ex-Dropbox, Facebook, Airtable Growth Lead, now CGO at Otter.ai) & Alexey Komissarouk

**核心洞察**: RICE框架在增长实验场景中存在盲点。DRICE通过添加"Distribution"维度,更准确地评估实验潜在影响。

---

## 为什么需要DRICE?

### RICE的局限性

**RICE公式**: `Score = (Reach × Impact × Confidence) / Effort`

**问题**: RICE假设所有用户都会看到/使用新功能,但现实中:
- 新功能需要推广才能被发现
- 用户不会自动采用新特性
- Distribution(分发)是成功的关键因素

**案例**: 
- 你构建了一个新功能
- RICE评分很高 (Reach=10000, Impact=3, Confidence=80%, Effort=2)
- 但如果只有5%的用户发现它,实际影响远低于预期

### DRICE的改进

**DRICE公式**: `Score = (Distribution × Reach × Impact × Confidence) / Effort`

**新增 "D" (Distribution)**:
- **定义**: 目标用户中有多少百分比会实际看到/体验到这个变化
- **范围**: 0-100%
- **关键**: Distribution不是自动的,需要主动设计

---

## DRICE 五要素详解

### D - Distribution (分发率)

**定义**: 目标用户中会实际体验到这个变化的百分比

**评估问题**:
- 新功能如何被用户发现?
- 需要主动推广吗?
- 是在主流程中还是需要用户导航到?
- 默认开启还是需要用户opt-in?

**评分指南**:

| Distribution | 场景示例 |
|--------------|----------|
| **100%** | 主页重设计、核心流程变更、所有用户默认看到 |
| **50-80%** | 需要导航但位置明显、部分用户群体可见 |
| **20-50%** | 需要主动发现、设置菜单中、需要一定操作 |
| **5-20%** | 深层功能、需要多步骤到达、小众需求 |
| **<5%** | 隐藏功能、无推广、需要用户主动搜索 |

**提升Distribution策略**:
1. **In-App推广**: 弹窗、横幅、工具提示
2. **Onboarding集成**: 在新用户引导中展示
3. **Email/Push通知**: 向现有用户推广
4. **主流程嵌入**: 放在用户必经路径上

**关键原则**: **If users don't see it, it doesn't exist.**

---

### R - Reach (覆盖用户数)

**定义**: 在给定时间段内,有多少用户**可能**受到影响

**评估单位**: 用户数/月 或 用户数/季度

**评分方法**:
- 绝对数字: 10,000 users/month
- 或百分比: 20% of user base

**注意**: Reach是"潜在"用户数,Distribution是"实际"用户数
- **实际影响用户数 = Reach × Distribution**

**示例**:
- Reach = 50,000 users/month (所有使用checkout的用户)
- Distribution = 30% (只有30%会看到新的支付选项)
- **实际影响 = 15,000 users**

---

### I - Impact (影响程度)

**定义**: 对每个用户的预期影响有多大

**评分标准** (1-3分制):

| Score | 影响程度 | 指标变化 |
|-------|----------|----------|
| **3** | 巨大影响 | 北极星指标提升 ≥5% |
| **2** | 中等影响 | 北极星指标提升 1-5% |
| **1** | 小幅影响 | 北极星指标提升 <1% |
| **0.5** | 微小影响 | 几乎无法测量 |

**评估问题**:
- 这个变化会如何影响用户行为?
- 预期转化率/留存率/参与度提升多少?
- 对北极星指标的影响是什么?

**示例**:
- **Impact = 3**: 新onboarding流程让激活率从30% → 40%
- **Impact = 2**: 新功能让周活跃时间从10小时 → 11小时
- **Impact = 1**: UI优化让点击率从5% → 5.2%

---

### C - Confidence (信心程度)

**定义**: 对以上估计(D, R, I)和预期结果的信心

**评分范围**: 0-100%

**信心等级**:

| Confidence | 证据水平 |
|------------|----------|
| **80-100%** | 强数据支持、类似实验成功、用户强烈需求 |
| **50-80%** | 部分数据、合理假设、有一定风险 |
| **20-50%** | 假设为主、数据有限、高不确定性 |
| **<20%** | 纯猜测、无数据支持、探索性实验 |

**提升Confidence的方法**:
1. **用户研究**: 访谈、调研验证假设
2. **历史数据**: 参考过去类似实验结果
3. **小规模测试**: A/B test 原型或MVP
4. **竞品分析**: 其他产品的类似功能表现

**示例**:
- **80%**: 用户调研显示强烈需求 + 竞品有成功案例
- **50%**: 基于数据的合理假设,但未验证
- **30%**: 新想法,缺乏证据支持

---

### E - Effort (工作量)

**定义**: 实施这个项目需要的总工作量

**评分单位**: "人周"或"人月"

**包含内容**:
- **工程**: 开发、测试、部署
- **设计**: UI/UX设计、用户体验优化
- **产品**: 需求定义、项目管理、发布协调
- **数据**: 埋点、分析、实验设置

**评分示例**:

| Effort | 典型场景 |
|--------|----------|
| **0.5人周** | 简单文案修改、小型UI调整 |
| **1-2人周** | 单个功能开发、中等复杂度 |
| **3-4人周** | 多个团队协作、新功能模块 |
| **5+人周** | 大型项目、跨团队依赖 |

**注意**: 包含"隐藏成本"
- Code review时间
- QA测试时间
- 发布和监控时间
- 技术债务

---

## DRICE计算示例

### 案例: Dropbox添加PayPal支付选项

**背景**: Dropbox考虑在checkout页面添加PayPal作为支付方式

#### 评分过程

**D - Distribution**: 60%
- 位置: Checkout页面(所有购买用户都会看到)
- 但需要用户主动选择PayPal选项
- 估计60%用户会注意到这个新选项

**R - Reach**: 100,000 users/month
- 每月约10万用户进入checkout流程

**I - Impact**: 2
- 预期: 为更喜欢PayPal的用户移除支付摩擦
- 估计转化率提升2-3%
- 中等影响

**C - Confidence**: 70%
- 竞品数据显示PayPal能提升转化
- 用户调研显示有PayPal需求
- 但不确定Dropbox用户群体偏好

**E - Effort**: 3 person-weeks
- 集成PayPal API: 1.5周
- 前端UI: 0.5周
- 测试和QA: 0.5周
- 发布和监控: 0.5周

#### 计算DRICE Score

```
DRICE = (D × R × I × C) / E
      = (0.6 × 100,000 × 2 × 0.7) / 3
      = 84,000 / 3
      = 28,000
```

**对比RICE Score** (不考虑Distribution):
```
RICE = (R × I × C) / E
     = (100,000 × 2 × 0.7) / 3
     = 140,000 / 3
     = 46,667  ← 高估了实际影响!
```

**关键差异**: 
- RICE假设所有10万用户都会受益
- DRICE考虑只有60%(6万)用户实际注意到
- DRICE提供更现实的优先级评估

---

## 使用DRICE的完整流程

### Step 1: 列出候选项目 (Backlog)

创建实验/功能候选列表,每个项目简要描述:
- 项目名称
- 目标(预期改善什么指标)
- 简要方案

### Step 2: 团队评分 (Scoring Session)

**参与者**: 产品、工程、设计、数据
**时长**: 30-60分钟

**流程**:
1. 逐个项目讨论
2. 团队共同评估D, R, I, C, E
3. 记录假设和依据
4. 计算DRICE分数

**技巧**:
- 使用相对评分 (对比已完成的项目)
- 记录分歧和讨论要点
- 允许"待调研"标记不确定的项目

### Step 3: 排序和选择 (Prioritization)

- 按DRICE分数从高到低排序
- 考虑战略优先级 (不仅仅看分数)
- 选择Top 3-5个项目进入sprint

**平衡因素**:
- **Quick Wins**: 低Effort高Impact的项目
- **Bets**: 高潜力但高不确定性的项目
- **Infrastructure**: 必要的技术债务清理

### Step 4: 执行和学习 (Execute & Learn)

- 实施选定的项目
- 跟踪实际结果 vs 预期
- 回顾并更新评分模型

**持续优化**:
- 记录实际D, R, I, C vs 预测值
- 分析偏差原因
- 提升未来评分准确度

---

## DRICE vs RICE: 何时使用?

### 使用DRICE的场景

✅ **增长实验**: 需要推广的新功能
✅ **A/B测试优先级**: 多个测试idea排序
✅ **功能发布**: 需要用户发现和采用的新特性
✅ **优化项目**: 改进现有流程或页面

**核心**: 当Distribution不是100%时,DRICE更准确

### 使用RICE的场景

✅ **基础设施项目**: 所有用户自动受益
✅ **核心流程变更**: 用户无需主动发现
✅ **产品路线图**: 长期战略项目规划
✅ **简化场景**: 团队不熟悉DRICE或项目较少

---

## 关键原则

### 1. Distribution is Not Automatic

**❌ 错误假设**: "如果我们构建了,用户就会用"
**✅ 现实**: 大多数新功能需要主动推广和引导

**行动**:
- 为每个新功能设计Discovery策略
- 在评分时明确Distribution计划
- 跟踪功能采用率

### 2. 数据驱动的直觉 (Data-Informed Intuition)

- DRICE是工具,不是绝对真理
- 用数据支持决策,但保留判断力
- 战略重要性可以override分数

### 3. 持续校准 (Continuous Calibration)

- 初期评分会不准确 → 正常
- 随着经验积累,准确度提升
- 定期回顾实际结果,调整模型

### 4. 团队共识 (Team Alignment)

- DRICE的最大价值是对齐团队认知
- 评分过程中的讨论比最终分数更重要
- 记录假设和争议点

---

## 常见陷阱

### ❌ 陷阱 1: 过度精确化

**问题**: 花大量时间争论Impact是2.3还是2.4
**解决**: 使用粗粒度评分 (1-3整数), 接受不确定性

### ❌ 陷阱 2: 忽视战略优先级

**问题**: 只看DRICE分数,忽视公司战略
**解决**: DRICE是输入,不是唯一决策因素

### ❌ 陷阱 3: 不更新评分

**问题**: 评分一次就不再调整
**解决**: 每季度或每次冲刺前重新评估Top项目

### ❌ 陷阱 4: Distribution估计过高

**问题**: 假设用户会自动发现新功能
**解决**: 默认Distribution < 50%,除非有明确推广计划

---

## 工具和模板

### DRICE评分表模板

| 项目 | D | R | I | C | E | DRICE | 优先级 |
|------|---|---|---|---|---|-------|--------|
| PayPal集成 | 60% | 100K | 2 | 70% | 3 | 28K | High |
| Email重设计 | 90% | 200K | 1 | 80% | 4 | 36K | High |
| 新分享功能 | 20% | 150K | 3 | 50% | 2 | 22.5K | Med |
| ... | ... | ... | ... | ... | ... | ... | ... |

### 评分协作工具

- **Google Sheets / Excel**: 简单直接
- **Notion / Airtable**: 更强大的数据库功能
- **Productboard / Aha!**: 专业产品管理工具

---

## 延伸学习

### 相关框架

- **RICE** (Intercom): DRICE的前身
- **ICE** (Growth Hackers): Simpler版本 (Impact, Confidence, Ease)
- **Value vs Effort Matrix**: 可视化优先级

### 推荐资源

- Lenny's Newsletter: DRICE完整文章
- Reforge: DRICE Prioritization Artifact (Dropbox案例)
- Darius Contractor on LinkedIn: 增长实验最佳实践

---

**关键要点**: 

DRICE通过添加Distribution维度,修正了RICE框架在增长实验场景中的盲点。记住: **构建功能只是第一步,让用户发现和使用才是成功的关键**。

在评估优先级时,始终问自己: **"即使我们构建了这个功能,有多少用户会实际使用它?"**

*基于 Darius Contractor & Alexey Komissarouk 在 Lenny's Newsletter 的框架 | 2023年11月*
