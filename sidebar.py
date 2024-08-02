from tkinter import Tk,Label,Button,PhotoImage,Frame

root=Tk()

root_frame = Frame(root)
root_frame['bg']='#393b39'

px=0
py=15

someone_Gym=Label(root_frame,text='Pro-Fit-Gym',fg='#DC5F00',font=('RUbik',30),bg='#393b39')
someone_Gym.grid(column=0,row=0,padx=px,pady=py)

#--------------------home button------------------------
home_icon=PhotoImage(file=r'D:\WorkSpace\Project Python\images\home.png')
add_button=Button(root_frame,compound='left',text='Home',padx=30,font=('RUbik',20),fg='#EEEEEE',image=home_icon,relief='flat',bg='#393b39',activebackground='#292b29')
add_button.grid(column=0,row=1,pady=py)

#--------------------add member button-------------------
add_member_icon=PhotoImage(file=r'D:\WorkSpace\Project Python\images\add-user.png')
add_member=Button(root_frame,compound='left',text='Membership',padx=30,font=('RUbik',20),fg='#EEEEEE',image=add_member_icon,relief='flat',bg='#393b39',activebackground='#292b29')
add_member.grid(column=0,row=2,pady=py)

#--------------------gym equipment button-----------------
gym_equipment_icon=PhotoImage(file=r'D:\WorkSpace\Project Python\images\gym.png')
gym_equipment=Button(root_frame,compound='left',text='Gym equipment',padx=30,font=('RUbik',20),fg='#EEEEEE',image=gym_equipment_icon,relief='flat',bg='#393b39',activebackground='#292b29')
gym_equipment.grid(column=0,row=3,pady=py)

#--------------------trainer button-----------------------
trainer_icon=PhotoImage(file=r'D:\WorkSpace\Project Python\images\trainer.png')
trainer=Button(root_frame,compound='left',text='Trainer',padx=30,font=('RUbik',20),fg='#EEEEEE',image=trainer_icon,relief='flat',bg='#393b39',activebackground='#292b29')
trainer.grid(column=0,row=4,pady=py)

#--------------------gymers button------------------------
gymers_icon=PhotoImage(file=r'D:\WorkSpace\Project Python\images\membership.png')
gymers=Button(root_frame,compound='left',text='Gymers',padx=30,font=('RUbik',20),fg='#EEEEEE',image=gymers_icon,relief='flat',bg='#393b39',activebackground='#292b29')
gymers.grid(column=0,row=5,pady=py)

#--------------------employees button---------------------
employees_icon=PhotoImage(file=r'D:\WorkSpace\Project Python\images\employee.png')
employees=Button(root_frame,compound='left',text='Employees',padx=30,font=('RUbik',20),fg='#EEEEEE',image=employees_icon,relief='flat',bg='#393b39',activebackground='#292b29')
employees.grid(column=0,row=6,pady=py)

#--------------------create user account button------------
user_acc_icon=PhotoImage(file=r'D:\WorkSpace\Project Python\images\add-user.png')
user_acc=Button(root_frame,compound='left',text='Create User Account',padx=30,font=('RUbik',20),fg='#EEEEEE',image=user_acc_icon,relief='flat',bg='#393b39',activebackground='#292b29')
user_acc.grid(column=0,row=7,pady=py)

#--------------------logout button-------------------------
logout=Button(root_frame,text='Logout',padx=30,font=('RUbik',20),fg='#EEEEEE',relief='flat',bg='red',activebackground='darkred')
logout.grid(columnspan=2,row=8,pady=py)

root_frame.pack()
root.mainloop()
