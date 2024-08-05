from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
from backend import addEquipment  # Assuming you have a function to add equipment


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
root = Tk()
# Set the size
root.geometry("850x600")
root.resizable(False, False)
# Set the title
root.title("Register Gym Equipment")
# Create the register frame and centering it
frame = ctk.CTkFrame(root, corner_radius=10, bg_color="#555", width=500, height=400)
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
root.configure(bg="#333")
root.mainloop()
