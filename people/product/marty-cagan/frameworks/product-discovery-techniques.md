---
framework: Product Discovery Techniques
creator: Marty Cagan
source: SVPG, Inspired Book
verification_status: verified
verification_date: 2026-03-11
content_type: curated_framework
tags: [product-discovery, validation, prototyping, user-research]
---

# 产品发现技术 (Product Discovery Techniques)

## 框架概述

产品发现是 Marty Cagan 产品方法论的核心。这不是一个一次性活动，而是持续的过程，目的是在投入工程资源之前验证产品想法的四大风险。

## 核心原则

### 1. 目的是降低风险

> "The purpose of product discovery is to address these risks: Will the user buy this, or choose to use it? Can the user figure out how to use it? Can we build it? Does this solution work for our business?"

### 2. 最快最便宜地验证

- 优先使用原型
- 优先使用定性研究
- 优先使用现有工具
- 生产代码是最后手段

### 3. 持续而非一次性

- 发现不是一个阶段
- 而是持续的活动
- 与交付并行进行

## 发现技术分类

### 一、定性用户研究技术

#### 1. 用户访谈 (User Interviews)

**目的**: 理解用户问题和需求

**最佳实践**:
- 开放式问题
- 观察行为而非只听言语
- 关注问题而非解决方案
- 每周进行

**适用风险**: 价值风险

#### 2. 用户观察 (User Observation)

**目的**: 了解用户真实行为

**方法**:
- 情境访谈
- 跟踪观察
- 屏幕录制

**适用风险**: 价值风险、可用性风险

#### 3. 焦点小组 (Focus Groups)

**注意**: Marty Cagan不推荐用于产品发现
- 容易被强势者主导
- 群体思维
- 适合品牌/营销研究

### 二、原型技术

#### 1. 低保真原型 (Lo-Fi Prototypes)

**形式**:
- 纸上原型
- 白板草图
- 简单线框图

**适用场景**:
- 早期概念验证
- 快速迭代
- 团队对齐

**适用风险**: 价值风险（早期）

#### 2. 高保真原型 (Hi-Fi Prototypes)

**形式**:
- Figma/Sketch交互原型
- 看起来像真产品
- 可点击交互

**适用场景**:
- 可用性测试
- 用户验证
- 利益相关者演示

**适用风险**: 可用性风险、价值风险

#### 3. 实时数据原型 (Live Data Prototypes)

**形式**:
- 连接真实数据
- 高度仿真
- 复杂交互

**适用场景**:
- 复杂功能验证
- 最终用户测试

**适用风险**: 所有风险

#### 4. 可行性原型 (Feasibility Prototypes)

**形式**:
- 技术验证代码
- Spike
- 概念验证

**适用场景**:
- 技术风险评估
- 性能测试
- 第三方集成测试

**适用风险**: 可行性风险

### 三、可用性测试技术

#### 1. 定性可用性测试

**方法**:
- 1对1用户测试
- 给予任务观察完成
- Think-aloud协议

**最佳实践**:
- 每周进行
- 5个用户足够发现主要问题
- 测试者保持沉默
- 记录而非解释

**适用风险**: 可用性风险

#### 2. 无主持可用性测试

**工具**: UserTesting、Maze等

**优势**:
- 规模化
- 成本低
- 地理覆盖广

**适用风险**: 可用性风险

### 四、验证技术

#### 1. 价值验证测试

**方法**:
- 需求测试（用户会不会要）
- 支付意愿测试
- 优先级测试

**技术**:
- 假门测试 (Fake Door)
- 预注册页面
- 众筹验证

**适用风险**: 价值风险

#### 2. 定量验证

**方法**:
- A/B测试
- 多变量测试
- 漏斗分析

**注意**: 
- 需要足够流量
- 通常在定性验证后使用

**适用风险**: 价值风险、可用性风险

### 五、商业可行性验证

#### 1. 利益相关者访谈

**对象**:
- 法务
- 合规
- 销售
- 财务
- 市场

**目的**: 验证商业约束

**适用风险**: 商业可行性风险

#### 2. 财务建模

**内容**:
- 单位经济
- 获客成本
- 生命周期价值

**适用风险**: 商业可行性风险

## 发现流程建议

### 每周节奏

```
周一：规划本周发现目标
周二-周四：用户测试、访谈、原型迭代
周五：回顾和学习整理
```

### 团队分工

| 角色 | 主要发现职责 |
|-----|------------|
| PM | 价值验证、商业可行性 |
| Designer | 可用性测试、原型设计 |
| Tech Lead | 可行性评估 |

## 常见反模式

### ❌ 跳过发现直接构建
"我们很确定用户需要这个"

### ❌ 只做定量不做定性
"我们做了A/B测试"但不理解为什么

### ❌ 只访谈不测试
"用户说他们想要"但没验证

### ❌ 原型过于复杂
花几周做原型，不如花几天做简单版本测试

### ❌ 测试错误的事情
验证了可用性，但没验证价值

## Marty Cagan 原话

> "The purpose of product discovery is to make sure we have some evidence that when we ask the engineers to build a production-quality product, it won't be a waste of time and money."

> "We need to change the mindset from 'launching features' to 'learning and iterating'."

## 延伸阅读

- **书籍**: 《Inspired》产品发现章节
- **书籍**: Teresa Torres《Continuous Discovery Habits》
- **SVPG**: [Product Discovery Articles](https://www.svpg.com/insights/product-discovery-articles/)
- **视频**: [How to structure Product Discovery](https://www.youtube.com/watch?v=dHkb--_BhGI)

---
*Framework curated from SVPG articles and Inspired book*
*Last updated: 2026-03-11*
