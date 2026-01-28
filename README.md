# AI Skills Repository

This repository contains a collection of user-level skills for AI programming assistants that support the Skill feature. It supports syncing skills across different systems (Ubuntu and Windows) and is compatible with various AI programming assistant tools (such as Cursor, Claude Code, Windsurf, etc.).

## What are Skills?

Skills are a mechanism for extending the capabilities of AI programming assistants, allowing developers to create, share, and use specialized knowledge bases, workflows, and tool integrations. Different AI programming assistants may use different terms (such as Skills, Tools, Plugins, etc.), but the core concept is similar: enhancing the functionality of the AI assistant in a modular way.

## Directory Structure

```
~/.cursor/skills/  # Or the skills directory of other AI tools
├── anthropics-skills/          # Git Submodule: Official Anthropics Skills Repository
├── vercel-agent-skills/         # Git Submodule: Vercel Labs Skills Repository
├── skills-updater/              # Git Submodule: Skill Update Management Tool
├── external/                    # Externally added skills (e.g., via npx add-skill)
│   ├── brainstorming/           # Brainstorming skill (Source: obra/superpowers)
│   └── vue-best-practices/      # Vue 3 best practices (Source: hyf0/vue-skills)
└── custom/                      # Locally created skills
    ├── code-review/             # Code review skill
    ├── api-design-principles/   # API design principles skill
    ├── project-framework-analyzer/  # Project framework analyzer skill
    ├── qt-ui-framework/          # Qt UI framework setup skill
    └── qt-backend-framework/     # Qt backend service framework skill
```

## Skill Categories

### 1. Skills Managed by Git Submodule (20, can be updated independently)

#### Official Anthropics Skills (16)

