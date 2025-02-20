import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from src.droptask.ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.iconOnlySideBarWidget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.menuButton.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
