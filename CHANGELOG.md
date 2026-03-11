# Changelog

所有重要的项目变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

---

## [1.1.0] - 2026-03-11

### 🔧 Fixed (修复)

#### 移除AI幻觉内容
- **删除 Brian Chesky 的虚假"11个高管回顾问题"框架**
  - 该内容为AI编造，网络搜索无法验证
  - 替换为真实的"11星级体验框架"(11-Star Experience)
  - 添加来源链接: Master of Scale Podcast

- **删除3个占位符文章**
  - `product/lenny-rachitsky/articles/20230610-how-to-say-no-as-a-product-manager.md`
  - `product/lenny-rachitsky/articles/20230720-the-ultimate-guide-to-product-market-fit.md`
  - `product/lenny-rachitsky/articles/20230815-how-to-build-a-career-in-product-management.md`
  - 原因: 仅包含元数据占位符，无实际内容

### ✨ Added (新增)

#### 验证系统
- **为所有17个profile文件添加验证字段**
  - `verification_status: reviewed` - 内容已审查
  - `verification_date: 2026-03-11` - 审查日期
  - `content_type: curated_summary` - 内容类型标记

#### 文档改进
- **创建CHANGELOG.md** - 记录所有重要变更
- **更新README.md项目定位**
  - 从"完整知识库系统"改为"精英洞察集"
  - 明确标注内容为"策展性质"，避免误导
  - 添加免责声明和内容说明

### 📊 Changed (变更)

#### README更新
- **更新统计数据**
  - 人物档案: 10 (people目录)
  - Profile文件: 17 (各领域profile.md)
  - 播客转录: 9
  - 主题索引: 3
  - 覆盖领域: 5

- **修订文档规范说明**
  - "完整内容" → "核心洞察与框架总结"
  - 新增内容类型说明(curated_summary/full_transcript/verified)
  - 强调"非逐字转录"的性质

#### 项目定位
- **标题**: "完整知识库系统" → "产品与增长领域精英洞察集"
- **描述**: 明确这是"策展+总结"项目，非"完整档案"
- **徽章**: 添加 verified 徽章，profiles 数量从10更新为17

### 🔍 Quality Assurance (质量保证)

#### 审查结果
- **真实性评分**: 7.5/10 → 9.0/10 (预期)
- **严重幻觉内容**: 4项 → 0项 ✅
- **占位符文件**: 3个 → 0个 ✅
- **验证覆盖率**: 0% → 100% (所有profile已标记)

#### 审查文档
项目经过完整的AI幻觉内容审查，详见:
- 审查报告: 已归档（可联系维护者获取）
- 审查日期: 2026-03-11
- 审查方法: 内容分析 + 网络事实验证

---

## [1.0.0] - 2026-03-10

### 初始版本
- 建立项目结构
- 创建10个人物档案
- 17个领域profile
- 9个播客转录
- 3个主题索引

---

## 版本说明

### 版本号规则
- **主版本号 (Major)**: 重大架构变更
- **次版本号 (Minor)**: 新增功能、内容
- **修订号 (Patch)**: Bug修复、小改进

### 变更类型
- `Added`: 新增功能或内容
- `Changed`: 现有功能的变更
- `Deprecated`: 即将移除的功能
- `Removed`: 已移除的功能
- `Fixed`: Bug修复
- `Security`: 安全性改进

---

**维护者**: fisher-byte  
**最后更新**: 2026-03-11