- **Source**: [anthropics/skills](https://github.com/anthropics/skills)
- **Location**: `anthropics-skills/skills/`
- **Includes**: algorithmic-art, brand-guidelines, canvas-design, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, webapp-testing, web-artifacts-builder, xlsx

#### Vercel Skills (3)

- **Source**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **Location**: `vercel-agent-skills/skills/`
- **Includes**: claude.ai, react-best-practices, web-design-guidelines

#### Skills Updater (1)

- **Source**: [yizhiyanhua-ai/skills-updater](https://github.com/yizhiyanhua-ai/skills-updater)
- **Location**: `skills-updater/`
- **Description**: A utility for managing and updating skills.

### 2. Externally Added Skills (2, managed in the main repository)

- **brainstorming**
  - **Source**: [obra/superpowers](https://github.com/obra/superpowers)
  - **Location**: `external/brainstorming/`
  - **How to add**: `npx skills add obra/superpowers`
  - **Description**: Used before creative work to explore user intent, needs, and design.

- **vue-best-practices**
  - **Source**: [hyf0/vue-skills](https://github.com/hyf0/vue-skills)
  - **Location**: `external/vue-best-practices/`
  - **How to add**: `npx skills add hyf0/vue-skills`
  - **Description**: Best practices for Vue 3 and Vue.js, for use with TypeScript, vue-tsc, and Volar.

### 3. Locally Created Skills (5, managed in the main repository)

- **code-review** - Code Review Skill
  - **Location**: `custom/code-review/`
  - **Description**: Provides a systematic code review workflow, checking for logic errors, formatting issues, redundant code, memory/thread leaks, and optimization opportunities.

- **api-design-principles** - API Design Principles Skill
  - **Location**: `custom/api-design-principles/`
  - **Description**: Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs.

- **project-framework-analyzer** - Project Framework Analyzer Skill
  - **Location**: `custom/project-framework-analyzer/`
  - **Description**: A skill for analyzing project framework architecture, functional modules, and the relationships between modules.

- **qt-ui-framework** - Qt UI Framework Setup Skill
  - **Location**: `custom/qt-ui-framework/`
  - **Description**: Qt UI framework setup, supporting C++ (Qt Widgets) and Python (PyQt5/PyQt6), following the principle of frontend-backend separation.

- **qt-backend-framework** - Qt Backend Service Framework Skill
  - **Location**: `custom/qt-backend-framework/`
  - **Description**: Qt backend Controller-Service-Model architecture, supporting C++ and Python, can be used with qt-ui-framework.

## Installation

### Prerequisites

- Git (for managing repositories and submodules)
- Node.js and npm (for adding external skills with npx)
- An AI programming assistant that supports the Skill feature

### Determine the Skills Directory Location

The skills directory location may vary for different AI tools:
- **Cursor**: `~/.cursor/skills` (Linux/Mac) or `%USERPROFILE%\.cursor\skills` (Windows)
- **Claude Code**: `~/.codebuddy/skills` (Linux/Mac) or `%USERPROFILE%\.codebuddy\skills` (Windows)
- **Windsurf**: `~/.windsurf/skills` (Linux/Mac) or `%USERPROFILE%\.windsurf\skills` (Windows)
- **Other tools**: Please refer to the respective documentation.

### On Ubuntu/Linux/Mac

```bash
# Replace SKILLS_DIR with the path to your AI tool's skills directory
SKILLS_DIR=~/.cursor/skills  # or ~/.codebuddy/skills, etc.
cd $SKILLS_DIR
git clone https://github.com/Konggou/my_skills.git .
# Initialize and update submodules
git submodule update --init --recursive
```

### On Windows

```powershell
# Replace $SKILLS_DIR with the path to your AI tool's skills directory
$SKILLS_DIR = "$env:USERPROFILE\.cursor\skills"  # or .codebuddy\skills, etc.
cd $SKILLS_DIR
git clone https://github.com/Konggou/my_skills.git .
# Initialize and update submodules
git submodule update --init --recursive
```

### Configure the AI Programming Assistant

Different AI programming assistants may have different configuration methods. Usually, you need to add the skills directory to the assistant's configuration.

#### Example: Cursor

In Cursor, skills are typically located in the `~/.cursor/skills/` directory. You can:

1. **Create Symbolic Links** (Recommended):
   ```bash
   # Linux/macOS
   ln -s /path/to/my_skills/anthropics-skills/skills ~/.cursor/skills/anthropics-skills
   ln -s /path/to/my_skills/vercel-agent-skills/skills ~/.cursor/skills/vercel-agent-skills
   ln -s /path/to/my_skills/external ~/.cursor/skills/external
   ln -s /path/to/my_skills/custom ~/.cursor/skills/custom
   
   # Windows (PowerShell)
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.cursor\skills\anthropics-skills" -Target "C:\path\to\my_skills\anthropics-skills\skills"
   ```

2. **Direct Copy** (if symbolic links are not supported):
   ```bash
   cp -r anthropics-skills/skills/* ~/.cursor/skills/
   cp -r vercel-agent-skills/skills/* ~/.cursor/skills/
   cp -r external/* ~/.cursor/skills/
   cp -r custom/* ~/.cursor/skills/
   ```

#### Example: Other AI Programming Assistants

Please refer to the official documentation of the AI programming assistant you are using to learn how to configure the skills directory. Most assistants support:
- Recursive search for skills in subdirectories
- Specifying skill paths via a configuration file
- Automatic discovery of skill directories that match a specific format

## Updating Skills

### Update All Submodules

```bash
cd $SKILLS_DIR  # Your skills directory
git submodule update --remote --merge
```

### Update a Specific Submodule

```bash
# Update Official Anthropics Skills
cd $SKILLS_DIR/anthropics-skills
git pull origin main
cd $SKILLS_DIR
git add anthropics-skills
git commit -m "Update Anthropics skills"

# Update Vercel Skills
cd $SKILLS_DIR/vercel-agent-skills
git pull origin main
cd $SKILLS_DIR
git add vercel-agent-skills
git commit -m "Update Vercel skills"

# Update Skills Updater
cd $SKILLS_DIR/skills-updater
git pull origin main
cd $SKILLS_DIR
git add skills-updater
git commit -m "Update Skills Updater"
```

### Update Local Skills (managed in the main repository)

```bash
cd $SKILLS_DIR
git pull origin main
```

### Commit Submodule Updates

After updating submodules, you need to commit the main repository to record the new submodule versions:

```bash
git add anthropics-skills vercel-agent-skills skills-updater
git commit -m "Update skill submodules"
git push
```

## Skill Management Notes

### Git Submodules (can be updated independently)

The following skills are managed using Git Submodules, retaining their own Git repositories and can be updated independently:

- **anthropics-skills/** - Official Anthropics Skills Repository
- **vercel-agent-skills/** - Vercel Labs Skills Repository
- **skills-updater/** - Skill Update Management Tool

### Folder Organization

- **external/** - For skills added from external sources (e.g., via `npx skills add`)
- **custom/** - For locally created skills

Most AI tools that support skills will recursively search for skills in subdirectories, so symbolic links are not needed to recognize skills in the `external/` and `custom/` directories.

### Adding New Skills

#### Add from an External Source

Use the `npx skills add` tool:

```bash
npx skills add <repository-url-or-name>
```

For example:
```bash
npx skills add obra/superpowers
npx skills add hyf0/vue-skills
```

#### Create a Local Skill

1. Create a new folder in the `custom/` directory.
2. Create a `SKILL.md` file according to the skill format requirements of your AI programming assistant.
3. Refer to the structure and format of existing skills.

## Utilities

### `move_skills.py`

This script is used to organize the skills directory by moving skills from various subdirectories (e.g., `anthropics-skills/skills`, `custom/`) to the root skills directory (`~/.trae/skills`). This is useful for AI assistants that do not support recursive skill searching.

**Usage**:

```bash
python move_skills.py
```

The script will automatically detect the operating system and find the correct root skills directory.

## Cross-Tool Usage

This skill collection is designed in a universal format and can be shared among multiple AI programming assistant tools:

1. **Symbolic Link Method** (Recommended, avoids duplicate storage):
   ```bash
   # Linux/Mac Example: Use one skill set for multiple tools
   ln -s ~/.cursor/skills ~/.codebuddy/skills
   ln -s ~/.cursor/skills ~/.windsurf/skills
   ```

   ```powershell
   # Windows Example (requires administrator privileges)
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.codebuddy\skills" -Target "$env:USERPROFILE\.cursor\skills"
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.windsurf\skills" -Target "$env:USERPROFILE\.cursor\skills"
   ```

2. **Multiple Repository Clone Method** (if symbolic links are not supported):
   ```bash
   # Clone in each tool's skills directory
   cd ~/.cursor/skills && git clone https://github.com/Konggou/my_skills.git .
   cd ~/.codebuddy/skills && git clone https://github.com/Konggou/my_skills.git .
   ```

## Notes

- After updating submodules, you need to commit the main repository to record the new submodule versions.
- Most AI tools automatically search for skills in subdirectories recursively, no symbolic links needed.
- Different AI tools may have slight differences in skill format; please refer to each tool's documentation before use.
- When using the symbolic link method, updating a skill in one tool will automatically sync it to others.
- It is recommended to update submodules regularly to get the latest features and fixes.

## Skill Statistics

- **Git Submodules**: 20 (Anthropics 16 + Vercel 3 + Skills Updater 1)
- **Externally Added**: 2 (brainstorming, vue-best-practices)
- **Locally Created**: 5 (code-review, api-design-principles, project-framework-analyzer, qt-ui-framework, qt-backend-framework)

**Total: 27 Skills**

## Compatibility

This skill repository is compatible with the following AI programming assistants:

- ✅ Cursor
- ✅ CodeBuddy Code / Claude Code
- ✅ Windsurf
- ✅ Other AI assistants that support a similar skill format

> **Note**: Different AI programming assistants may use different skill formats and configuration methods. This repository primarily follows the skill format specifications of Cursor and Claude, but its structure is designed to be universal and can be adapted to other AI assistants that support similar mechanisms.

## Contributing

Contributions of new skills or improvements to existing ones are welcome! Please follow these steps:

1. Fork this repository.
2. Create your feature branch (`git checkout -b feature/AmazingSkill`).
3. Commit your changes (`git commit -m 'Add some AmazingSkill'`).
4. Push to the branch (`git push origin feature/AmazingSkill`).
5. Open a Pull Request.

## Related Links

- **This Repository**: [https://github.com/Konggou/my_skills](https://github.com/Konggou/my_skills)
- **Anthropics Skills**: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)
- **Vercel Agent Skills**: [https://github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **Skills Updater**: [https://github.com/yizhiyanhua-ai/skills-updater](https://github.com/yizhiyanhua-ai/skills-updater)
- **Cursor Skills Documentation**: [https://docs.cursor.com](https://docs.cursor.com)

## License

The skills in this repository may use different licenses. Please check the LICENSE files in the individual skill directories for details.
