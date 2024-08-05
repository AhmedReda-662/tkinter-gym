from tkinter import *
from tkinter import messagebox
from os import getcwd
import customtkinter as ctk
from backend import addEquipment,showEquipment,searchEquipment
from tkinter import ttk
import re
icon_PATH = r"{}\Assets".format(getcwd())
def open_register_equipment_window():
    root.withdraw()
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


    # Validation for quantity
    quantity_exp = "^([0-9]+)$"


    # = button-actions
    def back_equipment():
        root.destroy()  # Close the window
        import equipment  # Open the equipment window


    def add_equipment():
        if (len(EquipmentName_entry.get()) == 0 or len(Brand_entry.get()) == 0 or len(Model_entry.get()) == 0 or
                len(SerialNo_entry.get()) == 0 or len(Quantity_entry.get()) == 0):
            messagebox.askretrycancel("Error in registration", "Please fill all the fields")
            return

        if re.search(quantity_exp, Quantity_entry.get()) is None:
            messagebox.askretrycancel("Error in quantity", "Please enter a valid quantity")
            return

        addEquipment(EquipmentName_entry.get(), Brand_entry.get(), Model_entry.get(), SerialNo_entry.get(),
                    int(Quantity_entry.get()), Condition_combobox.get(), Type_combobox.get(),
                    Status_combobox.get(), Location_combobox.get(), TrainingRequired_combobox.get())
        clear()
        messagebox.showinfo("Register", "Equipment registered successfully.")


    # ===================================================================== #

    # Create the root frame of the app
    register_equipment_window = ctk.CTkToplevel(root)
    # Set the size
    register_equipment_window.geometry("850x600")
    register_equipment_window.resizable(False, False)
    # Set the title
    register_equipment_window.title("Register Gym Equipment")
    # Create the register frame and centering it
    frame = ctk.CTkFrame(register_equipment_window, corner_radius=10, fg_color="#333", width=500, height=400)
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

    # ---------------------Register---------------------
    Register_button = ctk.CTkButton(frame, text="Register", font=ctk.CTkFont(family="arial", size=18, weight="bold"),
                                    text_color="white", fg_color="green", hover_color="dark green", command=add_equipment)
    Register_button.grid(row=10, column=0, padx=20, pady=(20, 5))
    # ---------------------Register---------------------

    # ---------------------Back---------------------
    Back_button = ctk.CTkButton(frame, text="Back", text_color="white",
                                font=ctk.CTkFont(family="arial", size=18, weight="bold"), fg_color="red",
                                hover_color="dark red", command=back_equipment)
    Back_button.grid(row=10, column=1, padx=20, pady=(20, 5))
def open_view_equipment_window():
    root.withdraw()

    def clear_search():
        search_entry.delete(0, END)

    def update_treeview(data):
        # Clear existing treeview entries
        for row in tree.get_children():
            tree.delete(row)
        # Insert new data into the treeview
        for equipment in data:
            tree.insert("", "end", values=equipment)

    def search_equipment():
            search_term = search_entry.get()
            search_result = searchEquipment(search_term)
            tree.delete(*tree.get_children())
            for row in search_result:
                tree.insert('', 'end', values=row)
    def back_equipment():
        root.deiconify()
        view_equipment_window.destroy()

    # Create the root frame of the app
    view_equipment_window = ctk.CTkToplevel(root)
    # Set the size of the frame
    view_equipment_window.geometry("1000x600")
    view_equipment_window.resizable(False, False)
    # Set the title of the frame
    view_equipment_window.title("View Equipment")

    # Create a label
    label = ctk.CTkLabel(view_equipment_window, text="View Equipment", font=("arial", 18, "bold"), text_color="white", bg_color="#333")
    label.pack(pady=(20, 10))

    # Create a frame for the search section and treeview
    frame = ctk.CTkFrame(view_equipment_window,fg_color="#333", width=800, height=400)
    frame.place(relx=0.5, rely=0.45, anchor=CENTER)

    # Entry for the search
    search_entry = ctk.CTkEntry(frame, font=("arial", 14), width=300, placeholder_text="Enter a name to search...")
    search_entry.grid(row=0, column=0, padx=10, pady=10)

    # Search button
    search_button = ctk.CTkButton(frame, text="Search", font=("arial", 14), fg_color="#4CAF50", text_color="white",hover_color="dark green", command=search_equipment)
    search_button.grid(row=0, column=1, padx=5, pady=10)



    # Create a Treeview within a CustomTkinter frame
    tree_frame = Frame(frame)  # Create a separate frame for the Treeview and scrollbar
    tree_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Create the Treeview
    tree = ttk.Treeview(tree_frame, columns=("ID","Name","Brand","Model","Serial No","Quantity", "Type", "Status", "Location","Training Required"), show="headings")
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Define the column headings
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Brand", text="Brand")
    tree.heading("Model", text="Model")
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
    tree.column("Type", width=150)
    tree.column("Status", width=100)
    tree.column("Location", width=150)
    tree.column("Training Required", width=150)
    #define the rest of the coulmn width

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
    

    # Create the back button
    back_button = ctk.CTkButton(frame, text="Back", font=("arial", 14), fg_color="red", text_color="white",hover_color="dark red", command=back_equipment)
    back_button.grid(row=2, columnspan=2, pady=20)


    # Populate the Treeview with initial equipment data
    update_treeview(showEquipment())

root = ctk.CTk()
# set the title
root.title("PRO-FIT-GYM-Equipments")
root.resizable(False,False)
# set the size
root.geometry("850x600")


# create-button
#create a frame for the buttons
frame = ctk.CTkFrame(root,fg_color="#242424",width=500,height=500)
frame.place(relx=0.5,rely=0.5,anchor=CENTER)

regIcon = PhotoImage(file=f"{icon_PATH}\\dumbell_dark.png")
btn1 = Button(frame , text="Register Equipment", bg="#fff", padx=9 , pady=9 , image=regIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150,command=open_register_equipment_window )
btn1.grid(row=0,column=0,padx=20)

viewIcon = PhotoImage(file=f"{icon_PATH}\list_black .png")
btn2 = Button(frame , text="View Record", bg="#fff", padx=9 , pady=9 , image=viewIcon, compound="top",font=("Rubik",15), justify=CENTER , width=150,command=open_view_equipment_window)
btn2.grid(row=0,column=1,padx=20)

# root.config(bg='#393b39')
root.mainloop()
