from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from backend import showMembership

def back_membership():
    root.destroy() # close the windwo
    import membership # open the window
def insertData():
    result = showMembership()
    for i in result:
        tree.insert('','end',values=i)
# Create the root frame of the app
root = Tk()
# Set the size of the frame
root.geometry("1000x600")
root.resizable(False, False)
# Set the title of the frame
root.title("View Memberships")

# Create a label
label = ctk.CTkLabel(root, text="View Memberships", font=("arial", 18, "bold"), text_color="white", bg_color="#333")
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
search_button = ctk.CTkButton(frame, text="Search", font=("arial", 14), fg_color="#4CAF50", text_color="white")
search_button.grid(row=0, column=1, padx=5, pady=10)

# Clear button
clear_button = ctk.CTkButton(frame, text="Clear", font=("arial", 14), fg_color="red", text_color="white")
clear_button.grid(row=0, column=2, padx=5, pady=10)

# Create a Treeview within a CustomTkinter frame
tree_frame = Frame(frame)  # Create a separate frame for the Treeview and scrollbar
tree_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Create the Treeview
tree = ttk.Treeview(tree_frame, columns=("ID", "First Name","Middle Name","Last Name", "Age", "Gender","Address","Subscription"), show="headings")
tree.pack(side=LEFT, fill=BOTH, expand=True)

# Define the column headings
tree.heading("ID", text="ID")
tree.heading("First Name", text="First Name")
tree.heading("Middle Name", text="Middle Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Age", text="Age")
tree.heading("Gender", text="Gender")
tree.heading("Address" , text="Address")
tree.heading("Subscription", text="Subscription")

# Define the column width
tree.column("ID", width=50)
tree.column("First Name", width=150)
tree.column("Middle Name", width=150)
tree.column("Last Name", width=150)
tree.column("Age", width=50)
tree.column("Gender", width=100)
tree.column("Address" , width=100)
tree.column("Subscription", width=150)

# insert data
insertData()
# Add a vertical scrollbar to the Treeview
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=RIGHT, fill=Y)
tree.configure(yscrollcommand=scrollbar.set)
# Add a horizontal scrollbar to the tree view
scrollbar_x = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
scrollbar.pack(side=BOTTOM, fill=X)
tree.configure(xscrollcommand=scrollbar.set)
# Adjust column weights to make sure tree expands correctly
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=0)
frame.grid_columnconfigure(2, weight=0)

# Create the view button
view_button = ctk.CTkButton(frame, text="View", font=("arial", 14), fg_color="#4CAF50", text_color="white")
view_button.grid(row=2, column=0, pady=20)

# Create the back button
back_button = ctk.CTkButton(frame, text="Back", font=("arial", 14), fg_color="red", text_color="white",command=back_membership)
back_button.grid(row=2, column=1, pady=20)

root.configure(bg="#333")
root.mainloop()
