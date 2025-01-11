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

def get_mahasiswa():
    connection = create_connnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tb_mahasiswa")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def up_mahasiswa(id_mahasiswa, nama, npm, jurusan, alamat):
    connection = create_connnection()
    cursor = connection.cursor()
    querry ="UPDATE tb_mahasiswa SET nm_mahasiswa=%s, npm%s, jurusan%s, alamat%s WHERE id_mahasiswa%s)"
    values = (nama, npm, jurusan, alamat, id_mahasiswa)
    cursor.execute(querry, values)
    connection.commit()
    cursor.close()
    connection.close()