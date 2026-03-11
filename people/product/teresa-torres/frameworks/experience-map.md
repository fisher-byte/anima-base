---
type: framework
person: teresa-torres
title: Experience Map
date: 2026-03-12
source: https://miro.com/blog/mapping-product-teams-teresa-torres/
status: published
verification_status: reviewed
tags: [user-research, customer-journey, opportunity-mapping, visual-synthesis]
language: en
---

# Experience Map

**Experience Map** 是 Teresa Torres 持续发现方法中的关键综合工具，用于可视化用户在完成特定任务时的完整体验，并标注其中的机会（痛点、需求、期望）。

## 框架概述

### 定义

Experience Map 捕捉用户"现在"如何完成任务——无论是使用你的产品还是其他替代方案。它是一个动态文档，随着每次用户访谈持续演进。

### 与其他地图的区别

| 地图类型 | 焦点 | 时态 | 使用场景 |
|----------|------|------|----------|
| **Experience Map** | 用户当前如何完成任务 | 现在 | 发现机会 |
| **Customer Journey Map** | 用户与品牌的整体旅程 | 现在/未来 | 体验优化 |
| **User Story Map** | 解决方案的功能结构 | 未来 | 交付规划 |
| **Service Blueprint** | 前台后台的完整流程 | 现在/未来 | 服务设计 |

## Experience Map 结构

### 基本元素

```
[触发点] → [步骤1] → [步骤2] → [步骤3] → ... → [目标达成]
              |          |          |
           [机会]     [机会]     [机会]
```

### 详细模板

```markdown
# Experience Map: [任务名称]

## 用户目标
用户想要达成什么？

## 触发点
什么触发了这个任务？

## 体验步骤

### 步骤 1: [动作描述]
- 用户做什么
- 使用什么工具
- **机会**: [痛点/需求/期望]
- **引用**: "用户原话..."

### 步骤 2: [动作描述]
- 用户做什么
- 使用什么工具
- **机会**: [痛点/需求/期望]
- **引用**: "用户原话..."

[继续添加步骤...]

## 变体路径
- 路径A: 当 [条件] 时
- 路径B: 当 [条件] 时
```

## 创建流程

### Step 1: 从访谈中提取故事

使用 Story Excavation 技术收集具体故事：

```markdown
引导问题：
- "上次你做[任务]时，发生了什么？"
- "带我从头到尾走一遍..."
- "然后呢？"（持续推进）
- "那是什么感觉？"
```

### Step 2: 绘制步骤

将每个故事转化为时间线上的步骤：

```
用户故事：
"我先打开邮件，看到客户的请求，然后去系统查数据，
 但系统很慢，等了5分钟，最后手动整理成Excel发给他们"

转化为：
[打开邮件] → [阅读请求] → [查系统] → [等待加载] → [整理Excel] → [发送]
                              ↓              ↓
                        [机会:数据访问]  [机会:等待时间]
```

### Step 3: 累积多个访谈

每次访谈后更新 Experience Map：

```
访谈 1: 路径 A-B-C-D
访谈 2: 路径 A-B-E-D (新发现 E)
访谈 3: 路径 A-F-C-D (新发现 F)
        ↓
综合地图: 包含所有路径变体和机会
```

### Step 4: 识别模式

分析累积的 Experience Map：

- 哪些痛点反复出现？
- 用户在哪里花费最多时间？
- 有哪些常见的变通方案？
- 最大的机会在哪里？

## 机会标注

### 机会类型

| 类型 | 标识 | 示例 |
|------|------|------|
| **痛点** | 🔴 | "这个步骤总是出错" |
| **需求** | 🔵 | "我需要更快地获取这个信息" |
| **期望** | 🟢 | "如果能自动完成就好了" |
| **变通** | 🟡 | "我通常会用Excel来处理" |

### 记录格式

```markdown
**机会**: [简短描述]
- 类型: 痛点/需求/期望
- 频率: 每次访谈都提到 / 偶尔提到
- 引用: "[用户原话]"
- 来源: 访谈 #1, #3, #5
```

## 与其他工具的关系

### 在发现流程中的位置

```
[用户访谈]
     ↓
[Interview Snapshot] ← 单次访谈记录
     ↓
[Experience Map] ← 累积综合（本框架）
     ↓
[Opportunity Solution Tree] ← 结构化机会
     ↓
[假设测试] ← 验证解决方案
```

### 输入与输出

**输入**:
- Interview Snapshots
- 用户观察笔记
- 支持数据

**输出**:
- OST 的机会节点
- 优先级排序依据
- 团队共识

## 实施建议

### 工具选择

- **Miro/FigJam**: 可视化协作白板
- **Notion**: 结构化文档
- **实体白板**: 面对面协作时

### 更新频率

```markdown
推荐节奏：
- 每次访谈后：添加新发现
- 每周：团队回顾和整合
- 每月：识别模式和优先级
```

### 团队协作

- Product Trio 共同维护
- 访谈后立即更新
- 定期回顾讨论

## 常见错误

### 1. 地图太抽象

**错误**: 高层次的流程图，缺乏细节
**正确**: 基于真实用户故事的具体步骤

### 2. 一成不变

**错误**: 创建一次后不再更新
**正确**: 每次访谈后持续演进

### 3. 解决方案思维

**错误**: 包含"用户应该做什么"
**正确**: 记录"用户现在做什么"

### 4. 忽略变体

**错误**: 只记录一条"标准"路径
**正确**: 捕捉所有观察到的路径变体

## 案例示例

### 任务: 提交报销申请

```markdown
触发: 员工完成出差后需要报销

[收集票据] → [拍照存档] → [登录系统] → [填写表单] → [上传票据] → [提交等待]
     |            |            |            |             |
  🔴 易丢失    🔵 需分类    🔴 忘记密码  🔴 字段太多   🔴 格式要求多

机会优先级：
1. 票据管理（高频痛点）
2. 表单简化（影响大）
3. 系统登录（可快速解决）
```

## 来源

- **原文**: [Mapping - Miro Blog](https://miro.com/blog/mapping-product-teams-teresa-torres/)
- **书籍**: Continuous Discovery Habits, Chapter 5
- **相关**: [Discovery Is Messy - Product Talk](https://www.producttalk.org/keeping-track-of-discovery/)

---
*Framework documented based on Teresa Torres's official Product Talk materials*
