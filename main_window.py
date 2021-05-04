# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from FCPX_XML import FCPX_XML
from preview import Preview_UI

class MainWindow_UI(object):

    # 창 크기 초기화(가로: 800, 세로: 300)
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.xmlFilename = ''
        self.__xml_saved = True

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
        self.xmlPathText = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.xmlPathText.setReadOnly(True)
        self.xmlPathText.setObjectName("xmlPathText")
        self.xmlLayout.addWidget(self.xmlPathText)

        # xml 파일을 여는 벼튼
        # TODO: 버튼을 누르면 파일을 불러오는 기능 구현하며, xml이 아닌 경우 경고창 띄우고 불러오지 않기
        self.locateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.locateButton.setObjectName("locateButton")
        self.xmlLayout.addWidget(self.locateButton)
        self.locateButton.clicked.connect(self.fileopen)



        # 버튼 영역의 레이아웃 생성
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 140, self.__width-260, 32))
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
        self.xmlConversionButton.clicked.connect(self.xmlConversion)
        # 위 버튼을 누르면 XML 변환이 시작된다.
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
        self.saveButton.clicked.connect(self.filesave)

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
        

    # "경로지정" 버튼을 누르면 XML 파일을 지정하는 함수 - XML 파일만 불러오도록 지정
    def fileopen(self):
        try:
            if (self.__xml_saved == False):
                xmlSaveMessage = QtWidgets.QMessageBox()
                xmlSaveMessage.setIcon(QtWidgets.QMessageBox.Warning)
                xmlSaveMessage.setWindowTitle('XML vkdlf wjwkd')
                xmlSaveMessage.setText('''변환된 XML 파일이 저장되지 않았습니다.
                    저장하시려면 저장을, 저장하지 않고 파일을 불러오시려면 ?를 눌러주세요.
                    불러오기를 취소하려면 취소를 눌러주세요
                    ''')
                xmlSaveMessage.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Discard, QtWidgets.QMessageBox.Save)
                xmlSaveMessage.setDefaultButton(QtWidgets.QMessageBox.Save)

                xmlSaveMessage.exec()
            else:
                #파일 불러오기 창을 띄워서 XML 파일 불러오기
                self.xmlFilename = QtWidgets.QFileDialog.getOpenFileName(None, "파일 열기...", filter="FCPX XML File (*.fcpxml)")
                # 파일을 사용자가 직접 선택했을 경우 수행 (선택하지 않고 취소하면 코드 실행 안함)
                if self.xmlFilename[0] != '':
                    # XML 파일이 아니면 XML 파일을 선택하라는 메시지박스 띄우기 
                    if not self.xmlFilename[0].endswith('.fcpxml') and not (self.xmlFilename[0].endswith('.xml')):
                        xmlConfirmMessage = QtWidgets.QMessageBox()
                        xmlConfirmMessage.setIcon(QtWidgets.QMessageBox.Warning)
                        xmlConfirmMessage.setWindowTitle('XML 불러오기 오류')
                        xmlConfirmMessage.setText('XML 파일이 아닙니다. 파일을 다시 선택하세요.')
                        xmlConfirmMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        xmlConfirmMessage.exec()
                    else:    
                        self.xmlPathText.setText(self.xmlFilename[0])
                        self.fcpx_xml = FCPX_XML(self.xmlFilename[0])
                     
            
        # 파일 불러오는 과정에서 오류가 발생하면 파일 불러오기 오류 메시지 박스 띄우기 
        except Exception:
            # fileErrorMessage = QtWidgets.QMessageBox()
            # fileErrorMessage.setIcon(QtWidgets.QMessageBox.Critical)
            # fileErrorMessage.setWindowTitle('파일 불러오기 오류')
            # fileErrorMessage.setText('파일을 불러오는 데 오류가 발생했습니다.')
            # fileErrorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
            # fileErrorMessage.exec()
            pass

    # "XML 버튼"을 누르면 XML 안의 자막을 감정분석해서 바꾸는 함수           
    def xmlConversion(self):
        try:
            # XMl 파일이 안 불러와진 상태에서 XML 변환 버튼을 누르면 파일 없음 메시지 박스 띄위기 
            if self.xmlFilename == '':
                raise FileNotFoundError

            self.fcpx_xml.xml_text_analysis()
            # 변환된 xml 저장상태를 저장 안됨(False)로 변경
            self.__xml_saved = False
            # XML 변환완료 메시지박스
            xmlCompleteMessageBox = QtWidgets.QMessageBox()
            xmlCompleteMessageBox.setIcon(QtWidgets.QMessageBox.Information)
            xmlCompleteMessageBox.setWindowTitle('XML 변화 완료')
            xmlCompleteMessageBox.setText('자막의 감정을 분석하여 XML 파일 변환이 완료되었습니다')
            xmlCompleteMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            xmlCompleteMessageBox.exec()

        # XML 파일을 불러오지 않았을 경우 메시지 박스 
        except FileNotFoundError:
            xmlConversionError = QtWidgets.QMessageBox()
            xmlConversionError.setIcon(QtWidgets.QMessageBox.Warning)
            xmlConversionError.setWindowTitle('XML 파일 불러오기 오류')
            xmlConversionError.setText('XML 파일을 찾지 못했습니다. \nXML 파일을 불러온 다음 다시 시도하세요.')
            xmlConversionError.setStandardButtons(QtWidgets.QMessageBox.Ok)
            xmlConversionError.exec()


        # XML 변동 오류가 발생했을 경우 오류 발생 메시지박스 띄우기
        except Exception:
            xmlConversionError = QtWidgets.QMessageBox()
            xmlConversionError.setIcon(QtWidgets.QMessageBox.Critical)
            xmlConversionError.setWindowTitle('XML 변환 오류')
            xmlConversionError.setText('XML로 변환하는 데 오류가 발생했습니다')
            xmlConversionError.setStandardButtons(QtWidgets.QMessageBox.Ok)
            xmlConversionError.exec()
    
       # "저장" 버튼을 누르면 XML 파일을 저장하는 함수 - 새로 바뀐 XML 파일만 저장하도록 지정 
    def filesave(self):
        try:
            # XML 파일이 없는 경우 처리
            if self.xmlFilename == '':
                raise FileNotFoundError

            # 변경된 xml 트리 가져오기(분석이 다 끝났으면 XML 트리를 리턴, 분석이 덜 됐으면 None을 리턴) 
            xml_tree = self.fcpx_xml.write_xml()

            # XML 파일 분석이 되지 않는 경우 
            if xml_tree == None:
                raise AttributeError

            #파일 불러오기 창을 띄워서 XML 파일 불러오기
            filename = QtWidgets.QFileDialog.getSaveFileName(None, "파일 저장...", filter="FCPX XML File (*.fcpxml)")

            # 취소를 눌러서 저장을 취소하지 않았으면 파일을 정상적으로 저장
            if filename[0] != '':
                # 파일 이름이 .fcpxml로 안 끝나면 뒤에 '.fcpxml' 붙여줌
                if not filename[0].endswith('.fcpxml') : 
                    filename = filename[0] + '.fcpxml'
                else:
                    filename = filename[0]
                # xml 파일 저장 
                xml_tree.write(filename, encoding="utf8", xml_declaration=True)

                # xml 저장 상태를 저장됨(True)으로 변경
                self.__xml_saved = True

        # XML 파일이 분석이 안 된 경우 메시지박스
        # 파일을 불러온 상태에서 바로 저장 버튼을 누르면 AttributeError가 뜸
        except AttributeError:
            fileErrorMessage = QtWidgets.QMessageBox()
            fileErrorMessage.setIcon(QtWidgets.QMessageBox.Warning)
            fileErrorMessage.setWindowTitle('XML 분석이 완료되지 않음')
            fileErrorMessage.setText('XML 파일이 분석되지 않았습니다.\n다시 한 번 시도해보세요.')
            fileErrorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
            fileErrorMessage.exec()

        # 파일을 안 불러왔을 때 메시지박스
        except FileNotFoundError:
            fileErrorMessage = QtWidgets.QMessageBox()
            fileErrorMessage.setIcon(QtWidgets.QMessageBox.Warning)
            fileErrorMessage.setWindowTitle('파일 저장 오류')
            fileErrorMessage.setText('XML 파일을 찾을 수 없습니다. \nXML 파일을 불러오고 변환 버튼을 누른 다음 다시 시도해보세요')
            fileErrorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
            fileErrorMessage.exec()

        # XML 파일이 분석이 안 된 경우 메시지박스 
        # 왜 Attribute를 했어요? A: 파일을 불러온 상태에서 바로 저장 버튼을 누르면 AttributeError가 뜸 
        except AttributeError:
            fileErrorMessage = QtWidgets.QMessageBox()
            fileErrorMessage.setIcon(QtWidgets.QMessageBox.Warning)
            fileErrorMessage.setWindowTitle('XML 분석이 완료되지 않음')
            fileErrorMessage.setText('XML 파일이 분석되지 않았습니다..\n다시 한번 시도해주세요')
            fileErrorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
            fileErrorMessage.exec()
            
        # 파일 저장하는 과정에서 오류가 발생하면 오류 메시지 박스 띄우기 
        # except Exception:
        #     fileErrorMessage = QtWidgets.QMessageBox()
        #     fileErrorMessage.setIcon(QtWidgets.QMessageBox.Critical)
        #     fileErrorMessage.setWindowTitle('파일 저장 오류')
        #     fileErrorMessage.setText('파일을 저장하는 데 오류가 발생했습니다.')
        #     fileErrorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
        #     fileErrorMessage.exec()
        


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
    
