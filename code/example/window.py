#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : button_msg.py
@site    :
@Time    : 2018/11/20 15:08
@Software: PyCharm Community Edition
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QIcon


# demo_2:显示一个窗体，设置一个图标
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):   # 定义初始化界面的方法
        self.resize(500, 300)
        self.setWindowTitle('带图标窗体')
        # self.move(300,300)
        self.center()
        self.setWindowIcon(QIcon('images/beauty.jpg')) # 设置窗体标题图标
        self.show()

    def center(self):
        """
        居中显示窗口
        :return:
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QApplication(sys.argv)  # 所有的PyQt5应用必须创建一个应用（Application）对象
window = Window()
sys.exit(app.exec())
