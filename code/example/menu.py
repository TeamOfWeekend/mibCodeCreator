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


class Example(QMainWindow):
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
        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

    def init_statusbar(self):
        """
        初始化状态栏
        :return:
        """
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

    def init_menu(self):
        """
        初始化菜单栏
        :return:
        """
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)         # 新建子菜单
        impAct = QAction('Import mail', self)   # 新建动作菜单
        impMenu.addAction(impAct)               # 将动作菜单添加到子菜单
        newAct = QAction('New', self)

        fileMenu.addAction(newAct)              # 增加子动作菜单
        fileMenu.addMenu(impMenu)               # 增加子菜单

        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

    def init_UI(self):
        """
        初始化窗体UI
        :return:
        """
        qw = QWidget()
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
        qw.setLayout(hbox)

        self.setCentralWidget(qw)
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Submenu')
        self.show()

    def toggleMenu(self, state):
        if state:
            print('show')
            self.statusbar.show()
        else:
            print('hide')
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
