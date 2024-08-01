import sqlite3
import os
from tkinter import messagebox

print(os.getcwd())
PATH = r"D:\WorkSpace\Project Python\gym_db\login.db"

def showLoginData():
    
    found = False # flag the indicate wheter we found username and password in the db
    # open connection
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    # get data
    cur.execute("SELECT * from users")
    result = cur.fetchall()
    con.commit()
    con.close()
    return result

    