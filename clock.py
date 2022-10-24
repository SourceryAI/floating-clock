import sys

from PySide6.QtCore import QPoint, Qt, QTime, QTimer
from PySide6.QtGui import QAction, QCursor, QFont, QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel, QMenu, QVBoxLayout, QWidget


class Clock(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60

        # mouse
        self.pressed = False
        self.oldPos = QPoint(0, 0)

        # Menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.mouseRightMenu)

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
        self.actionA = QAction('fontsize', self)
        self.menu.addAction(self.actionA)

        self.actionB = QAction('fontcolor', self)
        self.menu.addAction(self.actionB)

        self.menu.exec(self.mapToGlobal(pos))

    def initUI(self) -> None:

        # geometry of main window
        self.setGeometry(self.left, self.top, self.width, self.height)

        # hide frame
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # font
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        # font.setBold(True)

        # label object
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setStyleSheet("color:blue;")

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
        label_time = current_time.toString('hh:mm')  # convert timer to string
        self.label.setText(label_time)  # show it to the label


if __name__ == '__main__':

    App = QApplication(sys.argv)
    clock = Clock()
    clock.show()  # show all the widgets
    App.exit(App.exec())  # start the app
