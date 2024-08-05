from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from backend import showEquipment  # Ensure showEquipment is correctly imported

def back_membership():
    root.destroy()
    import equipment  # Ensure this module exists

def clear_search():
    search_entry.delete(0, END)
    search_entry.insert(0, "Enter a name to search...")
    update_treeview(showEquipment())

def update_treeview(data):
    # Clear existing treeview entries
    for row in tree.get_children():
        tree.delete(row)
    # Insert new data into the treeview
    for equipment in data:
        tree.insert("", "end", values=equipment)

def clear_tree():
    for row in tree.get_children():
        tree.delete(row)

def search_equipment():
    search_term = search_entry.get()
    if search_term == "" or search_term == "Enter a name to search...":
        update_treeview(showEquipment())
    else:
        filtered_data = [item for item in showEquipment() if search_term.lower() in item[0].lower()]
        update_treeview(filtered_data)

# Create the root frame of the app
root = Tk()
# Set the size of the frame
root.geometry("850x600")
root.resizable(False, False)
# Set the title of the frame
root.title("View Equipment")

# Create a label
label = ctk.CTkLabel(root, text="View Equipment", font=("arial", 18, "bold"), text_color="white", bg_color="#333")
label.pack(pady=(20, 10))

# Create a frame for the search section and treeview
frame = ctk.CTkFrame(root, bg_color="#555", width=800, height=400)
frame.place(relx=0.5, rely=0.45, anchor=CENTER)

# Entry for the search
def on_entry_click(event):
    if search_entry.get() == "Enter a name to search...":
        search_entry.delete(0, END)
        search_entry.configure(fg_color="black")

def on_focus_out(event):
    if search_entry.get() == "":
        search_entry.insert(0, "Enter a name to search...")
        search_entry.configure(fg_color="gray")

search_entry = ctk.CTkEntry(frame, font=("arial", 14), width=300, placeholder_text="Enter a name to search...")
search_entry.insert(0, "Enter a name to search...")
search_entry.bind("<FocusIn>", on_entry_click)
search_entry.bind("<FocusOut>", on_focus_out)
search_entry.grid(row=0, column=0, padx=10, pady=10)

# Search button
search_button = ctk.CTkButton(frame, text="Search", font=("arial", 14), fg_color="#4CAF50", text_color="white", command=search_equipment)
search_button.grid(row=0, column=1, padx=5, pady=10)

# Clear button
clear_button = ctk.CTkButton(frame, text="Clear", font=("arial", 14), fg_color="red", text_color="white", command=clear_search)
clear_button.grid(row=0, column=2, padx=5, pady=10)

# Create a Treeview within a CustomTkinter frame
tree_frame = Frame(frame)  # Create a separate frame for the Treeview and scrollbar
tree_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Create the Treeview
tree = ttk.Treeview(tree_frame, columns=("Name", "Quantity", "Type", "Status", "Training Required"), show="headings")
tree.pack(side=LEFT, fill=BOTH, expand=True)

# Define the column headings
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Type", text="Type")
tree.heading("Status", text="Status")
tree.heading("Training Required", text="Training Required")

# Define the column width
tree.column("Name", width=150)
tree.column("Quantity", width=100)
tree.column("Type", width=150)
tree.column("Status", width=100)
tree.column("Training Required", width=150)

# Add a vertical scrollbar to the Treeview
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=RIGHT, fill=Y)
tree.configure(yscrollcommand=scrollbar.set)

# Adjust column weights to make sure tree expands correctly
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=0)
frame.grid_columnconfigure(2, weight=0)

# Create the back button
back_button = ctk.CTkButton(frame, text="Back", font=("arial", 14), fg_color="red", text_color="white", command=back_membership)
back_button.grid(row=2, column=0, pady=20)

clear_tree_button = ctk.CTkButton(frame, text="Clear data", font=("arial", 14), fg_color="red", text_color="white", command=clear_tree)
clear_tree_button.grid(row=2, column=1, pady=20)

# Populate the Treeview with initial equipment data
update_treeview(showEquipment())

root.configure(bg="#333")
root.mainloop()
