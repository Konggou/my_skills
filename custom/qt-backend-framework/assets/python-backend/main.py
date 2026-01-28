#!/usr/bin/env python3
"""
Backend demo: run from python-backend directory.
  python main.py

Or add python-backend to PYTHONPATH and run from project root.
"""

import sys
from pathlib import Path

# Ensure package root is on path when run as script
_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from PyQt6.QtCore import QCoreApplication
from controller.main_controller import MainController


def main():
    app = QCoreApplication(sys.argv)
    ctrl = MainController()

    ctrl.work_completed.connect(lambda ok, msg: print(f"Work completed: {ok} -> {msg}"))
    ctrl.work_completed.connect(app.quit)
    ctrl.error_occurred.connect(lambda msg: print(f"Error: {msg}"))
    ctrl.error_occurred.connect(app.quit)

    ctrl.RequestDoWork("hello")
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
