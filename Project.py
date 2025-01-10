import customtkinter as ctk
from tkinter import *
from backend import *
import sidebar
from tkinter import ttk
from PIL import Image
import re
import os
global icon_PATH 
icon_PATH = r"{}\Assets".format(os.getcwd())

# Initialize the main frame
root = ctk.CTk()
root.geometry("1300x600")
root.resizable(False, False)
root.title("Dashboard")

# Create the main content frame
main_content_frame = ctk.CTkFrame(root)
main_content_frame.pack(side="right", fill="both", expand=True)

def clear_main_content():
    for widget in main_content_frame.winfo_children():
        widget.destroy()

def show_dashboard():
    clear_main_content()
    main_label = ctk.CTkLabel(main_content_frame, text="Dashboard | Overview", text_color="White", font=("arial", 20, "bold"))
    main_label.pack(side=LEFT, anchor=NE, padx=30, pady=30)

    labels_frame = ctk.CTkFrame(main_content_frame, corner_radius=10, width=800, height=400,fg_color="#242424")
    labels_frame.place(rely=0.2, relx=0.025)

    labels_container = ctk.CTkFrame(labels_frame,corner_radius=10,width=800,height=200,fg_color="#242424")
    labels_container.place(rely=0.25,relx=0.6,anchor=CENTER)

    member_frame = ctk.CTkFrame(labels_container, corner_radius=10, width=200, height=100, fg_color="#333")
    member_frame.place(rely=0.2, relx=0)
    member_label = ctk.CTkLabel(member_frame, text="Members", text_color="White", font=("arial", 15, "bold"))
    member_label.pack(padx=10, pady=10)
    member_number_label = ctk.CTkLabel(member_frame, text=f"{len(showMembership())}", text_color="white", font=("arial", 15, "bold"))
    member_number_label.pack(padx=10, pady=10)

    trainer_frame = ctk.CTkFrame(labels_container, corner_radius=10, width=200, height=100, fg_color="#333")
    trainer_frame.place(rely=0.2, relx=0.2)
    trainer_label = ctk.CTkLabel(trainer_frame, text="Trainers", text_color="White", font=("arial", 15, "bold"))
    trainer_label.pack(padx=10, pady=10)
    trainer_number_label = ctk.CTkLabel(trainer_frame, text=f"{len(showTrainer())}", text_color="white", font=("arial", 15, "bold"))
    trainer_number_label.pack(padx=10, pady=10)

    equipment_frame = ctk.CTkFrame(labels_container, corner_radius=10, width=200, height=100, fg_color="#333")
    equipment_frame.place(rely=0.2, relx=0.4)
    equipment_label = ctk.CTkLabel(equipment_frame, text="Equipments", text_color="White", font=("arial", 15, "bold"))
    equipment_label.pack(padx=10, pady=10)
    equipment_number_label = ctk.CTkLabel(equipment_frame, text=f"{len(showEquipment())}", text_color="white", font=("arial", 15, "bold"))
    equipment_number_label.pack(padx=10, pady=10)

    employees_frame = ctk.CTkFrame(labels_container, corner_radius=10, width=200, height=100, fg_color="#333")
    employees_frame.place(rely=0.2, relx=0.6)
    employees_label = ctk.CTkLabel(employees_frame, text="Employees", text_color="White", font=("arial", 15, "bold"))
    employees_label.pack(padx=10, pady=10)
    employees_number_label = ctk.CTkLabel(employees_frame, text=f"{len(showEmployees())}", text_color="white", font=("arial", 15, "bold"))
    employees_number_label.pack(padx=10, pady=10)

