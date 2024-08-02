from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
from backend import addMembership
# ===================================================================== #
def clear():
    FName_entry.delete(0,END)
    MName_entry.delete(0,END)
    LName_entry.delete(0,END)
    Age_entry.delete(0,END)
    Address_entry.delete(0,END)
exp = "^([0-9]+)$"
# = buttone-actions
def back_membership():
    root.destroy() # close the windwo
    import membership # open the window
def add_membership():
    if len(FName_entry.get()) == 0 or len(MName_entry.get()) == 0 or len(LName_entry.get()) == 0 or len(Age_entry.get()) == 0 or len(Address_entry.get()) == 0 or len(subscription_var.get()) == 0:
        messagebox.askretrycancel("Error in register" , "Pleas you must fill all the fields")
        return
    if len(FName_entry.get()) < 3 or len(MName_entry.get()) < 3 or len(LName_entry.get()) < 3 or len(Age_entry.get()) > 2 or len(Address_entry.get()) < 5:
        messagebox.askretrycancel("Error in register" , "The character of name should be more than 3\ncharacter address should be more than 5 character\nage should be between 0-90")
        return
    if(re.search(exp, Age_entry.get()) == None):
        messagebox.askretrycancel("Error in age" , "Pleas Enter vaild age")
        return
    addMembership(FName_entry.get() , MName_entry.get() , LName_entry.get() , int(Age_entry.get()), Gender_combobox.get() ,Address_entry.get() , subscription_var.get())
    clear()
    messagebox.showinfo("Register" , "Register successfully.")
# ===================================================================== #

# Create the root frame of the app
root = Tk()
# Set the size 
root.geometry("850x600")
root.resizable(False,False)
# Set the title
root.title("Register Membership")
# Create the register frame and centering it
frame = ctk.CTkFrame(root, corner_radius=10, bg_color="#555",width=500, height=400)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
frame.grid_columnconfigure((0,1,2), weight=1)
# Create the registration form 
#---------------------First Name---------------------
FName_label = ctk.CTkLabel(frame,text="First Name:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
FName_label.grid(row=0, column=0, padx=20, pady=(20, 5))

FName_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your first name",)
FName_entry.grid(row=0,column=1, padx=20, pady=(20, 5))
#---------------------First Name---------------------

#---------------------Middle Name---------------------
MName_label = ctk.CTkLabel(frame,text="Middle Name:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
MName_label.grid(row=1,column=0, padx=20, pady=(20, 5))

MName_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your middle name",)
MName_entry.grid(row=1,column=1, padx=20, pady=(20, 5))
#---------------------Middle Name---------------------

#---------------------Last Name---------------------
LName_label = ctk.CTkLabel(frame,text="Last Name:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
LName_label.grid(row=2,column=0, padx=20, pady=(20, 5))

LName_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your last name",)
LName_entry.grid(row=2,column=1, padx=20, pady=(20, 5))
#---------------------Last Name---------------------

#---------------------Age---------------------
Age_label = ctk.CTkLabel(frame,text="Age:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
Age_label.grid(row=3,column=0, padx=20, pady=(20, 5))

Age_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your age")
Age_entry.grid(row=3,column=1, padx=20, pady=(20, 5))
#---------------------Age---------------------

#---------------------Gender---------------------
Gender_label = ctk.CTkLabel(frame,text="Gender:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
Gender_label.grid(row=4,column=0,padx=20, pady=(20, 5))

Gender_combobox = ctk.CTkComboBox(frame,values=["Male","Female"],font=ctk.CTkFont(family="Arial", size=12))
Gender_combobox.grid(row=4,column=1,padx=20, pady=(20, 5))
#---------------------Gender---------------------

#---------------------Address---------------------
Address_label=ctk.CTkLabel(frame,text="Address",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
Address_label.grid(row=5,column=0,padx=20, pady=(20, 5))

Address_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your address")
Address_entry.grid(row=5,column=1,padx=20, pady=(20, 5))
#---------------------Address---------------------

#---------------------Subscription Plan---------------------
Subscription_label = ctk.CTkLabel(frame, text="Subscription Type:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
Subscription_label.grid(row=6, column=0, padx=20, pady=(20, 5))

# Variable to hold the selected value
subscription_var = StringVar(value="")

# Radio buttons for subscription type

Monthly_radiobutton = ctk.CTkRadioButton(frame, text="Monthly", variable=subscription_var, value="Monthly", font=ctk.CTkFont(family="Arial", size=12))
Monthly_radiobutton.grid(row=6, column=1,pady=(20, 5), sticky="w")

Yearly_radiobutton = ctk.CTkRadioButton(frame, text="Yearly", variable=subscription_var, value="Yearly", font=ctk.CTkFont(family="Arial", size=12))
Yearly_radiobutton.grid(row=6, column=1, pady=(20, 5), sticky="e")

#---------------------Subscription Plan---------------------
#---------------------Register---------------------
Register_button = ctk.CTkButton(frame,text="Register",font=ctk.CTkFont(family="arial",size=18,weight="bold"),text_color="white",fg_color="green",hover_color="dark green", command=add_membership)
Register_button.grid(row=8,column=0,padx=20, pady=(20, 5))
#---------------------Register---------------------

#---------------------Back---------------------
Back_button = ctk.CTkButton(frame,text="Back",text_color="white",font=ctk.CTkFont(family="arial",size=18,weight="bold"),fg_color="red",hover_color="dark red", command=back_membership)
Back_button.grid(row=8,column=1,padx=20, pady=(20, 5))
root.configure(bg="#333")
root.mainloop()
