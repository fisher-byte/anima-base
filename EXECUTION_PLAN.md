# 执行计划 — Anima Base 内容扩充

> 本计划指导定时任务持续执行，分阶段完成全部人物的内容扩充。
>
> 最后更新：2026-03-11

---

## 当前进度回顾

**已完成（2026-03-11）：**
- ✅ Brian Chesky 语录集（50+ 条）
- ✅ Marty Cagan 书籍摘要（Inspired/Empowered/Transformed）
- ✅ 11位专家空档案启动（Jackie Bavaro、John Cutler、Brandon Chu、Elena Verna、Chamath Palihapitiya、Dave Gerhardt、Rand Fishkin、Satya Nadella、Reed Hastings、Andy Grove、Paul Graham）

**待处理优先级队列：**
- P0: Shreyas Doshi Twitter精华（API配置待定）
- P1: Julie Zhuo、Teresa Torres、Paul Graham、April Dunford、Ben Horowitz、Ray Dalio
- P2: 上述11位已建目录但需完善profile的人物

---

## 持续执行策略

### 执行原则
1. **每次一个人物**：单次执行专注于完成一个人物的一种内容类型
2. **由易到难**：优先处理不需要复杂API的任务（播客、文章、框架）
3. **可追溯**：每次执行记录人物、内容类型、完成度
4. **自动提交**：每个任务完成后自动提交到GitHub

### 任务队列（按执行顺序）

#### Phase 1: P1 现有内容扩充（7人）

每轮处理一个人物的指定内容类型：

| 轮次 | 人物 | 内容类型 | 目标量 |
|------|------|----------|--------|
| 1 | paul-graham | essays | 补充15+篇精选文章 |
| 2 | april-dunford | frameworks | Obviously Awesome完整框架 |
| 3 | ben-horowitz | books | The Hard Thing About Hard Things摘要 |
| 4 | ray-dalio | frameworks | Principles核心框架 |
| 5 | julie-zhuo | podcasts | 整理10+个播客洞察 |
| 6 | teresa-torres | podcasts | 整理10+个播客洞察 |
| 7 | julie-zhuo | frameworks | 补充5+个框架文档 |
| 8 | teresa-torres | frameworks | 补充5+个框架文档 |

#### Phase 2: P2 空档案完善（11人）

每轮完成一个人物的完整profile：

| 轮次 | 人物 | 任务 |
|------|------|------|
| 9 | jackie-bavaro | 完整profile + 初步内容 |
| 10 | john-cutler | 完整profile + 初步内容 |
| 11 | brandon-chu | 完整profile + 初步内容 |
| 12 | elena-verna | 完整profile + 初步内容 |
| 13 | chamath-palihapitiya | 完整profile + 初步内容 |
| 14 | dave-gerhardt | 完整profile + 初步内容 |
| 15 | rand-fishkin | 完整profile + 初步内容 |
| 16 | satya-nadella | 完整profile + 初步内容 |
| 17 | reed-hastings | 完整profile + 初步内容 |
| 18 | andy-grove | 完整profile + 初步内容 |

#### Phase 3: P0 延后任务

- Shreyas Doshi Twitter精华（等待API配置或手动导入）
- Lenny Rachitsky 更多框架（基于281集转录提炼，可并行进行）

#### Phase 4: P3 新增人物

- naval-ravikant、gustaf-alstromer、amanda-natividad 等

---

## 定时任务配置

### 执行频率
- **当前配置**：每小时执行（0 * * * *）
- **建议配置**：每2小时执行（0 */2 * * *）
  - 避免过度消耗token
  - 给每次执行充足时间完成一个完整人物任务
  - 每天约12次执行，可完成更多进度

### 单次任务流程

```python
# 定时任务提示词模板
"""
每次执行时：

1. 读取 COLLECTION_STATUS.md 了解当前进度
2. 读取 EXECUTION_PLAN.md 查看待处理任务队列
3. 执行队列中下一个待完成任务：
   - 通过网络搜索收集该人物的所有公开资源
   - **强制要求：下载并保存原文文件到 media/ 或 files/ 目录**
   - 创建对应类型的内容文件（frameworks/podcasts/articles/books）
   - 每个文件包含：YAML frontmatter + 核心内容 + 原文链接
   - **必须验证：原文文件存在且大小合理（>10KB）**
4. 更新 COLLECTION_STATUS.md 对应人物的数字
5. 记录本次执行到 TASK_LOG.md
6. 提交到GitHub，格式：feat(collection): add {人物名} {内容类型}

执行顺序：严格按照 EXECUTION_PLAN 中的 Phase 1 → 2 → 3 → 4

## 质量检查清单（必须通过）
- [ ] 原文文件已下载到正确目录
- [ ] 原文文件大小合理（>10KB，非空）
- [ ] 索引文件包含 original_file 或 original_urls 字段
- [ ] 来源链接有效且可访问
- [ ] 关键信息有来源标注
- [ ] verification_status 已设置
"""
```

### 原文保存规范（强制执行）

