import mysql.connector

def create_connnection():
    connection = mysql.connector.connect(
        host = "localhost",
        user =  "root",
        password = "",
        database = "db_mahasiswa"
    )
    return connection

def add_mahasiswa(nama, npm, jurusan, alamat):
    connection = create_connnection()
    cursor = connection.cursor()
    querry ="INSERT INTO tb_mahasiswa(nm_mahasiswa, npm, jurusan, alamat) VALUES (%s, %s, %s, %s)"
    values = (nama, npm, jurusan, alamat)
    cursor.execute(querry, values)
    connection.commit()
    cursor.close()
    connection.close()

