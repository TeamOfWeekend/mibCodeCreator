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

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication, QMainWindow, QAction, qApp, QMenu)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class My_StatusBar():
    def __init__(self, mainWindow):
        self.init_statusbar(mainWindow)

    @staticmethod
    def init_statusbar(mainWindow):
        """
        初始化状态栏
        :return:
        """
        mainWindow.statusbar = mainWindow.statusBar()
        mainWindow.statusbar.showMessage('Ready')


# app = QApplication(sys.argv)
# ex = My_StatusBar()
# sys.exit(app.exec_())
