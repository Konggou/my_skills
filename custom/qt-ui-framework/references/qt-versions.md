# Qt Version Differences

## Qt5 vs Qt6

### CMake

**Qt5:**
```cmake
find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

target_link_libraries(${PROJECT_NAME}
    Qt5::Core
    Qt5::Gui
    Qt5::Widgets
)
```

**Qt6:**
```cmake
find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

target_link_libraries(${PROJECT_NAME}
    Qt6::Core
    Qt6::Gui
    Qt6::Widgets
)
```

**Summary:** Qt5 uses `Qt5::*`, Qt6 uses `Qt6::*`.

### Qt5 + Qt6–compatible CMakeLists.txt

```cmake
find_package(Qt6 QUIET COMPONENTS Core Gui Widgets)
if(Qt6_FOUND)
    set(QT_VERSION_MAJOR 6)
    message(STATUS "Using Qt6")
else()
    find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
    set(QT_VERSION_MAJOR 5)
    message(STATUS "Using Qt5")
endif()

if(QT_VERSION_MAJOR EQUAL 6)
    target_link_libraries(${PROJECT_NAME}
        Qt6::Core
        Qt6::Gui
        Qt6::Widgets
    )
else()
    target_link_libraries(${PROJECT_NAME}
        Qt5::Core
        Qt5::Gui
        Qt5::Widgets
    )
endif()
```

### Code changes

#### 1. QApplication::exec()

Same in both: `return app.exec();`

#### 2. QFontMetrics::width() deprecated

**Qt5:**
```cpp
int w = fontMetrics.width(text);
```

**Qt6:**
```cpp
int w = fontMetrics.horizontalAdvance(text);
```

#### 3. QRegExp vs QRegularExpression

**Qt5:**
```cpp
QRegExp re("pattern");
```

**Qt6:** Prefer `QRegularExpression`:
```cpp
QRegularExpression re("pattern");
```

#### 4. QTextCodec removed in Qt6

**Qt5:**
```cpp
QTextCodec *codec = QTextCodec::codecForName("UTF-8");
QString text = codec->toUnicode(data);
```

**Qt6:**
```cpp
QString text = QString::fromUtf8(data);
```

### Python: PyQt5 vs PyQt6

#### Imports

**PyQt5:**
```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal
```

**PyQt6:**
```python
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, pyqtSignal
```

#### exec() vs exec_()

**PyQt5:**
```python
sys.exit(app.exec_())
```

**PyQt6:**
```python
sys.exit(app.exec())
```

#### Enums

**PyQt5:**
```python
alignment = Qt.AlignCenter
```

**PyQt6:**
```python
alignment = Qt.AlignmentFlag.AlignCenter
```

#### Signals

Same in both; only the import package changes (`PyQt5` vs `PyQt6`).

## When to use which

**Qt5:**

- Older systems or toolchains
- Existing Qt5 codebase
- Dependencies that support only Qt5

**Qt6:**

- New projects
- Need Qt6 features
- Prefer modern APIs and performance

**Compatibility:**

1. Prefer Qt6 for new work.
2. Use conditional compilation if you must support both.
3. Use the auto-detect CMake pattern above.

## FAQ

**Q: How do I check the Qt version in use?**

**C++:**
```cpp
#include <QtGlobal>
qDebug() << "Qt version:" << QT_VERSION_STR;
```

**Python:**
```python
from PyQt6.QtCore import QT_VERSION_STR
print(f"Qt version: {QT_VERSION_STR}")
```

**Q: How do I write code that works with both Qt5 and Qt6?**

Use `#if` based on `QT_VERSION`:

```cpp
#if QT_VERSION >= QT_VERSION_CHECK(6, 0, 0)
    int w = fontMetrics.horizontalAdvance(text);
#else
    int w = fontMetrics.width(text);
#endif
```

**Q: How does CMake auto-select Qt?**

Try Qt6 first with `QUIET`; if not found, use Qt5:

```cmake
find_package(Qt6 QUIET COMPONENTS Core Gui Widgets)
if(NOT Qt6_FOUND)
    find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
endif()
```
