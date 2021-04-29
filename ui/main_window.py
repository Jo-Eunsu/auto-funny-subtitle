# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(self.__width, self.__height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 60, 611, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.xmlLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.xmlLayout.setContentsMargins(1, 2, 3, 4)
        self.xmlLayout.setObjectName("xmlLayout")
        self.xmlLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.xmlLabel.setObjectName("xmlLabel")
        self.xmlLayout.addWidget(self.xmlLabel)
        self.xmlPathText = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.xmlPathText.setUndoRedoEnabled(False)
        self.xmlPathText.setReadOnly(True)
        self.xmlPathText.setObjectName("xmlPathText")
        self.xmlLayout.addWidget(self.xmlPathText)
        self.locateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.locateButton.setObjectName("locateButton")
        self.xmlLayout.addWidget(self.locateButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 140, 521, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.buttonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.xmlConversionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.xmlConversionButton.setObjectName("xmlConversionButton")
        self.buttonLayout.addWidget(self.xmlConversionButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)
        self.previewButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.previewButton.setObjectName("previewButton")
        self.buttonLayout.addWidget(self.previewButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem2)
        self.quitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.quitButton.setObjectName("quitButton")
        self.buttonLayout.addWidget(self.quitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.xmlLabel.setText(_translate("MainWindow", "XML 경로"))
        self.locateButton.setText(_translate("MainWindow", "경로 지정..."))
        self.xmlConversionButton.setText(_translate("MainWindow", "XML 변환"))
        self.previewButton.setText(_translate("MainWindow", "프리뷰..."))
        self.saveButton.setText(_translate("MainWindow", "저장..."))
        self.quitButton.setText(_translate("MainWindow", "종료"))

# 메인함수 실행
def main() -> int:
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainwindow_ui = Ui_MainWindow(800, 300)
    mainwindow_ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    return 0

# 이 코드가 처음으로 실행될 경우 메인함수 실행
if __name__ == '__main__':
    print("program exited with code", main())
    