def show_membership_view():
    clear_main_content()
    def open_membership_register_window():
        clear_main_content()
        # Create the register frame and centering it
        frame = ctk.CTkFrame(main_content_frame , corner_radius=10, fg_color="#333",width=500, height=400)
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
        Address_label=ctk.CTkLabel(frame,text="Address:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
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
        Button_frame = ctk.CTkFrame(main_content_frame,corner_radius=5)
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
            clear_main_content()
            main_view()
        Back_button = ctk.CTkButton(Button_frame,text="Back",text_color="white",font=ctk.CTkFont(family="arial",size=18,weight="bold"),fg_color="red",hover_color="dark red", command=back_membership)
        Back_button.grid(row=0,column=1,padx=20, pady=10)
    def open_membership_view_window():
    #----------------------------------------------------#
        clear_main_content()
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
            edit_window = ctk.CTkToplevel(main_content_frame)
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
            Address_label=ctk.CTkLabel(frame,text="Address:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
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
        

        # Create a label
        label = ctk.CTkLabel(main_content_frame, text="Membership Window", font=("arial", 18, "bold"), text_color="white")
        label.pack(pady=(20, 10))

        # Create a frame for the search section and treeview
        frame = ctk.CTkFrame(main_content_frame, width=800, height=400,fg_color="#333")
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
            clear_main_content()
            main_view()
        
        btn_frame = ctk.CTkFrame(main_content_frame)
        btn_frame.place(relx=0.5,rely=0.75, anchor="center")
        # create view button
        view_button = ctk.CTkButton(btn_frame, text="view", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white", command=selectedItem)
        view_button.grid(row=2,column=0,padx=30,pady=10)
        # Create the back button
        
        back_button = ctk.CTkButton(btn_frame, text="Back", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white", command=membership_view_window_close)
        back_button.grid(row=2,column=1, padx=30)
    
    def main_view():
        clear_main_content()
        #create a frame for the buttons
        # Create a label 
        label = ctk.CTkLabel(main_content_frame, text="Memberships", font=("arial",20,"bold"))
        label.pack(pady=20)
        frame = ctk.CTkFrame(main_content_frame,fg_color="#2b2b2b")
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        reg = Image.open(f"{icon_PATH}\\edit.png")
        regIcon = ctk.CTkImage(light_image=reg,size=(64,64))
        btn1 = ctk.CTkButton(frame ,image=regIcon, text="Register Membership",hover_color="dark grey",fg_color="#ddd",text_color="black" , compound="top",font=("Rubik",15), width=50,command=open_membership_register_window)
        btn1.grid(row=0,column=0,padx=20,pady=20)

        view = Image.open(f"{icon_PATH}\list_black .png")
        viewIcon = ctk.CTkImage(light_image=view,size=(64,64))
        btn2 = ctk.CTkButton(frame , image=viewIcon,text="View Record" ,hover_color="dark grey",fg_color="#ddd", text_color="black",compound="top",font=("Rubik",15),  width=50,command=open_membership_view_window)
        btn2.grid(row=0,column=1,padx=20,pady=20)
    main_view()

def show_equipment_main_view():
    clear_main_content()
    def open_register_equipment_window():
        clear_main_content()
        # ===================================================================== #
        def clear():
            EquipmentName_entry.delete(0, END)
            Brand_entry.delete(0, END)
            Model_entry.delete(0, END)
            SerialNo_entry.delete(0, END)
            Quantity_entry.delete(0, END)
            Condition_combobox.set("")
            Type_combobox.set("")
            Status_combobox.set("")
            Location_combobox.set("")
            TrainingRequired_combobox.set("")  

        # Validation 
        exp = "^([0-9]+)$"
        string_epx = "^[A-z\s]+$"
        def back_equipment():
            clear_main_content()
            main_view()
        def add_equipment():
            
            if(len(EquipmentName_entry.get())== 0 or len(Model_entry.get()) == 0 or len(SerialNo_entry.get()) == 0 or len(Location_combobox.get()) == 0 or len(TrainingRequired_combobox.get()) == 0):
                messagebox.showerror("Error", "Please fill all fields")
                return
            if (re.match(string_epx, EquipmentName_entry.get()) is None  or re.match(string_epx, Location_combobox.get()) is None or re.match(string_epx, TrainingRequired_combobox.get()) is None):
                    messagebox.showerror("Error", "Name must be character only")
                    return
            if(len(Brand_entry.get()) < 2 or len(EquipmentName_entry.get()) <2 or len(Location_combobox.get()) < 2 or len(TrainingRequired_combobox .get()) < 2):
                messagebox.showerror("Error", "Please fill all fields with minimum 2 characters")
                return
            if(re.search(exp, Model_entry.get()) is None or  re.search(exp,Quantity_entry.get()) is None):
                messagebox.askretrycancel("Error" , "Pleas Enter valid numbers")
                return

            addEquipment(EquipmentName_entry.get(), Brand_entry.get(), Model_entry.get(), SerialNo_entry.get(),
                        int(Quantity_entry.get()), Condition_combobox.get(), Type_combobox.get(),
                        Status_combobox.get(), Location_combobox.get(), TrainingRequired_combobox.get())
            messagebox.showinfo("Register", "Equipment registered successfully.")
            clear()

        # ===================================================================== #

       
        
        main_label = ctk.CTkLabel(main_content_frame, text="Register Gym Equipment",font=("arial",18,"bold"))
        main_label.pack(pady=20, padx=20, anchor="center")
        # Create the register frame and centering it
        frame = ctk.CTkScrollableFrame(main_content_frame, corner_radius=10, fg_color="#333", width=500, height=400)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the registration form
        # ---------------------Equipment Name---------------------
        EquipmentName_label = ctk.CTkLabel(frame, text="Equipment Name:",
                                        font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
        EquipmentName_label.grid(row=0, column=0, padx=20, pady=(20, 5))

        EquipmentName_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                        placeholder_text="Enter equipment name")
        EquipmentName_entry.grid(row=0, column=1, padx=20, pady=(20, 5))
        # ---------------------Equipment Name---------------------

        # ---------------------Brand---------------------
        Brand_label = ctk.CTkLabel(frame, text="Brand:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
        Brand_label.grid(row=1, column=0, padx=20, pady=(20, 5))

        Brand_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                placeholder_text="Enter brand/manufacturer")
        Brand_entry.grid(row=1, column=1, padx=20, pady=(20, 5))
        # ---------------------Brand---------------------

        # ---------------------Model---------------------
        Model_label = ctk.CTkLabel(frame, text="Model:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
        Model_label.grid(row=2, column=0, padx=20, pady=(20, 5))

        Model_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                placeholder_text="Enter model/year")
        Model_entry.grid(row=2, column=1, padx=20, pady=(20, 5))
        # ---------------------Model---------------------

        # ---------------------Serial No---------------------
        SerialNo_label = ctk.CTkLabel(frame, text="Serial No:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                    anchor='w')
        SerialNo_label.grid(row=3, column=0, padx=20, pady=(20, 5))

        SerialNo_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                    placeholder_text="Enter serial number")
        SerialNo_entry.grid(row=3, column=1, padx=20, pady=(20, 5))
        # ---------------------Serial No---------------------

        # ---------------------Quantity---------------------
        Quantity_label = ctk.CTkLabel(frame, text="Quantity:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                    anchor='w')
        Quantity_label.grid(row=4, column=0, padx=20, pady=(20, 5))

        Quantity_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                    placeholder_text="Enter quantity")
        Quantity_entry.grid(row=4, column=1, padx=20, pady=(20, 5))
        # ---------------------Quantity---------------------

        # ---------------------Condition---------------------
        Condition_label = ctk.CTkLabel(frame, text="Condition:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                    anchor='w')
        Condition_label.grid(row=5, column=0, padx=20, pady=(20, 5))

        Condition_combobox = ctk.CTkComboBox(frame, values=["New", "Used"], font=ctk.CTkFont(family="Arial", size=12))
        Condition_combobox.grid(row=5, column=1, padx=20, pady=(20, 5))
        # ---------------------Condition---------------------

        # ---------------------Type---------------------
        Type_label = ctk.CTkLabel(frame, text="Type:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
        Type_label.grid(row=6, column=0, padx=20, pady=(20, 5))

        Type_combobox = ctk.CTkComboBox(frame, values=["Cardio", "Strength", "Flexibility"],
                                        font=ctk.CTkFont(family="Arial", size=12))
        Type_combobox.grid(row=6, column=1, padx=20, pady=(20, 5))
        # ---------------------Type---------------------

        # ---------------------Status---------------------
        Status_label = ctk.CTkLabel(frame, text="Status:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
        Status_label.grid(row=7, column=0, padx=20, pady=(20, 5))

        Status_combobox = ctk.CTkComboBox(frame, values=["Available", "Out of Order"],
                                        font=ctk.CTkFont(family="Arial", size=12))
        Status_combobox.grid(row=7, column=1, padx=20, pady=(20, 5))
        # ---------------------Status---------------------

        # ---------------------Location---------------------
        Location_label = ctk.CTkLabel(frame, text="Location:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                    anchor='w')
        Location_label.grid(row=8, column=0, padx=20, pady=(20, 5))

        Location_combobox = ctk.CTkComboBox(frame, values=["First Floor", "Second Floor", "Basement"],
                                            font=ctk.CTkFont(family="Arial", size=12))
        Location_combobox.grid(row=8, column=1, padx=20, pady=(20, 5))
        # ---------------------Location---------------------

        # ---------------------Training Required---------------------
        TrainingRequired_label = ctk.CTkLabel(frame, text="Training Required:",
                                            font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
        TrainingRequired_label.grid(row=9, column=0, padx=20, pady=(20, 5))

        TrainingRequired_combobox = ctk.CTkComboBox(frame, values=["Yes", "No"], font=ctk.CTkFont(family="Arial", size=12))
        TrainingRequired_combobox.grid(row=9, column=1, padx=20, pady=(20, 5))
        # ---------------------Training Required---------------------
        #----------------------Button Frame-------------------------#
        Button_frame = ctk.CTkFrame(main_content_frame, corner_radius=10)
        Button_frame.place(relx=0.5,rely=0.9,anchor=CENTER)
        # ---------------------Register---------------------
        Register_button = ctk.CTkButton(Button_frame, text="Register", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                        text_color="white", fg_color="green", hover_color="dark green", command=add_equipment)
        Register_button.grid(row=0, column=0, padx=20 , pady=10)
        # ---------------------Register---------------------

        # ---------------------Back---------------------
        Back_button = ctk.CTkButton(Button_frame, text="Back", text_color="white",
                                    font=ctk.CTkFont(family="arial", size=18, weight="bold"), fg_color="red",
                                    hover_color="dark red", command=back_equipment)
        Back_button.grid(row=0, column=1, padx=20 , pady=10)
    def open_view_equipment_window():
    
        # open window
        def open_edit_window(values):
            # ================================================ #
            # buttons actions
            def delete_record():
                deleteEquipment(int(values[0]))
                deleteTree()
                InsertData()
                edit_window.destroy()
            def update_record():
                exp = "^([0-9]+)$"
                string_epx = "^[A-z\s]+$"
                # Set the validation of the fields and the regex
                # if (len(EquipmentName_entry.get()) == "" or Model_entry.get() == "" or SerialNo_entry.get() == "" or Status_combobox.get() == "" or Location_combobox.get()== "" or TrainingRequired_combobox.get() == ""):
                #     messagebox.showerror("Error", "Please fill all fields")
                # make sure that the len does not equal 0 in the fields
                if (re.match(string_epx, EquipmentName_entry.get()) is None or re.match(string_epx,Brand_entry.get()) is None or re.match(string_epx, Location_combobox.get()) is None or re.match(string_epx, TrainingRequired_combobox.get()) is None):
                    messagebox.showerror("Error", "Name must be character only")
                    return
                if(len(EquipmentName_entry.get())== 0 or len(Model_entry.get()) == 0 or len(SerialNo_entry.get()) == 0 or len(Location_combobox.get()) == 0 or len(TrainingRequired_combobox.get()) == 0):
                    messagebox.showerror("Error", "Please fill all fields")
                    return
                if(re.search(exp, Model_entry.get()) is None or  re.search(exp,Quantity_entry.get()) is None):
                    messagebox.askretrycancel("Error" , "Pleas Enter valid numbers")
                    return
                # check the minimum length of the string based fields 
                if(len(Brand_entry.get()) < 2 or len(EquipmentName_entry.get()) <2 or len(Location_combobox.get()) < 2 or len(TrainingRequired_combobox .get()) < 2):
                    messagebox.showerror("Error", "Please fill all fields with minimum 2 characters")
                    return
                #Update the required data from the edit window (id,equipment_name, brand, model, serial_no, quantity, condition, type,status, location, training_required)
                updateEquipment(int(values[0]), EquipmentName_entry.get(), Brand_entry.get(), Model_entry.get(), SerialNo_entry.get(), int(Quantity_entry.get()), Condition_combobox.get(), Type_combobox.get(), Status_combobox.get(), Location_combobox.get(), TrainingRequired_combobox.get())
                deleteTree()
                InsertData()
                edit_window.destroy()
            # ================================================ #
            edit_window = ctk.CTkToplevel(main_content_frame)
            edit_window.title("Edit Window")
            edit_window.geometry("550x500")
            # Create the register frame and centering it
            frame = ctk.CTkScrollableFrame(edit_window, corner_radius=10, bg_color="#333",width=400,height=250)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            # Create the registration form
            # ---------------------Equipment Name---------------------
            EquipmentName_label = ctk.CTkLabel(frame, text="Equipment Name:",
                                            font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
            
            EquipmentName_label.grid(row=0, column=0, padx=20, pady=(20, 5))

            EquipmentName_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                            placeholder_text="Enter equipment name")
            EquipmentName_entry.insert(0,values[1])
            EquipmentName_entry.grid(row=0, column=1, padx=20, pady=(20, 5))
            # ---------------------Equipment Name---------------------

            # ---------------------Brand---------------------
            Brand_label = ctk.CTkLabel(frame, text="Brand:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
            Brand_label.grid(row=1, column=0, padx=20, pady=(20, 5))

            Brand_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                    placeholder_text="Enter brand/manufacturer")
            Brand_entry.insert(0,values[2])
            Brand_entry.grid(row=1, column=1, padx=20, pady=(20, 5))
            # ---------------------Brand---------------------

            # ---------------------Model---------------------
            Model_label = ctk.CTkLabel(frame, text="Model:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
            Model_label.grid(row=2, column=0, padx=20, pady=(20, 5))

            Model_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                    placeholder_text="Enter model/year")
            Model_entry.insert(0,values[3])
            Model_entry.grid(row=2, column=1, padx=20, pady=(20, 5))
            # ---------------------Model---------------------

            # ---------------------Serial No---------------------
            SerialNo_label = ctk.CTkLabel(frame, text="Serial No:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                        anchor='w')
            SerialNo_label.grid(row=3, column=0, padx=20, pady=(20, 5))

            SerialNo_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                        placeholder_text="Enter serial number")
            SerialNo_entry.insert(0,values[4])
            SerialNo_entry.grid(row=3, column=1, padx=20, pady=(20, 5))
            # ---------------------Serial No---------------------

            # ---------------------Quantity---------------------
            Quantity_label = ctk.CTkLabel(frame, text="Quantity:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                        anchor='w')
            Quantity_label.grid(row=4, column=0, padx=20, pady=(20, 5))

            Quantity_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(family="arial", size=12), corner_radius=5,
                                        placeholder_text="Enter quantity")
            Quantity_entry.insert(0,values[5])
            Quantity_entry.grid(row=4, column=1, padx=20, pady=(20, 5))
            # ---------------------Quantity---------------------

            # ---------------------Condition---------------------
            Condition_label = ctk.CTkLabel(frame, text="Condition:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                        anchor='w')
            Condition_label.grid(row=5, column=0, padx=20, pady=(20, 5))

            Condition_combobox = ctk.CTkComboBox(frame, values=["New", "Used"], font=ctk.CTkFont(family="Arial", size=12))
            Condition_combobox.set(values[6])
            Condition_combobox.grid(row=5, column=1, padx=20, pady=(20, 5))
            # ---------------------Condition---------------------

            # ---------------------Type---------------------
            Type_label = ctk.CTkLabel(frame, text="Type:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
            Type_label.grid(row=6, column=0, padx=20, pady=(20, 5))

            Type_combobox = ctk.CTkComboBox(frame, values=["Cardio", "Strength", "Flexibility"],
                                            font=ctk.CTkFont(family="Arial", size=12))
            Type_combobox.set(values[7])
            Type_combobox.grid(row=6, column=1, padx=20, pady=(20, 5))
            # ---------------------Type---------------------

            # ---------------------Status---------------------
            Status_label = ctk.CTkLabel(frame, text="Status:", font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
            Status_label.grid(row=7, column=0, padx=20, pady=(20, 5))

            Status_combobox = ctk.CTkComboBox(frame, values=["Available", "Out of Order"],
                                            font=ctk.CTkFont(family="Arial", size=12))
            Status_combobox.set(values[8])
            Status_combobox.grid(row=7, column=1, padx=20, pady=(20, 5))
            # ---------------------Status---------------------

            # ---------------------Location---------------------
            Location_label = ctk.CTkLabel(frame, text="Location:", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                        anchor='w')
            Location_label.grid(row=8, column=0, padx=20, pady=(20, 5))

            Location_combobox = ctk.CTkComboBox(frame, values=["First Floor", "Second Floor", "Basement"],
                                                font=ctk.CTkFont(family="Arial", size=12))
            Location_combobox.set(values[9])
            Location_combobox.grid(row=8, column=1, padx=20, pady=(20, 5))
            # ---------------------Location---------------------

            # ---------------------Training Required---------------------
            TrainingRequired_label = ctk.CTkLabel(frame, text="Training Required:",
                                                font=ctk.CTkFont(family="arial", size=18, weight="bold"), anchor='w')
            TrainingRequired_label.grid(row=9, column=0, padx=20, pady=(20, 5))

            TrainingRequired_combobox = ctk.CTkComboBox(frame, values=["Yes", "No"], font=ctk.CTkFont(family="Arial", size=12))
            TrainingRequired_combobox.set(values[10])
            TrainingRequired_combobox.grid(row=9, column=1, padx=20, pady=(20, 5))
            # ---------------------Training Required---------------------
            # create button frame
            button_frame = ctk.CTkFrame(edit_window, corner_radius=5)
            button_frame.place(relx=0.5,rely=0.90,anchor=CENTER)
            # Create update button
            update_button = ctk.CTkButton(button_frame, text="Update",text_color="white",fg_color="#4CAF50",hover_color="dark green", command=update_record)
            update_button.grid(row=0,column=0,padx=20, pady=10)
            # Create delete button
            delete_button = ctk.CTkButton(button_frame, text="Delete",text_color="white",fg_color="red",hover_color="dark red", command=delete_record)
            delete_button.grid(row=0,column=1,padx=20)


        
        def clear_search():
            search_entry.delete(0, END)

        def search_equipment():
                search_term = search_entry.get()
                search_result = searchEquipment(search_term)
                tree.delete(*tree.get_children())
                for row in search_result:
                    tree.insert('', 'end', values=row)
        
        def back_equipment():
            clear_main_content()
            main_view()

        # Create a label
        label = ctk.CTkLabel(main_content_frame, text="View Equipment", font=("arial", 18, "bold"), text_color="white")
        label.pack(pady=20)

        # Create a frame for the search section and treeview
        frame = ctk.CTkFrame(main_content_frame,fg_color="#333", width=800, height=400)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        search_entry = ctk.CTkEntry(frame, font=("arial", 14), width=800, placeholder_text="Enter a name to search...")
        
        search_entry.grid(row=0, column=0, padx=10, pady=10)

        # Search button
        search_button = ctk.CTkButton(frame, text="Search", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white",command=search_equipment)
        search_button.grid(row=0, column=1, padx=5, pady=10)

        # Clear button
        clear_button = ctk.CTkButton(frame, text="Clear", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white",command=clear_search)
        clear_button.grid(row=0, column=2, padx=5, pady=10)



        # Create a Treeview within a CustomTkinter frame
        tree_frame = Frame(frame)  # Create a separate frame for the Treeview and scrollbar
        tree_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create the Treeview
        tree = ttk.Treeview(tree_frame, columns=("ID","Name","Brand","Model","Serial No","Quantity","Condition", "Type", "Status", "Location","Training Required"), show="headings")
        tree.pack(side=LEFT, fill=BOTH, expand=True)

        # Define the column headings
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Brand", text="Brand")
        tree.heading("Model", text="Model")
        tree.heading("Condition", text="Condition")
        tree.heading("Serial No", text="Serial No")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Type", text="Type")
        tree.heading("Status", text="Status")
        tree.heading("Location", text="Location")
        
        tree.heading("Training Required", text="Training Required")
        
        # Create a scrollbar and attach it to the Treeview
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        

        # Define the column width
        tree.column("ID", width=50)
        
        tree.column("Name", width=150)
        tree.column("Brand", width=100)
        tree.column("Model", width=100)
        tree.column("Serial No", width=150)
        tree.column("Quantity", width=100)
        tree.column("Condition",width=150)
        tree.column("Type", width=150)
        tree.column("Status", width=100)
        tree.column("Location", width=150)
        tree.column("Training Required", width=150)
        #define the rest of the coulmn width
        # selected Item
        def selectedItem():
            values = tree.item(tree.focus())['values']
            if(values == ''):
                messagebox.askretrycancel("Error", "Please Select an item or Just select one item")
                return
            # open view window
            open_edit_window(values)
        # Insert data
        def InsertData():
            result = showEquipment()
            for i in result:
                tree.insert('', 'end', values=i)
        InsertData()
        def deleteTree():
            tree.delete(*tree.get_children())
        # Define the column width for the rest of the columns

        # Add a vertical scrollbar to the Treeview
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scrollbar.set)

        # Adjust column weight to ensure the tree expands correctly
        tree_frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)
        frame.grid_columnconfigure(2, weight=0)
        
        btn_frame = ctk.CTkFrame(main_content_frame)
        btn_frame.place(relx=0.5,rely=0.75, anchor="center")
        # create view button
        view_button = ctk.CTkButton(btn_frame, text="view", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white", command=selectedItem)
        view_button.grid(row=2,column=0,padx=30,pady=10)
        # create the back button 
        back_button = ctk.CTkButton(btn_frame, text="Back", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white", command=back_equipment)
        back_button.grid(row=2,column=1, padx=30)

    def main_view():
        #create a frame for the buttons
        label = ctk.CTkLabel(main_content_frame, text="Equipment", font=("arial",20,"bold"))
        label.pack(pady=20)
        frame = ctk.CTkFrame(main_content_frame,fg_color="#2b2b2b")
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        reg = Image.open(f"{icon_PATH}\\edit.png")
        regIcon = ctk.CTkImage(light_image=reg,size=(64,64))
        btn1 = ctk.CTkButton(frame ,image=regIcon, text="Register Equipment",hover_color="dark grey",fg_color="#ddd",text_color="black" , compound="top",font=("Rubik",15), width=50,command=open_register_equipment_window)
        btn1.grid(row=0,column=0,padx=20,pady=20)

        view = Image.open(f"{icon_PATH}\list_black .png")
        viewIcon = ctk.CTkImage(light_image=view,size=(64,64))
        btn2 = ctk.CTkButton(frame , image=viewIcon,text="View Record" ,hover_color="dark grey",fg_color="#ddd", text_color="black",compound="top",font=("Rubik",15),  width=50,command=open_view_equipment_window)
        btn2.grid(row=0,column=1,padx=20,pady=20)
    main_view()

def show_trainers_view():
    clear_main_content()
    def open_trainer_register_window():
        clear_main_content()
        # Create a frame for the search section and treeview
        frame = ctk.CTkFrame(main_content_frame, width=800, height=400,fg_color="#333")
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
        Address_label=ctk.CTkLabel(frame,text="Address:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
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
            clear_main_content()
            main_view()
        Back_button = ctk.CTkButton(frame,text="Back",text_color="white",font=ctk.CTkFont(family="arial",size=18,weight="bold"),fg_color="red",hover_color="dark red", command=back_trainer)
        Back_button.grid(row=8,column=1,padx=20, pady=(20, 5))
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
            
            edit_window = ctk.CTkToplevel(main_content_frame)
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
            Address_label=ctk.CTkLabel(frame,text="Address:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
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
        
        # Create a frame for the search section and treeview
        frame = ctk.CTkFrame(main_content_frame, width=800, height=400,fg_color="#333")
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
            clear_main_content()
            main_view()
        btn_frame = ctk.CTkFrame(main_content_frame)
        btn_frame.place(relx=0.5,rely=0.75, anchor="center")
        # create view button
        view_button = ctk.CTkButton(btn_frame, text="view", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white", command=selectedItem)
        view_button.grid(row=2,column=0,padx=30,pady=10)
        # Create the back button
        
        back_button = ctk.CTkButton(btn_frame, text="Back", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white", command=trainer_view_window_close)
        back_button.grid(row=2,column=1, padx=30)
            
    def main_view():
        #create a frame for the buttons
        label = ctk.CTkLabel(main_content_frame, text="Trainers", font=("arial",20,"bold"))
        label.pack(pady=20)
        frame = ctk.CTkFrame(main_content_frame,fg_color="#2b2b2b")
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        reg = Image.open(f"{icon_PATH}\\edit.png")
        regIcon = ctk.CTkImage(light_image=reg,size=(64,64))
        btn1 = ctk.CTkButton(frame ,image=regIcon, text="Register Trainer",hover_color="dark grey",fg_color="#ddd",text_color="black" , compound="top",font=("Rubik",15), width=50,command=open_trainer_register_window)
        btn1.grid(row=0,column=0,padx=20,pady=20)

        view = Image.open(f"{icon_PATH}\list_black .png")
        viewIcon = ctk.CTkImage(light_image=view,size=(64,64))
        btn2 = ctk.CTkButton(frame , image=viewIcon,text="View Record" ,hover_color="dark grey",fg_color="#ddd", text_color="black",compound="top",font=("Rubik",15),  width=50,command=open_trainer_view_window)
        btn2.grid(row=0,column=1,padx=20,pady=20)
    main_view()

def show_employees_view():
    clear_main_content()
    def open_register_employee_window():
        clear_main_content()
        # Create a frame for the search section and treeview
        frame = ctk.CTkFrame(main_content_frame, width=800, height=400,fg_color="#333")
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
        Address_label=ctk.CTkLabel(frame,text="Address:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
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
        def add_employee():
            if len(FName_entry.get()) == 0 or len(MName_entry.get()) == 0 or len(LName_entry.get()) == 0 or len(Age_entry.get()) == 0 or len(Address_entry.get()) == 0 :
                messagebox.askretrycancel("Error in register" , "Pleas you must fill all the fields")
                return
            if len(FName_entry.get()) < 3 or len(MName_entry.get()) < 3 or len(LName_entry.get()) < 3 or len(Age_entry.get()) > 2 or len(Address_entry.get()) < 5:
                messagebox.askretrycancel("Error in register" , "The character of name should be more than 3\ncharacter address should be more than 5 character\nage should be between 0-90")
                return
            if(re.search(exp, Age_entry.get()) == None):
                messagebox.askretrycancel("Error in age" , "Pleas Enter valid age")
                return
            addEmployee(FName_entry.get() , MName_entry.get() , LName_entry.get() , int(Age_entry.get()), Gender_combobox.get() ,Address_entry.get())
            clear()
            messagebox.showinfo("Register" , "Register successfully.")
        Register_button = ctk.CTkButton(frame,text="Register",font=ctk.CTkFont(family="arial",size=18,weight="bold"),text_color="white",fg_color="green",hover_color="dark green", command=add_employee)
        Register_button.grid(row=8,column=0,padx=20, pady=(20, 5))
        #---------------------Register---------------------

        #---------------------Back---------------------
        def back_employee():
            clear_main_content()
            main_view()
        Back_button = ctk.CTkButton(frame,text="Back",text_color="white",font=ctk.CTkFont(family="arial",size=18,weight="bold"),fg_color="red",hover_color="dark red", command=back_employee)
        Back_button.grid(row=8,column=1,padx=20, pady=(20, 5))
    def open_view_employee_window():
        def open_edit_window(values):
            # ================================================ #
            def InsertData():
                result = showEmployees()
                for i in result:
                    tree.insert('', 'end', values=i)
            def deleteTree():
                tree.delete(*tree.get_children())
            # buttons actions
            def delete_record():
                deleteEmployees(int(values[0]))
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

                updateEmployees(int(values[0]), FName_entry.get(), MName_entry.get(), LName_entry.get(),int(Age_entry.get()),Address_entry.get())
                deleteTree()
                InsertData()
                edit_window.destroy()
            # ================================================ #
            
            edit_window = ctk.CTkToplevel(main_content_frame)
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
            Address_label=ctk.CTkLabel(frame,text="Address:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
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
    
        # Create a frame for the search section and treeview
        frame = ctk.CTkFrame(main_content_frame, width=800, height=400,fg_color="#333")
        frame.place(relx=0.5, rely=0.45, anchor=CENTER)
        
        #--------------------------------------------#
        def clear():
            search_entry.delete(0,END)
        def search():
            search_term = search_entry.get()
            search_result = searchEmployee(search_term)
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
        result = showEmployees()
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
        def employee_view_window_close():
            clear_main_content()
            main_view()
        btn_frame = ctk.CTkFrame(main_content_frame)
        btn_frame.place(relx=0.5,rely=0.75, anchor="center")
        # create view button
        view_button = ctk.CTkButton(btn_frame, text="view", font=("arial", 14), fg_color="#4CAF50",hover_color="dark green", text_color="white", command=selectedItem)
        view_button.grid(row=2,column=0,padx=30,pady=10)
        # Create the back button
        
        back_button = ctk.CTkButton(btn_frame, text="Back", font=("arial", 14), fg_color="red",hover_color="dark red", text_color="white", command=employee_view_window_close)
        back_button.grid(row=2,column=1, padx=30)
    def main_view():
        #create a frame for the buttons
        label = ctk.CTkLabel(main_content_frame, text="Employees", font=("arial",20,"bold"))
        label.pack(pady=20)
        frame = ctk.CTkFrame(main_content_frame,fg_color="#2b2b2b")
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        reg = Image.open(f"{icon_PATH}\\edit.png")
        regIcon = ctk.CTkImage(light_image=reg,size=(64,64))
        btn1 = ctk.CTkButton(frame ,image=regIcon, text="Register Employee",hover_color="dark grey",fg_color="#ddd",text_color="black" , compound="top",font=("Rubik",15), width=50,command=open_register_employee_window)
        btn1.grid(row=0,column=0,padx=20,pady=20)

        view = Image.open(f"{icon_PATH}\list_black .png")
        viewIcon = ctk.CTkImage(light_image=view,size=(64,64))
        btn2 = ctk.CTkButton(frame , image=viewIcon,text="View Record" ,hover_color="dark grey",fg_color="#ddd", text_color="black",compound="top",font=("Rubik",15),  width=50,command=open_view_employee_window)
        btn2.grid(row=0,column=1,padx=20,pady=20)
    main_view()

def show_create_user_view():
    clear_main_content()
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
    label = ctk.CTkLabel(main_content_frame, text="Create User", font=("arial",20,"bold"))
    label.pack(pady=20)
    # Create the register frame and centering it
    frame = ctk.CTkFrame(main_content_frame, corner_radius=10,width=500, height=400)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
    frame.grid_columnconfigure((0,1,2), weight=1)
    # Create the registration form 
    #---------------------Full Name---------------------
    FName_label = ctk.CTkLabel(frame,text="Fullname:",font=ctk.CTkFont(family="arial",size=18,weight="bold"),anchor='w')
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
    Register_button.grid(columnspan=3,pady=(20,5))
    #---------------------Register---------------------


# Define the callbacks dictionary
callbacks = {
    "Home": show_dashboard,
    "Membership": show_membership_view,
    "Equipment": show_equipment_main_view,
    "Trainers": show_trainers_view,
    "Employees": show_employees_view,
    "Create User Account": show_create_user_view
}

# Create the sidebar
sidebar.create_sidebar(root, callbacks)

root.mainloop()