**根据 FILE_STORAGE_POLICY.md，必须执行双轨制：**

#### 1. 播客内容
- 下载 MP3 → `media/audio/{person}/podcast/{date}-show-name.mp3`
- 保存转录 TXT → `media/audio/{person}/podcast/{date}-show-name-transcript.txt`
- 索引文件包含原文链接

#### 2. 文章内容
- 保存 HTML → `files/articles/{person}/{date}-title.html`
- 保存 PDF（如有）→ `files/pdf/{person}/articles/{date}-title.pdf`
- 索引文件包含原文链接

#### 3. 书籍内容
- 保存 EPUB → `media/ebook/{title}.epub`
- 保存 PDF → `files/pdf/{person}/books/{title}.pdf`

#### 4. 索引文件原文链接模板
```markdown
**原文链接**: [查看HTML](../../../files/articles/{person}/{date}-title.html)
**PDF版本**: [下载PDF](../../../files/pdf/{person}/articles/{date}-title.pdf)
**音频文件**: [下载MP3](../../../media/audio/{person}/podcast/{date}-show-name.mp3)
**完整转录**: [查看TXT](../../../media/audio/{person}/podcast/{date}-show-name-transcript.txt)
```

**重要：禁止只保存摘要，必须保存原文文件！**

### 跳过任务条件
如果遇到以下情况，跳过当前人物并记录原因：
- 人物资料极其稀少，搜索无结果
- 需要API认证但未配置（如Twitter）
- 遇到技术障碍无法解决

---

## 任务追踪

每次执行后，在 `TASK_LOG.md` 中记录：

```markdown
| 日期时间 | 人物 | 内容类型 | 状态 | 文件数 | Commit |
|----------|------|----------|------|--------|--------|
| 2026-03-11 18:00 | paul-graham | essays | ✅ | 16 | abc123 |
```

---

## 质量标准

### 内容文件规范

所有新建文件必须包含：
1. **YAML frontmatter**（完整）
   ```yaml
   ---
   type: article/framework/podcast/book
   person: person-name
   title: 文档标题
   date: YYYY-MM-DD
   source: 原始来源URL
   original_file: 原文文件路径（相对路径）
   status: published/draft
   verification_status: reviewed/needs-review
   ---
   ```

2. **核心内容**
   - 框架文档：框架说明 + 应用场景 + 实施步骤
   - 播客文档：嘉宾 + 核心洞察（5-10点） + 时间戳
   - 文章文档：摘要 + 核心观点 + 实践建议
   - 书籍摘要：章节概览 + 核心思想 + 适用场景

3. **原文文件**（必须保存）
   - 播客：保存 MP3 和转录到 `media/audio/{person}/podcast/`
   - 文章：保存 HTML 到 `files/articles/{person}/` 或 PDF 到 `files/pdf/{person}/articles/`
   - 书籍：保存 EPUB 到 `media/ebook/` 或 PDF 到 `files/pdf/{person}/books/`
   - 在索引文件中添加原文链接

4. **来源验证**
   - 所有框架和数字必须来自原始来源
   - 标注来源链接
   - 避免AI幻觉
   - 原文文件是验证来源的关键依据

### 提交规范

```bash
git add .
git commit -m "feat(collection): add {人物名} {内容类型} ({数量})"
git push
```

---

## 监控与调整

### 进度监控
- 每周检查 `COLLECTION_STATUS.md` 完成度
- 每10次执行检查 `TASK_LOG.md` 执行情况

### 必要调整
- 如果某个人物连续跳过2次，考虑移至队列末尾
- 如果某类内容类型耗时过长，考虑拆分任务
- 根据token消耗调整执行频率

---

## 附录：快速参考

### 人物路径对照表

| 人物 | 目录路径 |
|------|----------|
| paul-graham | `people/product/paul-graham/` |
| april-dunford | `people/product/april-dunford/` |
| ben-horowitz | `people/leadership/ben-horowitz/` |
| ray-dalio | `people/leadership/ray-dalio/` |
| julie-zhuo | `people/product/julie-zhuo/` |
| teresa-torres | `people/product/teresa-torres/` |
| jackie-bavaro | `people/product/jackie-bavaro/` |
| john-cutler | `people/product/john-cutler/` |
| brandon-chu | `people/product/brandon-chu/` |
| elena-verna | `people/growth/elena-verna/` |
| chamath-palihapitiya | `people/growth/chamath-palihapitiya/` |
| dave-gerhardt | `people/marketing/dave-gerhardt/` |
| rand-fishkin | `people/marketing/rand-fishkin/` |
| satya-nadella | `people/leadership/satya-nadella/` |
| reed-hastings | `people/leadership/reed-hastings/` |
| andy-grove | `people/leadership/andy-grove/` |

### 质量检查清单

- [ ] YAML frontmatter 完整
- [ ] 文件名符合命名规范（lowercase-with-hyphens）
- [ ] 来源链接已标注
- [ ] verification_status 已设置
- [ ] 无明显的AI幻觉内容
- [ ] 内容达到最低标准要求
