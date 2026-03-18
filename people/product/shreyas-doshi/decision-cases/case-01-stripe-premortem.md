---
case_id: case-01
case_name: Stripe 产品发布 Pre-mortem 决策
decision_maker: Shreyas Doshi
company: Stripe
timeframe: 2015-2021
decision_type: 风险预防决策
outcome: 成功（持续实践，成为 Stripe 产品文化）
verification_status: A级（作者亲述，Coda 文档，Medium 文章，Lenny's Podcast）
sources:
  - https://coda.io/@shreyas/pre-mortems
  - https://medium.com/@shreyashere/how-to-use-pre-mortems-to-prevent-problems-blunders-and-disasters-6ecc6df6e22a
  - https://www.lennysnewsletter.com/p/episode-3-shreyas-doshi
keywords:
  - pre-mortem
  - 风险预防
  - 产品发布
  - 团队沟通
  - 心理安全
created_at: 2026-03-18
---

# Case-01: Stripe 产品发布 Pre-mortem 决策

## 📋 决策背景

### 情境设定
- **时间**：Shreyas 在 Stripe 担任首位产品负责人期间（2015-2021）
- **场景**：重大产品发布前的风险管理
- **挑战**：
  1. **事后补救困境**：团队习惯在产品发布后通过 post-mortem 复盘问题，但此时已造成损失
  2. **问题可见性低**：团队成员因为"政治正确"不敢提前指出潜在问题
  3. **救火文化**：产品发布总是伴随着混乱和临时救火，团队士气受损
  4. **预警机制缺失**：缺乏系统性的方法在项目早期识别和预防问题

### 关键约束
- **时间压力**：产品发布时间表紧张，没有太多缓冲时间
- **心理安全**：团队成员担心提出"消极"意见会被视为不支持团队
- **流程成本**：额外增加流程可能被视为官僚主义，降低执行效率
- **执行一致性**：需要确保 pre-mortem 的发现能在整个项目周期持续发挥作用

---

## 🤔 决策选项

### 选项 A：继续现状（仅做 Post-mortem）
**描述**：保持现有流程，在产品发布后做 post-mortem 复盘。

**优势**：
- 流程简单，无需改变现有工作方式
- 不增加项目前期负担
- 事后总结经验教训

**劣势**：
- 问题已经发生，损失无法挽回
- 团队士气因发布混乱受损
- 客户体验受影响
- 持续陷入"救火-复盘-再救火"循环

**Shreyas 的评估**：❌ 不可接受
> "If you do a pre-mortem right, you won't need a tough post-mortem."

---

### 选项 B：标准 Pre-mortem（Gary Klein 版本）
**描述**：采用 Gary Klein 在《The Power of Intuition》中提出的标准 pre-mortem 流程：
1. 假设项目失败
2. 每人写下失败原因
3. 轮流分享
4. 会后整理和改进计划

**优势**：
- 经典方法论，已被证明有效
- 形式简单，易于执行
- 能识别潜在风险

**劣势**：
- **会后遗忘**：会议很engaging，但结束后团队立刻回到老模式
- **缺乏持续性**：pre-mortem 变成一次性活动，没有在项目全周期发挥作用
- **心理障碍**：直接讨论"失败原因"仍然有一定心理压力
- **缺少行动词汇**：团队在会后缺乏便捷的方式持续讨论这些问题

**Shreyas 的评估**：⚠️ 部分可行，但需改进

---

### 选项 C：改进版 Pre-mortem + Tigers/Paper Tigers/Elephants 隐喻 ✅
**描述**：在标准 pre-mortem 基础上引入隐喻词汇系统：

**核心创新**：
1. **🐅 Tiger（真老虎）**：明确的威胁，如果不处理会伤害我们
2. **🐯 Paper Tiger（纸老虎）**：表面威胁，但你个人并不担心（但别人可能担心）
3. **🐘 Elephant（房间里的大象）**：你担心团队没有谈论的问题

