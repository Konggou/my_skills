"""
PyQt6 Main Window
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.SetupUI()
        self.ConnectSignals()
    
    def SetupUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        label = QLabel("Hello, PyQt6!", self)
        layout.addWidget(label)

        self.setWindowTitle("My Application")
        self.resize(800, 600)

    def ConnectSignals(self):
        # Connect signals and slots here.
        # Example: button.clicked.connect(self.OnButtonClicked)
        pass
