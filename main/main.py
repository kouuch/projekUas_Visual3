import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from getstarted import Ui_Form
from Login import Ui_Form as Ui_Login
from mainDashboard import Ui_Dialog

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
        d_npm = "user"
        d_password = "1"

        input_npm = self.ui_login.lineNpm.text()
        input_password = self.ui_login.linePassword.text()

        if input_npm == d_npm and input_password == d_password:
            self.show_dashboard()
        else:
            QMessageBox.warning(self, "Login Failed", "NPM or Password is incorrect!")

    def show_dashboard(self):
        self.login_window.hide()
        self.dasboard_window = QWidget()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.dasboard_window)
        self.dasboard_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
