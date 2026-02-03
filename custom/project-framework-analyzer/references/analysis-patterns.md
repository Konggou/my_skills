# Project Analysis Patterns Reference

This document provides analysis patterns and best practices for different project types.

## Contents

1. [Frontend Project Analysis](#frontend-project-analysis)
2. [Backend Project Analysis](#backend-project-analysis)
3. [Full-Stack Project Analysis](#full-stack-project-analysis)
4. [ROS2 Project Analysis](#ros2-project-analysis)
5. [Microservices Project Analysis](#microservices-project-analysis)

## Frontend Project Analysis

### Typical Structure

```
frontend/
├── src/
│   ├── components/     # UI components
│   ├── views/          # Page views
│   ├── api/            # API client
│   ├── store/          # State management
│   ├── router/         # Routing configuration
│   ├── utils/          # Utility functions
│   └── types/          # Type definitions
├── public/             # Static assets
└── package.json        # Dependencies
```

### Key Focus Areas

1. **Component hierarchy**
   - Identify base components and business components
   - Identify page-level components vs. feature components
   - Evaluate component reuse patterns

2. **State management**
   - Identify global vs. local state
   - Analyze state flow paths
   - Identify state libraries (Vuex/Pinia, Redux, Zustand, etc.)

3. **Routing structure**
   - Identify route hierarchy
   - Analyze route guards and access control
   - Identify lazy-loading strategies

4. **API integration**
   - Identify API client abstraction
   - Analyze request/response handling
   - Identify WebSocket connection management

### Common Frameworks

- **Vue 3**: Composition API, Pinia, Vue Router
- **React**: Hooks, Redux, React Router
- **Angular**: Modules, Services, RxJS

## Backend Project Analysis

### Typical Structure

```
backend/
├── server/
│   ├── api/            # API routes
│   ├── basic/          # Business logic
│   ├── models/         # Data models
│   ├── utils/          # Utilities
│   └── app.py          # App entry
├── include/            # Shared libraries
└── requirements.txt    # Dependencies
```

### Key Focus Areas

1. **API layer**
   - Identify RESTful endpoints
   - Analyze route organization
   - Identify middleware and interceptors

2. **Business logic layer**
   - Identify service classes and methods
   - Analyze business rules implementation
   - Identify transaction boundaries

3. **Data access layer**
   - Identify data models
   - Analyze database operations
   - Identify ORM or data access patterns

4. **Communication mechanisms**
   - WebSocket connection management
   - Message queue usage
   - Event pub/sub patterns

### Common Frameworks

- **Flask**: Blueprint, Flask-SocketIO
- **Django**: Apps, Models, Views
- **FastAPI**: Routers, Dependencies, WebSocket

## Full-Stack Project Analysis

### Typical Structure

```
project/
├── frontend/           # Frontend code
├── backend/            # Backend code
├── shared/             # Shared code (optional)
└── docs/               # Documentation
```

### Key Focus Areas

1. **Frontend-backend separation**
   - Identify communication interfaces (REST API, WebSocket)
   - Analyze data format conventions (JSON Schema)
   - Identify authentication/authorization mechanisms

2. **Data flow**
   - Frontend-to-backend request flow
   - Backend-to-frontend response flow
   - Real-time data push (WebSocket)

3. **Deployment architecture**
   - Identify build configuration
   - Analyze deployment scripts
   - Identify environment configuration

## ROS2 Project Analysis

### Typical Structure

```
ros2_ws/
├── src/
│   └── package_name/
│       ├── nodes/      # ROS2 nodes
│       ├── launch/     # Launch files
│       ├── config/     # Config files
│       └── CMakeLists.txt
└── install/            # Install directory
```

### Key Focus Areas

1. **Node identification**
   - Identify publisher nodes
   - Identify subscriber nodes
   - Identify service nodes (Service/Client)
   - Identify action nodes

2. **Topics and services**
   - Identify topics and message types
   - Identify services and request/response types
   - Identify actions and goal/feedback types

3. **Node relationships**
   - Analyze inter-node communication
   - Identify data flow direction
   - Identify node startup order

4. **External integrations**
   - Identify integration points with backend APIs
   - Analyze data transformation logic
   - Identify hardware interfaces

## Microservices Project Analysis

### Typical Structure

```
microservices/
├── service1/           # Service 1
├── service2/           # Service 2
├── gateway/            # API gateway
└── shared/             # Shared libraries
```

### Key Focus Areas

1. **Service boundaries**
   - Identify service responsibilities
   - Analyze inter-service interfaces
   - Identify shared data models

2. **Service communication**
   - REST API calls
   - Message queues (RabbitMQ, Kafka)
   - gRPC calls

3. **Service discovery and configuration**
   - Identify service registry mechanisms
   - Analyze config management approach
   - Identify load-balancing strategies

## General Analysis Patterns

### 1. Top-down analysis

1. Start from the project root
2. Identify key directories and files
3. Deep dive into critical modules
4. Map module relationships

### 2. Bottom-up analysis

1. Start from concrete files
2. Identify file responsibilities
3. Generalize into modules
4. Build the overall architecture

### 3. Critical path analysis

1. Identify core business flows
2. Trace data movement
3. Analyze key modules
4. Identify potential bottlenecks

### 4. Dependency analysis

1. Identify direct dependencies
2. Identify indirect dependencies
3. Identify cyclic dependencies
4. Identify core dependencies

## Analysis Checklist

- [ ] Project root structure identified
- [ ] Tech stack clarified
- [ ] Major modules listed
- [ ] Module responsibilities described
- [ ] Module dependencies mapped
- [ ] Data flow analyzed
- [ ] Control flow analyzed
- [ ] Framework diagrams generated
- [ ] Analysis report complete
