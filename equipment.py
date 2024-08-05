from tkinter import *
from tkinter import messagebox
from os import getcwd

icon_PATH = r"{}\Assets".format(getcwd())

# ========================================================================= #
# button Actions
def open_register():
    # close the window
    root.destroy()
    # open the register window
    import equipment_register
def open_view():
    root.destroy()
    import equipment_view


# ========================================================================= #

root = Tk()
# set the title
root.title("PRO-FIT-GYM-Equipments")
root.resizable(False,False)
# set the size
root.geometry("850x600")


# create-button
regIcon = PhotoImage(file=f"{icon_PATH}\\dumbell_dark.png")
btn1 = Button(root , text="Register Equipment", bg="#fff", padx=9 , pady=9 , image=regIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150 , command=open_register)
btn1.place(x=850/2 - 200, y=200)

viewIcon = PhotoImage(file=f"{icon_PATH}\list_black .png")
btn2 = Button(root , text="View Record", bg="#fff", padx=9 , pady=9 , image=viewIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150, command=open_view)
btn2.place(x=850/2 + 50, y=200)

root.config(bg='#393b39')
root.mainloop()