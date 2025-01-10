from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re 
import customtkinter as ctk
from backend import searchMembership , deleteMembership , addMembership , showMembership , updateMembership
import os
from PIL import Image
icon_PATH = r"{}\Assets".format(os.getcwd())
def open_membership_view_window():
    #----------------------------------------------------#
    def open_edit_window(values):
        # ================================================ #
        # buttons actions
        def delete_record():
            deleteMembership(int(values[0]))
            deleteTree()

            InsertData()
            edit_window.destroy()
        def update_record():
            exp = "^([0-9]+)$"
            string_epx = "^[A-z\s]+$"
            if len(FName_entry.get()) == 0 or len(MName_entry.get()) == 0 or len(LName_entry.get()) == 0 or len(Age_entry.get()) == 0 or len(Address_entry.get()) == 0 or len(subscription_var.get()) == 0:
                messagebox.askretrycancel("Error in register" , "Pleas you must fill all the fields")
                return
            if(re.search(string_epx , FName_entry.get()) == None or re.search(string_epx , MName_entry.get()) == None or re.search(string_epx , LName_entry.get()) == None):
                messagebox.showerror("Error", "Name must be character only")
                return
            if len(FName_entry.get()) < 3 or len(MName_entry.get()) < 3 or len(LName_entry.get()) < 3 or len(Age_entry.get()) > 2 or len(Address_entry.get()) < 5:
                messagebox.askretrycancel("Error in register" , "The character of name should be more than 3\ncharacter address should be more than 5 character\nage should be between 0-90")
                return
            if(re.search(exp, Age_entry.get()) == None):
                messagebox.askretrycancel("Error in age" , "Pleas Enter valid age")
                return

            updateMembership(int(values[0]), FName_entry.get(), MName_entry.get(), LName_entry.get(),int(Age_entry.get()),Address_entry.get(),subscription_var.get())
            deleteTree()
            InsertData()
            edit_window.destroy()
        # ================================================ #
        edit_window = ctk.CTkToplevel(membership_view_window)
        edit_window.title("Edit Window")
        edit_window.geometry("550x500")
        # Create the register frame and centering it
        frame = ctk.CTkScrollableFrame( edit_window, corner_radius=10, bg_color="#333",width=500,height=250)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
        frame.grid_columnconfigure((0,1,2), weight=1)
        # Create the registration form 
        #---------------------First Name---------------------
        FName_label = ctk.CTkLabel(frame,text="First Name:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
        FName_label.grid(row=0, column=0, padx=20, pady=(20, 5))

        FName_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your first name",)
        FName_entry.grid(row=0,column=1, padx=20, pady=(20, 5))
        FName_entry.insert(0, values[1])
        #---------------------First Name---------------------

        #---------------------Middle Name---------------------
        MName_label = ctk.CTkLabel(frame,text="Middle Name:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
        MName_label.grid(row=1,column=0, padx=20, pady=(20, 5))

        MName_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your middle name",)
        MName_entry.grid(row=1,column=1, padx=20, pady=(20, 5))
        MName_entry.insert(0, values[2])
        #---------------------Middle Name---------------------

        #---------------------Last Name---------------------
        LName_label = ctk.CTkLabel(frame,text="Last Name:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
        LName_label.grid(row=2,column=0, padx=20, pady=(20, 5))

        LName_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your last name",)
        LName_entry.grid(row=2,column=1, padx=20, pady=(20, 5))
        LName_entry.insert(0, values[3])
        #---------------------Last Name---------------------

        #---------------------Age---------------------
        Age_label = ctk.CTkLabel(frame,text="Age:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
        Age_label.grid(row=3,column=0, padx=20, pady=(20, 5))

        Age_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your age")
        Age_entry.grid(row=3,column=1, padx=20, pady=(20, 5))
        Age_entry.insert(0, values[4])
        #---------------------Age---------------------

        #---------------------Gender---------------------
        Gender_label = ctk.CTkLabel(frame,text="Gender:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
        Gender_label.grid(row=4,column=0,padx=20, pady=(20, 5))

        Gender_combobox = ctk.CTkComboBox(frame,values=["Male","Female"],font=ctk.CTkFont(family="Arial", size=12))
        Gender_combobox.grid(row=4,column=1,padx=20, pady=(20, 5))
        Gender_combobox.set(value=values[5])
        #---------------------Gender---------------------

        #---------------------Address---------------------
        Address_label=ctk.CTkLabel(frame,text="Address",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
        Address_label.grid(row=5,column=0,padx=20, pady=(20, 5))

        Address_entry = ctk.CTkEntry(frame,font=ctk.CTkFont(family="arial",size=12),corner_radius=5,placeholder_text="Enter your address")
        Address_entry.grid(row=5,column=1,padx=20, pady=(20, 5))
        Address_entry.insert(0,values[6])
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

        subscription_var.set(value=values[7])
        #---------------------Subscription Plan---------------------
        # create button frame
        button_frame = ctk.CTkFrame(edit_window, corner_radius=5)
        button_frame.place(relx=0.5,rely=0.90,anchor=CENTER)
        # Create update button
        update_button = ctk.CTkButton(button_frame, text="Update",text_color="white",fg_color="#4CAF50",hover_color="dark green", command=update_record)
        update_button.grid(row=0,column=0,padx=20, pady=10)
        # Create delete button
        delete_button = ctk.CTkButton(button_frame, text="Delete",text_color="white",fg_color="red",hover_color="dark red", command=delete_record)
        delete_button.grid(row=0,column=1,padx=20)
        
        #-----------------------------------------------------------#
    root.withdraw()
    # Open a new Toplevel window instead of re-importing
    membership_view_window = ctk.CTkToplevel(root)
    membership_view_window.geometry("1000x600")
    membership_view_window.title("Membership Window")

    # Create a label
    label = ctk.CTkLabel(membership_view_window, text="Membership Window", font=("arial", 18, "bold"), text_color="white")
    label.pack(pady=(20, 10))

    # Create a frame for the search section and treeview
    frame = ctk.CTkFrame(membership_view_window, width=800, height=400,fg_color="#333")
    frame.place(relx=0.5, rely=0.45, anchor=CENTER)
    
    #--------------------------------------------#
    def clear():
        search_entry.delete(0,END)
    def search():
        search_term = search_entry.get()
        search_result = searchMembership(search_term)
        tree.delete(*tree.get_children())
        for row in search_result:
            tree.insert('', 'end', values=row)
        
    #--------------------------------------------#
    
    # Entry for the search
    search_entry = ctk.CTkEntry(frame, font=("arial", 14), width=500, placeholder_text="Enter a name to search...")
    
    search_entry.grid(row=0, column=0, padx=10, pady=10)

    # Search button
    search_button = ctk.CTkButton(frame, text="Search", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white",command=search)
    search_button.grid(row=0, column=1, padx=5, pady=10)

    # Clear button
    clear_button = ctk.CTkButton(frame, text="Clear", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white",command=clear)
    clear_button.grid(row=0, column=2, padx=5, pady=10)

    # Create a Treeview within the Toplevel frame
    tree_frame = Frame(frame)
    tree_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Create the Treeview
    tree = ttk.Treeview(tree_frame, columns=("ID", "First Name", "Middle Name", "Last Name", "Age", "Gender", "Address", "Subscription"), show="headings")
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Define the column headings
    tree.heading("ID", text="ID")
    tree.heading("First Name", text="First Name")
    tree.heading("Middle Name", text="Middle Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Age", text="Age")
    tree.heading("Gender", text="Gender")
    tree.heading("Address", text="Address")
    tree.heading("Subscription", text="Subscription")

    # Define the column width
    tree.column("ID", width=50)
    tree.column("First Name", width=150)
    tree.column("Middle Name", width=150)
    tree.column("Last Name", width=150)
    tree.column("Age", width=50)
    tree.column("Gender", width=100)
    tree.column("Address", width=100)
    tree.column("Subscription", width=150)

    def selectedItem():
        values = tree.item(tree.focus())['values']
        if(values == ''):
            messagebox.askretrycancel("Error", "Please Select an item or Just select one item")
            return
        # open view window
        open_edit_window(values)
    
    # Insert data
    def InsertData():
        result = showMembership()
        for i in result:
            tree.insert('', 'end', values=i)
    InsertData()
    
    def deleteTree():
        tree.delete(*tree.get_children())

    # Add a vertical scrollbar to the Treeview
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.configure(yscrollcommand=scrollbar.set)


    # Adjust column weights to make sure tree expands correctly
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=0)
    frame.grid_columnconfigure(2, weight=0)
    def membership_view_window_close():
        root.deiconify()
        membership_view_window.destroy()
    
    btn_frame = ctk.CTkFrame(membership_view_window)
    btn_frame.place(relx=0.5,rely=0.75, anchor="center")
    # create view button
    view_button = ctk.CTkButton(btn_frame, text="view", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white", command=selectedItem)
    view_button.grid(row=2,column=0,padx=30,pady=10)
    # Create the back button
    
    back_button = ctk.CTkButton(btn_frame, text="Back", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white", command=membership_view_window_close)
    back_button.grid(row=2,column=1, padx=30)
    
    # create toplevel
    
def open_membership_register_window():
    root.withdraw()
    # Open a new Toplevel window instead of re-importing
    membership_register_window = ctk.CTkToplevel(root)
    membership_register_window.geometry("850x600")
    membership_register_window.title("Register Membership")
    # Create the register frame and centering it
    frame = ctk.CTkFrame(membership_register_window , corner_radius=10, fg_color="#333",width=500, height=400)
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
    #---------------------Button Frame-------------------------#
    Button_frame = ctk.CTkFrame(membership_register_window,corner_radius=5)
    Button_frame.place(relx=0.5,rely=0.9,anchor=CENTER)
    #---------------------Register---------------------
    def clear():
        FName_entry.delete(0,END)
        MName_entry.delete(0,END)
        LName_entry.delete(0,END)
        Age_entry.delete(0,END)
        Address_entry.delete(0,END)
    exp = "^([0-9]+)$"
    def add_membership():
        if len(FName_entry.get()) == 0 or len(MName_entry.get()) == 0 or len(LName_entry.get()) == 0 or len(Age_entry.get()) == 0 or len(Address_entry.get()) == 0 or len(subscription_var.get()) == 0:
            messagebox.askretrycancel("Error in register" , "Pleas you must fill all the fields")
            return
        if len(FName_entry.get()) < 3 or len(MName_entry.get()) < 3 or len(LName_entry.get()) < 3 or len(Age_entry.get()) > 2 or len(Address_entry.get()) < 5:
            messagebox.askretrycancel("Error in register" , "The character of name should be more than 3\ncharacter address should be more than 5 character\nage should be between 0-90")
            return
        if(re.search(exp, Age_entry.get()) == None):
            messagebox.askretrycancel("Error in age" , "Pleas Enter valid age")
            return
        addMembership(FName_entry.get() , MName_entry.get() , LName_entry.get() , int(Age_entry.get()), Gender_combobox.get() ,Address_entry.get() , subscription_var.get())
        clear()
        messagebox.showinfo("Register" , "Register successfully.")
    Register_button = ctk.CTkButton(Button_frame,text="Register",font=ctk.CTkFont(family="arial",size=18,weight="bold"),text_color="white",fg_color="green",hover_color="dark green", command=add_membership)
    Register_button.grid(row=0,column=0,padx=20,pady=10)
    #---------------------Register---------------------

    #---------------------Back---------------------
    def back_membership():
        membership_register_window.destroy()
        root.deiconify()
    Back_button = ctk.CTkButton(Button_frame,text="Back",text_color="white",font=ctk.CTkFont(family="arial",size=18,weight="bold"),fg_color="red",hover_color="dark red", command=back_membership)
    Back_button.grid(row=0,column=1,padx=20, pady=10)
# Create the root frame of the app
root = ctk.CTk()
root.geometry("1000x600")
root.resizable(False, False)
root.title("Main Window")

#create a frame for the buttons
frame = ctk.CTkFrame(root,fg_color="#242424",width=500,height=500)
frame.place(relx=0.5,rely=0.5,anchor=CENTER)
icon1=  Image.open(f"{icon_PATH}\edit.png")
regIcon = ctk.CTkImage(light_image=icon1)
btn1 = ctk.CTkButton(frame , text="Register Membership", fg_color="#fff",compound="top",hover_color="dark grey", image=regIcon, font=("Rubik",15),  width=150 , command=open_membership_register_window)
btn1.grid(row=0,column=0,padx=20)

icon2 = Image.open(f"{icon_PATH}\search-file.png")
viewIcon = ctk.CTkImage(light_image=f"{icon_PATH}\search-file.png")
btn2 = ctk.CTkButton(frame , text="View Memberships", fg_color="#fff",compound="top",hover_color="dark grey", image=viewIcon, font=("Rubik",15),  width=150, command=open_membership_view_window)
btn2.grid(row=0,column=1,padx=20)

# root.config(bg='#393b39')
root.mainloop()