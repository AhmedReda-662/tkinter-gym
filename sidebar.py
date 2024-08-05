from tkinter import *
from os import getcwd

icon_PATH = r"{}\Assets".format(getcwd())

root = Tk()
root.title("Navbar")

root.resizable(False, False)


# home
home = PhotoImage(file=f"{icon_PATH}\\home.png")
btn1 = Button(image=home , compound='bottom', bg="#387F39", activebackground="#387F39" , bd=0 , relief=SOLID)
btn1.grid(row=0,column=0,padx=10, pady=10)

l1 = Label(text="Home", bg="#387F39", font=("Rubik", 10))
l1.grid(row=0,column=1,padx=5)

# membership
membership = PhotoImage(file=f"{icon_PATH}\\membership-card.png")
btn2 = Button(image=membership , compound='bottom', bg="#387F39", activebackground="#387F39" , bd=0 , relief=SOLID, justify=CENTER)
btn2.grid(row=1,column=0,padx=10, pady=10)

l2 = Label(text="Membership", bg="#387F39", font=("Rubik", 10))
l2.grid(row=1,column=1,padx=5)

# gym_equipment
gym_equipment = PhotoImage(file=f"{icon_PATH}\\gym.png")
btn3 = Button(image=gym_equipment , compound='bottom', bg="#387F39", activebackground="#387F39" , bd=0 , relief=SOLID, justify=CENTER)
btn3.grid(row=2,column=0,padx=10, pady=10)

l3 = Label(text="Gym Equipment", bg="#387F39", font=("Rubik", 10))
l3.grid(row=2,column=1,padx=5)

# trainer
trainer = PhotoImage(file=f"{icon_PATH}\\trainer.png")
btn4 = Button(image=trainer , compound='bottom', bg="#387F39", activebackground="#387F39" , bd=0 , relief=SOLID, justify=CENTER)
btn4.grid(row=3,column=0,padx=10, pady=10)

l4 = Label(text="trainer", bg="#387F39", font=("Rubik", 10))
l4.grid(row=3,column=1,padx=5)

# gymers
gymers = PhotoImage(file=f"{icon_PATH}\\weightlifting.png")
btn5 = Button(image=gymers , compound='bottom', bg="#387F39", activebackground="#387F39" , bd=0 , relief=SOLID, justify=CENTER)
btn5.grid(row=4,column=0,padx=10, pady=10)

l5 = Label(text="Gymers", bg="#387F39", font=("Rubik", 10))
l5.grid(row=4,column=1,padx=5)

# emp
emp = PhotoImage(file=f"{icon_PATH}\\employee.png")
btn6 = Button(image=emp , compound='bottom', bg="#387F39", activebackground="#387F39" , bd=0 , relief=SOLID, justify=CENTER)
btn6.grid(row=5,column=0,padx=10, pady=10)

l5 = Label(text="Employee", bg="#387F39", font=("Rubik", 10))
l5.grid(row=5,column=1,padx=5)

# create_user_account
create_user = PhotoImage(file=f"{icon_PATH}\\add-user.png")
btn7 = Button(image=create_user , compound='bottom', bg="#387F39", activebackground="#387F39" , bd=0 , relief=SOLID, justify=CENTER)
btn7.grid(row=6,column=0,padx=10, pady=10)

l6 = Label(text="Create User Account", bg="#387F39", font=("Rubik", 10))
l6.grid(row=6,column=1,padx=5)

root.config(bg="#387F39")
root.mainloop()