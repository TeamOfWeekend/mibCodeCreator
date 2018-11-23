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
from PyQt5.QtWidgets import QApplication
from elements.mainWindow import My_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 所有的PyQt5应用必须创建一个应用（Application）对象
    window = My_MainWindow()
    sys.exit(app.exec())
