from threading import Thread
from tkinter import tix
from threading import Thread
try:
    from otp import generateOTP
    import validator
except Exception:
    from .otp import generateOTP
    from . import validator
import pymongo
from bson import json_util
from os import listdir
from tkcalendar import DateEntry
from plyer import notification
from PIL import ImageTk
import PIL.Image
import bcrypt
from bson import json_util
from datetime import datetime
from tkinter import messagebox as tmsg
from tkinter import *
import decouple
import os
print("Starting...")

# Krishna@Gravia#2022

STATIC_DIR = os.path.join("","static\\")

APP_NAME = "Gravia"
DATABASE = "Gravia"
COLLECTION = "users"

def main():
    win = tix.Tk()
    Login_Window(win)
    win.mainloop()

class Login_Window():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title(f"Login - {APP_NAME}")
        self.root.geometry("600x650")
        # self.root.wm_resizable(False,False)
        self.root.eval('tk::PlaceWindow . center')
        self.root.iconbitmap(f"{STATIC_DIR}icons\\app icon.ico")


        self.logedinVar = StringVar(value="No")

        self.myclient = pymongo.MongoClient(decouple.config("DATABASE_URI"))
        self.mydb = self.myclient[DATABASE]
        self.mycol = self.mydb[COLLECTION]

        self.tooltip = tix.Balloon(self.root)
        for sub in self.tooltip.subwidgets_all():
            sub.config(bg="white")

        # Background image
        self.bg = ImageTk.PhotoImage(file = STATIC_DIR + "backgrounds\\0.jpg")
        Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.frame = Frame(self.root, bg="black")
        self.frame.place(relx=0.5,rely=0.5,width=345,height=480, anchor="center")

        img1 = PIL.Image.open(STATIC_DIR + "avatar.png")
        img1 = img1.resize((100,100),PIL.Image.ANTIALIAS)
        self.phtoimage1 = ImageTk.PhotoImage(img1)
        Label(self.frame,image=self.phtoimage1,bg="black",bd=0).place(x=125,y=2)

        getstr = Label(self.frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        getstr.place(x=105,y=100)
        
        emailadress = Label(self.frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        emailadress.place(x=80,y=155)

        self.textuser = Entry(self.frame,font=("times new roman",15,"bold"),bg="white",fg="black")
        self.textuser.place(x=40,y=190,width=270)

        password = Label(self.frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=80,y=245)

        self.textpass = Entry(self.frame,font=("times new roman",15,"bold"),bg="white",fg="black",show="•")
        self.textpass.place(x=40,y=280,width=270)

        img2 = PIL.Image.open(STATIC_DIR + "avatar.png")
        img2 = img2.resize((25,25),PIL.Image.ANTIALIAS)
        self.phtoimage2 = ImageTk.PhotoImage(img2)
        Label(self.frame, image=self.phtoimage2, bg="black", bd=0).place(x=55,y=155)

        img3 = PIL.Image.open(STATIC_DIR + "lock.png")
        img3 = img3.resize((25,25),PIL.Image.ANTIALIAS)
        self.phtoimage3 = ImageTk.PhotoImage(img3)
        Label(self.frame, image=self.phtoimage3, bg="black", bd=0).place(x=55,y=245)

        img4 = PIL.Image.open(STATIC_DIR + "close eye.png")
        img4 = img4.resize((30,24),PIL.Image.ANTIALIAS)
        self.hide_image = ImageTk.PhotoImage(img4)

        img5 = PIL.Image.open(STATIC_DIR + "open eye.png")
        img5 = img5.resize((30,24),PIL.Image.ANTIALIAS)
        self.show_image = ImageTk.PhotoImage(img5)

        def show():
            def hide():
                self.textpass.config(show="•")
                self.show_button.config(image=self.show_image, command=show)
                self.tooltip.bind_widget(self.show_button, msg="Hide")

            self.textpass.config(show="")
            self.show_button.config(image=self.hide_image, command=hide)
            self.tooltip.bind_widget(self.show_button, msg="Hide")

        self.show_button = Button(self.frame, text="show Button", image=self.show_image, borderwidth=0, command=show)
        self.show_image.image = self.show_image
        self.show_button.place(x=275,y=280)
        self.tooltip.bind_widget(self.show_button, msg="Show")

        loginbtn = Button(self.frame,text="Login",font=("Helvetica",12,"bold"),cursor="hand2",bg="red",fg="white",bd=3,relief=SUNKEN,activebackground="red",activeforeground="white",command=lambda : self.login(event=None))
        loginbtn.place(x=200,y=340,width=100)

        signupbtn = Button(self.frame,text="Signup",font=("Helvetica",10,"bold"),cursor="hand2",fg="white",bg="black",bd=0,activebackground="black",activeforeground="white",command=self.openRegisterWindow)
        signupbtn.place(x=20,y=390) 

        forgotten_pass_btn = Button(self.frame,text="Forgotten password",font=("Helvetica",10,"bold"),cursor="hand2",fg="white",bg="black",bd=0,activebackground="black",activeforeground="white",pady=-20,anchor="n",command=self.forgot)
        forgotten_pass_btn.place(x=20,y=415) 

        def normal(event):
            signupbtn.config(font=("Helvetica",10,"bold"),fg="white")

        def signuph(event):
            signupbtn.config(font=("Helvetica",10,"bold underline"),fg="sky blue")
            signupbtn.bind("<Leave>",normal)       

        def normal2(event):
            forgotten_pass_btn.config(font=("Helvetica",10,"bold"),fg="white")

        def forgoth(event):
            forgotten_pass_btn.config(font=("Helvetica",10,"bold underline"),fg="sky blue")
            forgotten_pass_btn.bind("<Leave>",normal2)           

    # Key Bindings
        self.textuser.bind("<Return>",lambda e: self.textpass.focus_set())
        signupbtn.bind("<Enter>",signuph)
        forgotten_pass_btn.bind("<Enter>",forgoth)
        self.textpass.bind("<Return>",self.login)

    def __str__(self) -> str:
        return self.logedinVar.get()

    def login(self,event=None):
        if self.textuser.get()=="" or self.textpass.get()=="":
            tmsg.showerror("Error","All fields are required")
        else:
            myquery = { "email": self.textuser.get()}

            mydoc = self.mycol.find_one(myquery)
            encoded_password = self.textpass.get().encode('ascii', 'ignore')

            if mydoc != None:
                if bcrypt.checkpw(encoded_password, mydoc["password"]):
                    self.logedinVar.set("Yes")
                    data = json_util.dumps(mydoc,indent=4)
                    with open(f"UserData.json", "w") as otfile:
                        otfile.write(data)
                    with open(f"login.txt", "w") as lgfile:
                        lgfile.write("1")
                    self.root.destroy()
                    notification.notify(
                        app_name = "Gravia",
                        title = "Successfull",
                        message = f"Congratulations you successfully logedin in {APP_NAME}",
                        app_icon = r"G:\Programming\Python Projects\Gravia\static\Icons\Gravia icon.ico",
                        timeout = 5,
                    )
                else:
                    tmsg.showerror("Error","Invalid password")
            else:tmsg.showerror("Error","Invalid username and password")
  
    def forgot(self):
        def revert():
            self.frame2.place_forget()
            self.frame.place(x=130,y=85,width=345,height=480)

        def normal(event):
            loginbtn.config(font=("Helvetica",10,"bold"),fg="white")

        def high(event):
            loginbtn.config(font=("Helvetica",10,"bold underline"),fg="sky blue")
            loginbtn.bind("<Leave>",normal) 

        def sendotp():
            myquery = { "email": self.emailEntery.get()}

            mylist = []

            mydoc = self.mycol.find(myquery)

            for x in mydoc:
                mylist.append(x)

            if len(mylist) == 0:
                tmsg.showerror("Error","Invalid email id")
            else:
                otp_window = Tk()    
                otp = generateOTP(otp_window, self.emailEntery.get(), self.emailEntery.get(),self.newPassword)   
                otp_window.mainloop()
                self.newPassword()

        self.frame.place_forget()
        self.frame2 = Frame(self.root,bg="black")
        self.frame2.place(x=130,y=85,width=360,height=400)
        
        emailLabel  = Label(self.frame2,text="Enter you email",font=("times new roman",18,"bold"),bg="black",fg="white")
        emailLabel.place(x=40,y=100)

        self.emailEntery = Entry(self.frame2,font=("times new roman",15),bg="white",fg="black")
        self.emailEntery.place(x=40,y=140,width=270,height=40)

        otpButton = Button(self.frame2,text="Get otp",command=sendotp, font=("Helvetica",12,"bold"),bg="red",fg="white",bd=3,relief=SUNKEN,activebackground="red",activeforeground="white")
        otpButton.place(x=250,y=220,width=100)
        
        loginbtn = Button(self.frame2,text="Login via password", command=revert, font=("Helvetica",10,"bold"),fg="white",bg="black",bd=0,activebackground="black",activeforeground="white")
        loginbtn.place(x=20,y=350) 
        
        loginbtn.bind("<Enter>",high)

    def newPassword(self):
        def updatePassword():
            myquery = { "email": self.emailEntery.get()}
            mydoc = self.mycol.find_one(myquery)
            vdpassowrd = validator.validatePassword.check(self.newPasswordEntery.get())

            if self.newPasswordEntery.get() != self.reEnternewPasswordEntery.get():
                tmsg.showerror("Invalid Password","Both Password and re enter password entery's password must be same")
            
            elif self.newPasswordEntery.get() == mydoc["password"]:
                tmsg.showerror("Invalid password","New password must be different from old password")

            elif vdpassowrd != True: tmsg.showerror("Invalid Password","Password must be longer than 8 character which contain atleast one capital letter, one small, one special character and one number")

            else:
                unicoded_password = self.newPasswordEntery.get().encode('ascii', 'ignore')
                hashedpassword = bcrypt.hashpw(unicoded_password, bcrypt.gensalt())

                myquery = { "email": self.emailEntery.get() }
                newvalues = { "$set": { "password": hashedpassword } }

                self.mycol.update_one(myquery, newvalues)
                notification.notify(
                    title = "Successfull",
                    message = "Password updated successfully!",
                    # app_icon = "G:\\components\\succes.png",
                    timeout = 5,
                )
                self.frame3.place_forget()
                self.frame.place(x=130,y=85,width=345,height=480)

        self.frame2.place_forget()
        self.frame3 = Frame(self.root,bg="white")
        self.frame3.place(x=130,y=85,width=360,height=400)

        newPasswordLabel  = Label(self.frame3,text="Enter you new password",font=("times new roman",12,"bold"),bg="white")
        newPasswordLabel.place(x=40,y=60)

        self.newPasswordEntery = Entry(self.frame3,font=("times new roman",15),bg="white",fg="black",highlightcolor="blue",highlightbackground="blue", highlightthickness=2)
        self.newPasswordEntery.place(x=40,y=92,width=270,height=40)
        
        reEnternewPasswordLabel  = Label(self.frame3,text="Re-Enter you new password",font=("times new roman",12,"bold"), bg="white")
        reEnternewPasswordLabel.place(x=38,y=180)

        self.reEnternewPasswordEntery = Entry(self.frame3,font=("times new roman",15),bg="white",fg="black",highlightcolor="blue",highlightbackground="blue", highlightthickness=2)
        self.reEnternewPasswordEntery.place(x=40,y=210,width=270,height=40)

        submitButton = Button(self.frame3,text="Submit",command=updatePassword, font=("Helvetica",12,"bold"),bg="white",fg="blue",bd=3,relief=SUNKEN,highlightcolor="blue",highlightbackground="blue", highlightthickness=2)
        submitButton.place(x=250,y=330,width=100)

    def openRegisterWindow(self):
        new_window = Toplevel(self.root)
        self.app = Signup(new_window, APP_NAME)

class Signup:
    def __init__(self, root, appname) -> None:
        self.root = root
        APP_NAME = appname
        self.root.title(f"{appname} - Signup")
        self.root.geometry("950x700+205+14")
        self.root.state("zoomed")
        self.root.minsize(950, 530)
        self.root.iconbitmap(STATIC_DIR + "icons\\app icon.ico")
        # self.root.iconbitmap(PhotoImage(r"static\app icon.ico"))
        # self.root.wm_overrideredirect(True)

        self.tooltip = tix.Balloon(self.root)
        for sub in self.tooltip.subwidgets_all():
            sub.config(bg="white")

        # Text variables
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.phonenumber = StringVar()
        self.dob = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.password = StringVar()
        self.cPassword = StringVar()
        self.TAM = IntVar()

        # Background image
        path = STATIC_DIR + "backgrounds"
        images = listdir(path)
        self.count = -1

        self.bg = ImageTk.PhotoImage(PIL.Image.open(f"{STATIC_DIR}\\backgrounds\\{images[0]}"))
        background_label = Label(self.root, image=self.bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def change():
            if self.count == len(images) - 1:
                self.bg = ImageTk.PhotoImage(PIL.Image.open(f"{STATIC_DIR}\\backgrounds\\{images[0]}")
                )
                background_label.config(image=self.bg)
                background_label.update()
                self.count = 0
            else:
                self.bg = ImageTk.PhotoImage(
                    PIL.Image.open(
                        f"{STATIC_DIR}\\backgrounds\\{images[self.count + 1]}")
                )
                background_label.config(image=self.bg)
                background_label.update()
                self.count += 1
            self.root.after(10 * 1000, change)

        Thread(target=change).start()

        frame = Frame(self.root, bg="white")
        frame.place(relx=0.5,rely=0.5, width=950, height=550, anchor="center")

        firstname_label = Label(
            frame,
            text="First name",
            font=("times new roman", 20, "bold"),
            background="white",
        )
        firstname_label.place(x=50, y=50)

        firstname_entry = Entry(
            frame, font=("times new roman", 20), textvariable=self.firstname
        )
        firstname_entry.place(x=50, y=90)

        lastname_label = Label(frame,text="Last name",font=("times new roman", 20, "bold"),background="white",)
        lastname_label.place(x=450, y=50)

        lastname_entry = Entry(frame, font=("times new roman", 20), textvariable=self.lastname)
        lastname_entry.place(x=450, y=90)

        phonenumber_label = Label(frame,text="Phone no.",font=("times new roman", 20, "bold"),background="white",)
        phonenumber_label.place(x=50, y=150)

        phonenumber_entry = Entry(frame, font=("times new roman", 20), textvariable=self.phonenumber)
        phonenumber_entry.place(x=50, y=190)

        date_of_birth_label = Label(frame,text="Date of Birth",font=("times new roman", 20, "bold"),background="white",)
        date_of_birth_label.place(x=450, y=150)

        date_of_birth_chooser = DateEntry(frame, cursor="hand2", state="readonly", textvariable=self.dob)
        date_of_birth_chooser.place(x=460, y=190)
        date_of_birth_chooser.bind("<ButtonPress-1>", lambda e: date_of_birth_chooser.drop_down())

        email_label = Label(frame,text="Email",font=("times new roman", 20, "bold"),background="white",)
        email_label.place(x=50, y=250)

        email_entry = Entry(frame, font=("times new roman", 20), textvariable=self.email)
        email_entry.place(x=50, y=290)

        address_label = Label(frame,text="Address (optional)",font=("times new roman", 20, "bold"),background="white",)
        address_label.place(x=450, y=250)

        self.address_entry = Entry(frame, font=("times new roman", 20), textvariable=self.address)
        self.address_entry.place(x=450, y=290)

        password_label = Label(frame,text="Password",font=("times new roman", 20, "bold"),background="white",)
        password_label.place(x=50, y=350)

        password_entry = Entry(frame, font=("times new roman", 20), textvariable=self.password, show="•")
        password_entry.place(x=50, y=390)

        confirm_password_label = Label(frame,text="Confirm Password",font=("times new roman", 20, "bold"),background="white",)
        confirm_password_label.place(x=450, y=350)

        confirm_password_entry = Entry(frame, font=("times new roman", 20), textvariable=self.cPassword, show="•")
        confirm_password_entry.place(x=450, y=390)

        self.hide_image = ImageTk.PhotoImage(PIL.Image.open(r"static\close eye.png"))
        self.show_image = ImageTk.PhotoImage(PIL.Image.open(r"static\open eye.png"))

        def show():
            def hide():
                password_entry.config(show="•")
                confirm_password_entry.config(show="•")
                self.show_button.config(image=self.show_image, command=show)
                self.tooltip.bind_widget(self.show_button, msg="Show")

            password_entry.config(show="")
            confirm_password_entry.config(show="")
            self.show_button.config(image=self.hide_image, command=hide)
            self.tooltip.bind_widget(self.show_button, msg="Hide")

        self.show_button = Button(
            frame, text="show Button", image=self.show_image, bd=0, command=show
        )
        self.show_image.image = self.show_image
        self.show_button.place(x=780, y=390)
        self.tooltip.bind_widget(self.show_button, msg="Show")

        termsandconditions = Checkbutton(
            frame,
            text="Terms & Conditions",
            background="white",
            foreground="red",
            activeforeground="yellow",
            font=("times new roman", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=self.TAM,
        )
        termsandconditions.place(x=50, y=460)

        # signup_image = ImageTk.PhotoImage(PIL.Image.open(r"static\signup.jpg"))
        signup_button = Button(frame, text="Signup", font="arial 14 bold", bd=0, command=self.signup)
        # signup_image.image = signup_image
        signup_button.place(x=780, y=500)

        # Events
        firstname_entry.bind("<Return>", lambda e: lastname_entry.focus_set())
        lastname_entry.bind("<Return>", lambda e: phonenumber_entry.focus_set())
        phonenumber_entry.bind("<Return>", lambda e: email_entry.focus_set())
        email_entry.bind("<Return>", self.validateMail)
        self.address_entry.bind("<Return>", lambda e: password_entry.focus_set())
        password_entry.bind("<Return>", lambda e: confirm_password_entry.focus_set())
        confirm_password_entry.bind("<Return>", lambda e: signup_button.focus_set())

    def signup(self):
        fname = self.firstname.get()
        lname = self.lastname.get()
        phone = self.phonenumber.get()
        d = self.dob.get()
        e = self.email.get()
        p = self.password.get()
        cp = self.cPassword.get()
        t = self.TAM.get()

        if (
            fname == ""
            or lname == ""
            or phone == ""
            or d == ""
            or e == ""
            or p == ""
            or cp == ""
        ):
            tmsg.showerror(
                "Could not Signup", "All fields are required, please fill all fields"
            )

        try:
            validator.validatePhonenumber.check(phone)
        except validator.invalidCountryCode:
            tmsg.showerror(
                "Invalid phone number",
                "Please write correct number with correct country code with the number",
            )
        c = validator.validatePhonenumber.getCountry(phone)

        vdpassowrd = validator.validatePassword.check(p)

        if t == 0:
            tmsg.showerror(
                "Terms & Conditions", "Please accept our terms & conditions to continue"
            )

        elif vdpassowrd != True: tmsg.showerror("Error","Your password is weak it means your pass can be hack.\nTo prevent it from hackers your password must be longer than 8 character which contain atleast one capital letter, one small, one special character and one number")

        elif p != cp:
            tmsg.showerror(
                "Password", "Password an Confirm password not matched")

        else:
            otp_window = Tk()    
            generateOTP(otp_window, e, fname, self.register)   
            otp_window.mainloop()

    def register(self):
        fname = self.firstname.get()
        lname = self.lastname.get()
        phone = self.phonenumber.get()
        d = self.dob.get()
        e = self.email.get()
        ad = self.address.get()
        p = self.password.get()
        c = validator.validatePhonenumber.getCountry(phone)

        unicoded_password = p.encode('ascii', 'ignore')
        hashedpassword = bcrypt.hashpw(unicoded_password, bcrypt.gensalt())

        myclient = pymongo.MongoClient(decouple.config("DATABASE_URI"))
        mydb = myclient[DATABASE]
        mycol = mydb[COLLECTION]

        myquery = {"email": e}

        mylist = []

        mydoc = mycol.find(myquery)
        for x in mydoc:
            mylist.append(x)

        if len(mylist) == 0:
            mydict = {
                "firstname": fname,
                "lastname": lname,
                "phone": phone,
                "Date of birth": d,
                "email": e,
                "couuntry": c,
                "address": ad,
                "password": hashedpassword,
                "registered on": datetime.utcnow(),
                "assistant_name": "Gravia"
            }

            x = mycol.insert_one(mydict)
            notification.notify(
                title="Sucesfully",
                message=f"You are succesfully signed up in {APP_NAME}",
            )
        else:
            tmsg.showerror(
                "Error",
                "User already exist.\nYo can try again with different email.",
            )

    def openLogin(self):
        self.root.destroy()

    def validateMail(self, e=None):
        email = self.email.get()
        m = validator.validateEmail.check(email)
        if m:
            self.address_entry.focus_set()
        else:
            tmsg.showwarning(
                "Invalid email", "This email is not valid.\nPlease check it again"
            )

if __name__ == '__main__':
    main()