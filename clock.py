import sys

from PySide6.QtCore import QPoint, Qt, QTime, QTimer
from PySide6.QtGui import QAction, QFont, QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel, QMenu, QVBoxLayout, QWidget


class Clock(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60

        # Mouse
        self.pressed = False
        self.oldPos = QPoint(0, 0)

        # Menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.mouseRightMenu)

        # Font
        self.font_color = 'blue'

        # UI
        self.initUI()

    def changeFontColor(self, fcolor) -> None:
        self.font_color = fcolor

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
        fontSizeMenu = self.menu.addMenu('font size')
        self.actionA1 = QAction('larger', self)
        self.actionA2 = QAction('smaller', self)
        fontSizeMenu.addAction(self.actionA1)
        fontSizeMenu.addAction(self.actionA2)

        fontColorMenu = self.menu.addMenu('font color')
        self.actionB1 = QAction('black', self)
        self.actionB2 = QAction('red', self)
        self.actionB3 = QAction('yellow', self)
        self.actionB4 = QAction('blue', self)
        self.actionB5 = QAction('orange', self)
        self.actionB6 = QAction('green', self)
        self.actionB7 = QAction('white', self)
        # self.actionB1.triggered.connect(self.changeFontColor('black'))
        # self.actionB2.triggered.connect(self.changeFontColor('red'))
        fontColorMenu.addAction(self.actionB1)
        fontColorMenu.addAction(self.actionB2)
        fontColorMenu.addAction(self.actionB3)
        fontColorMenu.addAction(self.actionB4)
        fontColorMenu.addAction(self.actionB5)
        fontColorMenu.addAction(self.actionB6)
        fontColorMenu.addAction(self.actionB7)

        fontOpacityMenu = self.menu.addMenu('font opacity')
        self.actionC1 = QAction('increase', self)
        self.actionC2 = QAction('decrease', self)
        fontOpacityMenu.addAction(self.actionC1)
        fontOpacityMenu.addAction(self.actionC2)

        bgColorMenu = self.menu.addMenu('bg color')
        self.actionD1 = QAction('black', self)
        self.actionD2 = QAction('red', self)
        self.actionD3 = QAction('yellow', self)
        self.actionD4 = QAction('blue', self)
        self.actionD5 = QAction('orange', self)
        self.actionD6 = QAction('green', self)
        self.actionD7 = QAction('white', self)
        bgColorMenu.addAction(self.actionD1)
        bgColorMenu.addAction(self.actionD2)
        bgColorMenu.addAction(self.actionD3)
        bgColorMenu.addAction(self.actionD4)
        bgColorMenu.addAction(self.actionD5)
        bgColorMenu.addAction(self.actionD6)
        bgColorMenu.addAction(self.actionD7)

        bgOpacityMenu = self.menu.addMenu('bg opacity')
        self.actionE1 = QAction('increase', self)
        self.actionE2 = QAction('decrease', self)
        bgOpacityMenu.addAction(self.actionE1)
        bgOpacityMenu.addAction(self.actionE2)

        self.actionZ = QAction('quit', self)
        self.actionZ.triggered.connect(self.close)
        self.menu.addAction(self.actionZ)

        self.menu.exec(self.mapToGlobal(pos))

    def showTime(self) -> None:

        current_time = QTime.currentTime()  # get the current time
        label_time = current_time.toString('hh:mm')  # convert timer to string
        self.label.setText(label_time)  # show it to the label

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


if __name__ == '__main__':

    App = QApplication(sys.argv)
    clock = Clock()
    clock.show()  # show all the widgets
    App.exit(App.exec())  # start the app
