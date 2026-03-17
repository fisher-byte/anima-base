---
type: framework
person: lenny-rachitsky
title: "SaaS Metrics & KPI Dashboard Framework: Bottom-Up SaaS 指标追踪体系"
date: 2020-10-20
source: "Lenny's Newsletter"
source_url: "https://www.lennysnewsletter.com/p/the-most-important-bottom-up-saas-69d"
verification_status: reviewed
tags:
  - saas-metrics
  - kpi-dashboard
  - product-analytics
  - bottom-up-saas
  - growth-metrics
---

# SaaS Metrics & KPI Dashboard Framework

## 核心概念

Lenny Rachitsky 为早期 **Bottom-Up SaaS** 公司总结的指标追踪体系，解答三个关键问题：
1. 🔬 应该关注哪些指标？
2. 🛠 使用什么工具追踪？
3. 🎨 如何最佳可视化和分享这些指标？

**Bottom-Up SaaS 定义：** 产品从个人用户或小团队开始使用，逐步扩展到整个组织的 SaaS 模式（如 Slack、Notion、Figma）

---

## 指标优先级体系

### Pre-Revenue 阶段（未收费前）

#### Tier 1: 核心留存指标
| 指标 | 定义 | 目标 | 优先级 |
|------|------|------|--------|
| **User Retention** | 3-6 个月后仍活跃的新用户百分比 | > 40% | ⭐⭐⭐⭐⭐ |
| **Logo Retention** | 3-6 个月后仍活跃的新公司百分比 | > 50% | ⭐⭐⭐⭐⭐ |
| **L7/L30 Retention** | 用户每周/月活跃天数 | L7 > 3天 | ⭐⭐⭐⭐⭐ |

#### Tier 2: 病毒增长指标
| 指标 | 定义 | 目标 | 优先级 |
|------|------|------|--------|
| **Invite Rate** | 前 X 天内至少发送一次邀请的新用户百分比 | > 30% | ⭐⭐⭐⭐ |
| **Invite Conversion Rate** | 收到邀请后 X 天内注册的用户百分比 | > 25% | ⭐⭐⭐⭐ |
| **Virality Factor** | 通过邀请而来的新用户百分比 | > 40% | ⭐⭐⭐⭐ |

#### Tier 3: 增长健康度指标
| 指标 | 定义 | 目标 | 优先级 |
|------|------|------|--------|
| **Traffic** | 每周网站访问量 | 持续增长 | ⭐⭐⭐ |
| **MoM User Growth** | 月环比用户增长率 | > 10% | ⭐⭐⭐⭐ |
| **Activation** | "激活"的新用户百分比（需自定义定义） | > 40% | ⭐⭐⭐⭐ |

---

### Post-Revenue 阶段（开始收费后）

#### Tier 1: 核心收入指标
| 指标 | 定义 | 目标 | 优先级 |
|------|------|------|--------|
| **MRR** | 月度经常性收入（总额 + MoM 增长） | MoM > 15% | ⭐⭐⭐⭐⭐ |
| **ARR** | 年度经常性收入（总额 + MoM 增长） | 持续增长 | ⭐⭐⭐⭐⭐ |
| **New Customers** | 每周新付费客户数 | 稳定增长 | ⭐⭐⭐⭐⭐ |

#### Tier 2: 留存与扩展指标
| 指标 | 定义 | 目标 | 优先级 |
|------|------|------|--------|
| **Customer Retention** | 3-6 个月后仍付费的新客户百分比 | > 80% | ⭐⭐⭐⭐⭐ |
| **Net Dollar Retention (NDR)** | 12 个月时每个队列的 MRR | > 100% | ⭐⭐⭐⭐⭐ |

#### Tier 3: 转化与效率指标
| 指标 | 定义 | 目标 | 优先级 |
|------|------|------|--------|
| **Paid Company Conversion** | X 天内从免费转付费的公司百分比 | > 20% | ⭐⭐⭐⭐ |
| **Payback Period** | 回收 CAC 的平均时间 | < 12 个月 | ⭐⭐⭐⭐ |
| **Gross Margins** | 净销售收入 - 商品成本 | > 70% | ⭐⭐⭐⭐ |