**流程设计**（1小时结构化会议）：
- **10分钟**：会议启动，设定场景（"3个月后项目惨败"）
- **10分钟**：静默头脑风暴（每人至少列出 2 个 Tigers 和其他威胁）
- **30分钟**：静默投票 + 小组讨论（逐个分享和投票）
- **10分钟**：起草行动计划（会议负责人总结 top 3-5 威胁和缓解措施）

**会后行动**：
- 制定 action plan，包括：
  - Top 主题
  - 逐字记录的威胁
  - 缓解措施
  - Owner 负责人

**优势**：
- ✅ **心理安全词汇**：使用隐喻降低讨论威胁的心理障碍
- ✅ **持续使用**：团队在项目全周期可以说"Bob 标记的那个 Tiger"或"昨天站会提到的 Elephant"
- ✅ **便捷沟通**：在 Slack、邮件、会议、1on1 中都可以使用这套词汇
- ✅ **系统化预警**：将 pre-mortem 从一次性活动变成持续实践
- ✅ **高参与度**：隐喻降低了提出"消极"意见的心理成本

**劣势**：
- 需要解释新概念
- 需要团队习惯这套词汇
- 需要会议负责人有较强的引导能力

**Shreyas 的评估**：✅ **最优选择**

---

## 💡 决策理由

Shreyas 选择了 **选项 C（改进版 Pre-mortem）** 并在 Stripe 团队持续实践，原因包括：

### 1. 预防成本远低于救火成本
> "In my experience, the standard pre-mortem meeting was very engaging while the team was in the room. But I frequently saw everyone forget about the progress made in the meeting."

**核心洞察**：
- 在项目早期投入 1 小时做 pre-mortem
- 可以节省后期数周的救火时间
- 避免客户体验受损和团队士气低落

### 2. 心理安全词汇是关键突破
> "What was missing, I realized, was an evocative, convenient lexicon that allowed people to talk about these things in a psychologically safe manner."

**核心创新**：
- **Tiger**：听起来比"风险"更具体和可视化
- **Paper Tiger**：允许表达"我不担心但别人可能担心"的微妙立场
- **Elephant**：优雅地指出"我们在回避的问题"

### 3. 持续性是成败关键
Shreyas 发现标准 pre-mortem 的最大问题是"会后遗忘"：
- ✅ 会议中：团队高度参与，识别出很多问题
- ❌ 会议后：立刻回到老模式，pre-mortem 的成果被遗忘

**解决方案**：
- 引入便捷词汇（Tigers/Elephants）让团队在项目全周期持续使用
- 在 Slack、邮件、会议中随时提及这些隐喻
- 将 pre-mortem 从"一次性活动"变成"持续文化"

### 4. 结构化流程确保执行质量
1小时会议的精确时间分配：
- 10min 启动 + 10min 静默头脑风暴 + 30min 讨论投票 + 10min 行动计划
- 静默环节避免群体思维和从众效应
- 强制输出 action plan（top 3-5 威胁 + owner + 缓解措施）

---

## 📊 决策结果

### 短期成果（Stripe 团队实践）
1. **"平静的产品发布"**：
   - Shreyas 团队在 Stripe 通过 pre-mortem 实现了 calm product launches
   - 大幅减少发布日的混乱和救火

2. **团队士气提升**：
   - 团队成员感到被倾听，心理安全感提升
   - 预防成功带来的正向反馈

3. **问题提前识别率高**：
   - 在项目早期（发布前 1-3 个月）识别出关键风险
   - 有充足时间制定和执行缓解措施

### 中期影响（成为 Stripe 产品文化）
1. **持续实践**：
   - Pre-mortem 成为 Stripe 重大产品发布的标准流程
   - Tigers/Elephants 词汇融入日常沟通

2. **团队能力提升**：
   - 团队主动识别和提出风险的能力增强
   - 从"reactive"（被动应对）转向"proactive"（主动预防）

### 长期影响（方法论传播）
1. **行业影响力**：
   - Shreyas 将方法分享到 Coda、Medium、Lenny's Podcast
   - 成为产品管理领域广泛使用的框架

2. **工具化**：
   - Coda 模板被数千团队使用
   - 衍生出多种变体和工具（如 Ludi 的 Futurespective 模板）

