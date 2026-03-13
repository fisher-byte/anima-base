# Sean Ellis — Frameworks

> **Sean Ellis**:增长黑客之父,创造"Growth Hacking"一词,开创了系统化、数据驱动的增长方法论。

## 核心框架体系

Sean Ellis的增长框架构成了现代增长黑客的基石,从产品市场契合度验证到高速实验执行,形成完整的增长方法论闭环。

---

## 🎯 产品市场契合度层

### 1. [PMF Survey — The 40% Test](./pmf-survey.md)
**一句话**: 通过一个问题衡量产品是否为用户"必需品"

**核心问题**: "如果你无法再使用[产品名称],你会有什么感受?"

**40%法则**: 
- ≥40%用户回答"非常失望" = 达到PMF
- <40% = 需继续优化产品以找到PMF

**适用场景**:
- 早期创业验证PMF
- 新产品上市前评估
- 现有产品迭代方向决策
- 识别"必需品"用户群体特征

**关键洞察**:
> "在找到产品市场契合度之前扩大规模,是扼杀初创公司最快的方式。"

---

## 📊 增长度量层

### 2. [North Star Metric (NSM)](./north-star-metric.md)
**一句话**: 对齐全公司围绕单一可持续增长指标

**定义**: 量化产品为客户提供核心价值的单一指标

**经典案例**:
- **Facebook**: 日活跃用户(DAUs)
- **Uber**: 每周乘车次数
- **Airbnb**: 每月预订夜数

**选择标准**:
1. 反映"必需品"客户获得的核心价值
2. 可以长期"向上向右"增长
3. 不会引导团队做违背长期利益的行为
4. 简单到每个人都能理解和记住
5. 与公司使命有明确连接

**与其他框架关系**:
- 量化[PMF Survey](./pmf-survey.md)识别的"必需品价值"
- 追踪达到[Aha Moment](./aha-moment-activation.md)的用户数量
- 作为[ICE评分](./ice-prioritization.md)的Impact评估基准

---

## 🚀 激活优化层

### 3. [Aha Moment & Activation](./aha-moment-activation.md)
**一句话**: 让用户首次体验到产品核心价值的神奇瞬间

**定义**:
- **Aha Moment**: 用户首次理解产品核心价值的瞬间
- **Activation**: 提高新用户达到Aha Moment比率的过程

**经典案例**:
- **Facebook**: 10天内添加7个好友
- **Twitter**: 关注30个账号
- **Slack**: 团队发送2000条消息
- **Dropbox**: 在一台设备保存,另一台设备访问

**优化框架**:
1. 识别Aha Moment(分析"必需品"用户早期行为)
2. 绘制用户旅程(从注册到Aha Moment)
3. 识别摩擦点(哪一步流失最大)
4. 减少达到时间(简化路径、提供指引、降低门槛)
5. 高速测试优化(用ICE排序实验)

**核心公式**:
```
激活率 = 达到Aha Moment的新用户 / 总新用户
```

---

## 🎯 实验优先级层

### 4. [ICE Prioritization Framework](./ice-prioritization.md)
**一句话**: 快速优先排序增长实验的最小可行框架

**ICE = Impact × Confidence × Ease**

**三要素评分**(1-10分):
- **Impact**: 这个测试预计影响有多大?
- **Confidence**: 你有多确信测试能证明假设?
- **Ease**: 启动这个测试有多容易?

**为什么有效?**
- 相对优先级排序,非完美排序
- 在增长流程中持续校准
- 团队协作提供现实检查
- 防止"分析瘫痪",保持测试速度

**实施流程**(GrowthHackers实践):
1. 设定增长目标 → 筛选1500+想法到30-75个
2. 团队提名 → 每人最多2个,筛选到10个
3. ICE评审 → 绿灯3-5个测试

**关键原则**:
> "把ICE评分看作最小可行的优先级框架。它不是客观完美的,但足够好完成工作。"

---

## 🔄 实验执行层

### 5. [High Tempo Testing](./high-tempo-testing.md)
**一句话**: 通过快速实验循环加速增长学习

**增长实验循环**(4步):
```
IDEATE (构思) → PRIORITIZE (优先级) → TEST (测试) → ANALYZE (分析) → 循环
```

**为什么速度至关重要?**
- **学习速度** = 有效测试数量 / 时间
- 每周10个测试 vs 每周2个测试 = **5倍学习优势**
- 更高概率找到突破性增长(幂律分布)
- 小改进的复合效应(每周1%改进 × 52周 = 67%增长)

**加速策略**:
1. 降低测试门槛(无代码工具、小流量测试)
2. 并行测试(不冲突的实验同时运行)
3. 快速失败(早期停止明显失败的测试)
4. 自动化(数据收集、结果报告、部署)
5. 简化设计(从MVP测试开始)

