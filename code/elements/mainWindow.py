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
from . import menu, statusBar, toolBar, mainWidget


class My_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_toolbar()
        self.init_statusbar()
        self.init_menu()
        self.init_UI()

    def init_toolbar(self):
        """
        初始化工具栏
        :return:
        """
        self.toolbar = toolBar.My_ToolBar(self)

    def init_statusbar(self):
        """
        初始化状态栏
        :return:
        """
        self.statusbar = statusBar.My_StatusBar(self)

    def init_menu(self):
        """
        初始化菜单栏
        :return:
        """
        menu.My_Menu(self)

    def init_UI(self):
        """
        初始化窗体UI
        :return:
        """
        self.setCentralWidget(mainWidget.My_MainWidget())
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Mib代码生成器')
        self.show()

    def toggleMenu(self, state):
        if state:
            print('show')
            # self.statusbar.show() # 问题待确认
        else:
            print('hide')
            # self.statusbar.hide() # 问题待确认

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()


# app = QApplication(sys.argv)
# ex = My_MainWindow()
# sys.exit(app.exec_())
