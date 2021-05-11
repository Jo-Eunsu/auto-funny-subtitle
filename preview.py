# -*- coding: utf-8 -*-

# Dialog implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from xml.etree.ElementTree import XML
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from FCPX_XML import FCPX_XML

class Preview_UI(QtWidgets.QWidget):

    # 초기화: 해당 창의 크기(가로, 세로) 설정
    # 프리뷰 화면이 열릴때 XML 객체도 같이 가지고 올 수 있도록 설정 
    def __init__(self, xml: FCPX_XML, width=800, height=500):
        super().__init__()
        self.__width = width
        self.__height = height
        self.fcpx_xml: FCPX_XML = xml
        self.__xml_saved = True

        # 창 설정 후 출력
        self.setupUi()
        self.show()

    # ui 형성 (가로:900, 세로:400)
    def setupUi(self):
        # 창 자체의 설정
        self.setObjectName("Dialog")
        self.setFixedSize(self.__width, self.__height)

        # TODO: 해당 UI는 영상에 들어간 자막 클립에 따라 가변적인 구조를 가지고 있음. 가변적인 구조의 창 필요
        # TODO: GridLayout 여러 개를 하나의 verticalLayout에 집어넣은 다음 scroolArea로 영역 제한을 할 필요가 있음

        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.setFont(font)

        # 레이아웃이 창 안으로 들어감 (전체 레이아웃)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        # 스크롤 가능한 영역 삽입
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # 버튼영역과 자막들 들어갈 영역을 나누는 세로 배치 레이아웃 설정
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")

        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_35.addWidget(self.label_34)
        self.gridLayout_8.addLayout(self.horizontalLayout_35, 2, 1, 1, 1)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.titleText_8 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.titleText_8.setObjectName("titleText_8")
        self.horizontalLayout_36.addWidget(self.titleText_8)
        self.gridLayout_8.addLayout(self.horizontalLayout_36, 2, 5, 1, 1)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_37.addWidget(self.label_35)
        self.gridLayout_8.addLayout(self.horizontalLayout_37, 1, 1, 1, 1)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.templateSelector_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.templateSelector_8.setObjectName("templateSelector_8")
        self.horizontalLayout_38.addWidget(self.templateSelector_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem3)
        self.gridLayout_8.addLayout(self.horizontalLayout_38, 1, 5, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_8.addWidget(self.label_36, 1, 4, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 2, 4, 1, 1)
        self.startTimeText_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.startTimeText_8.setObjectName("startTimeText_8")
        self.gridLayout_8.addWidget(self.startTimeText_8, 1, 2, 1, 1)
        self.endTimeText_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.endTimeText_8.setObjectName("endTimeText_8")
        self.gridLayout_8.addWidget(self.endTimeText_8, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 2, 3, 1, 1)
        self.horizontalLayout_34.addLayout(self.gridLayout_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem6)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_34.addWidget(self.label_38)
        self.verticalLayout.addLayout(self.horizontalLayout_34)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.titleText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.titleText.setObjectName("titleText")
        self.horizontalLayout_4.addWidget(self.titleText)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 5, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.templateSelector = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.templateSelector.setObjectName("templateSelector")
        self.horizontalLayout_6.addWidget(self.templateSelector)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)
        self.startTimeText = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.startTimeText.setObjectName("startTimeText")
        self.gridLayout.addWidget(self.startTimeText, 1, 2, 1, 1)
        self.endTimeText = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.endTimeText.setObjectName("endTimeText")
        self.gridLayout.addWidget(self.endTimeText, 2, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_15.addWidget(self.label_14)
        self.gridLayout_4.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.titleText_4 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.titleText_4.setObjectName("titleText_4")
        self.horizontalLayout_16.addWidget(self.titleText_4)
        self.gridLayout_4.addLayout(self.horizontalLayout_16, 2, 5, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.gridLayout_4.addLayout(self.horizontalLayout_17, 1, 1, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.templateSelector_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.templateSelector_4.setObjectName("templateSelector_4")
        self.horizontalLayout_18.addWidget(self.templateSelector_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem11)
        self.gridLayout_4.addLayout(self.horizontalLayout_18, 1, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 4, 1, 1)
        self.startTimeText_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.startTimeText_4.setObjectName("startTimeText_4")
        self.gridLayout_4.addWidget(self.startTimeText_4, 1, 2, 1, 1)
        self.endTimeText_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.endTimeText_4.setObjectName("endTimeText_4")
        self.gridLayout_4.addWidget(self.endTimeText_4, 2, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 1, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 2, 3, 1, 1)
        self.horizontalLayout_14.addLayout(self.gridLayout_4)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_14.addWidget(self.label_18)
        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_20.addWidget(self.label_19)
        self.gridLayout_5.addLayout(self.horizontalLayout_20, 2, 1, 1, 1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.titleText_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.titleText_5.setObjectName("titleText_5")
        self.horizontalLayout_21.addWidget(self.titleText_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_21, 2, 5, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_22.addWidget(self.label_20)
        self.gridLayout_5.addLayout(self.horizontalLayout_22, 1, 1, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.templateSelector_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.templateSelector_5.setObjectName("templateSelector_5")
        self.horizontalLayout_23.addWidget(self.templateSelector_5)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem15)
        self.gridLayout_5.addLayout(self.horizontalLayout_23, 1, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 2, 4, 1, 1)
        self.startTimeText_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.startTimeText_5.setObjectName("startTimeText_5")
        self.gridLayout_5.addWidget(self.startTimeText_5, 1, 2, 1, 1)
        self.endTimeText_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.endTimeText_5.setObjectName("endTimeText_5")
        self.gridLayout_5.addWidget(self.endTimeText_5, 2, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 1, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem17, 2, 3, 1, 1)
        self.horizontalLayout_19.addLayout(self.gridLayout_5)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem18)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_19.addWidget(self.label_23)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_25.addWidget(self.label_24)
        self.gridLayout_6.addLayout(self.horizontalLayout_25, 2, 1, 1, 1)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.titleText_6 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.titleText_6.setObjectName("titleText_6")
        self.horizontalLayout_26.addWidget(self.titleText_6)
        self.gridLayout_6.addLayout(self.horizontalLayout_26, 2, 5, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_27.addWidget(self.label_25)
        self.gridLayout_6.addLayout(self.horizontalLayout_27, 1, 1, 1, 1)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.templateSelector_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.templateSelector_6.setObjectName("templateSelector_6")
        self.horizontalLayout_28.addWidget(self.templateSelector_6)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem19)
        self.gridLayout_6.addLayout(self.horizontalLayout_28, 1, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 1, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 2, 4, 1, 1)
        self.startTimeText_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.startTimeText_6.setObjectName("startTimeText_6")
        self.gridLayout_6.addWidget(self.startTimeText_6, 1, 2, 1, 1)
        self.endTimeText_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.endTimeText_6.setObjectName("endTimeText_6")
        self.gridLayout_6.addWidget(self.endTimeText_6, 2, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem20, 1, 3, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem21, 2, 3, 1, 1)
        self.horizontalLayout_24.addLayout(self.gridLayout_6)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem22)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_24.addWidget(self.label_28)
        self.verticalLayout.addLayout(self.horizontalLayout_24)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        # 버튼 2개가 들어갈 레이아웃 설정하고 안에다가 스페이서 3개, 버튼 2개 집어넣음

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_10.addWidget(self.closeButton)
        self.closeButton.setText('닫기')
        self.closeButton.released.connect(QtCore.QCoreApplication.instance().quit)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(spacerItem1)
        self.saveButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_10.addWidget(self.saveButton)
        self.saveButton.setText('저장')

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "XML 프리뷰"))
        self.label_34.setText(_translate("Dialog", "끝"))
        self.label_35.setText(_translate("Dialog", "시작"))
        self.label_36.setText(_translate("Dialog", "자막 템플릿"))
        self.label_37.setText(_translate("Dialog", "자막 텍스트"))
        self.label_38.setText(_translate("Dialog", "Preview Image (Alternative Text)"))
        self.label_3.setText(_translate("Dialog", "끝"))
        self.label_2.setText(_translate("Dialog", "시작"))
        self.label_5.setText(_translate("Dialog", "자막 템플릿"))
        self.label_4.setText(_translate("Dialog", "자막 텍스트"))
        self.label.setText(_translate("Dialog", "Preview Image (Alternative Text)"))
        self.label_14.setText(_translate("Dialog", "끝"))
        self.label_15.setText(_translate("Dialog", "시작"))
        self.label_16.setText(_translate("Dialog", "자막 템플릿"))
        self.label_17.setText(_translate("Dialog", "자막 텍스트"))
        self.label_18.setText(_translate("Dialog", "Preview Image (Alternative Text)"))
        self.label_19.setText(_translate("Dialog", "끝"))
        self.label_20.setText(_translate("Dialog", "시작"))
        self.label_21.setText(_translate("Dialog", "자막 템플릿"))
        self.label_22.setText(_translate("Dialog", "자막 텍스트"))
        self.label_23.setText(_translate("Dialog", "Preview Image (Alternative Text)"))
        self.label_24.setText(_translate("Dialog", "끝"))
        self.label_25.setText(_translate("Dialog", "시작"))
        self.label_26.setText(_translate("Dialog", "자막 템플릿"))
        self.label_27.setText(_translate("Dialog", "자막 텍스트"))
        self.label_28.setText(_translate("Dialog", "Preview Image (Alternative Text)"))

    # 창을 닫으려 할 때 저장하지 않았으면 저장할 것인지 물음
    def closeEvent(self, event):
        # 테스트용
        self.__xml_saved = False
        if self.__xml_saved is True:
            event.accept()
        else:
            buttonSelected = QtWidgets.QMessageBox.question(self, '수정된 자막이 저장되지 않음', '수정된 자막 파일이 저장되지 않았습니다.\n저장하고 종료하시려면 Save를, 저장하지 않고 종료하시려면 Discard를 눌러주세요.\n종료를 취소하려면 Cancel을 눌러주세요.', QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
            if buttonSelected == QtWidgets.QMessageBox.Save: 
                #self.filesave()
                event.accept()
            elif buttonSelected == QtWidgets.QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()


# 메인함수 실행
def main() -> int:
    app = QtWidgets.QApplication(sys.argv)
    preview_ui = Preview_UI("contest_woowakgood.fcpxml", 800, 500)
    sys.exit(app.exec_())

    return 0

# 이 코드가 처음으로 실행될 경우 메인함수 실행
if __name__ == '__main__':
    print("program exited with code", main())
    
