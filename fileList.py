
import sqlite3

conn = sqlite3.connect('FileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                file_list TEXT \
                )")
    conn.commit()
conn.close()


conn = sqlite3.connect('FileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files (file_list) VALUES \
    ('Hello.txt')")
    cur.execute("INSERT INTO tbl_files (file_list) VALUES \
    ('myImage.png')")
    cur.execute("INSERT INTO tbl_files (file_list) VALUES \
    ('myMovie.mpg')")
    cur.execute("INSERT INTO tbl_files (file_list) VALUES \
    ('World.txt')")
    cur.execute("INSERT INTO tbl_files (file_list) VALUES \
    ('data.pdf')")
    cur.execute("INSERT INTO tbl_files (file_list) VALUES \
    ('myPhoto.jpg')")
    conn.commit()
conn.close()


conn = sqlite3.connect('FileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT file_list FROM tbl_files WHERE file_list LIKE '%txt'")
    varFiles = cur.fetchall()
    print (varFiles)        
        
