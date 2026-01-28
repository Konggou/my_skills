# Qt Frontend–Backend Separation

## Overview

In Qt projects, frontend–backend separation means keeping the UI layer distinct from business logic. The UI handles presentation and user interaction only; it does not implement business logic.

## Architecture

```
┌─────────────────────────────────┐
│      UI Layer (Frontend)         │
│  - Windows, widgets, layout      │
│  - User interaction              │
│  - Emit signals (no logic)       │
└──────────────┬──────────────────┘
               │ signals/slots
               ▼
┌─────────────────────────────────┐
│   Backend Layer                  │
│  - Service: logic, API calls     │
│  - Model: data                   │
│  - Controller: UI ↔ Service      │
└─────────────────────────────────┘
```

## UI Layer Responsibilities

### ✅ Do

1. **Presentation**
   - Create and manage windows and widgets
   - Set layout and style
   - Update display from backend data

2. **User interaction**
   - Handle input (clicks, edits, etc.)
   - Validate format at UI level (e.g. non-empty, valid format)

3. **Emit signals**
   - Turn user actions into signals for the backend
   - Example: `emit RequestOpenPort(portName, baudRate);`

4. **Show state**
   - Display status from the backend
   - Show error messages (message content comes from backend)

### ❌ Don’t

1. **Business logic**
   - ❌ Don’t call APIs directly from the UI
   - ❌ Don’t do data transformation in the UI
   - ❌ Don’t run complex computation in the UI

2. **Persistence**
   - ❌ Don’t read/write files or DB from the UI
   - ❌ Don’t manage config in the UI

3. **Communication**
   - ❌ Don’t open serial ports, sockets, etc. in the UI
   - ❌ Don’t parse protocols in the UI

## Communication

### C++ Qt signals and slots

**UI emits:**

```cpp
// mainwindow.h
class MainWindow : public QMainWindow
{
    Q_OBJECT
signals:
    void RequestOpenPort(const QString &portName, qint32 baudRate);
    void RequestClosePort();

private slots:
    void OnPortOpened(bool success);
    void OnPortClosed();
};
```

**UI connects:**

```cpp
// mainwindow.cpp
void MainWindow::ConnectSignals()
{
    connect(m_controller, &Controller::PortOpened,
            this, &MainWindow::OnPortOpened);
    connect(m_controller, &Controller::PortClosed,
            this, &MainWindow::OnPortClosed);
}

void MainWindow::OnOpenButtonClicked()
{
    emit RequestOpenPort(m_port_combo->currentText(),
                        m_baud_combo->currentText().toInt());
}
```

### Python PyQt signals and slots

**UI emits:**

```python
from PyQt6.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    request_open_port = pyqtSignal(str, int)
    request_close_port = pyqtSignal()

    def OnOpenButtonClicked(self):
        port_name = self.port_combo.currentText()
        baud_rate = int(self.baud_combo.currentText())
        self.request_open_port.emit(port_name, baud_rate)
```

**UI connects:**

```python
def ConnectSignals(self):
    self.controller.port_opened.connect(self.OnPortOpened)
    self.controller.port_closed.connect(self.OnPortClosed)
```

## Naming Conventions

### C++

- **Functions:** PascalCase  
  `SetupUI()`, `ConnectSignals()`, `OnButtonClicked()`
- **Members:** snake_case, `m_` prefix  
  `m_port_combo`, `m_open_button`, `m_status_label`
- **Signals:** `RequestXxx` or `OnXxx`  
  `RequestOpenPort()`, `RequestClosePort()`
- **Slots:** `OnXxx`  
  `OnPortOpened()`, `OnButtonClicked()`

### Python

- **Functions:** PascalCase  
  `SetupUI()`, `ConnectSignals()`, `OnButtonClicked()`
- **Members:** snake_case, `m_` prefix  
  `self.m_port_combo`, `self.m_open_button`
- **Signals:** `request_xxx` or `on_xxx`  
  `request_open_port`, `request_close_port`
- **Slots:** `OnXxx`  
  `OnPortOpened()`, `OnButtonClicked()`

## Best Practices

1. **Split UI setup**
   - `SetupUI()`: create and layout widgets
   - `ConnectSignals()`: connect signals and slots

2. **Error handling**
   - UI receives error text from the backend
   - Use `QMessageBox` to show it; don’t invent messages in the UI

3. **State updates**
   - UI updates via slots driven by backend signals
   - Keep UI purely reactive to backend state

4. **Avoid direct backend coupling**
   - UI doesn’t include business-logic headers directly
   - Interact only via signals/slots or clear interfaces

## Example: UI-only structure

```cpp
// mainwindow.h
class MainWindow : public QMainWindow
{
    Q_OBJECT
public:
    explicit MainWindow(QWidget *parent = nullptr);

signals:
    void RequestOpenPort(const QString &portName, qint32 baudRate);

private slots:
    void OnPortOpened(bool success);
    void OnPortError(const QString &error);

private:
    void SetupUI();
    void ConnectSignals();

    QComboBox *m_port_combo;
    QPushButton *m_open_button;
    QLabel *m_status_label;
};
```

```cpp
// mainwindow.cpp
void MainWindow::SetupUI()
{
    m_port_combo = new QComboBox(this);
    m_open_button = new QPushButton("Open", this);
    // ... layout
}

void MainWindow::ConnectSignals()
{
    connect(m_open_button, &QPushButton::clicked,
            this, &MainWindow::OnOpenButtonClicked);
    connect(m_backend_service, &BackendService::PortOpened,
            this, &MainWindow::OnPortOpened);
}

void MainWindow::OnOpenButtonClicked()
{
    emit RequestOpenPort(m_port_combo->currentText(), 9600);
}

void MainWindow::OnPortOpened(bool success)
{
    if (success)
        m_status_label->setText("Port opened");
    else
        m_status_label->setText("Open failed");
}
```