**测试速度基准**:
| 公司阶段 | 每周测试数 | 团队规模 |
|---------|-----------|---------|
| 早期创业 | 3-5 | 2-3人 |
| 成长期 | 10-20 | 4-6人 |
| 成熟期 | 50-100+ | 10+人 |

**关键洞察**:
> "测试的高速度对于找到产品市场契合度至关重要。最好的增长黑客不是欺骗用户的技巧,而是快速学习用户真正想要什么。"

---

## 🔗 框架关系图

```
         ┌─────────────────┐
         │  PMF Survey     │ 识别"必需品"价值
         │  (40% Test)     │
         └────────┬────────┘
                  ↓
         ┌─────────────────┐
         │ North Star      │ 量化核心价值
         │ Metric (NSM)    │
         └────────┬────────┘
                  ↓
         ┌─────────────────┐
         │ Aha Moment &    │ 新用户首次体验价值
         │ Activation      │
         └────────┬────────┘
                  ↓
    ┌─────────────────────────────┐
    │                             │
    ↓                             ↓
┌─────────────────┐    ┌─────────────────┐
│ ICE             │←───│ High Tempo      │
│ Prioritization  │    │ Testing         │
└─────────────────┘    └─────────────────┘
  优先排序实验           快速执行循环
```

**核心逻辑**:
1. **PMF Survey** → 识别产品"必需品"价值和用户群体
2. **North Star Metric** → 将价值量化为可追踪的增长指标
3. **Aha Moment** → 定义新用户首次体验价值的瞬间
4. **ICE Prioritization** → 快速决策哪些实验最值得运行
5. **High Tempo Testing** → 高速执行实验,加速学习和增长

---

## 📚 完整增长方法论

### 阶段1:寻找PMF
- **目标**: 让产品成为目标用户的"必需品"
- **工具**: [PMF Survey](./pmf-survey.md)
- **阈值**: ≥40%用户"非常失望"
- **禁止**: 在达到PMF前大规模增长投入

### 阶段2:定义增长指标
- **目标**: 量化核心价值,对齐团队
- **工具**: [North Star Metric](./north-star-metric.md)
- **要求**: 简单、可持续增长、反映价值、连接使命

### 阶段3:优化激活
- **目标**: 让更多新用户更快达到Aha Moment
- **工具**: [Aha Moment & Activation](./aha-moment-activation.md)
- **方法**: 识别Aha Moment → 绘制路径 → 减少摩擦 → 高速测试

### 阶段4:规模化增长
- **目标**: 通过系统化实验持续优化所有增长杠杆
- **工具**: [ICE](./ice-prioritization.md) + [High Tempo Testing](./high-tempo-testing.md)
- **流程**: 构思 → 优先级 → 测试 → 分析 → 循环

---

## 💡 关键原则

### 1. PMF是增长的前提
> "在找到产品市场契合度之前扩大规模,是扼杀初创公司最快的方式。"

### 2. 数据驱动决策
> "增长黑客是一种严格的、数据驱动的方法。"

### 3. 速度是竞争优势
> "测试越多,学习越快,增长越快。"

### 4. 简单胜过完美
> "保持指标和框架简单,让团队每个人都能理解和执行。"

### 5. 系统化流程
> "可持续增长来自系统化流程,而非偶然的增长黑客技巧。"

---

## 🛠️ 实战资源

### 工具
- **PMF调查**: [PMFSurvey.com](https://pmfsurvey.com) (免费)
- **增长项目管理**: [GrowthHackers Projects](https://growthhackers.com/solutions/software)
- **社区**: [GrowthHackers.com](https://growthhackers.com)

### 书籍
- **Hacking Growth** — Sean Ellis & Morgan Brown
  - 完整增长方法论
  - 真实案例研究
  - 实操指南

### 在线课程
- [Growth University](https://growthuniversity.teachable.com/) — Sean Ellis创办

---

## 📖 延伸阅读

- [Using Product/Market Fit to Drive Sustainable Growth](https://medium.com/growthhackers/using-product-market-fit-to-drive-sustainable-growth-58e9124ee8db)
- [Finding Your North Star Metric](https://medium.com/growthhackers/finding-your-north-star-metric-fc1c1f71cbcb)
- [The Practical Advantage Of The ICE Score](https://medium.com/growthhackers/the-practical-advantage-of-the-ice-score-as-a-test-prioritization-framework-cdd5f0808d64)
- [The Science of Growth with Sean Ellis](https://www.productcompass.pm/p/the-science-of-growth-with-sean-ellis)

---

**最后更新**: 2026-03-14