3. **教育普及**：
   - 成为产品管理课程的标准内容
   - 被 Y Combinator、Reforge 等机构推荐

---

## 🎯 启发式规则

从这个决策案例中可以提炼出以下决策启发式：

### 规则 1：预防优于治疗
**原则**：在项目早期投入时间做 pre-mortem，远比后期救火高效。

**判断标准**：
- ✅ 重大产品发布前 1-3 个月
- ✅ 高风险战略项目启动时
- ✅ 涉及多团队协作的复杂项目

**反例**：
- ❌ 小功能迭代不需要 pre-mortem（过度流程化）
- ❌ 时间紧迫到无法缓解风险的情况（此时 pre-mortem 价值有限）

---

### 规则 2：心理安全词汇降低沟通成本
**原则**：使用隐喻（Tigers/Paper Tigers/Elephants）降低团队讨论风险的心理障碍。

**判断标准**：
- ✅ 团队文化中"负面"意见难以表达
- ✅ 需要讨论敏感话题或"房间里的大象"
- ✅ 跨部门协作中存在政治因素

**应用场景**：
- 在 Slack 中说："我发现了一个 Elephant"
- 在会议中说："这个可能是 Paper Tiger，但我想确认一下"
- 在 1on1 中说："关于那个 Tiger，我们需要指定 owner"

---

### 规则 3：系统化预警需要持续机制
**原则**：将 pre-mortem 的发现持续使用在项目全周期，而非一次性会议。

**判断标准**：
- ✅ 在项目站会中回顾 Tigers 的缓解进度
- ✅ 在 Slack/邮件中随时引用 pre-mortem 的发现
- ✅ 定期检查 action plan 的执行情况

**反例**：
- ❌ Pre-mortem 会议记录被归档后再也没人看
- ❌ Action plan 没有明确的 owner 和 deadline

---

### 规则 4：结构化流程确保执行质量
**原则**：1小时结构化会议（10+10+30+10）+ 强制输出 action plan。

**关键要素**：
- **静默头脑风暴**：避免群体思维和从众效应
- **强制输出**：必须列出 top 3-5 威胁 + owner + 缓解措施
- **时间控制**：严格遵守时间分配，保持会议效率

---

### 规则 5：权衡流程成本和预防价值
**原则**：Pre-mortem 适用于高风险场景，但避免过度流程化。

**判断标准**：
- ✅ 重大产品发布：pre-mortem 价值 >> 流程成本
- ✅ 战略项目：失败成本高，值得投入预防
- ❌ 日常小迭代：pre-mortem 成本 > 预防价值（过度流程化）

---

## 📚 延伸阅读

### Shreyas Doshi 相关资源
- [Pre-mortems Coda 模板](https://coda.io/@shreyas/pre-mortems)
- [How to Use Pre-mortems to Prevent Problems](https://medium.com/@shreyashere/how-to-use-pre-mortems-to-prevent-problems-blunders-and-disasters-6ecc6df6e22a)
- [Lenny's Podcast: Shreyas on pre-mortems](https://www.lennysnewsletter.com/p/episode-3-shreyas-doshi)
- [YouTube: How to use my pre-mortem doc](https://www.youtube.com/watch?v=Pwh0RFqL2Sk)

### 相关决策框架
- [LNO Framework](../frameworks/lno-framework.md)（Shreyas Doshi）
- [Three Levels of Product Work](../frameworks/three-levels-product-work.md)（Shreyas Doshi）
- [Execution vs Strategy Problems](../frameworks/execution-strategy-problems.md)（Shreyas Doshi）

### 原始理论来源
- Gary Klein, *The Power of Intuition*（标准 pre-mortem 方法论）
- Daniel Kahneman, *Thinking, Fast and Slow*（认知偏差和群体思维）

---

**案例质量等级**：A 级（作者亲述，多来源验证）  
**最后更新**：2026-03-18  
**验证方式**：Shreyas 本人在 Coda、Medium、Lenny's Podcast 多次详细阐述