---

### Additional Metrics（按需追踪）

#### 参与度指标
- **DAU/MAU:** 日活/月活比率（衡量粘性）
- **Key Actions per Day/Week:** 关键行为频次（如创建任务数、发送图片数）
- **Average Time Spent/User/Day:** 平均每用户每天使用时长

#### 病毒扩展指标
- **Invite Volume:** 何时发送邀请，每用户中位数邀请数
- **Velocity of Virality:** 从 1 个用户增长到 N 个席位的中位数天数
- **Traction:** 至少 3 个用户注册的公司总数
- **Leads:** 用户最多的顶级域名（用于定向推广）

#### 商业化指标
- **ARPU:** 平均每用户收入
- **User Conversion:** X 天内从免费转付费的用户百分比
- **Quick Ratio:** (New MRR + Expansion MRR) / (Contraction MRR + Churned MRR)
- **Growth Spend Efficiency:** CAC/LTV
- **Speed to Next Tier:** 用量定价模式下升级到下一档的速度
- **Company Adoption:** 每个域名的用户数

#### 转化漏斗指标
- **Landing Conversion:** 点击 CTA 的访客百分比
- **Activation:** "激活"的访客百分比
- **% Visitors Complete Sign-up Flow:** 完成注册流程的访客百分比
- **% Visitors Signup:** 注册的访客百分比

---

## 工具栈推荐

### 指标追踪工具（按使用频率排序）

#### 1. Google Sheets
**优势：** 灵活、免费、易分享、全员可访问  
**最佳实践：**
- 使用 Google Data Studio 可视化
- 建立单一事实来源（Single Source of Truth）
- 每周自动更新（通过脚本或 API）

**示例结构：**
```
[Summary Tab]
- MRR: $XXX (+X% MoM)
- New Customers: XX (+X% WoW)
- Churn Rate: X%
- Net Dollar Retention: XXX%

[Cohort Analysis Tab]
[Funnel Metrics Tab]
[Growth Metrics Tab]
```

#### 2. Profitwell
**优势：** 免费、自动计算 SaaS 指标、Stripe 集成  
**核心指标：** MRR、ARR、Churn、LTV

#### 3. Mixpanel / Amplitude
**优势：** 强大的用户行为分析、事件追踪、漏斗分析  
**最佳用途：** 激活率、留存分析、用户旅程

#### 4. ChartMogul
**优势：** SaaS 收入分析、队列分析、订阅指标  
**核心功能：** MRR 运动图、客户终身价值

#### 5. Segment
**优势：** 数据管道，连接所有工具  
**用途：** 统一数据收集，一次发送到多个工具

---

## KPI Dashboard 最佳实践

### Dashboard 设计原则

#### 1. 单页概览
**结构：**
```
[Top Metrics]
MRR  |  ARR  |  New Customers  |  Churn

[Growth Trends]
📈 MRR Growth Chart (12 months)
📊 User Retention Cohort

[Current Focus]
🎯 North Star Metric Progress
⚠️ Red Flags / Action Items
```

#### 2. 层级化展示
- **Executive View:** 5-7 个核心指标
- **Product View:** 参与度 + 留存 + 激活
- **Growth View:** 获客 + 病毒传播 + 转化
- **Finance View:** 收入 + 成本 + 效率

#### 3. 可视化最佳实践
✅ **推荐：**
- 趋势图显示季节性和周期
- 队列分析显示留存演进
- 颜色编码（绿色=好，红色=警告）
- 目标线清晰标注

❌ **避免：**
- 过多指标（< 10 个核心指标）
- 复杂图表（保持简洁）
- 静态数据（至少每周更新）

### 真实案例参考

#### 案例 1: Early-Stage SaaS Dashboard
```
WEEKLY SNAPSHOT
─────────────────────────────────
📊 Core Metrics
   MRR: $12,450 (+18% MoM)
   Active Companies: 87 (+12 this week)
   User Retention (3m): 68%

📈 Growth
   Weekly Signups: 145
   Activation Rate: 42%
   Invite Conversion: 28%

⚠️ Flags
   Churn spike in Enterprise segment
   Onboarding drop-off at Step 3
```

