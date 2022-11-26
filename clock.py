import sys

from PySide6.QtCore import QPoint, Qt, QTime, QTimer
from PySide6.QtGui import QAction, QFont, QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel, QMenu, QVBoxLayout, QWidget


class Clock(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.left = 1100
        self.top = 800
        self.width = 320
        self.height = 60

        # Mouse
        self.pressed = False
        self.oldPos = QPoint(0, 0)

        # Menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.mouseRightMenu)

        # Font
        self.font_color = "blue"

        # UI
        self.initUI()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.pressed = True
        self.oldPos = event.pos()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.pressed:
            self.move(self.pos() + (event.pos() - self.oldPos))
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.pressed = False
        self.oldPos = event.pos()
        return super().mouseReleaseEvent(event)

    def mouseRightMenu(self, pos) -> None:
        self.menu = QMenu(self)
        fontSizeMenu = self.menu.addMenu("font size")
        self.actionA1 = QAction("larger", self)
        self.actionA2 = QAction("smaller", self)
        fontSizeMenu.addAction(self.actionA1)
        fontSizeMenu.addAction(self.actionA2)

        self.actionZ = QAction("quit", self)
        self.actionZ.triggered.connect(self.close)
        self.menu.addAction(self.actionZ)

        self.menu.exec(self.mapToGlobal(pos))

    def initUI(self) -> None:

        # geometry of main window
        self.setGeometry(self.left, self.top, self.width, self.height)

        # hide frame
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # font
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        # font.setBold(True)

        # label object
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setStyleSheet(f"color:{self.font_color};")

        # layout
        layout = QVBoxLayout(self, spacing=0)

        layout.addWidget(self.label)  # add label
        self.setLayout(layout)

        # timer object
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)  # update the timer per second
        self.show()

    def showTime(self) -> None:

        current_time = QTime.currentTime()  # get the current time
        label_time = current_time.toString("hh:mm")  # convert timer to string
        self.label.setText(label_time)  # show it to the label


if __name__ == "__main__":

    App = QApplication(sys.argv)
    clock = Clock()
    clock.show()  # show all the widgets
    App.exit(App.exec())  # start the app
