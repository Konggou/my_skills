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
```

### 在 Windows 上
```powershell
cd $env:USERPROFILE\.cursor\skills
git clone https://github.com/Konggou/my_skills.git .
```

## 更新技能

```bash
cd ~/.cursor/skills
git pull origin main
```

## 注意事项

- 某些技能（frontend-design, skill-creator, skills-updater）已配置独立的 Git 连接，可以单独更新
- 符号链接的技能已转换为实际目录以便跨平台同步
- 如果某个技能有独立的 Git 仓库，其 `.git` 目录已被排除

## 技能来源

- **Anthropics 官方**: frontend-design, skill-creator
- **第三方**: skills-updater (yizhiyanhua-ai), vue-best-practices (hyf0), vercel-react-best-practices (vercel-labs)
- **本地创建**: code-review, api-design-principles
