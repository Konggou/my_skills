"""
Coordinates UI and backend services.
Owns services and models; wires UI requests to services and
service signals back to UI or other layers.
"""

from PyQt6.QtCore import QObject, pyqtSignal

from service.app_service import AppService
from model.app_model import AppModel


class MainController(QObject):
    work_completed = pyqtSignal(bool, str)
    error_occurred = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._app_service = AppService(self)
        self._app_model = AppModel()

        self._app_service.work_completed.connect(self._on_service_work_completed)
        self._app_service.error_occurred.connect(self._on_service_error)

    @property
    def app_service(self):
        return self._app_service

    @property
    def app_model(self):
        return self._app_model

    def RequestDoWork(self, input_value: str) -> None:
        self._app_service.DoWork(input_value)

    def _on_service_work_completed(self, success: bool, result: str) -> None:
        self._app_model.status = "ok" if success else "error"
        self.work_completed.emit(success, result)

    def _on_service_error(self, message: str) -> None:
        self._app_model.status = "error"
        self.error_occurred.emit(message)
