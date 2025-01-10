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
def deleteMembership(id):
    con = sqlite3.connect(f"{PATH}\\membership.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM membership WHERE id = ?",(id,))
    con.commit()
    con.close()
    
def updateMembership(id,fname,mname,lname,age,address,sub_plan):
    con = sqlite3.connect(f"{PATH}\\membership.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE
                membership
                SET
                fname = ?,
                mname = ?,
                lname = ?,
                age = ?,
                address = ?,
                subscribe_plan = ?
                WHERE id = ?
                """,(fname,mname,lname,age,address,sub_plan,id))
    con.commit()
    con.close()
    
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

def deleteTrainer(id):
    con = sqlite3.connect(f"{PATH}\\trainer.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM trainer WHERE id = ?",(id,))
    con.commit()
    con.close()
    
def updateTrainer(id,fname,mname,lname,age,address):
    con = sqlite3.connect(f"{PATH}\\trainer.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE
                trainer
                SET
                fname = ?,
                mname = ?,
                lname = ?,
                age = ?,
                address = ?
                WHERE id = ?
                """,(fname,mname,lname,age,address,id))
    con.commit()
    con.close()
# ================================================================== #
#Equipment Database
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
    cursor.execute('SELECT * FROM equipment')
    rows = cursor.fetchall()
    conn.close()
    return rows
# Search Equipment
def searchEquipment(search_item):
    conn = sqlite3.connect(f'{PATH}\\equipment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipment WHERE equipment_name LIKE ?", (f"%{search_item}%",))
    result = cursor.fetchall()
    conn.close()
    return result
# Update equipment
def updateEquipment(id,equipment_name, brand, model, serial_no, quantity, condition, type,status, location, training_required):
    con = sqlite3.connect(f"{PATH}\\equipment.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE
                equipment
                SET
                equipment_name = ?,
                brand = ?,
                model = ?,
                serial_no = ?,
                quantity = ?,
                condition = ?,
                type = ?,
                status = ?,
                location = ?,
                training_required = ?
                WHERE id = ?
                """, (equipment_name, brand, model, serial_no, quantity, condition, type,status, location, training_required, id))
    con.commit()
    con.close()
# Delete equipment
def deleteEquipment(id):
    conn = sqlite3.connect(f'{PATH}\\equipment.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM equipment WHERE id = ?', (id,))
    conn.commit()
    conn.close()
#---------------------------------------------------------#
#Employees Database
def addEmployee(fname,mname,lname,age,gender,address):
    # Open Connection
    conn = sqlite3.connect(f"{PATH}\\employees.db")
    cur = conn.cursor()
    # insert the data
    cur.execute("""INSERT 
                INTO 
                employees (fname , mname , lname , age , gender , address)
                Values(?,?,?,?,?,?)
                """,(fname , mname , lname, age,gender,address))
    conn.commit()
    conn.close()
    

def showEmployees():
    conn = sqlite3.connect(f'{PATH}\\employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    conn.close()

    return rows

def updateEmployees(id,fname,mname,lname,age,address):
    con = sqlite3.connect(f"{PATH}\\employees.db")
    cur = con.cursor()
    cur.execute("""
                UPDATE
                employees
                SET
                fname = ?,
                mname = ?,
                lname = ?,
                age = ?,
                address = ?
                WHERE id = ?
                """,(fname,mname,lname,age,address,id))
    con.commit()
    con.close()

def searchEmployee(search_item):
    # Open Connection
    con = sqlite3.connect(f"{PATH}\\employees.db")
    cur = con.cursor()
    # Get Data
    cur.execute("SELECT * FROM employees WHERE fname LIKE ?", (f"%{search_item}%",))
    result = cur.fetchall()
    con.close()
    return result

def deleteEmployees(id):
    con = sqlite3.connect(f"{PATH}\\employees.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM employees WHERE id = ?",(id,))
    con.commit()
    con.close()
#---------------------------------------------------------#