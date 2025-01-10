from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
from backend import createUser
# ===================================================================== #
def clear():
    FName_entry.delete(0,END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)

exp_fullname = "^[A-Z][a-z]+\s[a-zA-Z\s\.]+"
exp_password = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
exp_username = "^[A-Za-z][A-Za-z0-9_]$"
# ===================================================================== #
# ===================================================================== #
# button actions
def create_account():
    if(len(FName_entry.get()) == 0 or len(username_entry.get()) == 0):
        messagebox.askretrycancel("Error","Pleas you must fill all the fields")
        return
    if(len(FName_entry.get()) < 10 or len(username_entry.get()) > 8):
        messagebox.showinfo("Error", "Fullname should be 10 character at least\nUsername should be less than 5 character\nPassword should be 10 character at least")
        return
    if(re.search(exp_fullname, FName_entry.get()) == None):
        messagebox.askretrycancel("Error", "Full name contains only character")
        return
    if(re.search(exp_username, username_entry.get())):
        messagebox.askretrycancel("Error", "start with character follwed by any character,number whatever.")
    if(re.search(exp_password, password_entry.get()) == None):
        messagebox.askretrycancel("Error", "Has minimum 8 characters in length. 10\nAt least one uppercase English letter.\nAt least one lowercase English letter.\nAt least one digit.\nAt least one special character, ")
        return
    
    createUser(FName_entry.get(), username_entry.get(), password_entry.get())
    messagebox.showinfo("Create_user" , "You created a new account successfully.")
    clear()
# ===================================================================== #
# Create the root frame of the app
root = Tk()
# Set the size 
root.geometry("850x600")
root.resizable(False,False)
# Set the title
root.title("Create User Account")
# Create the register frame and centering it
frame = ctk.CTkFrame(root, corner_radius=10, bg_color="#555",width=500, height=400)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
frame.grid_columnconfigure((0,1,2), weight=1)
# Create the registration form 
#---------------------Full Name---------------------
FName_label = ctk.CTkLabel(frame,text="Fullname",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
FName_label.grid(row=0, column=0, padx=20, pady=(20, 5))

FName_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your Fullname")
FName_entry.grid(row=0,column=1, padx=20, pady=(20, 5))
#---------------------Full Name---------------------

#---------------------username---------------------
username_label = ctk.CTkLabel(frame,text="Username:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
username_label.grid(row=1,column=0, padx=20, pady=(20, 5))

username_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your username",)
username_entry.grid(row=1,column=1, padx=20, pady=(20, 5))
#---------------------username---------------------

#---------------------password---------------------
password_lable = ctk.CTkLabel(frame,text="Password:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
password_lable.grid(row=2,column=0, padx=20, pady=(20, 5))

password_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your password",)
password_entry.grid(row=2,column=1, padx=20, pady=(20, 5))
#---------------------password---------------------

#---------------------Register---------------------
Register_button = ctk.CTkButton(frame,text="Create",font=ctk.CTkFont(family="arial",size=18,weight="bold"),text_color="white",fg_color="green",hover_color="dark green",command=create_account)
Register_button.grid(row=8,column=0,padx=20, pady=(20, 5))
#---------------------Register---------------------

#---------------------Back---------------------
Back_button = ctk.CTkButton(frame,text="Back",text_color="white",font=ctk.CTkFont(family="arial",size=18,weight="bold"),fg_color="red",hover_color="dark red")
Back_button.grid(row=8,column=1,padx=20, pady=(20, 5))
root.configure(bg="#333")
root.mainloop()
