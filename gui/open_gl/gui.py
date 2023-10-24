#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
from PyQt5 import QtGui,QtCore,QtWidgets

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtOpenGL import *

import read_stl
import numpy as np

RED_COLOR =     [255, 92, 92]
GREEN_COLOR =   [57, 217, 138]
BLUE_COLOR =    [91, 141, 236]
ORANGE_COLOR =  [253, 172, 66]
YELLOW_COLOR =  [255, 255, 51]
PURPLE_COLOR =  [75, 0, 130]
MAROON_COLOR =  [222, 184, 135]
WHITE_COLOR =   [255, 255, 255]

class InvalidValue(Exception):
    def __init__(self):
        Exception.__init__(self, "Not real solution")

class GlWidget(QGLWidget):
    xRotationChanged = QtCore.pyqtSignal(int)
    yRotationChanged = QtCore.pyqtSignal(int)
    zRotationChanged = QtCore.pyqtSignal(int)

    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(600, 600)
        self.base = read_stl.loader('./Cad/base.stl')
        self.link_1 = read_stl.loader('./Cad/link_1.stl')
        self.link_2 = read_stl.loader('./Cad/link_2.stl')
        self.link_3 = read_stl.loader('./Cad/link_3.stl')

        self.x_view = 100
        self.y_view = 100
        self.z_view = 100
        self.w = 0
        self.h = 0

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        self.drawGL()
        glPopMatrix()

    def drawGL(self):  
        glPushMatrix()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.drawGrid()

        glBegin(GL_LINES)
        # X axis
        self.setupColor(RED_COLOR)
        glVertex3f(200,0,0)
        glVertex3f(0,0,0)
        # Y axis
        self.setupColor(GREEN_COLOR)
        glVertex3f(0,200,0)
        glVertex3f(0,0,0)
        # Z axis
        self.setupColor(BLUE_COLOR)
        glVertex3f(0,0,200)
        glVertex3f(0,0,0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        self.setupColor(RED_COLOR)
        glRotated(90, 1.0, 0.0, 0.0)
        glTranslated(0, 32, 0)
        self.base.draw()
        glPopMatrix()

        glPushMatrix()
        self.setupColor([255,0,0])
        glRotated(90, 1.0, 0.0, 0.0)
        glTranslated(0, 32, 2)
        self.link_1.draw()
        glPopMatrix()

        glPushMatrix()
        self.setupColor([0,0,255])
        glRotated(90, 1.0, 0.0, 0.0)
        self.link_2.draw()
        glPopMatrix()

        glPushMatrix()
        self.setupColor([0,255,0])
        glRotated(90, 1.0, 0.0, 0.0)
        self.link_3.draw()
        glPopMatrix()

    def resizeGL(self, w, h):
        self.w = w
        self.h = h
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w/h, 1, 1000.0)
        gluLookAt(self.x_view, self.y_view, self.z_view, 0, 0, 0, 0, 0.0, 40.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def font_view(self):
        self.x_view = 100
        self.y_view = 0
        self.z_view = 0
        self.resizeGL(self.w, self.h)
        self.updateGL()

    def right_side_view(self):
        self.x_view = 100
        self.y_view = 100
        self.z_view = 0
        self.resizeGL(self.w, self.h)
        self.updateGL()
        
    def top_view(self):
        self.x_view = 0
        self.y_view = 100
        self.z_view = 0
        self.resizeGL(self.w, self.h)
        self.updateGL()

    def initializeGL(self):
        ambientLight = [0.7, 0.7, 0.7, 1.0]
        diffuseLight = [0.7, 0.8, 0.8, 1.0]
        specularLight = [0.4, 0.4, 0.4, 1.0]
        positionLight = [20.0, 20.0, 20.0, 0.0]

        glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
        glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight)
        glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, 1.0)
        glLightfv(GL_LIGHT0, GL_POSITION, positionLight)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glEnable(GL_BLEND)
        glClearColor(1.0, 1.0, 1.0, 1.0)

    def drawGrid(self):
        glPushMatrix()
        glLineWidth(2)
        color = [8.0/255, 108.0/255, 162.0/255]
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color)
        step = 10
        num = 10
        for i in range(-num, num+1):
            glBegin(GL_LINES)
            glVertex3f(i*step, -num * step, 0)
            glVertex3f(i*step, num*step, 0)
            glVertex3f(-num * step, i*step, 0)
            glVertex3f(num*step, i*step, 0)
            glEnd()
        glPopMatrix()

    def setupColor(self, color):
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [color[0]/255.0, color[1]/255.0, color[2]/255.0])

class MainWindow(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.resize(1500, 800)
        self.open_gl = GlWidget(self)

        self.font_view = QtWidgets.QPushButton("A")
        self.font_view.clicked.connect(self.reload_font_view)

        self.right_side_view = QtWidgets.QPushButton("C")
        self.right_side_view.clicked.connect(self.reload_right_side_view)

        self.top_view = QtWidgets.QPushButton("B")
        self.top_view.clicked.connect(self.reload_top_view)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.open_gl)

        box = QtWidgets.QHBoxLayout()
        box.addWidget(self.font_view)
        box.addWidget(self.right_side_view)
        box.addWidget(self.top_view)

        layout.addLayout(box)

    def reload_font_view(self):
        self.open_gl.font_view()

    def reload_right_side_view(self):
        self.open_gl.right_side_view()

    def reload_top_view(self):
        self.open_gl.top_view()    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
