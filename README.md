# My Cursor Skills

这个仓库包含我在 Cursor 中使用的所有用户级技能，用于在不同系统（Ubuntu 和 Windows）之间同步技能。

## 目录结构

```
~/.cursor/skills/
├── anthropics-skills/          # Git Submodule: Anthropics 官方技能仓库
├── vercel-agent-skills/         # Git Submodule: Vercel Labs 技能仓库
├── skills-updater/              # Git Submodule: 技能更新管理工具
├── external/                    # 外部添加的技能（通过 npx add-skill 等）
│   └── vue-best-practices/      # Vue 3 最佳实践（来源：hyf0/vue-skills）
└── custom/                      # 本地创建的技能
    ├── code-review/             # 代码审查技能
    ├── api-design-principles/   # API 设计原则
    └── project-framework-analyzer/  # 项目框架分析器
```

## 技能分类

### 1. Git Submodule 管理的技能（20个，可独立更新）

#### Anthropics 官方技能（16个）
- 来源：`https://github.com/anthropics/skills.git`
- 位置：`anthropics-skills/skills/`
- 包括：algorithmic-art, brand-guidelines, canvas-design, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, webapp-testing, web-artifacts-builder, xlsx

#### Vercel 技能（3个）
- 来源：`https://github.com/vercel-labs/agent-skills.git`
- 位置：`vercel-agent-skills/skills/`
- 包括：claude.ai, react-best-practices, web-design-guidelines

#### Skills Updater（1个）
- 来源：`https://github.com/yizhiyanhua-ai/skills-updater.git`
- 位置：`skills-updater/`

### 2. 外部添加的技能（1个，在主仓库中管理）

- **vue-best-practices**
  - 来源：`hyf0/vue-skills`
  - 添加方式：`npx add-skill hyf0/vue-skills`
  - 位置：`external/vue-best-practices/`

### 3. 本地创建的技能（3个，在主仓库中管理）

- **code-review** - 代码审查技能
  - 位置：`custom/code-review/`

- **api-design-principles** - API 设计原则
  - 位置：`custom/api-design-principles/`

- **project-framework-analyzer** - 项目框架分析器
  - 位置：`custom/project-framework-analyzer/`

## 安装方法

### 在 Ubuntu/Linux 上
```bash
cd ~/.cursor/skills
git clone https://github.com/Konggou/my_skills.git .
# 初始化并更新 submodule
git submodule update --init --recursive
```

### 在 Windows 上
```powershell
cd $env:USERPROFILE\.cursor\skills
git clone https://github.com/Konggou/my_skills.git .
# 初始化并更新 submodule
git submodule update --init --recursive
```

## 更新技能

### 更新所有 Submodule
```bash
cd ~/.cursor/skills
git submodule update --remote --merge
```

### 更新特定的 Submodule
```bash
# 更新 Anthropics 官方技能
cd ~/.cursor/skills/anthropics-skills
git pull origin main
cd ~/.cursor/skills
git add anthropics-skills
git commit -m "更新 Anthropics 技能"

# 更新 Vercel 技能
cd ~/.cursor/skills/vercel-agent-skills
git pull origin main
cd ~/.cursor/skills
git add vercel-agent-skills
git commit -m "更新 Vercel 技能"

# 更新 Skills Updater
cd ~/.cursor/skills/skills-updater
git pull origin main
cd ~/.cursor/skills
git add skills-updater
git commit -m "更新 Skills Updater"
```

### 更新本地技能（在主仓库中管理）
```bash
cd ~/.cursor/skills
git pull origin main
```

## 技能管理说明

### Git Submodule（可独立更新）
以下技能使用 Git Submodule 管理，保留自己的 Git 仓库，可以独立更新：

- `anthropics-skills` - Anthropics 官方技能仓库
- `vercel-agent-skills` - Vercel Labs 技能仓库
- `skills-updater` - 技能更新管理工具

### 文件夹组织
- **external/** - 存放从外部来源添加的技能（通过 npx add-skill 等）
- **custom/** - 存放本地创建的技能

Cursor 支持递归查找子目录中的技能，因此不需要符号链接即可识别 `external/` 和 `custom/` 目录中的技能。

## 注意事项

- 更新 submodule 后需要提交主仓库以记录新的 submodule 版本
- Cursor 会自动递归查找子目录中的技能，无需符号链接

## 技能统计

- **Git Submodule**: 20 个（Anthropics 16 + Vercel 3 + Skills Updater 1）
- **外部添加**: 1 个（vue-best-practices）
- **本地创建**: 3 个（code-review, api-design-principles, project-framework-analyzer）

**总计：24 个技能**
