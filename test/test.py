from tkinter import *
from bson import json_util

def frameSwitch(framename):
    profileFrame.pack_forget()
    generalFrame.pack_forget()
    appearenceFrame.pack_forget()
    hfm_setting_Frame.pack_forget()
    framename.pack(fill=BOTH, expand= True)
    pass

def colorTheme():
    pass

root = Tk()
root.geometry('800x600')

bg_color = "#D0D3D3"
fg_color = "white"

# Getting user info
user_data = open('UserData.json')
user_info = json_util.loads(user_data.read())

# Frames 
sidebarFrame = Frame(root, bg=bg_color)
sidebarFrame.pack(side=LEFT,fill=Y, ipadx=20)

profileFrame = Frame(root, bg="red")
generalFrame = Frame(root, bg="green")
appearenceFrame = Frame(root, bg="blue")
hfm_setting_Frame = Frame(root, bg="yellow")

# Nav Buttons 
profileButton = Button(sidebarFrame, bd=0, bg=bg_color, text="Profile", font=("arial", 14), anchor="w", padx=10, pady=5, command=lambda:  frameSwitch(profileFrame), activebackground="#575757")
profileButton.pack(fill=X,pady=(0,5))
profileButton.bind("<Enter>", lambda e: profileButton.config(bg="#575757"))
profileButton.bind("<Leave>", lambda e: profileButton.config(bg=bg_color))

generalButton = Button(sidebarFrame, bd=0, bg=bg_color, text="General", font=("arial", 14), anchor="w", padx=10, pady=5, command=lambda:  frameSwitch(generalFrame), activebackground="#575757")
generalButton.pack(fill=X,pady=(0,5))
generalButton.bind("<Enter>", lambda e: generalButton.config(bg="#575757"))
generalButton.bind("<Leave>", lambda e: generalButton.config(bg=bg_color))

appearenceButton = Button(sidebarFrame, bd=0, bg=bg_color, text="Appearance", font=("arial", 14), anchor="w", padx=10, pady=5, command=lambda: frameSwitch(appearenceFrame), activebackground="#575757")
appearenceButton.pack(fill=X,pady=(0,5))
appearenceButton.bind("<Enter>", lambda e: appearenceButton.config(bg="#575757"))
appearenceButton.bind("<Leave>", lambda e: appearenceButton.config(bg=bg_color))

hfm_setting_Button = Button(sidebarFrame, bd=0, bg=bg_color, text="Handsfreemode", font=("arial", 14), anchor="w", padx=10, pady=5, command=lambda: frameSwitch(hfm_setting_Frame), activebackground="#575757")
hfm_setting_Button.pack(fill=X,pady=(0,5))
hfm_setting_Button.bind("<Enter>", lambda e: hfm_setting_Button.config(bg="#575757"))
hfm_setting_Button.bind("<Leave>", lambda e: hfm_setting_Button.config(bg=bg_color))

# Frame content 
first_nameLabel = Label(profileFrame, text=f"First name - {user_info['firstname']}")
last_nameLabel = Label(profileFrame, text=f"Last name - {user_info['lastname']}")
phone_Label = Label(profileFrame, text=f"Phone - {user_info['phone']}")
email_Label = Label(profileFrame, text=f"Email - {user_info['email']}")
address_Label = Label(profileFrame, text=f"Address - {user_info['address']}")

first_nameLabel.pack()
last_nameLabel.pack()
phone_Label.pack()
email_Label.pack()
address_Label.pack()

root.mainloop()