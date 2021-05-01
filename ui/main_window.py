# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.preview import Preview_UI

class MainWindow_UI(object):

    # 창 크기 초기화(가로: 800, 세로: 300)
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # UI의 각 요소 초기화
    def setupUi(self, MainWindow):
        # 창 생성 
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(self.__width, self.__height)

        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # xml 관련 부분을 처리하는 영역의 레이아웃 생성
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 60, self.__width-180, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.xmlLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.xmlLayout.setContentsMargins(1, 2, 3, 4)
        self.xmlLayout.setObjectName("xmlLayout")

        # "xml 경로" 라벨
        self.xmlLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.xmlLabel.setObjectName("xmlLabel")
        self.xmlLayout.addWidget(self.xmlLabel)

        # xml 파일을 불러오면 텍스트박스에 경로 표시
        # TODO: 오른쪽 버튼을 눌러 파일을 불러오면 경로 표시
        self.xmlPathText = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.xmlPathText.setUndoRedoEnabled(False)
        self.xmlPathText.setReadOnly(True)
        self.xmlPathText.setObjectName("xmlPathText")
        self.xmlLayout.addWidget(self.xmlPathText)

        # xml 파일을 여는 벼튼
        # TODO: 버튼을 누르면 파일을 불러오는 기능 구현하며, xml이 아닌 경우 경고창 띄우고 불러오지 않기
        self.locateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.locateButton.setObjectName("locateButton")
        self.xmlLayout.addWidget(self.locateButton)


        # 버튼 영역의 레이아웃 생성
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 140, 521, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.buttonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")

        # XML 변환 버튼
        # TODO: XML 변환 버튼을 누르면 변환이 진행되도록 지정
        self.xmlConversionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.xmlConversionButton.setObjectName("xmlConversionButton")
        self.buttonLayout.addWidget(self.xmlConversionButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)

        # 프리뷰 창 띄우는 버튼
        # TODO: 버튼을 누르면 새로운 창이 뜨도록 지정
        self.previewButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.previewButton.setObjectName("previewButton")
        self.buttonLayout.addWidget(self.previewButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)

        # 변환된 XML 저장 버튼
        # TODO: 버튼을 누르면 수정된 XML 저장이 되도록 지정. 변환이 안 된 상태에서 버튼 누르면 메시지박스 띄우도록 지정
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem2)

        # 종료 버튼 구현
        self.quitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.quitButton.setObjectName("quitButton")
        self.buttonLayout.addWidget(self.quitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.quitButton.clicked.connect(MainWindow.close)

        # 버튼에 이름 지정 등
        self.retranslateUi(MainWindow)
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
    mainwindow_ui = MainWindow_UI(800, 300)
    mainwindow_ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    return 0

# 이 코드가 처음으로 실행될 경우 메인함수 실행
if __name__ == '__main__':
    print("program exited with code", main())
    
