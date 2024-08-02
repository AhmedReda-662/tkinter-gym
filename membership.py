from tkinter import *
from tkinter import messagebox

icon_PATH = r"D:\WorkSpace\Project Python\Assets"

# ========================================================================= #
# button Actions
def open_register():
    # close the window
    root.destroy()
    # open the register window
    import membership_register
def open_view():
    root.destroy()
    import membership_view


# ========================================================================= #

root = Tk()
# set the title
root.title("PRO-FIT-GYM-Membership")
root.resizable(False,False)
# set the size
root.geometry("850x600")


# create-button
regIcon = PhotoImage(file=f"{icon_PATH}\\edit.png")
btn1 = Button(root , text="Register member", bg="#fff", padx=5 , pady=5 , image=regIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150 , command=open_register)
btn1.place(x=850/2 - 200, y=200)

viewIcon = PhotoImage(file=f"{icon_PATH}\search-file.png")
btn2 = Button(root , text="View member", bg="#fff", padx=5 , pady=5 , image=viewIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150, command=open_view)
btn2.place(x=850/2 + 50, y=200)

root.config(bg='#393b39')
root.mainloop()