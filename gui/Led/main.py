
from PyQt5 import QtGui, QtCore, QtWidgets

class Led(QtWidgets.QWidget):
    color_on  = """
        QLabel {
            border:solid #F7B515;
            background-color: #F7B515
            }
        """
    color_off  = """
        QLabel {
            border:solid gray;
            background-color: gray;
            }
        """
    def __init__(self, *args, **kwargs):
        super(Led, self).__init__()

        content_la = QtWidgets.QLabel(kwargs['text'])
        content_la.setStyleSheet("font-size: 10pt;")

        self.led = QtWidgets.QLabel()
        self.led.setFixedSize(20, 20)
        self.led.setStyleSheet(self.color_off)

        self.status = QtWidgets.QLabel(kwargs['status'])
        self.status.setStyleSheet("color: #F7B515; font-size: 10pt;")

        led_layout = QtWidgets.QHBoxLayout(self)
        led_layout.addWidget(self.led)
        led_layout.addWidget(content_la)
        led_layout.addWidget(self.status)
        led_layout.setContentsMargins(0,0,0,0)

    def set_value(self, value):
        if value != 0:
            self.led.setStyleSheet(self.color_on)
        else:
            self.led.setStyleSheet(self.color_off)
    
    def set_status(self, status):
        self.status.setText(status)

class GUI(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__()
        
        
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