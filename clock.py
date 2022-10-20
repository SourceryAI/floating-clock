# importing required librarie
import sys

from PySide6.QtCore import Qt, QTime, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class Clock(QWidget):

    def __init__(self):

        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60

        self.initUI()

    def initUI(self):

        # geometry of main window
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.setWindowOpacity(0.5)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # font
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(60)
        font.setBold(True)

        # label object
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0,0,0);")
        # self.label.setAutoFillBackground(True)

        # layout
        layout = QVBoxLayout()
        # add label to the layout
        layout.addWidget(self.label)
        self.setLayout(layout)

        # timer object
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        # update the timer every second
        timer.start(1000)
        self.show()

    # method called by timer
    def showTime(self):
        # getting current time
        current_time = QTime.currentTime()
        # converting QTime object to string
        label_time = current_time.toString('hh:mm')

        # show it to the label
        self.label.setText(label_time)


if __name__ == '__main__':
    # app
    App = QApplication(sys.argv)
    # window
    clock = Clock()

    # show all the widgets
    clock.show()

    # start the app
    App.exit(App.exec())
