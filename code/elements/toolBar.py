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


class My_ToolBar():
    def __init__(self, mainWindow):
        self.init_toolbar(mainWindow)

    @staticmethod
    def init_toolbar(mainWindow):
        """
        初始化工具栏
        :return:
        """
        exitAct = QAction(QIcon('exit24.png'), 'Exit', mainWindow)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        mainWindow.toolbar = mainWindow.addToolBar('Exit')
        mainWindow.toolbar.addAction(exitAct)


# app = QApplication(sys.argv)
# ex = My_ToolBar()
# sys.exit(app.exec_())
