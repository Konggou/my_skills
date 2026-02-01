---
name: qt-ui-framework
description: >-
  Qt UI framework scaffolding for desktop apps. Supports C++ (Qt Widgets) and
  Python (PyQt5/PyQt6). Use when creating a new Qt project, scaffolding the UI
  layer, or bootstrapping a minimal runnable Qt window app. Follows
  frontend-backend separation: the UI layer handles presentation and user
  interaction only, no business logic.
---

# Qt UI Framework Scaffolding

## Overview

This skill helps scaffold the UI layer for Qt desktop applications, providing minimal runnable project templates. It supports C++ (Qt Widgets) and Python (PyQt5/PyQt6) and enforces frontend-backend separation so the UI layer is responsible only for presentation and user interaction.

## Quick Start

### C++ Qt Widgets Project

Use the templates in `assets/cpp-widgets/`:

1. **Copy template files** into your project directory.
2. **Edit CMakeLists.txt** to set your project name.
3. **Configure Qt version** (CMakeLists.txt auto-detects Qt5/Qt6).
4. **Build and run.**

**File structure:**
```
project/
  main.cpp          # Application entry
  mainwindow.h      # Main window header
  mainwindow.cpp    # Main window implementation
  CMakeLists.txt    # CMake config
  .gitignore        # Git ignore rules
```

### Python PyQt6 Project

Use the templates in `assets/pyqt6/`:

1. **Copy template files** into your project directory.
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run:** `python main.py`

**File structure:**
```
project/
  main.py           # Application entry
  mainwindow.py     # Main window class
  requirements.txt  # Python dependencies
```

### Python PyQt5 Project

Use the templates in `assets/pyqt5/`. Structure mirrors PyQt6.

## Frontend-Backend Separation

The UI layer should:

- Present the interface and layout
- Handle user interaction
- Emit signals (no business logic)
- Show state based on backend data

The UI layer should **not**:

- Implement business logic
- Call APIs directly
- Persist data
- Handle communication protocols

**Details:** See `references/frontend-backend-separation.md`

## Creating a C++ Qt Widgets Project

### 1. Use Template Files

Copy from `assets/cpp-widgets/`:

- `main.cpp` - Application entry; creates QApplication and main window
- `mainwindow.h` - Main window class declaration
- `mainwindow.cpp` - Main window implementation with `SetupUI()` and `ConnectSignals()`
- `CMakeLists.txt` - CMake config with Qt5/Qt6 auto-detection
- `.gitignore` - Git ignore rules

### 2. Adjust Project Config

**CMakeLists.txt:**
```cmake
project(MyApp VERSION 1.0.0 LANGUAGES CXX)
```

Replace `MyApp` with your project name.

### 3. Build and Run

```bash
mkdir build && cd build
cmake ..
cmake --build .
./bin/MyApp   # Linux/macOS
# or bin\MyApp.exe on Windows
```

### 4. Extend the UI

Add widgets in `MainWindow::SetupUI()`:

```cpp
void MainWindow::SetupUI()
{
    QWidget *central_widget = new QWidget(this);
    setCentralWidget(central_widget);

    QVBoxLayout *layout = new QVBoxLayout(central_widget);

    QPushButton *button = new QPushButton("Click", this);
    layout->addWidget(button);

    setWindowTitle("My Application");
    resize(800, 600);
}
```

## Creating a Python PyQt6 Project

### 1. Use Template Files

Copy from `assets/pyqt6/`:

- `main.py` - Application entry
- `mainwindow.py` - Main window class
- `requirements.txt` - Dependencies

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
python main.py
```

### 4. Extend the UI

Add widgets in `MainWindow.SetupUI()`:

```python
def SetupUI(self):
    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    button = QPushButton("Click", self)
    layout.addWidget(button)

    self.setWindowTitle("My Application")
    self.resize(800, 600)
```

## Creating a Python PyQt5 Project

Same steps as PyQt6, but use `assets/pyqt5/`.

**Note:** PyQt5 uses `app.exec_()`; PyQt6 uses `app.exec()`.

## Qt Version Differences

### CMakeLists.txt Auto-Detection

The template CMakeLists.txt auto-detects Qt5 or Qt6:

```cmake
find_package(Qt6 QUIET COMPONENTS Core Gui Widgets)
if(Qt6_FOUND)
    set(QT_VERSION_MAJOR 6)
