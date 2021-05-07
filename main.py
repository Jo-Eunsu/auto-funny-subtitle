
import sys

# 파이널 컷 프로(FCPX)의 XML 파일을 읽는 클래스인 FCPX_XML 불러오기
from FCPX_XML import FCPX_XML
from main_window import MainWindow_UI
from PyQt5 import QtWidgets


# 메인함수 실행
def main() -> int:
    app = QtWidgets.QApplication(sys.argv)
    mainwindow_ui = MainWindow_UI(800, 300)
    sys.exit(app.exec_())

    """
    # 파이널 컷 XML 파일을 읽어오고 파이널컷 예능자막 템플릿 정보 추출
    fcpx_xml = FCPX_XML(sys.argv[1])
    # XML의 자막 텍스트를 읽어와서 텍스트 정보 분석 후 수정
    fcpx_xml.xml_text_analysis()
    # 수정된 XML 파일을 따로 저장
    fcpx_xml.write_xml()
    """

    return 0

# 이 코드가 처음으로 실행될 경우 메인함수 실행
if __name__ == '__main__':
    print("program exited with code", main())
    
