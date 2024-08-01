from tkinter import *
from tkinter import messagebox
from customtkinter import *
import backend

# ===================================================== #
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
# ==================================================== #

root = Tk()
# set the title 
root.title("Login Page")
# set the size of the window
root.geometry("400x500")

# create the label title
l1 = Label(root , text="WELCOME TO PRO-FIT-GYM" , font=('Forte' , 16 , "bold") , bg="#393b39" , fg="#ddd")
l1.pack(pady=30)

# ========================================================= #
# create the form part

l2 = Label(root, text="Login" , font=("Arial" , 14), bg="#393b39", fg="#ddd")
l2.pack(pady=20)

# create Entry
frame = Frame(root, bg="#0c0d0c", padx=10 ,pady=10)
frame.pack(fill='both', padx=30)

l3 = Label(frame, text="username" , font=("Arial" , 14), bg="#000", fg="#ddd")
l3.pack()

username = Entry(frame,
                 bg="#393b39", 
                 fg="#ddd", 
                 font=("Arial" , 12), 
                 relief="flat",
                 highlightthickness=2,
                 )
username.pack()

l4 = Label(frame, text="password" , font=("Arial" , 14), bg="#000", fg="#ddd")
l4.pack()
password = Entry(frame,
                 bg="#393b39", 
                 fg="#ddd", 
                 font=("Arial" , 12), 
                 relief="flat",
                 highlightthickness=2,
                 show='*'
                 )
password.pack()

btn = Button(frame, text="Login",
             bg="#fff",
             activebackground="#fff",
             fg="#0c0d0c",
             activeforeground="#0c0d0c",
             font=('Arial' , 13, "bold"),
             bd=2,
             relief="flat",
             width=20,
             command=login)
btn.pack(pady=30)
# ========================================================= #

# set the color of the window
root.config(bg="#393b39")
root.mainloop()