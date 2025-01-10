import customtkinter as ctk
from PIL import Image
import os
def create_sidebar(root, callbacks):
    sidebar_frame = ctk.CTkFrame(root, width=200, height=600, fg_color="#242424", corner_radius=0)
    sidebar_frame.pack(side="left", fill="y")

    icon_path = f"{os.getcwd()}/Assets"
    #Main label
    main_label  = ctk.CTkLabel(sidebar_frame,text="Pro-Fit-GYM",text_color="white",font=("forte",18,"bold"))
    main_label.grid(row=0,column=0, padx=10, pady=10, sticky="ew")
    def create_button(icon_filename, text, command, row):
        image = Image.open(f"{icon_path}/{icon_filename}")
        icon = ctk.CTkImage(light_image=image, size=(32, 32))

        button = ctk.CTkButton(
            sidebar_frame,
            image=icon,
            text=text,
            compound="left",
            command=command,
            fg_color="#242424",  
            hover_color="#2c2c2c",  
            text_color="white",  
            border_width=0
        )
        button.grid(row=row, column=0, padx=10, pady=10, sticky="ew")

    # Create sidebar buttons with images
    create_button("home.png", "Home", callbacks.get("Home"), 1)
    create_button("membership-card.png", "Membership", callbacks.get("Membership"), 2)
    create_button("gym.png", "Equipment", callbacks.get("Equipment"), 3)
    create_button("trainer.png", "Trainers", callbacks.get("Trainers"), 4)
    create_button("employee.png", "Employees", callbacks.get("Employees"), 5)
    create_button("add-user.png", "Create User Account", callbacks.get("Create User Account"), 6)
