
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

    return 0

# 이 코드가 처음으로 실행될 경우 메인함수 실행
if __name__ == '__main__':
    print("program exited with code", main())
    
