# -*- coding: utf-8 -*-

# Dialog implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from xml.etree.ElementTree import Element, XML
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, copy
from FCPX_XML import FCPX_XML

class Preview_UI(QtWidgets.QWidget):

    # 초기화: 해당 창의 크기(가로, 세로) 설정
    # 프리뷰 화면이 열릴때 XML 객체도 같이 가지고 올 수 있도록 설정 
    def __init__(self, xml: FCPX_XML, width=800, height=500):
        super().__init__()
        self.__width = width
        self.__height = height
        self.fcpx_xml: FCPX_XML = xml
        self.modified_xml = copy.deepcopy(self.fcpx_xml)
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
        # 레이아웃이 창 안으로 들어감 (전체 레이아웃) - 자막들과 버튼들을 구분하는 영역
        self.wholeLayout = QtWidgets.QVBoxLayout(self)
        self.wholeLayout.setObjectName("wholeLayout")
        
        # 스크롤 가능한 영역 삽입
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.wholeLayout.addWidget(self.scrollArea)

        # 자막들이 들어가는 세로 배치 레이아웃 설정
        self.multipleTitleLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.multipleTitleLayout.setObjectName("verticalLayout")

        # 각 예능자막 텍스트 태그를 불러오고, 요소를 불러와 UI에 적용하는 과정(Initialize)
        self.initializeTitles()

        # 버튼 2개가 들어갈 레이아웃 설정하고 안에다가 스페이서 3개, 버튼 2개 집어넣음

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("horizontalLayout_10")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.buttonLayout.addItem(spacerItem)

        self.closeButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.closeButton.setObjectName("closeButton")
        self.buttonLayout.addWidget(self.closeButton)
        self.closeButton.setText('닫기')
        self.closeButton.released.connect(self.close)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.buttonLayout.addItem(spacerItem1)

        self.saveButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        self.saveButton.setText('저장')
        self.saveButton.clicked.connect(self.close)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.buttonLayout.addItem(spacerItem2)

        self.wholeLayout.addLayout(self.buttonLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "XML 프리뷰"))

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


    # 예능자막 태그를 전부 불러와서 UI에 적용시키는 함수
    def initializeTitles(self):
        # 텍스트박스와 프리뷰 이미지 라벨을 리스트로 초기화
        self.startLineEditList = self.endLineEditList = self.templateSelectorList = self.titlePlainTextEdits = self.previewLabelList = []
        self.startHHLineEditList = self.startMMLineEditList = self.startSSLineEditList = self.startMSLineEditList = []
        self.endHHLineEditList = self.endMMLineEditList = self.endSSLineEditList = self.endMSLineEditList = []

        # 모든 변환된 예능자막 템플릿 태그(<video> 태그)를 불러오기
        self.videoElements = self.modified_xml.loadAllVideoElements()
            
        videoElement: Element = None #타입 지정 
        for videoElement in self.videoElements:

            # 시작, 끝, 자막템플릿 종류, 자막 텍스트 등 정보를 UI에 표시
            # 전체 레이아웃
            self.titleWholeLayout = QtWidgets.QHBoxLayout()
            self.titleWholeLayout.setObjectName("titleWholeLayout")

            # 시작~자막텍스트 레이아웃
            self.titleGridLayout = QtWidgets.QGridLayout()
            self.titleGridLayout.setObjectName("titleGridLayout")

            # 시작 부분 레이아웃
            self.startHLayout = QtWidgets.QHBoxLayout()
            self.startHLayout.setObjectName("startHLayout")

            # '시작' 라벨
            self.startLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setFamily("Apple SD Gothic Neo")
            self.startLabel.setFont(font)
            self.startLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.startLabel.setObjectName("startLabel")
            self.startLabel.setText("시작")
            self.startHLayout.addWidget(self.startLabel)
            self.startHLayout.setObjectName('startHLayout')
            self.titleGridLayout.addLayout(self.startHLayout, 1, 1, 1, 1)

            # 시작 시각 (시:분:초:1/100초)을 표시하고 수정할 수 있는 라인에디트 박스
            # TODO: 시작 시각을 video태그에서 검색한 다음 계산해서 settext 명령어로 텍스트를 삽입
            self.startLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
            self.startLayout.setObjectName("startLayout")
            self.startLayout.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.titleGridLayout.addLayout(self.startLayout, 1, 2, 1, 1)

            #시작 시간을 직접 계산해서 텍스트 박스애 넣어 주기
            offset_attrib = videoElement['node'].attrib['offset']                           #'161300/2997s'
            offset_attrib = offset_attrib.rstrip('s')                               #'161300/2997'
            start_numbers = offset_attrib .split('/')                               #['161300, '2997']
            dividend, divisor = int(start_numbers[0]), int(start_numbers[1])        #dividend = 161300, divisor = 2997
            start_second = dividend / divisor

            # 시작 시간, 분, 초, 밀리초 부분을 따로 라인에디트로 만듬
            hh, mm, ss, ms = self.secondsToHMSSTuple(start_second)
            self.startHHLineEditList.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
            self.startHHLineEditList[-1].setAlignment(QtCore.Qt.AlignRight)
            self.startHHLineEditList[-1].setText(hh)
            self.startLayout.addWidget(self.startHHLineEditList[-1])
            
            self.startTimeDividor1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.startTimeDividor1.setText(":")
            self.startLayout.addWidget(self.startTimeDividor1)

            self.startMMLineEditList.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
            self.startMMLineEditList[-1].setAlignment(QtCore.Qt.AlignRight)
            self.startMMLineEditList[-1].setText(mm)
            self.startLayout.addWidget(self.startMMLineEditList[-1])

            self.startTimeDividor2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.startTimeDividor2.setText(":")
            self.startLayout.addWidget(self.startTimeDividor2)

            self.startSSLineEditList.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
            self.startSSLineEditList[-1].setAlignment(QtCore.Qt.AlignRight)
            self.startSSLineEditList[-1].setText(ss)
            self.startLayout.addWidget(self.startSSLineEditList[-1])

            self.startTimeDividor3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.startTimeDividor3.setText(".")
            self.startLayout.addWidget(self.startTimeDividor3)

            self.startMSLineEditList.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
            self.startMSLineEditList[-1].setAlignment(QtCore.Qt.AlignRight)
            self.startMSLineEditList[-1].setText(ms)
            self.startLayout.addWidget(self.startMSLineEditList[-1])


            # '끝' 라벨
            self.endHLayout = QtWidgets.QHBoxLayout()
            self.endHLayout.setObjectName('endHLayout')
            self.titleGridLayout.addLayout(self.endHLayout, 2, 1, 1, 1)

            self.endLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setFamily("Apple SD Gothic Neo")
            self.endLabel.setFont(font)
            self.endLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.endLabel.setObjectName("endLabel")
            self.endLabel.setText('끝')
            self.endHLayout.addWidget(self.endLabel)

            # 끝 시각 (시:분:초:1/100초)을 표시하고 수정할 수 있는 라인에디트 박스
            # TODO: 끝 시각을 video태그에서 검색한 다음 계산해서 settext 명령어로 텍스트를 삽입
            self.endLineEditList.append( QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
            self.endLineEditList[-1].setObjectName("endLineEdit")

            #끝 시간을 직접 계산해서 텍스트 박스애 넣어 주기
            offset_attrib = videoElement['node'].attrib['duration']                           #'161300/2997s'
            offset_attrib = offset_attrib.rstrip('s')                               #'161300/2997'
            duration_numbers = offset_attrib .split('/')                               #['161300, '2997']
            dividend, divisor = int(duration_numbers[0]), int(duration_numbers[1])        #dividend = 161300, divisor = 2997
            duration_second = dividend / divisor
            end_second = start_second + duration_second



            
            self.endLineEditList[-1].setText(self.secondsToHMSS(end_second))
            self.titleGridLayout.addWidget(self.endLineEditList[-1], 2, 2, 1, 1)

            # 2열과 3열 사이 Spacer 설정  
            spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.titleGridLayout.addItem(spacerItem4, 1, 3, 1, 1)
            spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.titleGridLayout.addItem(spacerItem5, 2, 3, 1, 1)

            # '자막 템플릿' 라벨
            self.titleTemplateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setFamily("Apple SD Gothic Neo")
            self.titleTemplateLabel.setFont(font)
            self.titleTemplateLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.titleTemplateLabel.setObjectName("titleTemplateLabel")
            self.titleTemplateLabel.setText("자막 템플릿")
            self.titleGridLayout.addWidget(self.titleTemplateLabel, 1, 4, 1, 1)

            # 자막 템플릿을 선택할 수 있는 콤보박스와 이를 감싸는 레이아웃
            self.titleTemplateComboLayout = QtWidgets.QHBoxLayout()
            self.titleTemplateComboLayout.setObjectName("titleTemplateComboLayout")
            self.titleGridLayout.addLayout(self.titleTemplateComboLayout, 1, 5, 1, 1)
            # 콤보박스
            # TODO: 콤보박스에 현재 프로그램이 불러온 예능자막 템플릿의 제목이 리스트로 들어가고, 선택 시 해당 자막이 적용된 태그로 교체
            self.templateSelector = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            self.templateSelector.setObjectName("templateSelector")
            self.titleTemplateComboLayout.addWidget(self.templateSelector)
            # 오른쪽에 Spacer 배치
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.titleTemplateComboLayout.addItem(spacerItem)

            # '자막 텍스트' 라벨
            self.titleTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setFamily("Apple SD Gothic Neo")
            self.titleTextLabel.setFont(font)
            self.titleTextLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.titleTextLabel.setObjectName("titleTextLabel")
            self.titleTextLabel.setText("자막 텍스트")
            self.titleGridLayout.addWidget(self.titleTextLabel, 2, 4, 1, 1)

            # 자막 텍스트가 출력되는 텍스트박스 
            # TODO: 비디오 태그에서 자막 텍스트를 불러와서 settext로 표시
            self.titleTextLayout = QtWidgets.QHBoxLayout()
            self.titleTextLayout.setObjectName("titleTextLayout")
            self.titleGridLayout.addLayout(self.titleTextLayout, 2, 5, 1, 1)

            # 자막 텍스트 표시
            self.titlePlainTextEdits.append(QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents))
            self.titlePlainTextEdits[-1].setObjectName("titlePlainTextEdit")
            for param in videoElement["node"].iter():
                if param.attrib["name"] == "Text":
                    self.titlePlainTextEdits[-1].setPlainText(param.attrib["value"])

            self.titleTextLayout.addWidget(self.titlePlainTextEdits[-1])

            # 미리보기 이미지의 왼쪽 요소를 전체 레이아웃에 왼쪽부터 삽입
            self.titleWholeLayout.addLayout(self.titleGridLayout)

            # 미리보기 이미지와 나머지 요소간 spacer 설정
            spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.titleWholeLayout.addItem(spacerItem6)

            # 미리보기 이미지 라벨 (지금 작업 안함)
            self.previewLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.previewLabel.setObjectName("previewLabel")
            "Preview Image (Alternative Text)"
            self.titleWholeLayout.addWidget(self.previewLabel)

            # 만들어진 요소를 이어붙이기
            self.multipleTitleLayout.addLayout(self.titleWholeLayout)
            
            # 디버깅 용도: 처리되고 있는 자막 표시
            
            print("showing titles", text())

    #초를 시분초로 바꾸는 함수
    def secondsToHMSS(self, seconds: float) -> str:
        hours = int(seconds // 3600)
        minuts = int( ( seconds - (hours*3600) ) // 60 )
        ss = int( seconds % 60 )

        hours = str(hours).zfill(2)
        minuts = str(minuts).zfill(2)
        ss = str(ss).zfill(2)
        ms = "{:.3f}".format(seconds)[-3:]

        return hours + ":" + minuts + ":" + ss + "." + ms

    #초를 시분초로 바꾸는 함수 (튜플 변환)
    def secondsToHMSSTuple(self, seconds: float) -> tuple:
        hours = int(seconds // 3600)
        minuts = int( ( seconds - (hours*3600) ) // 60 )
        ss = int( seconds % 60 )

        hours = str(hours).zfill(2)
        minuts = str(minuts).zfill(2)
        ss = str(ss).zfill(2)
        ms = "{:.3f}".format(seconds)[-3:]

        return hours, minuts, ss, ms


# 메인함수 실행
def main() -> int:
    app = QtWidgets.QApplication(sys.argv)
    preview_xml = FCPX_XML('히밥님12.fcpxml')
    preview_ui = Preview_UI(preview_xml, 800, 500)
    sys.exit(app.exec_())

    return 0

# 이 코드가 처음으로 실행될 경우 메인함수 실행
if __name__ == '__main__':
    print("program exited with code", main())
    
