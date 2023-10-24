
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class weather(QtWidgets.QGroupBox):
    def __init__(self, *arg, **kwargs):
        super(weather, self).__init__()

        self.setStyleSheet("font-family: Consolas;"
                           "color: white;"
                           "background-color: #393939;"
                           "border: solid;"
                           "border-radius: 5px;")
        self.setFixedSize(300,200)
        self.la_title = QtWidgets.QLabel("Weather")
        self.la_title.setStyleSheet("font-size: 15pt;")
        self.la_img = QtWidgets.QLabel()
        self.la_img.setPixmap(QtGui.QPixmap('./image/sun_weather.png'))
        self.la_temp = QtWidgets.QLabel("15\N{DEGREE SIGN}C")
        self.la_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.la_temp.setStyleSheet("font-size: 60pt;")
        self.la_humi_num = QtWidgets.QLabel("0")
        self.la_humi_num.setAlignment(QtCore.Qt.AlignCenter)
        self.la_humi_num.setStyleSheet("font-size: 30pt;")
        self.la_humi_txt = QtWidgets.QLabel("% Humidity")
        self.la_humi_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.la_humi_txt.setStyleSheet("font-size: 20pt;")
        box = QtWidgets.QVBoxLayout(self)
        box_1 = QtWidgets.QHBoxLayout()
        box_1.addWidget(self.la_img)
        box_2 = QtWidgets.QHBoxLayout()
        box_2.addWidget(self.la_humi_num)
        box_2.addWidget(self.la_humi_txt)
        box_3 = QtWidgets.QVBoxLayout()
        box_3.addWidget(self.la_temp)
        box_3.addLayout(box_2)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(box_1)
        hbox.addLayout(box_3)
        box.addWidget(self.la_title)
        box.addLayout(hbox)

class on_off(QtWidgets.QGroupBox):
    def __init__(self, *arg, **kwargs):
        super(on_off, self).__init__()
        self.setStyleSheet("font-family: Consolas;"
                           "color: white;"
                           "background-color: #393939;"
                           "border: solid;"
                           "border-radius: 5px;")
        
        title = kwargs['title']
        self.image_on = QtGui.QPixmap(kwargs['img_on'])
        self.image_off = QtGui.QPixmap(kwargs['img_off'])

        self.la_title = QtWidgets.QLabel(title)
        self.la_title.setStyleSheet("font-size: 15pt;")
        self.la_img = QtWidgets.QLabel()
        self.la_img.setPixmap(self.image_off)

        self.bt_on = QtWidgets.QPushButton(kwargs['name_on'])
        self.bt_on.setStyleSheet(
            """QPushButton {
                background-color: #444444;
                border: none;
                font-size: 15pt;
                Text-align:center;
            }
            QPushButton::hover {
                background-color: #26B1E6;
            }
            """
        )
        self.bt_off = QtWidgets.QPushButton(kwargs['name_off'])
        self.bt_off.setStyleSheet(
            """QPushButton {
                background-color: #444444;
                border: none;
                font-size: 15pt;
                Text-align:center;
            }
            QPushButton::hover {
                background-color: #26B1E6;
            }
            """
        )

        self.bt_on.clicked.connect(self.reload_light_on)
        self.bt_off.clicked.connect(self.reload_light_off)

        box = QtWidgets.QVBoxLayout(self)
        box_1 = QtWidgets.QHBoxLayout()
        box_1.addWidget(self.la_img)
        box_2 = QtWidgets.QVBoxLayout()
        box_2.addWidget(self.bt_on)
        box_2.addWidget(self.bt_off)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(box_1)
        hbox.addLayout(box_2)
        box.addWidget(self.la_title)
        box.addLayout(hbox)

    def reload_light_on(self):
        self.la_img.setPixmap(self.image_on)

    def reload_light_off(self):
        self.la_img.setPixmap(self.image_off)

class circular_progress(QtWidgets.QWidget):
    def __init__(self, *arg, **kwargs):
        super(circular_progress, self).__init__()

        # CUSTOM PROPERTIES
        self.value = 25
        self.width = 150
        self.height = 150
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.max_value = 100
        self.progress_color = 0x26B1E6
        # Text
        self.enable_text = True
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0xffffff
        # BG
        self.enable_bg = True
        self.bg_color = 0x545454

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.setFixedSize(self.width, self.height)

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()  # Render progress bar after change value

    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, e):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        # PAINTER
        paint = QPainter()
        paint.begin(self)

        # remove pixelated edges
        paint.setRenderHint(QPainter.Antialiasing)  
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PEN
        pen = QPen()
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(int(margin), int(margin), int(width), int(height), 0, 360 * 16)

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(int(margin), int(margin), int(width), int(height), 90 * 16, int(-value * 16))

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # END
        paint.end()

class circle_bar(QtWidgets.QWidget):
    def __init__(self, *arg, **kwargs):
        super(circle_bar, self).__init__()
        self.setFixedSize(200,200)

        self.la_title = QtWidgets.QLabel(kwargs["title"])
        self.la_title.setStyleSheet("font-size: 15pt;")
        self.circle = circular_progress()

        box = QtWidgets.QVBoxLayout(self)
        box.addWidget(self.la_title)
        box.addWidget(self.circle)

class power_gas(QtWidgets.QGroupBox):
    def __init__(self, *arg, **kwargs):
        super(power_gas, self).__init__()
        self.setStyleSheet("font-family: Consolas;"
                           "color: white;"
                           "background-color: #393939;"
                           "border: solid;"
                           "border-radius: 5px;")
         
        self.bar_power = circle_bar(title = "Power")
        self.bar_gas = circle_bar(title = "Gas")

        box = QtWidgets.QHBoxLayout(self)
        box.addWidget(self.bar_power)
        box.addWidget(self.bar_gas)
        box.setContentsMargins(0, 0, 0, 0)
        
