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

from PyQt5.QtWidgets import (QAction, qApp, QMenu)


class My_Menu():
    def __init__(self, mainWindow):
        self.init_menu(mainWindow)

    @staticmethod
    def init_menu(mainWindow):
        """
        初始化菜单栏
        :return:
        """
        menubar = mainWindow.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', mainWindow)         # 新建子菜单
        impAct = QAction('Import mail', mainWindow)   # 新建动作菜单
        impMenu.addAction(impAct)               # 将动作菜单添加到子菜单
        newAct = QAction('New', mainWindow)

        fileMenu.addAction(newAct)              # 增加子动作菜单
        fileMenu.addMenu(impMenu)               # 增加子菜单

        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', mainWindow, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(mainWindow.toggleMenu)

        viewMenu.addAction(viewStatAct)

    @staticmethod
    def contextMenuEvent(mainWindow, event):
        cmenu = QMenu(mainWindow)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(mainWindow.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()


# app = QApplication(sys.argv)
# ex = My_Meau()
# sys.exit(app.exec_())
