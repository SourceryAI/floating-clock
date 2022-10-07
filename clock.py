import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QMainWindow()
# Windows are hidden by default.
window.show()

# Start the event loop.
app.exec()
