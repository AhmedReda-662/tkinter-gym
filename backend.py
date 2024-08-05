import sqlite3
import os
from tkinter import messagebox

print(os.getcwd())
PATH = r"{}\gym_db".format(os.getcwd())

# login_database
def showLoginData():
    found = False # flag the indicate whether we found username and password in the db
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

def searchMembership(search_item):
    con = sqlite3.connect(f"{PATH}\\membership.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM membership WHERE fname LIKE ?", (f"%{search_item}%",))
    result = cur.fetchall()
    con.close()
    return result
# ================================================================== #
# Trainer Database
def addTrainer(fname,mname,lname,age,gender,address):
    # Open Connection
    conn = sqlite3.connect(f"{PATH}\\trainer.db")
    cur = conn.cursor()
    # insert the data
    cur.execute("""INSERT 
                INTO 
                trainer (fname , mname , lname , age , gender , address)
                Values(?,?,?,?,?,?)
                """,(fname , mname , lname, age,gender,address))
    conn.commit()
    conn.close()
def showTrainer():
    # Open Connection
    conn = sqlite3.connect(f"{PATH}\\trainer.db")
    cur = conn.cursor()
    # get data
    cur.execute("SELECT * from trainer")
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

def searchTrainer(search_item):
    # Open Connection
    con = sqlite3.connect(f"{PATH}\\trainer.db")
    cur = con.cursor()
    # Get Data
    cur.execute("SELECT * FROM trainer WHERE fname LIKE ?", (f"%{search_item}%",))
    result = cur.fetchall()
    con.close()
    return result
# ================================================================== #
# add equipment
def addEquipment(equipment_name, brand, model, serial_no, quantity, condition, type, status, location, training_required):
    conn = sqlite3.connect(f'{PATH}\\equipment.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO equipment (equipment_name, brand, model, serial_no, quantity, condition, type, status, location, training_required)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (equipment_name, brand, model, serial_no, quantity, condition, type, status, location, training_required))

    conn.commit()
    conn.close()

# show equipment
def showEquipment():
    conn = sqlite3.connect(f'{PATH}\\equipment.db')
    cursor = conn.cursor()
    cursor.execute('SELECT equipment_name, quantity, type, status, training_required FROM equipment')
    rows = cursor.fetchall()
    conn.close()

    return rows