else()
    find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
    set(QT_VERSION_MAJOR 5)
endif()
```

### Code Compatibility

**Details:** See `references/qt-versions.md`

Notable changes:

- Qt6: use `QFontMetrics::horizontalAdvance()` instead of `width()`
- Qt6: prefer `QRegularExpression` over `QRegExp`
- Qt6: `QTextCodec` removed; use `QString::fromUtf8()`

## Naming Conventions

### C++

- **Functions:** PascalCase  
  e.g. `SetupUI()`, `ConnectSignals()`, `OnButtonClicked()`
- **Member variables:** snake_case with `m_` prefix  
  e.g. `m_port_combo`, `m_open_button`, `m_status_label`
- **Signals:** `RequestXxx` or `OnXxx`  
  e.g. `RequestOpenPort()`, `RequestClosePort()`
- **Slots:** `OnXxx`  
  e.g. `OnPortOpened()`, `OnButtonClicked()`

### Python

- **Functions:** PascalCase  
  e.g. `SetupUI()`, `ConnectSignals()`, `OnButtonClicked()`
- **Member variables:** snake_case with `m_` prefix  
  e.g. `self.m_port_combo`, `self.m_open_button`
- **Signals:** `request_xxx` or `on_xxx`  
  e.g. `request_open_port`, `request_close_port`
- **Slots:** `OnXxx`  
  e.g. `OnPortOpened()`, `OnButtonClicked()`

## Communicating with the Backend

To scaffold the backend (Controller-Service-Model), use the **qt-backend-framework** skill. The UI connects to a `MainController` via signals and slots.

### C++ Signals and Slots

Example assumes the backend is integrated (see qt-backend-framework) and its include path is set.

**UI calls controller and connects to its signals:**

```cpp
// mainwindow.h
#include "controller/maincontroller.h"

class MainWindow : public QMainWindow {
    // ...
private slots:
    void OnWorkCompleted(bool success, const QString &result);
    void OnError(const QString &message);
private:
    MainController *m_controller;
};

// mainwindow.cpp
void MainWindow::ConnectSignals()
{
    m_controller = new MainController(this);
    connect(m_controller, &MainController::WorkCompleted,
            this, &MainWindow::OnWorkCompleted);
    connect(m_controller, &MainController::ErrorOccurred,
            this, &MainWindow::OnError);
}

void MainWindow::OnDoWorkClicked()
{
    m_controller->RequestDoWork(m_input_edit->text());
}

void MainWindow::OnWorkCompleted(bool success, const QString &result)
{
    if (success)
        m_status_label->setText("Done: " + result);
    else
        m_status_label->setText("Failed");
}

void MainWindow::OnError(const QString &message)
{
    m_status_label->setText("Error: " + message);
}
```

### Python Signals and Slots

**UI connects to MainController (from qt-backend-framework):**

```python
from controller import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_controller = MainController(self)
        self.m_controller.work_completed.connect(self.OnWorkCompleted)
        self.m_controller.error_occurred.connect(self.OnError)

    def OnDoWorkClicked(self):
        self.m_controller.RequestDoWork(self.m_input_edit.text())

    def OnWorkCompleted(self, success, result):
        self.m_status_label.setText("Done: " + result if success else "Failed")

    def OnError(self, message):
        self.m_status_label.setText("Error: " + message)
```

## Resources

### assets/

Project templates:

- `cpp-widgets/` - C++ Qt Widgets
- `pyqt6/` - Python PyQt6
- `pyqt5/` - Python PyQt5

### references/

- `frontend-backend-separation.md` - Separation rules and practices
- `qt-versions.md` - Qt5 vs Qt6 differences and compatibility

## FAQ

**Q: Qt5 or Qt6?**  
New projects: prefer Qt6. Existing codebase: stay on Qt5. For flexibility, use the auto-detect CMake setup from the template.

**Q: Can the UI layer contain business logic?**  
No. Keep logic in the backend (Service/Controller); the UI only presents and forwards user actions via signals.

**Q: How do I add more widgets?**  
Create widgets in `SetupUI()` and add them to your layout. See the template examples.

**Q: How do I wire up the backend?**  
Use the **qt-backend-framework** skill to scaffold the backend. The UI holds a `MainController`, connects to its signals (`WorkCompleted`, `ErrorOccurred`), and calls methods like `RequestDoWork`. See "Communicating with the Backend" above.
