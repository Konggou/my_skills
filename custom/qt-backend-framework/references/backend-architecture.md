# Backend Architecture

## Overview

The backend layer holds business logic, data models, and coordination between UI and services. It is separate from the UI: the UI emits requests and displays results; the backend performs work and reports outcomes.

## Layers

```
┌─────────────────────────────────────────────────────────┐
│  UI (Frontend)                                          │
│  Emits: RequestXxx(...)   Receives: OnXxx(...)          │
└───────────────────────────┬─────────────────────────────┘
                            │ signals / callbacks
                            ▼
┌─────────────────────────────────────────────────────────┐
│  Controller                                             │
│  - Owns Service(s) and Model(s)                         │
│  - Connects UI requests → Service calls                 │
│  - Connects Service signals → UI updates (or Model)     │
└───────────────────────────┬─────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│   Service     │   │   Service     │   │     Model     │
│  (logic, API) │   │  (optional)   │   │  (data only)  │
└───────────────┘   └───────────────┘   └───────────────┘
```

## Controller

- **Role:** Mediates between UI and backend. Owns one or more services and models.
- **Responsibilities:**
  - Create and own `Service` and `Model` instances.
  - Expose methods like `RequestDoWork(...)` that forward to services.
  - Connect service signals to slots that update models and/or re-emit signals to the UI.
  - Optionally expose `GetXxx()` for UI or tests to access services/models.
- **Does not:** Implement business logic itself; that stays in services.

## Service

- **Role:** Encapsulates business logic, external API calls, I/O, etc.
- **Responsibilities:**
  - Run operations (sync or async).
  - Emit signals when work completes or errors occur.
  - Optionally use callbacks (e.g. `std::function`) in addition to signals.
- **Does not:** Know about the UI. It only reports success/failure and data.

## Model

- **Role:** Holds domain data.
- **Responsibilities:**
  - Store state (e.g. status, cached values).
  - Provide getters/setters or methods to update state.
  - Optionally emit change notifications (e.g. Qt signals) if needed.
- **Does not:** Call APIs or perform business logic. Often a plain struct/class.

## Module Layout

### C++

```
backend/
├── controller/
│   ├── maincontroller.h
│   └── maincontroller.cpp
├── service/
│   ├── appservice.h
│   └── appservice.cpp
├── model/
│   └── appmodel.h
└── CMakeLists.txt
```

### Python

```
backend/
├── controller/
│   ├── __init__.py
│   └── main_controller.py
├── service/
│   ├── __init__.py
│   └── app_service.py
├── model/
│   ├── __init__.py
│   └── app_model.py
├── main.py          # optional demo entry
└── requirements.txt
```

## Adding New Modules

- **New service:** Add `XxxService` in `service/`, implement logic and signals. Controller creates it and connects its signals.
- **New model:** Add `XxxModel` in `model/`. Controller (or a dedicated controller) owns it and updates it from service results.
- **New controller:** Add `XxxController` for a distinct area. MainController can own sub-controllers and delegate UI requests to them.

## Naming Conventions

- **C++:** PascalCase for types and methods; `m_` + snake_case for members. Slots: `OnXxx`.
- **Python:** PascalCase for classes; snake_case for functions/variables. Private helpers: `_on_xxx`, `_helper`.

## Integration with UI

The UI layer (see `qt-ui-framework` skill) connects to the controller:

- UI connects its slots to controller signals (e.g. `WorkCompleted`, `ErrorOccurred`).
- UI calls controller methods (e.g. `RequestDoWork`) when the user acts.
- No direct UI → Service or UI → Model coupling; all go through the controller.
