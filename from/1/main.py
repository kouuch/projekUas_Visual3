import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from getstarted import Ui_Form
from Login import Ui_Form as Ui_Login

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mulaibtn.clicked.connect(self.show_login)

    def show_login(self):
        self.hide()
        self.login_window = QWidget()
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self.login_window)

        self.ui_login.loginbtn.clicked.connect(self.validate_login)
        self.login_window.show()

    def validate_login(self):
        d_npm = "2210010202"
        d_password = "12345678"

        input_npm = self.ui.login.lineNpm.text()
        input_password = self.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
