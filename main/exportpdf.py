from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from database import get_mahasiswa
from PyQt5.QtWidgets import QMessageBox
import os

def wrap_text(text, max_width, font, font_size, canvas_obj):
    canvas_obj.setFont(font, font_size)
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if canvas_obj.stringWidth(current_line + word + " ") <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    return lines

def export_to_pdf():
    directory = "exportpdf"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Logika untuk membuat nama file unik
    base_filename = "data_mahasiswa"
    file_extension = ".pdf"
    counter = 1
    file_path = os.path.join(directory, f"{base_filename}{file_extension}")
    while os.path.exists(file_path):
        file_path = os.path.join(directory, f"{base_filename}_{counter}{file_extension}")
        counter += 1

    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Laporan Data Mahasiswa")

    column_widths = [30, 150, 90, 100, 150]
    x_positions = [50, 80, 230, 320, 420, 570]
    header_labels = ["ID", "Nama", "NPM", "Jurusan", "Alamat"]

    def draw_header():
        c.setFillColorRGB(0.2, 0.6, 0.8)
        for i in range(len(header_labels)):
            c.rect(x_positions[i], 705, column_widths[i], 20, fill=1)

        c.setFillColorRGB(1, 1, 1)
        c.setFont("Helvetica-Bold", 10)
        for i, label in enumerate(header_labels):
            c.drawString(x_positions[i] + 5, 710, label)

        c.setFillColorRGB(0, 0, 0)
        c.line(x_positions[0], 700, x_positions[-1], 700)

    draw_header()

    mahasiswa_list = get_mahasiswa()
    y_position = 680

    if not mahasiswa_list:
        c.drawString(200, y_position, "Tidak ada data mahasiswa tersedia.")
    else:
        c.setFont("Helvetica", 10)
        for row_data in mahasiswa_list:
            lines = [
                wrap_text(str(row_data[0]), column_widths[0] - 10, "Helvetica", 10, c),
                wrap_text(str(row_data[1]), column_widths[1] - 10, "Helvetica", 10, c),
                wrap_text(str(row_data[2]), column_widths[2] - 10, "Helvetica", 10, c),
                wrap_text(str(row_data[3]), column_widths[3] - 10, "Helvetica", 10, c),
                wrap_text(str(row_data[4]), column_widths[4] - 10, "Helvetica", 10, c),
            ]
            max_lines = max(len(column) for column in lines)

            for i in range(max_lines):
                for j, column_lines in enumerate(lines):
                    if i < len(column_lines):
                        c.drawString(x_positions[j] + 5, y_position + 5, column_lines[i])

                y_position -= 12

            for x in x_positions:
                top_y_position = y_position + (max_lines - 1) * 12

                c.line(x, top_y_position + 12, x, y_position)

            c.line(x_positions[0], top_y_position + 12, x_positions[-1], top_y_position + 12)

            y_position -= 12

            if y_position < 50:
                c.showPage()
                y_position = 750
                draw_header()

    c.save()
    QMessageBox.information(None, "Informasi", f"Data berhasil diekspor ke {file_path}")
