"""
Generic data model for the backend layer.
Holds domain data. Use plain attributes or properties.
"""


class AppModel:
    def __init__(self):
        self._status = ""

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
