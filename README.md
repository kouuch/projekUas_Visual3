# Aplikasi Pengelolaan Data Mahasiswa

## Deskripsi Aplikasi
Aplikasi ini merupakan sistem informasi pengelolaan data mahasiswa berbasis desktop yang dibangun dengan **PyQt5** dan **Python**. Aplikasi ini memungkinkan pengguna untuk melakukan berbagai operasi terhadap data mahasiswa, seperti menambah, mengedit, menghapus, dan melihat data mahasiswa yang ada.

Aplikasi ini terhubung dengan **MySQL Database** untuk menyimpan dan mengambil data mahasiswa yang digunakan dalam aplikasi. Selain itu, aplikasi ini juga dilengkapi dengan fitur untuk mengekspor data mahasiswa ke dalam format **PDF** dan **Excel**.

## Fitur Utama
- **Login Sistem**: Pengguna dapat login menggunakan kredensial yang telah disediakan.
- **Dashboard**: Halaman utama aplikasi yang memungkinkan pengguna untuk memilih menu yang tersedia seperti Data Mahasiswa dan Laporan.
- **Manajemen Data Mahasiswa**: Pengguna dapat menambah, mengedit, dan menghapus data mahasiswa dengan memasukkan informasi seperti NPM, Nama, Jurusan, dan Alamat.
- **Export PDF**: Pengguna dapat mengunduh laporan data mahasiswa dalam format PDF yang dapat disimpan atau dicetak.
- **Export Excel**: Pengguna dapat mengekspor data mahasiswa ke dalam file Excel untuk keperluan analisis lebih lanjut.
- **Laporan Data Mahasiswa**: Tampilan laporan data mahasiswa yang dapat dilihat secara lengkap dan diunduh ke dalam format PDF atau Excel.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama untuk pengembangan aplikasi.
- **PyQt5**: Framework GUI yang digunakan untuk membangun antarmuka pengguna desktop.
- **MySQL**: Database yang digunakan untuk menyimpan data mahasiswa.
- **ReportLab**: Library Python yang digunakan untuk menghasilkan file PDF dari data mahasiswa.
- **Pandas**: Library Python yang digunakan untuk menangani file Excel dan data mahasiswa.

## Cara Penggunaan
1. **Login**: Masukkan NPM dan password untuk mengakses aplikasi.
2. **Manajemen Data Mahasiswa**:
    - Klik tombol *Tambah* untuk menambahkan mahasiswa baru.
    - Klik tombol *Edit* untuk mengubah data mahasiswa yang sudah ada.
    - Klik tombol *Hapus* untuk menghapus data mahasiswa.
3. **Export Data**:
    - Pilih *Export PDF* untuk mendownload data mahasiswa dalam bentuk PDF.
    - Pilih *Export Excel* untuk mendownload data mahasiswa dalam bentuk Excel.
4. **Laporan Data Mahasiswa**: Lihat laporan data mahasiswa yang lengkap di halaman ini.

## Instalasi dan Persyaratan
1. Pastikan Python sudah terinstall di sistem Anda.
2. Install PyQt5 dengan menjalankan perintah berikut di terminal:
   ```bash
   pip install PyQt5
