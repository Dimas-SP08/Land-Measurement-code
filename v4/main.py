"""Land Measurement Program - Main Entry Point.

This program provides tools for land surveying calculations and visualization.
It features a graphical interface built with PyQt5.

Usage:
    Run this file to start the land measurement application.
    The program will open a window with 600x600 dimensions.
"""

from PyQt5 import QtWidgets
import sys
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Land Measurement Program")
    window.resize(600, 600)
    window.setMaximumSize(600,600)
    window.show()
    sys.exit(app.exec_())