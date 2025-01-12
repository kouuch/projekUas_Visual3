import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem
from getstarted import Ui_Form
from Login import Ui_Form as Ui_Login
from mainDashboard import Ui_Dialog as Ui_mainDashboard
from mahasiswaDashboard import Ui_Dialog as Ui_mahasiswaDashboard
from laporanDashboard import Ui_Dialog as Ui_laporan
from database import add_mahasiswa, up_mahasiswa, del_mahasiswa, get_mahasiswa

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mulaibtn.clicked.connect(self.show_login)

        self.dasboard_window = None
        self.mahasiswa_dashboard_window = None
        self.laporan_dashboard_window = None

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
        self.ui_window = Ui_mainDashboard()
        self.ui_window.setupUi(self.dasboard_window)
        
        self.ui_window.dmahasiswabtn.clicked.connect(self.show_mahasiswa_dashboard)
        self.ui_window.laporanbtn.clicked.connect(self.show_laporan_dashboard)
        self.ui_window.logoutbtn.clicked.connect(self.logout)
        self.dasboard_window.show()

    def show_mahasiswa_dashboard(self):
        self.dasboard_window.hide()
        if self.laporan_dashboard_window:
            self.laporan_dashboard_window.hide()
        self.mahasiswa_dashboard_window = QWidget()
        self.ui_mahasiswa_dashboard_window = Ui_mahasiswaDashboard()
        self.ui_mahasiswa_dashboard_window.setupUi(self.mahasiswa_dashboard_window)
        
        self.ui_mahasiswa_dashboard_window.tambahbtn.clicked.connect(self.add_data_mahasiswa)

        self.ui_mahasiswa_dashboard_window.laporanbtn.clicked.connect(self.show_laporan_dashboard)
        self.ui_mahasiswa_dashboard_window.logoutbtn.clicked.connect(self.logout)
        self.mahasiswa_dashboard_window.show()

    def add_data_mahasiswa(self):
        nama = self.ui_mahasiswa_dashboard_window.lineNama.text()
        npm = self.ui_mahasiswa_dashboard_window.lineNpminput.text()
        jurusan = self.ui_mahasiswa_dashboard_window.cmbJurusan.currentText()
        alamat = self.ui_mahasiswa_dashboard_window.lineAlamat.text()

        add_mahasiswa(nama, npm, jurusan, alamat)
        QMessageBox.information(self, "Data Berhasil di Tambahkan")

    def update_mahasiswa(self):
        nama = self.ui_mahasiswa_dashboard_window.lineNama.text()
        npm = self.ui_mahasiswa_dashboard_window.lineNpminput.text()
        jurusan = self.ui_mahasiswa_dashboard_window.cmbJurusan.currentText()
        alamat = self.ui_mahasiswa_dashboard_window.lineAlamat.text()

        up_mahasiswa(nama, npm, jurusan, alamat)
        QMessageBox.information(self, "Data Berhasil di Ubah")

    def delete_mahasiswa(self):
        id_mahasiswa = self.ui_mahasiswa_dashboard_window.tbldmahasiswa.setRowCount(0)

        up_mahasiswa(id_mahasiswa)
        QMessageBox.information(self, "Data Berhasil di Hapus")

    def show_data_mahasiswa(self):
        mahasiswa_list = get_mahasiswa()
        
        self.ui_mahasiswa_dashboard_window.tbldmahasiswa.setRowCount(0)

        for row_number, row_data in enumerate(mahasiswa_list):
            self.ui_mahasiswa_dashboard_window.tbldmahasiswa.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui_mahasiswa_dashboard_window.tbldmahasiswa.setItem(row_number,column_number, QTableWidgetItem(str(data)))

            
        

    def show_laporan_dashboard(self):
        self.dasboard_window.hide()
        if self.mahasiswa_dashboard_window:
            self.mahasiswa_dashboard_window.hide()
        self.laporan_dashboard_window = QWidget()
        self.ui_laporan_dashboard_window = Ui_laporan()
        self.ui_laporan_dashboard_window.setupUi(self.laporan_dashboard_window)

        self.ui_laporan_dashboard_window.dmahasiswabtn.clicked.connect(self.show_mahasiswa_dashboard)
        self.ui_laporan_dashboard_window.logoutbtn.clicked.connect(self.logout)
        self.laporan_dashboard_window.show()


    def logout(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
