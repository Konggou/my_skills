# My Cursor Skills

这个仓库包含我在 Cursor 中使用的所有用户级技能，用于在不同系统（Ubuntu 和 Windows）之间同步技能。

## 技能列表

### 代码质量
- **code-review** - 代码审查技能，提供系统化的代码审查工作流程
- **api-design-principles** - API 设计原则，涵盖 REST 和 GraphQL 设计

### 前端开发
- **vue-best-practices** - Vue 3 和 Vue.js 最佳实践（TypeScript, vue-tsc, Volar）
- **vercel-react-best-practices** - React 和 Next.js 性能优化指南
- **frontend-design** - 前端设计指南（Anthropics 官方）
- **web-design-guidelines** - Web 设计指南

### 工具类
- **skill-creator** - 技能创建工具（Anthropics 官方）
- **skills-updater** - 技能更新管理工具

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

### 更新主仓库和所有 submodule
```bash
cd ~/.cursor/skills
git pull origin main
git submodule update --remote --merge
```

### 更新特定的 submodule
```bash
# 更新 Anthropics 官方技能（frontend-design, skill-creator）
cd ~/.cursor/skills/anthropics-skills
git pull origin main
cd ~/.cursor/skills
git add anthropics-skills
git commit -m "更新 Anthropics 技能"

# 更新 Vercel 技能（vercel-react-best-practices, web-design-guidelines）
cd ~/.cursor/skills/vercel-agent-skills
git pull origin main
cd ~/.cursor/skills
git add vercel-agent-skills
git commit -m "更新 Vercel 技能"
```

### 更新本地技能（在主仓库中管理）
```bash
cd ~/.cursor/skills
git pull origin main
```

## 技能管理方式

### Git Submodule（可独立更新）
以下技能使用 Git Submodule 管理，保留自己的 Git 仓库，可以独立更新：

- **frontend-design** → `anthropics-skills/skills/frontend-design` (符号链接)
- **skill-creator** → `anthropics-skills/skills/skill-creator` (符号链接)
- **vercel-react-best-practices** → `vercel-agent-skills/skills/react-best-practices` (符号链接)
- **web-design-guidelines** → `vercel-agent-skills/skills/web-design-guidelines` (符号链接)

**Submodule 仓库：**
- `anthropics-skills` - Anthropics 官方技能仓库
- `vercel-agent-skills` - Vercel Labs 技能仓库

### 本地管理（在主仓库中）
以下技能直接在主仓库中管理，通过 `git pull` 同步：

- **code-review** - 代码审查技能
- **api-design-principles** - API 设计原则
- **vue-best-practices** - Vue 3 最佳实践
- **skills-updater** - 技能更新管理工具

## 技能来源

- **Anthropics 官方**: frontend-design, skill-creator (通过 submodule)
- **Vercel Labs**: vercel-react-best-practices, web-design-guidelines (通过 submodule)
- **第三方**: vue-best-practices, skills-updater (本地管理)
- **本地创建**: code-review, api-design-principles (本地管理)

## 注意事项

- 符号链接的技能指向 submodule 中的实际目录，确保跨平台兼容性
- 更新 submodule 后需要提交主仓库以记录新的 submodule 版本
- 如果需要在 Windows 上使用，确保 Git 配置支持符号链接（需要管理员权限或启用 `core.symlinks=true`）
