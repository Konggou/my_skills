---
name: project-framework-analyzer
description: Analyze project architecture, functional modules, and their relationships. Use when users need to understand project structure, analyze code architecture, identify module responsibilities, map dependencies, or generate framework diagrams. Applicable to any codebase (Python, TypeScript, Vue, C++, ROS2, etc.) to quickly grasp overall architecture and design patterns.
---

# Project Framework Analyzer

## Overview

This skill provides a systematic framework analysis workflow to understand a project’s overall architecture, functional modules, and inter-module relationships, and to generate visual framework diagrams.

## Analysis Workflow

### Step 1: Project Structure Exploration

1. **Identify the project root and key directories**
   - Use `list_dir` to inspect the root directory
   - Identify frontend/backend directories, config files, docs directories
   - Note `.gitignore`, `package.json`, `requirements.txt`, etc.

2. **Identify the tech stack**
   - Check dependency files (`package.json`, `requirements.txt`, `CMakeLists.txt`, etc.)
   - Identify major frameworks and libraries (Vue, React, Flask, ROS2, etc.)
   - Identify programming languages (Python, TypeScript, C++, etc.)

3. **Understand project organization patterns**
   - Identify layered architectures (frontend/backend split, MVC, microservices, etc.)
   - Identify module organization style (by feature, layer, or domain)

### Step 2: Architecture Analysis

1. **Identify core architectural patterns**
   - Client-server architecture
   - Frontend-backend separation
   - Microservices architecture
   - Event-driven architecture
   - ROS2 node architecture

2. **Identify major component layers**
   - Frontend layer: UI components, state management, routing
   - Backend layer: APIs, business logic, data access
   - Communication layer: WebSocket, REST APIs, ROS2 Topics
   - Infrastructure layer: databases, filesystem, external services

3. **Analyze dependencies**
   - Use `codebase_search` to find imports/dependencies
   - Identify module import relationships
   - Identify service call relationships

### Step 3: Functional Module Analysis

1. **Identify functional modules**
   - Use directory structure to identify module boundaries
   - Use API routes to identify functional domains
   - Use component/class names to infer responsibilities

2. **Analyze each module’s behavior**
   - Read key files in the module
   - Identify module inputs and outputs
   - Identify core functionality
   - Identify dependencies and dependents

3. **Record module information**
   - Module name and location
   - Main responsibilities
   - Key classes and functions
   - Dependencies
   - Dependents

### Step 4: Connect Module Relationships

1. **Build a dependency graph**
   - Map direct dependencies between modules
   - Identify cyclic dependencies (if any)
   - Identify core vs. peripheral modules

2. **Identify data flow**
   - Frontend-to-backend data flow
   - Backend internal data flow
   - Event/message propagation paths

3. **Identify control flow**
   - User interaction → system response
   - Business process execution paths
   - Error handling flows

### Step 5: Generate Framework Diagrams

1. **Choose diagram types**
   - **Architecture diagram**: overall system structure and layers
   - **Module relationship diagram**: dependencies between modules
   - **Data flow diagram**: data movement across the system
   - **Component diagram**: interactions between components

2. **Generate diagrams using Mermaid**
   - Refer to `assets/framework-diagram-template.md`
   - Use flowcharts, class diagrams, component diagrams, etc.
   - Keep diagrams clear and layered

3. **Produce the analysis report**
   - Project overview
   - Architecture summary
   - Functional module list
   - Module relationship summary
   - Framework diagrams

## Analysis Tips

### Code Search Strategy

- Use `codebase_search` for semantic search
- Use `grep` to find specific imports, class names, function names
- Use `read_file` to inspect critical files

### Module Identification Patterns

- **By directory structure**: `src/components/`, `src/api/`, `server/api/`, etc.
- **By naming conventions**: `*Controller`, `*Service`, `*Module`, etc.
- **By config files**: routing configs, API endpoint definitions

### Dependency Identification

- Inspect `import`/`require` statements
- Inspect API calls
- Inspect dependency declarations in config files
- Inspect WebSocket event subscriptions

## Output Format

### Analysis Report Structure

```markdown
# [Project Name] Framework Analysis Report

## 1. Project Overview
- Project type: [frontend/backend/full-stack/ROS2/etc]
- Tech stack: [list main technologies]
- Project structure: [brief directory summary]

## 2. Architecture Analysis
- Architecture pattern: [client-server/microservices/event-driven/etc]
- Major layers: [list layers]
- Communication: [REST/WebSocket/ROS2 Topics/etc]

## 3. Functional Modules
### Module 1: [Module Name]
- Location: [file path]
- Responsibility: [description]
- Dependencies: [modules depended on]
- Dependents: [modules depending on this]

### Module 2: [Module Name]
...

## 4. Module Relationship Diagram
[Mermaid diagram]

## 5. System Architecture Diagram
[Mermaid diagram]
```

## References

- **Analysis patterns**: see `references/analysis-patterns.md`
- **Diagram templates**: see `assets/framework-diagram-template.md`

## Notes

1. **Progressive analysis**: start broad, then deep
2. **Multi-angle validation**: validate via code, config, and docs
3. **Focus on critical paths**: prioritize core flows and modules
4. **Keep it concise**: diagrams should be clear and minimal
5. **English output**: write reports and explanations in English
