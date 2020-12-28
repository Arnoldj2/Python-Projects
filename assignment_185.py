import sqlite3

conn = sqlite3.connect('dataBase.db') #creating database

with conn:
    cur = conn.cursor() # creating database_cursor to perform SQL operation
    cur.execute("create table if not exists tbl_fileList(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filename TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('dataBase.db')

fileList = ('information.docx','hello.txt','myImage.png', \
            'mymovie.mpg','world.txt','data.pdf','myphoto.jpg')

for x in fileList:
    if x.endswith('.txt'): #pulls values ending with txt from fileList 
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileList(col_filename) VALUES(?)",(x,))
            print(x)
    conn.commit()
conn.close()
