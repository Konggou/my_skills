# Framework Diagram Templates

This document provides Mermaid templates for generating project framework diagrams.

## Architecture Diagram Templates

### Layered Architecture Diagram

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[UI Components]
        B[State Management]
        C[Routing]
    end
    
    subgraph "API Layer"
        D[REST API]
        E[WebSocket]
    end
    
    subgraph "Business Logic Layer"
        F[Service 1]
        G[Service 2]
    end
    
    subgraph "Data Layer"
        H[Database]
        I[Filesystem]
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

### Module Relationship Diagram

```mermaid
graph LR
    A[Module A] --> B[Module B]
    A --> C[Module C]
    B --> D[Module D]
    C --> D
    D --> E[Module E]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#fff4e1
    style D fill:#ffe1f5
    style E fill:#e1ffe1
```

### Component Interaction Diagram

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant A as API
    participant B as Business Logic
    participant D as Database
    
    U->>F: Interaction
    F->>A: HTTP Request
    A->>B: Call Service
    B->>D: Query Data
    D-->>B: Return Data
    B-->>A: Return Result
    A-->>F: JSON Response
    F-->>U: Update UI
```

## ROS2 Node Diagram Template

```mermaid
graph TB
    subgraph "ROS2 Nodes"
        N1[Node 1<br/>Publisher]
        N2[Node 2<br/>Subscriber]
        N3[Node 3<br/>Service]
    end
    
    subgraph "Topics/Services"
        T1[Topic 1]
        S1[Service 1]
    end
    
    subgraph "External Systems"
        API[Backend API]
    end
    
    N1 -->|Publish| T1
    T1 -->|Subscribe| N2
    N3 -->|Call| S1
    N2 -->|HTTP| API
```

## Data Flow Diagram Template

```mermaid
flowchart LR
    A[Data Source] -->|Input| B[Processing Module 1]
    B -->|Processed Data| C[Processing Module 2]
    C -->|Final Output| D[Data Output]
    
    E[Config] -.->|Config| B
    E -.->|Config| C
```

## Microservices Architecture Diagram Template

```mermaid
graph TB
    subgraph "API Gateway"
        GW[Gateway]
    end
    
    subgraph "Microservices"
        S1[Service 1]
        S2[Service 2]
        S3[Service 3]
    end
    
    subgraph "Infrastructure"
        DB[(Database)]
        MQ[Message Queue]
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

## Class Diagram Template

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

## Usage Notes

1. **Choose the right diagram type**
   - Architecture diagram: overall system structure
   - Module relationship diagram: module dependencies
   - Sequence diagram: interaction flow
   - Data flow diagram: data processing flow

2. **Customize styles**
   - Use `style` to add node colors
   - Use different arrow types for different relationships
   - Use subgraphs to group related nodes

3. **Keep it concise**
   - Avoid too many nodes in a single diagram
   - Use layering or grouping for complex structures
   - Highlight critical paths and core modules

4. **Labeling**
   - Use consistent labels for nodes and edges
   - Ensure readability

## Mermaid Syntax Reference

- **Flowchart**: `graph TB` (top-down), `graph LR` (left-right)
- **Sequence diagram**: `sequenceDiagram`
- **Class diagram**: `classDiagram`
- **State diagram**: `stateDiagram-v2`
- **Gantt chart**: `gantt`

More syntax references: [Mermaid Documentation](https://mermaid.js.org/)
