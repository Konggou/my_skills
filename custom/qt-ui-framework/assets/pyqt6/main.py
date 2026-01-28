#!/usr/bin/env python3
"""
PyQt6 Application Entry Point
"""

import sys
from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Set app metadata (optional)
    app.setApplicationName("MyApp")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("MyCompany")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
