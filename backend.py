import sqlite3
import os
from tkinter import messagebox

print(os.getcwd())
PATH = r"D:\WorkSpace\Project Python\gym_db"

# login_database
def showLoginData():
    found = False # flag the indicate wheter we found username and password in the db
    # open connection
    con = sqlite3.connect(f"{PATH}\\login.db")
    cur = con.cursor()
    # get data
    cur.execute("SELECT * from users")
    result = cur.fetchall()
    con.commit()
    con.close()
    return result

def createUser(fname, username , password):
    # open_connection
    con = sqlite3.connect(f"{PATH}\\login.db")
    cur = con.cursor()
    # insert data
    cur.execute("""INSERT
                INTO
                users(fullname,username,password)
                VALUES(?,?,?)
                """,(fname,username,password))
    con.commit()
    con.close()
# ================================================================== #
# membership_database
def addMembership(fname,mname,lname,age,gender,address,sub_plan):
    # open connection
    con = sqlite3.connect(f"{PATH}\\membership.db")
    cur = con.cursor()
    # insert data
    cur.execute("""INSERT 
                INTO 
                membership (fname , mname , lname , age , gender , address , subscribe_plan)
                Values(?,?,?,?,?,?,?)
                """,(fname , mname , lname, age,gender,address,sub_plan))
    con.commit()
    con.close()
# ================================================================== #
def showMembership():
    # open connection
    con = sqlite3.connect(f"{PATH}\\membership.db")
    cur = con.cursor()
    # get data
    cur.execute("SELECT * from membership")
    result = cur.fetchall()
    con.commit()
    con.close()
    return result