# 定时任务提示词 — 王慧文 & Paul Graham 决策案例收集

> **任务目标**：持续扩充王慧文和Paul Graham的决策案例库，每人目标10个核心案例  
> **当前进度**：王慧文 2/10（20%），Paul Graham 1/10（10%）  
> **更新时间**：2026-03-17

---

## 任务指令

你是anima-base项目的定时任务执行者，负责持续收集王慧文和Paul Graham的决策案例。

### 核心目标
每次定时任务执行时：
1. 为**王慧文**创建1-2个新决策案例
2. 为**Paul Graham**创建1-2个新决策案例
3. 更新README和进度跟踪
4. 提交到GitHub

### 当前进度

#### 王慧文（2/10完成，20%）
✅ 已完成：
- case-01: 校内网实名制策略（发现规律并坚持）
- case-02: 美团后发优势战略（学习能力>先发时间）

⏳ 待创建（按优先级）：
1. **π型人才培养决策** [优先]
   - 来源：清华课程第一课
   - 核心：复合人才 > 专才
   - 数据：2/3工程师转产品经理失败

2. **核心竞争力定义** [优先]
   - 来源：校内网卖掉后的反思
   - 核心：学习能力 + 发现机会能力
   - 背景：与中移动对话的尴尬

3. **产品决策框架**
   - 来源：清华课程第四课
   - 核心：战略如同医生治病

4. **商业模式设计**
   - 来源：清华课程第五课
   - 核心：可持续商业模式

5. **组织建设方法论**
   - 来源：清华课程第六课
   - 核心：如何培养产品经理

6. **战略与执行平衡**
   - 来源：清华课程第七课
   - 核心：战略执行的平衡

7. **美团三类互联网分类**
   - 来源：清华课程
   - 核心：纯线上/O2O/自动化

8. **美团外卖决策**
   - 来源：美团历史
   - 核心：从团购到全品类

#### Paul Graham（1/10完成，10%）
✅ 已完成：
- case-01: YC创立决策（第一性原理+批量模式）

⏳ 待创建（按优先级）：
1. **Do Things That Don't Scale** [优先]
   - 来源：经典文章
   - 核心：早期手动获客
   - 案例：Airbnb拍照片、Stripe手动集成

2. **Relentlessly Resourceful** [优先]
   - 来源：经典文章
   - 核心：创始人本质特征
   - 反面：Hapless（无助）

3. **Maker's Schedule vs Manager's Schedule**
   - 来源：经典文章
   - 核心：创造者需要大块时间

4. **Startup = Growth**
   - 来源：经典文章
   - 核心：增长是创业本质定义

5. **How to Get Startup Ideas**
   - 来源：经典文章
   - 核心：活在未来，打造缺失的东西

6. **Schlep Blindness**
   - 来源：经典文章
   - 核心：人们回避艰难的好点子

7. **Make Something People Want**
   - 来源：YC口号
   - 核心：产品第一性原理

8. **How to Do Great Work**
   - 来源：2023文章
   - 核心：追随好奇心

9. **Founder Mode**
   - 来源：2024文章
   - 核心：创始人模式 vs 管理者模式

---

## 执行步骤

### Step 1: 选择案例（每次1-2个）
从待创建列表中选择标记为[优先]的案例，如果[优先]已完成，则按顺序选择。

### Step 2: 搜索补充材料
```bash
# 王慧文案例
web_search "王慧文 清华课程 [案例主题] 产品管理"
web_search "王慧文 美团 [决策场景]"

# Paul Graham案例
web_search "Paul Graham [essay title]"
web_fetch "https://paulgraham.com/[essay-name].html"
```

### Step 3: 创建案例文件
参考已完成案例的结构：
- 案例背景（时间/环境/挑战）
- 决策过程（思路/选项/权衡）
- 决策结果（短期/长期/数据）
- 核心洞察（3-5个）
- 决策框架提炼
- 启发式规则（IF-THEN格式）
- 可迁移性分析
- 对比案例

### Step 4: 更新进度
```bash
# 更新README
- 修改已完成案例数量
- 将完成的案例从待创建移到已完成

# 更新TASK_LOG.md
- 记录本次执行的案例
- 更新进度统计
```

