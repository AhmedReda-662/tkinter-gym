import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
from backend import showTrainer,addTrainer,searchTrainer,deleteTrainer,updateTrainer
import os

icon_PATH = r"{}\Assets".format(os.getcwd())
#create the toplevel frame view trainer
def open_trainer_view_window():
    def open_edit_window(values):
        # ================================================ #
        def InsertData():
            result = showTrainer()
            for i in result:
                tree.insert('', 'end', values=i)
        def deleteTree():
            tree.delete(*tree.get_children())
        # buttons actions
        def delete_record():
            deleteTrainer(int(values[0]))
            deleteTree()
            InsertData()
            edit_window.destroy()
        def update_record():
            exp = "^([0-9]+)$"
            string_epx = "^[A-z\s]+$"
            if len(FName_entry.get()) == 0 or len(MName_entry.get()) == 0 or len(LName_entry.get()) == 0 or len(Age_entry.get()) == 0 or len(Address_entry.get()) == 0:
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

            updateTrainer(int(values[0]), FName_entry.get(), MName_entry.get(), LName_entry.get(),int(Age_entry.get()),Address_entry.get())
            deleteTree()
            InsertData()
            edit_window.destroy()
        # ================================================ #
        
        edit_window = ctk.CTkToplevel(trainer_view_window)
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
    # Initialize the main frame 
    trainer_view_window = ctk.CTkToplevel(root)
    # Set the size of the frame
    trainer_view_window.geometry("1000x600")
    trainer_view_window.resizable(False,False)
    # Set the title of the frame
    trainer_view_window.title("View Trainers")
    # Create a frame for the search section and treeview
    frame = ctk.CTkFrame(trainer_view_window, width=800, height=400,fg_color="#333")
    frame.place(relx=0.5, rely=0.45, anchor=CENTER)
    
    #--------------------------------------------#
    def clear():
        search_entry.delete(0,END)
    def search():
        search_term = search_entry.get()
        search_result = searchTrainer(search_term)
        tree.delete(*tree.get_children())
        for row in search_result:
            tree.insert('', 'end', values=row)
    def selectedItem():
        values = tree.item(tree.focus())['values']
        if(values == ''):
            messagebox.askretrycancel("Error", "Please Select an item or Just select one item")
            return
        # open view window
        open_edit_window(values)
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
    tree = ttk.Treeview(tree_frame, columns=("ID", "First Name", "Middle Name", "Last Name", "Age", "Gender", "Address"), show="headings")
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Define the column headings
    tree.heading("ID", text="ID")
    tree.heading("First Name", text="First Name")
    tree.heading("Middle Name", text="Middle Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Age", text="Age")
    tree.heading("Gender", text="Gender")
    tree.heading("Address", text="Address")
    

    # Define the column width
    tree.column("ID", width=50)
    tree.column("First Name", width=150)
    tree.column("Middle Name", width=150)
    tree.column("Last Name", width=150)
    tree.column("Age", width=50)
    tree.column("Gender", width=100)
    tree.column("Address", width=100)

    # Insert data
    result = showTrainer()
    for i in result:
        tree.insert('', 'end', values=i)

    # Add a vertical scrollbar to the Treeview
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.configure(yscrollcommand=scrollbar.set)


    # Adjust column weights to make sure tree expands correctly
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=0)
    frame.grid_columnconfigure(2, weight=0)
    def trainer_view_window_close():
        root.deiconify()
        trainer_view_window.destroy()
    btn_frame = ctk.CTkFrame(trainer_view_window)
    btn_frame.place(relx=0.5,rely=0.75, anchor="center")
    # create view button
    view_button = ctk.CTkButton(btn_frame, text="view", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white", command=selectedItem)
    view_button.grid(row=2,column=0,padx=30,pady=10)
    # Create the back button
    
    back_button = ctk.CTkButton(btn_frame, text="Back", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white", command=trainer_view_window_close)
    back_button.grid(row=2,column=1, padx=30)
        
def open_trainer_register_window():
    root.withdraw()
    # Initialize the main frame 
    trainer_register_window = ctk.CTkToplevel(root)
    # Set the size of the frame
    trainer_register_window.geometry("850x600")
    trainer_register_window.resizable(False,False)
    # Set the title of the frame
    trainer_register_window.title("Register Trainers")
    # Create a frame for the search section and treeview
    frame = ctk.CTkFrame(trainer_register_window, width=800, height=400,fg_color="#333")
    frame.place(relx=0.5, rely=0.45, anchor=CENTER)
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
    #---------------------Register---------------------
    def clear():
        FName_entry.delete(0,END)
        MName_entry.delete(0,END)
        LName_entry.delete(0,END)
        Age_entry.delete(0,END)
        Address_entry.delete(0,END)
    exp = "^([0-9]+)$"
    def add_trainer():
        if len(FName_entry.get()) == 0 or len(MName_entry.get()) == 0 or len(LName_entry.get()) == 0 or len(Age_entry.get()) == 0 or len(Address_entry.get()) == 0 :
            messagebox.askretrycancel("Error in register" , "Pleas you must fill all the fields")
            return
        if len(FName_entry.get()) < 3 or len(MName_entry.get()) < 3 or len(LName_entry.get()) < 3 or len(Age_entry.get()) > 2 or len(Address_entry.get()) < 5:
            messagebox.askretrycancel("Error in register" , "The character of name should be more than 3\ncharacter address should be more than 5 character\nage should be between 0-90")
            return
        if(re.search(exp, Age_entry.get()) == None):
            messagebox.askretrycancel("Error in age" , "Pleas Enter valid age")
            return
        addTrainer(FName_entry.get() , MName_entry.get() , LName_entry.get() , int(Age_entry.get()), Gender_combobox.get() ,Address_entry.get())
        clear()
        messagebox.showinfo("Register" , "Register successfully.")
    Register_button = ctk.CTkButton(frame,text="Register",font=ctk.CTkFont(family="arial",size=18,weight="bold"),text_color="white",fg_color="green",hover_color="dark green", command=add_trainer)
    Register_button.grid(row=8,column=0,padx=20, pady=(20, 5))
    #---------------------Register---------------------

    #---------------------Back---------------------
    def back_trainer():
        trainer_register_window.destroy()
        root.deiconify()
    Back_button = ctk.CTkButton(frame,text="Back",text_color="white",font=ctk.CTkFont(family="arial",size=18,weight="bold"),fg_color="red",hover_color="dark red", command=back_trainer)
    Back_button.grid(row=8,column=1,padx=20, pady=(20, 5))
# Create the root frame of the app
root = ctk.CTk()
root.geometry("1000x600")
root.resizable(False, False)
root.title("Main Window")

# create-button
#create a frame for the buttons
frame = ctk.CTkFrame(root,fg_color="#242424",width=500,height=500)
frame.place(relx=0.5,rely=0.5,anchor=CENTER)

regIcon = PhotoImage(file=f"{icon_PATH}\\edit.png")
btn1 = Button(frame , text="Register Trainer", bg="#fff", padx=5 , pady=5 , image=regIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150 , command=open_trainer_register_window)
btn1.grid(row=0,column=0,padx=20)

viewIcon = PhotoImage(file=f"{icon_PATH}\search-file.png")
btn2 = Button(frame , text="View Trainers", bg="#fff", padx=5 , pady=5 , image=viewIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150, command=open_trainer_view_window)
btn2.grid(row=0,column=1,padx=20)

# root.config(bg='#393b39')
root.mainloop()
