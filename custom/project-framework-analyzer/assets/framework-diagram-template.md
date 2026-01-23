# 框架图模板

本文档提供 Mermaid 图表模板，用于生成项目框架图。

## 架构图模板

### 分层架构图

```mermaid
graph TB
    subgraph "前端层"
        A[UI 组件]
        B[状态管理]
        C[路由]
    end
    
    subgraph "API 层"
        D[REST API]
        E[WebSocket]
    end
    
    subgraph "业务逻辑层"
        F[服务1]
        G[服务2]
    end
    
    subgraph "数据层"
        H[数据库]
        I[文件系统]
    end
    
    A --> D
    B --> D
    C --> D
    A --> E
    D --> F
    D --> G
    F --> H
    G --> I
```

### 模块关系图

```mermaid
graph LR
    A[模块A] --> B[模块B]
    A --> C[模块C]
    B --> D[模块D]
    C --> D
    D --> E[模块E]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#fff4e1
    style D fill:#ffe1f5
    style E fill:#e1ffe1
```

### 组件交互图

```mermaid
sequenceDiagram
    participant U as 用户
    participant F as 前端
    participant A as API
    participant B as 业务逻辑
    participant D as 数据库
    
    U->>F: 操作
    F->>A: HTTP 请求
    A->>B: 调用服务
    B->>D: 查询数据
    D-->>B: 返回数据
    B-->>A: 返回结果
    A-->>F: JSON 响应
    F-->>U: 更新界面
```

## ROS2 节点图模板

```mermaid
graph TB
    subgraph "ROS2 节点"
        N1[节点1<br/>Publisher]
        N2[节点2<br/>Subscriber]
        N3[节点3<br/>Service]
    end
    
    subgraph "话题/服务"
        T1[话题1]
        S1[服务1]
    end
    
    subgraph "外部系统"
        API[后端 API]
    end
    
    N1 -->|发布| T1
    T1 -->|订阅| N2
    N3 -->|调用| S1
    N2 -->|HTTP| API
```

## 数据流图模板

```mermaid
flowchart LR
    A[数据源] -->|数据输入| B[处理模块1]
    B -->|处理后数据| C[处理模块2]
    C -->|最终数据| D[数据输出]
    
    E[配置] -.->|配置| B
    E -.->|配置| C
```

## 微服务架构图模板

```mermaid
graph TB
    subgraph "API 网关"
        GW[Gateway]
    end
    
    subgraph "微服务"
        S1[服务1]
        S2[服务2]
        S3[服务3]
    end
    
    subgraph "基础设施"
        DB[(数据库)]
        MQ[消息队列]
    end
    
    GW --> S1
    GW --> S2
    GW --> S3
    S1 --> DB
    S2 --> DB
    S1 --> MQ
    S2 --> MQ
    S3 --> MQ
```

## 类图模板

```mermaid
classDiagram
    class Controller {
        +handleRequest()
        +validateInput()
    }
    
    class Service {
        +processData()
        +businessLogic()
    }
    
    class Repository {
        +save()
        +find()
    }
    
    Controller --> Service
    Service --> Repository
```

## 使用说明

1. **选择合适的图表类型**
   - 架构图：展示系统整体结构
   - 模块关系图：展示模块依赖
   - 序列图：展示交互流程
   - 数据流图：展示数据处理流程

2. **自定义样式**
   - 使用 `style` 为节点添加颜色
   - 使用不同的箭头类型表示不同的关系
   - 使用子图组织相关节点

3. **保持简洁**
   - 避免在一个图中包含过多节点
   - 使用分层或分组组织复杂结构
   - 突出关键路径和核心模块

4. **中文标注**
   - 所有节点和关系使用中文标注
   - 确保图表易于理解

## Mermaid 语法参考

- **流程图**：`graph TB`（从上到下）、`graph LR`（从左到右）
- **序列图**：`sequenceDiagram`
- **类图**：`classDiagram`
- **状态图**：`stateDiagram-v2`
- **甘特图**：`gantt`

更多语法参考：[Mermaid 官方文档](https://mermaid.js.org/)
