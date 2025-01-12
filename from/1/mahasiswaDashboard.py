# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mahasiswaDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 800, 90))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 90))
        self.label.setStyleSheet("border-image: url(:/images/img/header.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 90, 150, 511))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 150, 511))
        self.label_2.setStyleSheet("border-image: url(:/images/img/Navbar.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.dmahasiswabtn = QtWidgets.QPushButton(self.frame_3)
        self.dmahasiswabtn.setGeometry(QtCore.QRect(10, 30, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dmahasiswabtn.setFont(font)
        self.dmahasiswabtn.setStyleSheet("font: 9pt \"Poppins\";\n"
"\n"
"QPushButton #pushButton {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, \n"
"        x2:1, y2:0, \n"
"        stop:0 rgba(11, 131, 120, 219), \n"
"        stop:1 rgba(85, 98, 112, 226)\n"
"    );\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton #pushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, \n"
"        x2:1, y2:0, \n"
"        stop:0 rgba(150, 123, 111, 219), \n"
"        stop:1 rgba(85, 81, 84, 226)\n"
"    );\n"
"}\n"
"\n"
"QPushButton #pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"}")
        self.dmahasiswabtn.setObjectName("dmahasiswabtn")
        self.laporanbtn = QtWidgets.QPushButton(self.frame_3)
        self.laporanbtn.setGeometry(QtCore.QRect(10, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.laporanbtn.setFont(font)
        self.laporanbtn.setStyleSheet("")
        self.laporanbtn.setObjectName("laporanbtn")
        self.logoutbtn = QtWidgets.QPushButton(self.frame_3)
        self.logoutbtn.setGeometry(QtCore.QRect(10, 460, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logoutbtn.setFont(font)
        self.logoutbtn.setStyleSheet("")
        self.logoutbtn.setObjectName("logoutbtn")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(150, 570, 651, 30))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 651, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: url(:/images/img/Footer.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(150, 90, 651, 481))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.widget = QtWidgets.QWidget(self.frame_5)
        self.widget.setGeometry(QtCore.QRect(10, 10, 631, 461))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(18, 60, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 9pt \"Poppins\";\n"
"color: #000;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.label_4.setObjectName("label_4")
        self.tambahbtn = QtWidgets.QPushButton(self.widget)
        self.tambahbtn.setGeometry(QtCore.QRect(10, 10, 100, 23))
        self.tambahbtn.setStyleSheet("QPushButton#tambahbtn {\n"
"    background-color: #77D0AA;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    font-family: \"Poppins\";\n"
"    font-size: 9pt;\n"
"    font-weight: 700;\n"
"    line-height: normal;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#tambahbtn:hover {\n"
"    background-color: #55B69F;\n"
"    transform: scale(1.1);  \n"
"}\n"
"\n"
"QPushButton#tambahbtn:pressed {\n"
"    background-color: #4A9D83;\n"
"    transform: scale(0.95);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"")
        self.tambahbtn.setObjectName("tambahbtn")
        self.editbtn = QtWidgets.QPushButton(self.widget)
        self.editbtn.setGeometry(QtCore.QRect(130, 10, 100, 23))
        self.editbtn.setStyleSheet("QPushButton#editbtn {\n"
"    background-color: #77D0AA;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    font-family: \"Poppins\";\n"
"    font-size: 9pt;\n"
"    font-weight: 700;\n"
"    line-height: normal;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#editbtn:hover {\n"
"    background-color: #55B69F;\n"
"    transform: scale(1.1);  \n"
"}\n"
"\n"
"QPushButton#editbtn:pressed {\n"
"    background-color: #4A9D83;\n"
"    transform: scale(0.95);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);\n"
"}")
        self.editbtn.setObjectName("editbtn")
        self.updatebtn = QtWidgets.QPushButton(self.widget)
        self.updatebtn.setGeometry(QtCore.QRect(250, 10, 100, 23))
        self.updatebtn.setStyleSheet("QPushButton#updatebtn {\n"
"    background-color: #77D0AA;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    font-family: \"Poppins\";\n"
"    font-size: 9pt;\n"
"    font-weight: 700;\n"
"    line-height: normal;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#updatebtn:hover {\n"
"    background-color: #55B69F;\n"
"    transform: scale(1.1);  \n"
"}\n"
"\n"
"QPushButton#updatebtn:pressed {\n"
"    background-color: #4A9D83;\n"
"    transform: scale(0.95);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);\n"
"}")
        self.updatebtn.setObjectName("updatebtn")
        self.hapusbtn = QtWidgets.QPushButton(self.widget)
        self.hapusbtn.setGeometry(QtCore.QRect(370, 10, 100, 23))
        self.hapusbtn.setStyleSheet("QPushButton#hapusbtn {\n"
"    background-color: #77D0AA;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    font-family: \"Poppins\";\n"
"    font-size: 9pt;\n"
"    font-weight: 700;\n"
"    line-height: normal;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#hapusbtn:hover {\n"
"    background-color: #55B69F;\n"
"    transform: scale(1.1);  \n"
"}\n"
"\n"
"QPushButton#hapusbtn:pressed {\n"
"    background-color: #4A9D83;\n"
"    transform: scale(0.95);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);\n"
"}")
        self.hapusbtn.setObjectName("hapusbtn")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(108, 60, 502, 22))
        self.lineEdit.setStyleSheet("font: 9pt \"Poppins\";\n"
"flex-shrink: 0;\n"
"border-radius: 4px;\n"
"border: 0.5px solid #000;\n"
"\n"
"background: #FFF;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(18, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 9pt \"Poppins\";\n"
"color: #000;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(108, 90, 502, 22))
        self.lineEdit_2.setStyleSheet("font: 9pt \"Poppins\";\n"
"flex-shrink: 0;\n"
"border-radius: 4px;\n"
"border: 0.5px solid #000;\n"
"\n"
"background: #FFF;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(18, 120, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 9pt \"Poppins\";\n"
"color: #000;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(108, 120, 502, 22))
        self.comboBox.setStyleSheet("font: 9pt \"Poppins\";\n"
"border-radius: 4px;\n"
"border: 0.5px solid #000;\n"
"\n"
"background: #FFF;")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(18, 150, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 9pt \"Poppins\";\n"
"color: #000;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(108, 150, 502, 22))
        self.lineEdit_3.setStyleSheet("font: 9pt \"Poppins\";\n"
"flex-shrink: 0;\n"
"border-radius: 4px;\n"
"border: 0.5px solid #000;\n"
"\n"
"background: #FFF;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 200, 601, 251))
        self.tableWidget.setStyleSheet("font: 9pt \"Poppins\";\n"
"color: #000;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dmahasiswabtn.setText(_translate("Dialog", "DATA MAHASISWA"))
        self.laporanbtn.setText(_translate("Dialog", "LAPORAN"))
        self.logoutbtn.setText(_translate("Dialog", "LOG OUT"))
        self.label_4.setText(_translate("Dialog", "Nama"))
        self.tambahbtn.setText(_translate("Dialog", "Tambah"))
        self.editbtn.setText(_translate("Dialog", "Edit"))
        self.updatebtn.setText(_translate("Dialog", "Update"))
        self.hapusbtn.setText(_translate("Dialog", "Hapus"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "  Masukan Nama"))
        self.label_5.setText(_translate("Dialog", "NPM"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "  Masukan NPM"))
        self.label_6.setText(_translate("Dialog", "Jurusan"))
        self.comboBox.setItemText(0, _translate("Dialog", "Teknik Informatika"))
        self.comboBox.setItemText(1, _translate("Dialog", "Manajemen"))
        self.comboBox.setItemText(2, _translate("Dialog", "Hukum"))
        self.comboBox.setItemText(3, _translate("Dialog", "Ekonomi"))
        self.label_7.setText(_translate("Dialog", "Alamat"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "  Masukan Alamat"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "NPM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Jurusan"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Alamat"))
import res_rc