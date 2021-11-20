import smtplib
import random
from tkinter.constants import BOTTOM, SUNKEN
from decouple import config
from tkinter import Button, Tk, Entry, Label
from tkinter.messagebox import *

class generateOTP:
    def __init__(self, root, email_address, sendername, callback) -> None:
        self.callback = callback
        self.root = root
        self.root.title("OTP")
        self.root.eval('tk::PlaceWindow . center')
        self.otp = random.randint(1,90000000)
        # self.root.protocol("WM_DELETE_WINDOW", self.onclick)

        Label(self.root, text="Enter your eight digit otp", font="arial 10 bold").pack(pady=8,padx=5)
        self.otp_entry = Entry(self.root)
        self.otp_entry.pack()
        submit_button = Button(self.root, text="Submit", borderwidth=4, relief=SUNKEN, font="lucida 10", command=self.checkOTP)
        submit_button.pack(side=BOTTOM,pady=4)
        # submit_button = Button(self.root, text="ReCorrect email", borderwidth=4, relief=SUNKEN, font="lucida 10", command=self.root.quit)
        # submit_button.pack(side=BOTTOM,pady=4)

        def sendEmail(to,sub,content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(config("EMAIL_ADDRESS"), config("PASSWORD"))
            server.sendmail(email_address, to,  f"Subject: {sub}\n\n{content}")
            server.close()

        try:
            sub = "OTP"         
            content = f'''
            Hi {sendername},
            Here is verification code -
            
                    {self.otp}

            Enter it in poped up window and then continue signup process.
            If it is not you don't worry, just ignore it.
            '''
            to = email_address
            sendEmail(to,sub,content)
            print("Mail sent!")
            showinfo("Email Verification", f"A 8 digit code ws sent on {email_address} to verify you.\nEnter yout one time otp in pop up window")
        except Exception as e:
            print(e)
            print("mail not sent")
        
    def checkOTP(self):
        answer = self.otp_entry.get()
        print("Actual otp:",self.otp)
        print("Entered otp:",answer)
        if answer.isalnum and len(answer) == 8:
            if int(answer) == self.otp:
                print("OTP match succesfully")
                showinfo("Info","Your OTP were matched successfully")
                self.callback()
                self.root.destroy()
            else:
                print("OTP dosen't match!")
                showerror("Invalid OTP","Your OTP were not matched successfully. \nMake sure you entered correct OTP")
                return False
        else:
            print("Invalid OTP")
            return False

    def onclick(self):
        q = askokcancel("Exit","Do you really want too quit? Your all progress will not be save")
        if q:
            root.destroy()
        

if __name__ == '__main__':
    root = Tk()
    # Label(root,text="SOmething").pack()
    root.geometry("230x100")
    # window = Tk()
    # window.geometry("230x100")
    generateOTP(root,"devloper2345@gmail.com", "Krishna")
    # window.mainloop()
    root.mainloop()