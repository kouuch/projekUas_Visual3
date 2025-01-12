from xhtml2pdf import pisa
from database import get_mahasiswa
from PyQt5.QtWidgets import QMessageBox
import os

def export_to_pdf():
    directory = "exportpdf"
    if not os.path.exists(directory):
        os.makedirs(directory)

    base_filename = "data_mahasiswa"
    file_extension = ".pdf"
    counter = 1
    file_path = os.path.join(directory, f"{base_filename}{file_extension}")
    while os.path.exists(file_path):
        file_path = os.path.join(directory, f"{base_filename}_{counter}{file_extension}")
        counter += 1

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { text-align: center; margin-bottom: 20px; }
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid black; padding: 8px; text-align: left; }
            th { background-color: #4CAF50; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Laporan Data Mahasiswa</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nama</th>
                    <th>NPM</th>
                    <th>Jurusan</th>
                    <th>Alamat</th>
                </tr>
            </thead>
            <tbody>
                {{table_rows}}
            </tbody>
        </table>
    </body>
    </html>
    """

    try:
        mahasiswa_list = get_mahasiswa()
        table_rows = ""
        for row in mahasiswa_list:
            table_rows += f"""
                <tr>
                    <td>{row[0]}</td>
                    <td>{row[1]}</td>
                    <td>{row[2]}</td>
                    <td>{row[3]}</td>
                    <td>{row[4]}</td>
                </tr>
            """

        html_content = html_template.replace("{{table_rows}}", table_rows)

        with open(file_path, "w+b") as result_file:
            pisa_status = pisa.CreatePDF(src=html_content, dest=result_file)

        if pisa_status.err:
            QMessageBox.warning(None, "Gagal", "Ekspor PDF gagal. Silakan coba lagi.")
        else:
            QMessageBox.information(None, "Berhasil", f"Data berhasil diekspor ke: {file_path}")

    except Exception as e:
        QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {str(e)}")
