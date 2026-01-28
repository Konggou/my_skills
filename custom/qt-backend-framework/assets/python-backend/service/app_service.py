"""
Generic backend service.
Encapsulates business logic and/or external API calls.
Uses PyQt signals (and optionally callbacks) to communicate.
"""

from PyQt6.QtCore import QObject, pyqtSignal


class AppService(QObject):
    work_completed = pyqtSignal(bool, str)
    error_occurred = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def DoWork(self, input_value: str) -> None:
        # Placeholder: run logic or API call, then emit result.
        ok = True
        result = "done"
        self.work_completed.emit(ok, result)
