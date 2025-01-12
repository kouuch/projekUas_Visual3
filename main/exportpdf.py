from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from database import get_mahasiswa
from PyQt5.QtWidgets import QMessageBox

def export_to_pdf():
    file_path = "data_mahasiswa.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFont("Poppins-Bold", 16)
    c.drawString(200, 750, "Laporan Data Mahasiswa")
    
    c.setFont("Poppins", 12)
    c.drawString(50, 720, "ID Mahasiswa")
    c.drawString(150, 720, "Nama")
    c.drawString(250, 720, "NPM")
    c.drawString(350, 720, "Jurusan")
    c.drawString(450, 720, "Alamat")

    c.setFont("Poppins", 12)
    mahasiswa_list = get_mahasiswa()
    y_position = 700

    for  row_data in mahasiswa_list:
        c.drawString(50, y_position, str(row_data[0]))
        c.drawString(150, y_position, str(row_data[1]))
        c.drawString(250, y_position, str(row_data[2]))
        c.drawString(350, y_position, str(row_data[3]))
        c.drawString(450, y_position, str(row_data[4]))
        y_position-= 20

    c.save
    QMessageBox.information(None, "Informasi", f"Data berhasil di eksport ke{file_path}")