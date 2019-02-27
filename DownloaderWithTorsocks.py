# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloaderWithTorsocks.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re
import datetime
from os import system
import urllib3
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(766, 495)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(766, 446))
        self.centralwidget.setMaximumSize(QtCore.QSize(766, 446))
        self.centralwidget.setObjectName("centralwidget")
        self.downloadPath = QtWidgets.QLineEdit(self.centralwidget)
        self.downloadPath.setGeometry(QtCore.QRect(120, 30, 191, 31))
        self.downloadPath.setObjectName("downloadPath")
        self.link = QtWidgets.QLineEdit(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(120, 80, 191, 29))
        self.link.setObjectName("link")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 62, 17))
        self.label_2.setObjectName("label_2")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(230, 130, 81, 27))
        self.btnAdd.setObjectName("btnAdd")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(10, 330, 741, 111))
        self.log.setObjectName("log")
        self.list_of_links = QtWidgets.QTextBrowser(self.centralwidget)
        self.list_of_links.setGeometry(QtCore.QRect(330, 30, 421, 291))
        self.list_of_links.setObjectName("list_of_links")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 10, 41, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 62, 17))
        self.label_4.setObjectName("label_4")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(10, 130, 91, 27))
        self.btnStart.setObjectName("btnStart")
        self.btnDetials = QtWidgets.QPushButton(self.centralwidget)
        self.btnDetials.setGeometry(QtCore.QRect(10, 160, 92, 27))
        self.btnDetials.setObjectName("btnDetials")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 170, 51, 20))
        self.label_5.setObjectName("label_5")
        self.btnRemove = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemove.setGeometry(QtCore.QRect(140, 130, 81, 27))
        self.btnRemove.setObjectName("btnRemove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnAdd.clicked.connect(self.addLinks)
        self.btnStart.clicked.connect(self.startDownload)
        self.btnDetials.clicked.connect(self.details)
        self.btnRemove.clicked.connect(self.removeLine)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def details(self):
        self.log.append("Created by kia hamedi\nkia.arta9793@gmail.com")


    def startDownload(self):
        while True:
            app.processEvents()
            tmp = self.list_of_links.toPlainText()
            if tmp == "":
                break
            Dlink = tmp.splitlines()[0]
            self.log.append(str(datetime.datetime.now())+" : Finding server's ip")
            app.processEvents()
            system('torsocks curl https://ipinfo.io/ip > lastIp.txt')
            ip = open("lastIp.txt", "r")
            myip = ip.readline()
            print(myip)
            self.log.append(str(datetime.datetime.now())+" : Connect to ip "+str(myip))
            app.processEvents()
            time.sleep(1)
            self.log.append(str(datetime.datetime.now())+" : Start Download")
            app.processEvents()
            time.sleep(1)
            system("torsocks wget '"+Dlink+"' -P "+self.downloadPath.text()+"")
            self.log.append(str(datetime.datetime.now())+" : Downloading...")
            app.processEvents()
            tmp = self.list_of_links.toPlainText()
            if '\n' in  tmp:
                tmp = tmp.split("\n",1)[1]
            else:
                tmp = ""
            self.list_of_links.setText(tmp)
            self.log.append(str(datetime.datetime.now())+" : Download Complated")
            app.processEvents()
            time.sleep(1)


    def addLinks(self):
        self.list_of_links.append(self.link.text())
        self.link.setText("")
        self.log.append(str(datetime.datetime.now())+" : Add new download's link")

    def removeLine(self):
        self.log.append(str(datetime.datetime.now())+" : Remove last download's link from list")
        tmp = self.list_of_links.toPlainText()
        if '\n' in  tmp:
            tmp = tmp.rsplit("\n",1)[0]
        else:
            tmp = ""
        self.list_of_links.setText(tmp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloader with Torsocks"))
        self.downloadPath.setText(_translate("MainWindow", "/home/kia/Downloads"))
        self.label.setText(_translate("MainWindow", "Download Path:"))
        self.label_2.setText(_translate("MainWindow", "Link:"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "LINKS"))
        self.label_4.setText(_translate("MainWindow", "Logs:"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnDetials.setText(_translate("MainWindow", "Details"))
        self.label_5.setText(_translate("MainWindow", "v 1.0.0"))
        self.btnRemove.setText(_translate("MainWindow", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

