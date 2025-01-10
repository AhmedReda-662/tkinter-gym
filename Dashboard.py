import customtkinter as ctk
from tkinter import ttk
from tkinter import *
from backend import *
from os import getcwd
import sidebar
#initialize the main frame
root = ctk.CTk()
root.geometry("850x600")
root.resizable(False,False)
root.title("Dashboard")

main_label = ctk.CTkLabel(root,text="Dashboard | Overview",text_color="White",font=("arial",20,"bold"))
main_label.pack(side=LEFT,anchor=NE,padx=30,pady=30)

# Create the labels frame
labels_frame = ctk.CTkFrame(root,corner_radius=10,width=800,height=400)
labels_frame.place(rely=0.2,relx=0.025)
#Create a container for the labels
labels_container = ctk.CTkFrame(labels_frame,corner_radius=10,width=780,height=200,fg_color="#2b2b2b")
labels_container.place(rely=0.25,relx=0.6,anchor=CENTER)
#Create the member frame
member_frame = ctk.CTkFrame(labels_container,corner_radius=10,width=200,height=100,fg_color="#333")
member_frame.place(rely=0.2,relx=0)
member_label = ctk.CTkLabel(member_frame,text="""Members
                            """,text_color="White",font=("arial",15,"bold"))
member_label.pack(padx=10,pady=10)
member_number_label = ctk.CTkLabel(member_frame,text=f"{len(showMembership())}",text_color="white",font=("arial",15,"bold"))
member_number_label.pack(padx=10,pady=10)

#Create the trainer frame
trainer_frame = ctk.CTkFrame(labels_container,corner_radius=10,width=200,height=100,fg_color="#333")
trainer_frame.place(rely=0.2,relx=0.2)
trainer_label = ctk.CTkLabel(trainer_frame,text="""Trainers
                            """,text_color="White",font=("arial",15,"bold"))
trainer_label.pack(padx=10,pady=10)
trainer_number_label = ctk.CTkLabel(trainer_frame,text=f"{len(showTrainer())}",text_color="white",font=("arial",15,"bold"))
trainer_number_label.pack(padx=10,pady=10)
#Create the equipment frame
equipment_frame = ctk.CTkFrame(labels_container,corner_radius=10,width=200,height=100,fg_color="#333")
equipment_frame.place(rely=0.2,relx=0.4)
equipment_label = ctk.CTkLabel(equipment_frame,text="""Equipments
                            """,text_color="White",font=("arial",15,"bold"))
equipment_label.pack(padx=10,pady=10)
equipment_number_label = ctk.CTkLabel(equipment_frame,text=f"{len(showEquipment())}",text_color="white",font=("arial",15,"bold"))
equipment_number_label.pack(padx=10,pady=10)
#Create the employees frame
employees_frame = ctk.CTkFrame(labels_container,corner_radius=10,width=200,height=100,fg_color="#333")
employees_frame.place(rely=0.2,relx=0.6)
employees_label = ctk.CTkLabel(employees_frame,text="""Employees
                            """,text_color="White",font=("arial",15,"bold"))
employees_label.pack(padx=10,pady=10)
employees_number_label = ctk.CTkLabel(employees_frame,text=f"{0}",text_color="white",font=("arial",15,"bold"))
employees_number_label.pack(padx=10,pady=10)

root.mainloop()