# 执行计划 - Anima Base 内容采集系统

## 第一阶段：立即执行（今天）

### 1.1 项目初始化 ✅
- [x] GitHub 仓库连接
- [x] 目录结构创建
- [x] 基础文档编写
- [ ] 首次提交到 GitHub

### 1.2 内容采集脚本开发

#### 脚本 1: RSS 订阅收集器 (rss_collector.py)
功能：
- 订阅产品/营销/增长相关 RSS
- 自动抓取新文章
- 保存为 Markdown 格式

目标 RSS 源：
- Lenny's Newsletter
- First Round Review
- Reforge Blog
- Growth.design
- Shreyas Doshi
- Julie Zhuo
- SVPG Blog (Marty Cagan)

#### 脚本 2: 播客转录器 (podcast_transcriber.py)
功能：
- 下载播客音频
- 使用 Whisper API 转录
- 分段整理，提取精华

目标播客：
- Lenny's Podcast
- How I Built This
- The Knowledge Project
- 20VC

#### 脚本 3: Twitter 精华抓取器 (twitter_curator.py)
功能：
- 抓取目标人物的精华推文
- 按主题分类整理
- 保存为语录合集

目标人物列表（见下方）

#### 脚本 4: YouTube 内容提取器 (youtube_extractor.py)
功能：
- 下载视频字幕
- 提取演讲/访谈精华
- 生成结构化笔记

#### 脚本 5: 书籍摘要生成器 (book_summarizer.py)
功能：
- 从 Z-Library 等渠道获取书籍
- 自动生成章节摘要
- 提取核心观点和语录

#### 脚本 6: 内容索引生成器 (index_generator.py)
功能：
- 扫描所有内容文件
- 按主题自动分类
- 生成索引 Markdown 文件

---

## 第二阶段：本周完成

### 2.1 人物档案建设

优先建设以下人物档案（每个包含 profile.md + quotes.md）：

**产品领域（10人）：**
1. Brian Chesky (Airbnb) - 产品直觉、设计思维
2. Lenny Rachitsky - 产品管理、职业发展
3. Shreyas Doshi - 产品领导力、沟通
4. Julie Zhuo - 产品管理、团队建设
5. John Cutler - 产品运营、组织效能
6. Marty Cagan - 产品发现、团队模式
7. Teresa Torres - 持续发现、客户访谈
8. Jackie Bavaro - 产品管理基础
9. Brandon Chu - 产品决策、Shopify经验
10. Casey Winters - 增长产品、Pinterest/Grubhub

**营销领域（8人）：**
1. Seth Godin - 现代营销、定位
2. April Dunford - 产品定位、市场策略
3. David Ogilvy - 广告经典
4. Ann Handley - 内容营销
5. Rand Fishkin - SEO、创业营销
6. Dave Gerhardt - B2B营销
7. Amanda Natividad - 内容策略
8. Katelyn Bourgoin - 客户研究

**增长领域（6人）：**
1. Sean Ellis - 增长黑客之父
2. Brian Balfour - 增长框架、Reforge
3. Andrew Chen - 增长策略、网络效应
4. Elena Verna - 增长运营、订阅模式
5. Chamath Palihapitiya - Facebook增长
6. Gustaf Alströmer - Airbnb增长

**领导力领域（6人）：**
1. Ben Horowitz - 创业领导、艰难决策
2. Andy Grove - 管理经典
3. Satya Nadella - 微软转型
4. Reed Hastings - Netflix文化
5. Ray Dalio - 原则、决策
6. Patrick Lencioni - 团队协作

### 2.2 内容采集计划

**每日自动采集：**
- RSS 新文章（定时检查）
- Twitter 精华（每日更新）
- 播客新节目（发布即采集）

**每周批量采集：**
- 书籍摘要生成
- YouTube 新视频
- 索引重建

---

## 第三阶段：持续运营

### 3.1 自动化工作流

**每日（08:00）：**
1. 检查 RSS 订阅更新
2. 抓取 Twitter 新内容
3. 检查播客新节目
4. 生成每日内容摘要

**每周（周日）：**
1. 内容质量审查
2. 索引更新
3. 缺失内容识别
4. 下周采集计划

**每月（1号）：**
1. 完整数据备份
2. 贡献统计报告
3. 内容质量评估
4. 新人物/主题规划

### 3.2 质量保障机制

- 所有内容必须标注来源
- 定期人工抽查验证
- 用户反馈收集
- 过时内容标记更新

---

## 资源配置

### API 和工具需求
- OpenAI API (Whisper + GPT) - 转录和摘要
- Twitter API v2 - 推文抓取
- YouTube Data API - 视频信息
- RSS 解析库 (feedparser)
- GitHub API - 自动提交

### 存储需求
- 文本内容：Git 仓库
- 音频/视频：本地/云存储
- 元数据：SQLite/JSON

---

## 下一步行动

### 立即执行（接下来2小时）：
1. [ ] 提交当前项目结构到 GitHub
2. [ ] 开发 rss_collector.py 基础版本
3. [ ] 创建第一个示例人物档案（Lenny Rachitsky）
4. [ ] 测试 RSS 采集流程

### 本周完成：
1. [ ] 完成6个核心脚本开发
2. [ ] 创建30个人物基础档案
3. [ ] 建立自动化工作流
4. [ ] 完成首次内容推送

---

## 成功指标

- 每周新增内容条目 > 50
- 人物档案覆盖 > 100人
- 内容来源渠道 > 20个
- 自动化率 > 80%
