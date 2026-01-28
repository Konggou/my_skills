# AI Skills 仓库

这个仓库包含用于支持 Skill 功能的 AI 编程助手的用户级技能集合，支持在不同系统（Ubuntu 和 Windows）之间同步技能。支持多种 AI 编程助手工具（如 Cursor、Claude Code、Windsurf 等）。

## 什么是 Skills？

Skills（技能）是一种扩展 AI 编程助手能力的机制，允许开发者创建、分享和使用专门的知识库、工作流程和工具集成。不同的 AI 编程助手可能使用不同的术语（如 Skills、Tools、Plugins 等），但核心概念相似：通过模块化的方式增强 AI 助手的功能。

## 目录结构

```
~/.cursor/skills/  # 或其他 AI 工具的 skills 目录
├── anthropics-skills/          # Git Submodule: Anthropics 官方技能仓库
├── vercel-agent-skills/         # Git Submodule: Vercel Labs 技能仓库
├── skills-updater/              # Git Submodule: 技能更新管理工具
├── external/                    # 外部添加的技能（通过 npx add-skill 等）
│   ├── brainstorming/           # 头脑风暴技能（来源：obra/superpowers）
│   └── vue-best-practices/      # Vue 3 最佳实践（来源：hyf0/vue-skills）
└── custom/                      # 本地创建的技能
    ├── code-review/             # 代码审查技能
    ├── api-design-principles/   # API 设计原则
    ├── project-framework-analyzer/  # 项目框架分析器
    ├── qt-ui-framework/          # Qt UI 框架搭建技能
    └── qt-backend-framework/     # Qt 后端服务框架技能
```

## 技能分类

### 1. Git Submodule 管理的技能（20个，可独立更新）

#### Anthropics 官方技能（16个）

