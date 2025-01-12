import pandas as pd
import os
from PyQt5.QtWidgets import QMessageBox
from database import get_mahasiswa

def export_to_excel(self):
    folder_path = "exportExcel"
    if not os.patg.exits(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, "data_mahasiswa.xlsx")
    mahasiswa_list = get_mahasiswa()

    data = {
        "Id Mahasiswa": [],
        "Nama": [],
        "NPM": [],
        "Jurusan": [],
        "Alamat": []
    }

    for row_data in mahasiswa_list:
        data["Id Mahasiswa"].append(row_data[0])
        data["Nama"].append(row_data[1])
        data["NPM"].append(row_data[2])
        data["Jurusan"].append(row_data[3])
        data["Alamat"].append(row_data[4])

    df = pd.DataFrame(data)

    file_path = "data_mahasiswa.xlsx"
    try:
        df.to_excel(file_path, index=False,engine='openpyxl')
        QMessageBox.information(self,"Informasi", f"Data berhasil diekpor ke {file_path}")
    except Exception as e:
        QMessageBox.warning(self, "Informasi",f"Gagal mengekspor dataa le Excel: {e}")