#### 案例 2: Growth-Stage Dashboard Focus
```
NORTH STAR METRIC: Weekly Active Teams
─────────────────────────────────
Current: 2,847 (+15% MoM)
Target: 3,200 (end of Q)

SUPPORTING METRICS:
├─ New Team Signups: 387/week
├─ Team Activation: 67%
└─ Team Retention (30d): 81%

REVENUE HEALTH:
├─ MRR: $285K (+12% MoM)
├─ NDR: 118%
└─ Gross Margin: 78%
```

---

## 阶段性指标策略

### Seed Stage（种子轮）
**聚焦：** 产品市场契合度信号
- ✅ User Retention (3m)
- ✅ L7/L30
- ✅ Activation Rate
- ✅ Organic Growth Rate

### Series A（A 轮）
**聚焦：** 增长引擎验证
- ✅ MoM User Growth
- ✅ Virality Factor
- ✅ Paid Conversion Rate
- ✅ Early Revenue ($10K+ MRR)

### Series B（B 轮）
**聚焦：** 规模化效率
- ✅ MRR / ARR Growth
- ✅ Net Dollar Retention
- ✅ CAC Payback Period
- ✅ Gross Margins

---

## 关键洞察

### 1. 循序渐进
**不要一开始就追踪所有指标**：
- 种子阶段：3-5 个核心指标
- A 轮：7-10 个指标
- B 轮+：15-20 个指标

### 2. 北极星指标优先
确定一个最能反映价值交付的指标：
- **Slack:** Daily Active Teams
- **Notion:** Weekly Active Workspaces
- **Figma:** Files Created per Week

### 3. 避免虚荣指标
❌ **注册数** → ✅ **激活用户数**  
❌ **总用户数** → ✅ **留存用户数**  
❌ **页面浏览量** → ✅ **关键行为完成率**

### 4. 工具选择原则
- **早期（< $1M ARR）:** Google Sheets + Mixpanel
- **中期（$1M-$10M ARR）:** + Profitwell + Segment
- **后期（$10M+ ARR）:** + ChartMogul + Data Warehouse

---

## 实践建议

### 建立指标仪表盘的 5 步法

1. **定义北极星指标**
   - 反映核心价值交付
   - 可持续增长
   - 可被团队影响

2. **分解支撑指标**
   - 获客指标（流量、转化）
   - 激活指标（首次价值实现）
   - 留存指标（持续使用）
   - 收入指标（商业化健康度）

3. **选择工具栈**
   - 从简单开始（Google Sheets）
   - 按需添加专业工具
   - 确保数据准确性

4. **设计可视化**
   - 单页概览 + 详细视图
   - 每周更新节奏
   - 全员可访问

5. **建立审查节奏**
   - 每周团队同步
   - 每月高管审查
   - 每季度战略调整

---

## 常见错误

❌ **追踪过多指标** → 关注分散，无法聚焦核心问题

❌ **缺乏目标值** → 无法判断指标好坏

❌ **工具过于复杂** → 增加维护成本，降低使用率

❌ **数据不准确** → 基于错误数据做决策

❌ **缺乏行动项** → 指标追踪但不推动改进

---

## 延伸阅读

- [The 16 Startup Metrics](https://a16z.com/2015/08/21/16-metrics/) - Andreessen Horowitz
- [The Power User Curve](https://a16z.com/2018/08/06/power-user-curve-l30-l7/) - Casey Winters
- [SaaS Metrics 2.0](https://www.forentrepreneurs.com/saas-metrics-2/) - David Skok
- [The Ultimate SaaS Metrics Guide](https://chartmogul.com/resources/saas-metrics-guide/) - ChartMogul

---

**来源:** Lenny's Newsletter · 2020-10-20 · [原文链接](https://www.lennysnewsletter.com/p/the-most-important-bottom-up-saas-69d)
