---
name: qt-backend-framework
description: Qt backend service framework scaffolding for desktop apps. Provides a generic Controller-Service-Model structure, supports C++ and Python, and integrates with the Qt UI layer via signals/slots or callbacks. Use when scaffolding the backend layer of a Qt project, adding a service/model/controller architecture, or wiring business logic and APIs to the UI.
---

# Qt Backend Framework Scaffolding

## Overview

This skill helps scaffold the **backend layer** of Qt desktop applications: business logic, data models, and coordination with the UI. It provides a generic **Controller-Service-Model** layout, supports **C++** and **Python**, and works with both **Qt signals/slots** and **callbacks**.

## Quick Start

### C++ Backend

Use the templates in `assets/cpp-backend/`:

```
cpp-backend/
  controller/
    maincontroller.h
    maincontroller.cpp
  service/
    appservice.h
    appservice.cpp
  model/
    appmodel.h
  CMakeLists.txt
```

1. Copy the directory into your project.

2. Add the library to your app CMake (or build it and link).

3. Create a `MainController` in your app, connect UI to its signals, and call `RequestDoWork` (or your own methods) from the UI.

### Python Backend

Use the templates in `assets/python-backend/`:

```
python-backend/
  controller/
  service/
  model/
  main.py
  requirements.txt
```

1. Copy the directory into your project.

2. `pip install -r requirements.txt`

3. Run `python main.py` from `python-backend/` for a minimal demo, or import `MainController` and wire it to your UI.

## Architecture

- **Controller:** Owns services and models. Receives UI requests, calls services, and emits results (or updates models) for the UI.

- **Service:** Implements business logic and/or API calls. Emits signals (or uses callbacks) when work completes.

- **Model:** Holds domain data. Updated by the controller from service results.

See `references/backend-architecture.md` for details and module layout.

## Communication with the UI

### Signals and Slots (recommended)

- **UI to Backend:** UI calls controller methods (e.g. `RequestDoWork(input)`).

- **Backend to UI:** Controller emits signals (e.g. `WorkCompleted`, `ErrorOccurred`). UI connects slots to these signals.

### Callbacks

- Services can accept callbacks (e.g. `std::function` in C++, `Callable` in Python) for one-off async work. The controller can wrap them and still emit Qt signals to the UI.

See `references/communication-patterns.md` for patterns and examples.

## Creating a C++ Backend

### 1. Copy Template

Copy `assets/cpp-backend/` into your repo. Adjust names (`AppService`, `AppModel`, `MainController`) to match your domain.

### 2. Integrate with CMake

**Option A: Subdirectory**  
Add the backend as a subdir and link it:

```cmake
add_subdirectory(path/to/cpp-backend)
target_link_libraries(${PROJECT_NAME} PRIVATE backend)
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/path/to/cpp-backend)
```

**Option B: Fold sources**  
Add `controller/`, `service/`, `model/` sources to your app `add_executable` and ensure their directory is in `target_include_directories`.

### 3. Wire to UI

In your UI layer (e.g. main window):

```cpp
m_controller = new MainController(this);
connect(m_controller, &MainController::WorkCompleted,
        this, &MainWindow::OnWorkCompleted);
connect(m_controller, &MainController::ErrorOccurred,
        this, &MainWindow::OnError);
// On user action:
m_controller->RequestDoWork(someInput);
```

### 4. Add Services and Models

- Add new `XxxService` classes in `service/`, implement logic and signals.

- Add new `XxxModel` in `model/` for domain data.

- In `MainController`, instantiate them, connect signals, and expose methods/signals for the UI.

## Creating a Python Backend

### 1. Copy Template

Copy `assets/python-backend/` into your project.

**Integration:** Add the backend root to `PYTHONPATH`, or run your app from the project root (with `python -m` or `sys.path`). For a single app, place `main.py` (or your UI entry) in the project root and add:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "python-backend"))
from controller import MainController
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Wire to UI

```python
from controller import MainController

ctrl = MainController()
ctrl.work_completed.connect(self.OnWorkCompleted)
ctrl.error_occurred.connect(self.OnError)
# On user action:
ctrl.RequestDoWork(some_input)
```

### 4. Add Services and Models

- Add `XxxService` in `service/`, `XxxModel` in `model/`.

- Update `MainController` to own them and forward requests/results.

## Full Integration (UI + Backend)

Use **qt-ui-framework** for the UI and this skill for the backend.

**C++:**  
1. Scaffold UI from `qt-ui-framework` (`assets/cpp-widgets/`).  
2. Add backend via `add_subdirectory` and `target_link_libraries(... backend)`.  
3. In `main.cpp`, create `QApplication`, `MainWindow`, and `MainController`. Pass `MainController` to `MainWindow` (or create it inside `MainWindow`).  
4. In `MainWindow::ConnectSignals()`, connect `m_controller->WorkCompleted` / `ErrorOccurred` to slots, and call `m_controller->RequestDoWork(...)` from button handlers.

**Python:**  
1. Scaffold UI from `qt-ui-framework` (`assets/pyqt6/` or `pyqt5/`).  
2. Copy `python-backend/` into the project; add its root to `sys.path`.  
3. In `MainWindow.__init__`, create `MainController`, connect `work_completed` / `error_occurred`, and call `RequestDoWork` from UI handlers.

## Naming Conventions

- **C++:** PascalCase for types and methods; `m_` + snake_case for members. Slots: `OnXxx`.

- **Python:** PascalCase for classes; snake_case for functions and variables. Private helpers: `_on_xxx`, `_helper`.

## Resources

### assets/

- `cpp-backend/` - C++ Controller-Service-Model template and CMake.

- `python-backend/` - Python package layout and demo `main.py`.

### references/

- `backend-architecture.md` - Layers, responsibilities, and module layout.

- `communication-patterns.md` - Signals/slots vs callbacks, threading, examples.

## FAQ

**Q: Where does the UI layer come from?**  

Use the **qt-ui-framework** skill to scaffold the Qt UI. The UI connects to the backend controller via signals/slots.

**Q: Can I use both signals and callbacks?**  

Yes. Use signals for UI-controller and controller-services; use callbacks for one-off async API completions if that fits better.

**Q: Do I need extra modules (e.g. logging, error handling)?**  

The template is intentionally minimal. Add handlers, loggers, or other modules as your project needs them; the architecture stays the same.

**Q: How do I add a new service?**  

Create a new `XxxService` in `service/`, implement logic and signals. Instantiate it in the controller, connect its signals, and expose a `RequestXxx`-style method and corresponding controller signals for the UI.

**Q: How should errors be reported?**  

Have services emit `ErrorOccurred(QString)` (or similar). The controller forwards it; the UI connects a slot and shows the message (e.g. `QMessageBox::warning` or a status bar). Keep error text in the backend; the UI only displays it.