### Step 5: Git提交
```bash
cd /Users/zhiyangyu/.box/Workspace/anima-base-scheduled
git add people/product/wang-huiwen/decision-cases/
git add people/product/paul-graham/decision-cases/
git commit -m "feat: 新增王慧文/PG决策案例

王慧文：
- case-XX: [案例标题]（核心洞察）

Paul Graham：
- case-XX: [案例标题]（核心洞察）

当前进度：王慧文 X/10，PG Y/10"
git push origin main
```

---

## 质量标准

### 必须包含的元素
✅ 案例元数据（id/person/title/date/outcome/impact_level）
✅ 决策背景（时间/环境/挑战）
✅ 决策过程（思路/选项/权衡）
✅ 决策结果（短期/长期/数据对比）
✅ 核心洞察（3-5个，可操作）
✅ 决策框架提炼（可复用）
✅ 启发式规则（IF-THEN格式，5-10条）
✅ 可迁移性分析（适用/不适用场景）
✅ 证据来源（A/B/C级标注）

### 案例长度标准
- 核心案例：8-12KB（如case-01/02）
- 扩展案例：5-8KB
- 避免：过短（<3KB）或过长（>15KB）

### 启发式规则格式
```
IF [条件]
AND [附加条件]
THEN [行动]

示例：
IF 你的决策逆主流
THEN 必须回答：
  Q1: 有什么证据？
  Q2: 为什么主流错了？
  Q3: 如何小成本验证？
```

---

## 资料来源

### 王慧文
- ✅ 清华大学《互联网产品管理课》（7课全文）
  * 路径：`files/articles/wang-huiwen/tsinghua-lesson-第X课.txt`
- ✅ 已有访谈/文章：
  * interviews/2019-geekpark-core-competitiveness.md
  * interviews/2023-36kr-agi-journey.md
  * talks/2019-strategy-organization-capability.md
  * talks/2020-chaos-university-decision-making.md
- 🔍 补充搜索：
  * 美团历史报道
  * 校内网发展历程
  * 王慧文博客/访谈

### Paul Graham
- ✅ Essays（200+篇）
  * 路径：`people/product/paul-graham/essays/`
  * 网站：https://paulgraham.com/articles.html
- ✅ 已有文章：
  * do-things-that-dont-scale.md
  * relentlessly-resourceful.md
  * makers-schedule-managers-schedule.md
  * startup-equals-growth.md
  * how-to-get-startup-ideas.md
  * schlep-blindness.md
  * founder-mode.md
  * how-to-do-great-work.md
- 🔍 补充搜索：
  * YC历史采访
  * Hacker News讨论
  * Viaweb创业故事

---

## 进度跟踪

### 完成标准
- ✅ 每人10个核心案例
- ✅ 每个案例8-12KB
- ✅ 100%覆盖核心方法论
- ✅ 所有案例推送到GitHub

### 时间规划
- **短期（本周）**：完成至少各2个案例
  * 王慧文：4/10（40%）
  * PG：3/10（30%）
- **中期（本月）**：完成至少各5个案例
  * 王慧文：7/10（70%）
  * PG：6/10（60%）
- **长期（下月）**：全部完成
  * 王慧文：10/10（100%）
  * PG：10/10（100%）

### 优先级原则
1. 先完成标记[优先]的案例
2. 优先覆盖核心方法论
3. 平衡两个Persona进度（不要一个100%另一个0%）

---

## 输出格式

每次任务完成后，输出进度报告：
```
📊 本次任务完成情况

王慧文：
  ✅ 新增：case-XX [案例标题]（核心洞察）
  📈 进度：X/10（Y%）

Paul Graham：
  ✅ 新增：case-XX [案例标题]（核心洞察）
  📈 进度：X/10（Y%）

总进度：(王慧文进度 + PG进度) / 20

下次任务目标：
  - 王慧文：case-XX [下一个案例]
  - PG：case-XX [下一个案例]
```

---

**任务创建时间**：2026-03-17  
**预计完成时间**：2026-04-15  
**当前状态**：进行中
