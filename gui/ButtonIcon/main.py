from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

class MyButton(QtWidgets.QPushButton):

    def __init__(self, *args, **kwargs):
        super(MyButton, self).__init__()
        self.setMouseTracking(True)
        
        self.text = kwargs['connect']
        self.icon = kwargs['icon']
        self.setFixedSize(50,50)
        self.setIcon(QtGui.QIcon(self.icon))

    def mouseMoveEvent(self, event):
        if event.button() == 0:
            self.setFixedSize(100,50)
            self.setText(self.text)

class GUI(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__()

        pixmap = QtGui.QPixmap("logo.png")
        cursor = QtGui.QCursor(pixmap, 10, 10)
        QtWidgets.QApplication.setOverrideCursor(cursor)

        self.setMouseTracking(True)
        self.connect_bt = MyButton(icon='connect.png', connect = "CONNECT")
        self.config_bt = MyButton(icon='config.png', connect = "CONFIG")
        self.register_bt = MyButton(icon='register.png', connect = "REGISTER")
        self.info = MyButton(icon='info.png', connect = "INFO")

        box = QtWidgets.QVBoxLayout(self)
        box.addWidget(self.connect_bt)
        box.addWidget(self.config_bt)
        box.addWidget(self.register_bt)
        box.addWidget(self.info)
        
    def mouseMoveEvent(self, event):
        self.connect_bt.setText("")
        self.connect_bt.setFixedSize(50,50)

        self.config_bt.setText("")
        self.config_bt.setFixedSize(50,50)
        
        self.register_bt.setText("")
        self.register_bt.setFixedSize(50,50)

        self.info.setText("")
        self.info.setFixedSize(50,50)
       
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = GUI()
    w.show()
    app.exec_()