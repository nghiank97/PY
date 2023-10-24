
import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class bt(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(bt, self).__init__()
        self.setFixedSize(50,50)
        self.setStyleSheet("background-color: #244442")
        self.setMouseTracking(True)

        self.la = QtWidgets.QLabel()
        self.la.setStyleSheet("background-color: red;")
        self.la.setFixedSize(50,5)

        self.bt = QtWidgets.QPushButton()
        self.bt.setIcon(QtGui.QIcon("./image/bt_0.png"))
        self.bt.setIconSize(QSize(50, 50))
        self.bt.setStyleSheet("background-color: #045B8F; border: solid")

        box = QtWidgets.QVBoxLayout(self)
        box.addWidget(self.la)
        box.addWidget(self.bt)
        box.setContentsMargins(0, 0, 0, 0)

    def mouseMoveEvent(self, event):
        if event.button() == 0:
            self.la.setStyleSheet("background-color: blue;")

class gui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(gui, self).__init__()
        self.setFixedSize(200,200)
        self.setStyleSheet("background-color: #244442")

        self.setMouseTracking(True)
        self.bt = bt()
        box = QtWidgets.QVBoxLayout(self)
        box.addWidget(self.bt)
        box.setContentsMargins(0, 0, 0, 0)

    def mouseMoveEvent(self, event):
        if event.button() == 0:
            self.bt.la.setStyleSheet("background-color: red;")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = gui()
    w.show()
    app.exec_()