- **来源**: [anthropics/skills](https://github.com/anthropics/skills)
- **位置**: `anthropics-skills/skills/`
- **包括**: algorithmic-art, brand-guidelines, canvas-design, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, webapp-testing, web-artifacts-builder, xlsx

#### Vercel 技能（3个）

- **来源**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **位置**: `vercel-agent-skills/skills/`
- **包括**: claude.ai, react-best-practices, web-design-guidelines

#### Skills Updater（1个）

- **来源**: [yizhiyanhua-ai/skills-updater](https://github.com/yizhiyanhua-ai/skills-updater)
- **位置**: `skills-updater/`
- **描述**: 用于管理和更新技能的实用工具

### 2. 外部添加的技能（2个，在主仓库中管理）

- **brainstorming**
  - **来源**: [obra/superpowers](https://github.com/obra/superpowers)
  - **位置**: `external/brainstorming/`
  - **添加方式**: `npx skills add obra/superpowers`
  - **描述**: 在创意工作前使用，探索用户意图、需求和设计

- **vue-best-practices**
  - **来源**: [hyf0/vue-skills](https://github.com/hyf0/vue-skills)
  - **位置**: `external/vue-best-practices/`
  - **添加方式**: `npx skills add hyf0/vue-skills`
  - **描述**: Vue 3 和 Vue.js 最佳实践，用于 TypeScript、vue-tsc 和 Volar

### 3. 本地创建的技能（5个，在主仓库中管理）

- **code-review** - 代码审查技能
  - **位置**: `custom/code-review/`
  - **描述**: 提供系统化的代码审查工作流程，检查逻辑错误、格式问题、冗余代码、内存/线程泄漏和优化机会

- **api-design-principles** - API 设计原则
  - **位置**: `custom/api-design-principles/`
  - **描述**: 掌握 REST 和 GraphQL API 设计原则，构建直观、可扩展和可维护的 API

- **project-framework-analyzer** - 项目框架分析器
  - **位置**: `custom/project-framework-analyzer/`
  - **描述**: 分析项目框架架构、功能模块和模块间关系的技能

- **qt-ui-framework** - Qt UI 框架搭建技能
  - **位置**: `custom/qt-ui-framework/`
  - **描述**: Qt UI 框架搭建，支持 C++ (Qt Widgets) 和 Python (PyQt5/PyQt6)，遵循前后端分离原则

- **qt-backend-framework** - Qt 后端服务框架技能
  - **位置**: `custom/qt-backend-framework/`
  - **描述**: Qt 后端 Controller-Service-Model 架构，支持 C++ 和 Python，可与 qt-ui-framework 配合使用

## 安装方法

### 基本要求

- Git（用于管理仓库和 Submodule）
- Node.js 和 npm（用于使用 npx 工具添加外部技能）
- 支持 Skill 功能的 AI 编程助手

### 确定 Skills 目录位置

不同 AI 工具的 skills 目录位置可能不同：
- **Cursor**: `~/.cursor/skills` (Linux/Mac) 或 `%USERPROFILE%\.cursor\skills` (Windows)
- **Claude Code**: `~/.codebuddy/skills` (Linux/Mac) 或 `%USERPROFILE%\.codebuddy\skills` (Windows)
- **Windsurf**: `~/.windsurf/skills` (Linux/Mac) 或 `%USERPROFILE%\.windsurf\skills` (Windows)
- **其他工具**: 请查阅相应文档

### 在 Ubuntu/Linux/Mac 上

```bash
# 将 SKILLS_DIR 替换为你的 AI 工具的 skills 目录路径
SKILLS_DIR=~/.cursor/skills  # 或 ~/.codebuddy/skills 等
cd $SKILLS_DIR
git clone https://github.com/Konggou/my_skills.git .
# 初始化并更新 submodule
git submodule update --init --recursive
```

### 在 Windows 上

```powershell
# 将 $SKILLS_DIR 替换为你的 AI 工具的 skills 目录路径
$SKILLS_DIR = "$env:USERPROFILE\.cursor\skills"  # 或 .codebuddy\skills 等
cd $SKILLS_DIR
git clone https://github.com/Konggou/my_skills.git .
# 初始化并更新 submodule
git submodule update --init --recursive
```

### 配置 AI 编程助手

不同的 AI 编程助手可能有不同的配置方式。通常需要将技能目录添加到助手的配置中。

#### 示例：Cursor

在 Cursor 中，技能通常位于 `~/.cursor/skills/` 目录。你可以：

1. **创建符号链接**（推荐）：
   ```bash
   # Linux/macOS
   ln -s /path/to/my_skills/anthropics-skills/skills ~/.cursor/skills/anthropics-skills
   ln -s /path/to/my_skills/vercel-agent-skills/skills ~/.cursor/skills/vercel-agent-skills
   ln -s /path/to/my_skills/external ~/.cursor/skills/external
   ln -s /path/to/my_skills/custom ~/.cursor/skills/custom
   
   # Windows (PowerShell)
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.cursor\skills\anthropics-skills" -Target "C:\path\to\my_skills\anthropics-skills\skills"
   ```

2. **直接复制**（如果符号链接不支持）：
   ```bash
   cp -r anthropics-skills/skills/* ~/.cursor/skills/
   cp -r vercel-agent-skills/skills/* ~/.cursor/skills/
   cp -r external/* ~/.cursor/skills/
   cp -r custom/* ~/.cursor/skills/
   ```

#### 示例：其他 AI 编程助手

请参考你使用的 AI 编程助手的官方文档，了解如何配置技能目录。大多数助手支持：
- 递归查找子目录中的技能
- 通过配置文件指定技能路径
- 自动发现符合特定格式的技能目录

## 更新技能

### 更新所有 Submodule

```bash
cd $SKILLS_DIR  # 你的 skills 目录
git submodule update --remote --merge
```

### 更新特定的 Submodule

```bash
# 更新 Anthropics 官方技能
cd $SKILLS_DIR/anthropics-skills
git pull origin main
cd $SKILLS_DIR
git add anthropics-skills
git commit -m "更新 Anthropics 技能"

# 更新 Vercel 技能
cd $SKILLS_DIR/vercel-agent-skills
git pull origin main
cd $SKILLS_DIR
git add vercel-agent-skills
git commit -m "更新 Vercel 技能"

# 更新 Skills Updater
cd $SKILLS_DIR/skills-updater
git pull origin main
cd $SKILLS_DIR
git add skills-updater
git commit -m "更新 Skills Updater"
```

### 更新本地技能（在主仓库中管理）

```bash
cd $SKILLS_DIR
git pull origin main
```

### 提交 Submodule 更新

更新 Submodule 后，需要提交主仓库以记录新的 Submodule 版本：

```bash
git add anthropics-skills vercel-agent-skills skills-updater
git commit -m "更新技能 Submodule"
git push
```

## 技能管理说明

### Git Submodule（可独立更新）

以下技能使用 Git Submodule 管理，保留自己的 Git 仓库，可以独立更新：

- **anthropics-skills/** - Anthropics 官方技能仓库
- **vercel-agent-skills/** - Vercel Labs 技能仓库
- **skills-updater/** - 技能更新管理工具

### 文件夹组织

- **external/** - 存放从外部来源添加的技能（通过 `npx skills add` 等工具）
- **custom/** - 存放本地创建的技能

大多数支持 skills 的 AI 工具都会递归查找子目录中的技能，因此不需要符号链接即可识别 `external/` 和 `custom/` 目录中的技能。

### 添加新技能

#### 从外部源添加

使用 `npx skills add` 工具：

```bash
npx skills add <repository-url-or-name>
```

例如：
```bash
npx skills add obra/superpowers
npx skills add hyf0/vue-skills
```

#### 创建本地技能

1. 在 `custom/` 目录下创建新文件夹
2. 按照你使用的 AI 编程助手的技能格式要求创建 `SKILL.md` 文件
3. 参考现有技能的结构和格式

## 实用工具

### `move_skills.py`

此脚本用于整理技能目录，将分散在各子目录（如 `anthropics-skills/skills`, `custom/` 等）中的技能移动到根技能目录 (`~/.trae/skills`)。这对于一些不支持递归搜索技能的 AI 助手非常有用。

**用法**:

```bash
python move_skills.py
```

脚本会自动检测操作系统并找到正确的技能根目录。

## 跨工具使用

本技能集合设计为通用格式，可以在多个 AI 编程助手工具之间共享：

1. **符号链接方式**（推荐，避免重复存储）：
   ```bash
   # Linux/Mac 示例：将一份技能集用于多个工具
   ln -s ~/.cursor/skills ~/.codebuddy/skills
   ln -s ~/.cursor/skills ~/.windsurf/skills
   ```

   ```powershell
   # Windows 示例（需要管理员权限）
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.codebuddy\skills" -Target "$env:USERPROFILE\.cursor\skills"
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.windsurf\skills" -Target "$env:USERPROFILE\.cursor\skills"
   ```

2. **多仓库克隆方式**（如果不支持符号链接）：
   ```bash
   # 在每个工具的 skills 目录下克隆
   cd ~/.cursor/skills && git clone https://github.com/Konggou/my_skills.git .
   cd ~/.codebuddy/skills && git clone https://github.com/Konggou/my_skills.git .
   ```

## 注意事项

- 更新 submodule 后需要提交主仓库以记录新的 submodule 版本
- 大多数 AI 工具会自动递归查找子目录中的技能，无需符号链接
- 不同 AI 工具可能对技能格式有轻微差异，使用前请参考各工具文档
- 使用符号链接方式时，在一个工具中更新技能会自动同步到其他工具
- 建议定期更新 Submodule 以获取最新功能和修复

## 技能统计

- **Git Submodule**: 20 个（Anthropics 16 + Vercel 3 + Skills Updater 1）
- **外部添加**: 2 个（brainstorming, vue-best-practices）
- **本地创建**: 5 个（code-review, api-design-principles, project-framework-analyzer, qt-ui-framework, qt-backend-framework）

**总计：27 个技能**

## 兼容性

本技能仓库兼容以下 AI 编程助手：

- ✅ Cursor
- ✅ CodeBuddy Code / Claude Code
- ✅ Windsurf
- ✅ 其他支持类似技能格式的 AI 助手

> **注意**: 不同 AI 编程助手可能使用不同的技能格式和配置方式。本仓库主要遵循 Cursor 和 Claude 的技能格式规范，但结构设计通用，可以适配其他支持类似机制的 AI 助手。

## 贡献

欢迎贡献新的技能或改进现有技能！请遵循以下步骤：

1. Fork 本仓库
2. 创建你的功能分支 (`git checkout -b feature/AmazingSkill`)
3. 提交你的更改 (`git commit -m 'Add some AmazingSkill'`)
4. 推送到分支 (`git push origin feature/AmazingSkill`)
5. 开启 Pull Request

## 相关链接

- **本仓库**: [https://github.com/Konggou/my_skills](https://github.com/Konggou/my_skills)
- **Anthropics Skills**: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)
- **Vercel Agent Skills**: [https://github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **Skills Updater**: [https://github.com/yizhiyanhua-ai/skills-updater](https://github.com/yizhiyanhua-ai/skills-updater)
- **Cursor Skills 文档**: [https://docs.cursor.com](https://docs.cursor.com)

## 许可证

本仓库中的技能可能使用不同的许可证。请查看各个技能目录中的 LICENSE 文件了解详情。
