# import mysql.connector
import sqlite3
import manage
from UI_functions import *
def connect():
    global connection
    try:
        connection = sqlite3.connect("pass_manager.db")
        curs = connection.cursor()
        sql_syntax = """CREATE TABLE IF NOT EXISTS Data_User(
    id INTEGER PRIMARY KEY,
    Website TEXT NOT NULL,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    time TEXT NOT NULL
    );"""
        curs.execute(sql_syntax)
        print('Koneksi berhasil')
        curs.close()
        return connection
    except sqlite3.Error as e:
        print('Gagal')
        curs.close()

def login_validation(username,passwd):
    validation = False
    if username == 'admin' and passwd == 'admin':
        validation = True
    else: 
        validation = False
    return validation

# fungsi store pass
def store_pass(website,email,passwd,time):
    try:
        connect()
        curs = connection.cursor()
        manage.encrypt(passwd)
        list_data=[(website,email,manage.b64_encrypt,time)]
        curs.executemany("INSERT INTO Data_User(Website,Email,Password,time) VALUES(?,?,?,?)",list_data)
        connection.commit()
        curs.close()
        connection.close()
    except sqlite3.Error as e:
        pass


def find_plainpass():
    global result
    connect()
    curs = connection.cursor()
    sql_syntax = """Select * from Data_User"""
    curs.execute(sql_syntax)
    result = curs.fetchall()
    connection.commit()
    curs.close()
    connection.close()
    

def delete_all_entries():
    connect()
    curs = connection.cursor()
    sql_syntax = """drop table Data_User"""
    curs.execute(sql_syntax)
    connection.commit()
    curs.close()
    connection.close()

def delete_row(id):
    print(type(id))
    connect()
    curs=connection.cursor()
    sql_syntax = """delete from Data_User where id = %d""" % (id)
    print(sql_syntax)
    curs.execute(sql_syntax)
    connection.commit()
    curs.close()
    connection.close()

def show_pass(id):
    global result
    connect()
    curs=connection.cursor()
    sql_syntax = """select Password from Data_User where id = %d""" % (id)
    curs.execute(sql_syntax)
    result = curs.fetchall()
    connection.commit()
    curs.close()
    connection.close()
   
def update_data(id,new_pass):
    global result
    connect()
    manage.encrypt(new_pass)
    curs=connection.cursor()
    list_data = [(manage.b64_encrypt,id)]
    curs.executemany("UPDATE Data_User SET Password = ? WHERE id = ?",list_data)
    connection.commit()
    curs.close()
    connection.close()