class bt_for_control(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(bt_for_control, self).__init__()
        self.setFixedSize(50,50)
        self.setMouseTracking(True)
        self.bt = QtWidgets.QPushButton()
        self.bt.setIcon(QtGui.QIcon(kwargs['icon']))
        self.bt.setIconSize(QSize(50, 50))
        self.bt.setStyleSheet(
            """QPushButton {
                padding : 0px 0px 10px 0px;
                background-color: #444444;
                border: none;
            }
            QPushButton::hover {
                background-color: #DEDEDF;
            }
            """
        )
        box = QtWidgets.QVBoxLayout(self)
        box.addWidget(self.bt)
        box.setContentsMargins(0, 0, 0, 0)

class bts_control(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(bts_control, self).__init__()
        self.setStyleSheet("background-color: #444444")

        self.setMouseTracking(True)
        self.bt_0 = bt_for_control(icon = './image/bt_0.png')
        self.bt_1 = bt_for_control(icon = './image/bt_1.png')
        self.bt_2 = bt_for_control(icon = './image/bt_2.png')
        self.bt_3 = bt_for_control(icon = './image/bt_3.png')
        self.bt_4 = bt_for_control(icon = './image/bt_4.png')
        self.bt_5 = bt_for_control(icon = './image/bt_5.png')
        self.bt_6 = bt_for_control(icon = './image/bt_6.png')
        self.bt_7 = bt_for_control(icon = './image/bt_7.png')

        box = QtWidgets.QHBoxLayout(self)
        box.addStretch(1)
        box.addWidget(self.bt_0)
        box.addWidget(self.bt_1)
        box.addWidget(self.bt_2)
        box.addWidget(self.bt_3)
        box.addWidget(self.bt_4)
        box.addWidget(self.bt_5)
        box.addWidget(self.bt_6)
        box.addWidget(self.bt_7)
        box.addStretch(1)

class bt_for_tab(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(bt_for_tab, self).__init__()
        self.setMouseTracking(True)
        self.bt = QtWidgets.QPushButton(kwargs['title'])
        self.bt.setFixedSize(120, 50)
        self.bt.setStyleSheet(
            """QPushButton {
                background-color: #393939;
                border: none;
                font-size: 10pt;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color: #26B1E6;
            }
            """
        )
        box = QtWidgets.QVBoxLayout(self)
        box.addWidget(self.bt)
        box.setContentsMargins(0, 0, 0, 0)

class bts_tab(QtWidgets.QGroupBox):
    def __init__(self, *args, **kwargs):
        super(bts_tab, self).__init__()
        self.setStyleSheet("font-family: Consolas;"
                           "color: white;"
                           "background-color: #393939;"
                           "border: solid;"
                           "border-radius: 5px;")
    
        self.setMouseTracking(True)

        self.bt_1 = bt_for_tab(title = "Dashboard")
        self.bt_2 = bt_for_tab(title = "Scenes")
        self.bt_3 = bt_for_tab(title = "Voice Control")
        self.bt_4 = bt_for_tab(title = "Weather Station")
        self.bt_5 = bt_for_tab(title = "Multilateral")

        box = QtWidgets.QHBoxLayout(self)
        box.addWidget(self.bt_1)
        box.addWidget(self.bt_2)
        box.addWidget(self.bt_3)
        box.addWidget(self.bt_4)
        box.addWidget(self.bt_5)
        box.setContentsMargins(0, 0, 0, 0)

class gui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(gui, self).__init__()
        self.setStyleSheet("background-color: #444444")

        la_title = QtWidgets.QLabel("Dashboard")
        la_title.setStyleSheet(
            """background-color: #444444;
            border-radius: 0px;
            font-size: 20pt;
            font-weight: bold;
            color: red;
            """)
        la_image = QtWidgets.QLabel()
        la_image.setPixmap(QtGui.QPixmap('./image/bt_0.png'))

        self.form_weather = weather()
        self.form_lights = on_off(
            title="Weather", name_on = "ON", name_off = "OFF",
            img_on = "./image/light_buld_on.png", img_off = "./image/light_buld_off.png"
        )

        self.form_shutters = on_off(
            title="Shutters", name_on = "UP", name_off = "DOWN",
            img_on = "./image/shutters_on.png", img_off = "./image/shutters_off.png"
        )
        self.form_alarm_panel = on_off(
            title="Alarm Panel", name_on = "ARM", name_off = " DISARM ",
            img_on = "./image/unlock.png", img_off = "./image/lock.png"
        )
        self.form_power_gas = power_gas()
        self.form_bts_control = bts_control()
        self.form_bts_tab = bts_tab()

        layout = QtWidgets.QVBoxLayout(self)
        box = QtWidgets.QHBoxLayout()

        box1 = QtWidgets.QVBoxLayout()
        box1.addWidget(self.form_weather)
        box2 = QtWidgets.QHBoxLayout()
        box2.addWidget(self.form_lights)
        box2.addWidget(self.form_shutters)
        box1.addLayout(box2)
        box.addLayout(box1)

        box3 = QtWidgets.QVBoxLayout()
        box3.addWidget(self.form_power_gas)

        box4 = QtWidgets.QHBoxLayout()
        box4.addWidget(self.form_alarm_panel)
        box4.addStretch(1)

        box3.addLayout(box4)
        box.addLayout(box3)

        box_tab = QtWidgets.QHBoxLayout()
        box_tab.addWidget(la_image)
        box_tab.addWidget(la_title)
        box_tab.addWidget(self.form_bts_tab)

        layout.addLayout(box_tab)
        layout.addLayout(box)
        layout.addWidget(self.form_bts_control)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = gui()
    w.show()
    app.exec_()