from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import customtkinter as ctk
import backend
import os
# button actions
def login():
    if len(username.get()) == 0 or len(password.get()) == 0:
        messagebox.askretrycancel("Login Error" , "You Must Fill The username and password field")
        return
    found = False # flag indicator
    result = backend.showLoginData()
    for i in result:
        if(username.get() in i and password.get() in i):
            found = True
            break
    if(found):
        messagebox.showinfo("login" , "login successfully.")
        root.destroy()
    else:
        messagebox.askretrycancel("login" , "Sorry Try again username or password are wrong.")
# ==================================================== #

root = Tk()
# set the title 
root.title("Login Page")
# set the size of the window
root.geometry("400x500")
def center_window(window, width, height):
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    x=(screen_width / 1.5) - (width / 1.5)
    y=(screen_height / 2) - (height / 2)
    window.geometry(f"{int(width)}x{int(height)}+{int(x)}+{int(y)}")

# center_window(root,400,500)
background_image=ImageTk.PhotoImage(file=f"{os.getcwd()}\\Assets\\background.jpg")
background_label=Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# create the label title
l1 = Label(root , text="WELCOME TO PRO-FIT-GYM" , font=('Forte' , 16 , "bold") , bg="#333" , fg="#ddd")
l1.pack(pady=30)

# ========================================================= #
# create the form part

l2 = Label(root, text="Login" , font=("Arial" , 14), bg="#333", fg="#ddd")
l2.pack(pady=20)

# create Entry
frame = Frame(root, bg="#333", padx=10 ,pady=10)
frame.pack(fill='both', padx=30)

l3 = Label(frame, text="Username" , font=("Arial" , 14), bg="#333", fg="#ddd")
l3.pack(pady=10)

username = Entry(frame,
                 bg="#393b39", 
                 fg="#ddd", 
                 font=("Arial" , 12), 
                 relief="flat",
                 highlightthickness=2,
                 )
username.pack()

l4 = Label(frame, text="Password" , font=("Arial" , 14), bg="#333", fg="#ddd")
l4.pack(pady=10)
password = Entry(frame,
                 bg="#393b39", 
                 fg="#ddd", 
                 font=("Arial" , 12), 
                 relief="flat",
                 highlightthickness=2,
                 show='*'
                 )
password.pack()
def show_password():
    if checkbx.get() == 0:
        password.configure(show='*')
    else:
        password.configure(show='')
checkbx = ctk.CTkCheckBox(frame,
                          text="Show Password",
                          font=ctk.CTkFont(family="arial",size=14,weight="bold"),
                          command=show_password)
checkbx.pack(pady=20)
btn = Button(frame, text="Login",
             bg="#fff",
             activebackground="#fff",
             fg="#0c0d0c",
             activeforeground="#0c0d0c",
             font=('Arial' , 13, "bold"),
             bd=2,
             relief="flat",
             width=20,
             command=login
) 
btn.pack(pady=30)
# ========================================================= #

# set the color of the window
root.config(bg="#393b39")
root.mainloop()
