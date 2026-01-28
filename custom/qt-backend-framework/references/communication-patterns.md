# Communication Patterns

## Overview

The backend can communicate with the UI (and internally) via **Qt signals/slots** or **callbacks**. Both are supported; choose based on whether you use Qt types and how you structure your app.

## 1. Qt Signals and Slots

Use when the UI and backend use Qt (QObject-derived types). Signals and slots are the standard Qt way to decouple components.

### C++

**Service emits; controller receives and re-emits or updates model:**

```cpp
// Service
class AppService : public QObject {
    Q_OBJECT
signals:
    void WorkCompleted(bool success, const QString &result);
    void ErrorOccurred(const QString &msg);
};

// Controller
MainController::MainController(QObject *parent) : QObject(parent) {
    m_app_service = new AppService(this);
    connect(m_app_service, &AppService::WorkCompleted,
            this, &MainController::OnServiceWorkCompleted);
    connect(m_app_service, &AppService::ErrorOccurred,
            this, &MainController::OnServiceError);
}

void MainController::OnServiceWorkCompleted(bool success, const QString &result) {
    m_app_model->setStatus(success ? "ok" : "error");
    emit WorkCompleted(success, result);  // to UI
}
```

**UI connects to controller:**

```cpp
connect(m_controller, &MainController::WorkCompleted,
        this, &MainWindow::OnWorkCompleted);
connect(m_controller, &MainController::ErrorOccurred,
        this, &MainWindow::OnError);
```

### Python (PyQt6)

**Service emits; controller forwards:**

```python
class AppService(QObject):
    work_completed = pyqtSignal(bool, str)
    error_occurred = pyqtSignal(str)

class MainController(QObject):
    work_completed = pyqtSignal(bool, str)
    error_occurred = pyqtSignal(str)

    def __init__(self):
        self._app_service = AppService(self)
        self._app_service.work_completed.connect(self._on_work_done)
        self._app_service.error_occurred.connect(self.error_occurred.emit)

    def _on_work_done(self, ok, result):
        self._app_model.status = "ok" if ok else "error"
        self.work_completed.emit(ok, result)
```

**UI connects to controller:**

```python
ctrl.work_completed.connect(self.OnWorkCompleted)
ctrl.error_occurred.connect(self.OnError)
```

## 2. Callbacks

Use when you have one-off or asynchronous operations (e.g. API calls) and prefer a callback instead of a dedicated signal.

### C++

```cpp
using WorkCallback = std::function<void(bool success, const QString &result)>;

void AppService::DoWorkAsync(const QString &input, WorkCallback cb) {
    // Start async work...
    // On completion:
    cb(true, "result");
}
```

Controller can wrap the callback to update model and emit signals:

```cpp
void MainController::RequestDoWork(const QString &input) {
    m_app_service->DoWorkAsync(input, [this](bool ok, const QString &res) {
        m_app_model->setStatus(ok ? "ok" : "error");
        emit WorkCompleted(ok, res);
    });
}
```

### Python

```python
from typing import Callable

def DoWorkAsync(self, input_value: str, callback: Callable[[bool, str], None]) -> None:
    # Run async work...
    callback(True, "result")
```

Controller:

```python
def RequestDoWork(self, input_value: str) -> None:
    def done(ok: bool, res: str) -> None:
        self._app_model.status = "ok" if ok else "error"
        self.work_completed.emit(ok, res)
    self._app_service.DoWorkAsync(input_value, done)
```

## 3. Combining Signals and Callbacks

- **Signals:** Use for ongoing, many-to-many communication (e.g. UI ↔ controller, controller ↔ services). Multiple slots can connect to one signal.
- **Callbacks:** Use for single async operations where you pass a `std::function` or Python `Callable`. The service invokes it once when done.

You can use both: e.g. service uses a callback for async API completion, and controller still emits Qt signals to the UI.

## 4. Threading

- **Main thread:** Qt UI and most controller/service code run here. Use signals/slots for thread-safe notification.
- **Worker thread:** If a service does heavy or blocking work, run it in `QThread` or `QtConcurrent`, then emit a signal (or call a callback) when done. Connect to that signal in the main thread to update UI or model.

## 5. Summary

| Pattern       | Use case                          | C++              | Python                |
|---------------|-----------------------------------|------------------|------------------------|
| Signals/slots | UI ↔ controller, controller ↔ svc| `connect`/`emit` | `connect`/`emit`      |
| Callbacks     | One-off async completion          | `std::function`  | `Callable[[bool,str],None]` |

Prefer signals/slots for integration with Qt UI; add callbacks where they simplify async API usage.
