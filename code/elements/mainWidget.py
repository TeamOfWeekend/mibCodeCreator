#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : menu.py
@site    : 
@Time    : 2018/11/20 15:58
@Software: PyCharm Community Edition
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication, QMainWindow, QAction, qApp, QMenu)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from . import menu, statusBar, toolBar


class My_MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        """
        初始化主窗体部件UI
        :return:
        """
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)


# app = QApplication(sys.argv)
# ex = My_MainWindow()
# sys.exit(app.exec_())
