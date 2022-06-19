print("initializing modules...")

# try:
import datetime
import os
import random
import winsound
from textwrap import wrap
from tkinter import tix
from tkinter.messagebox import *
from threading import Thread
from time import sleep
from tkinter import *

import pyautogui
import pyttsx3
import speech_recognition as sr
from bson import json_util
from PIL import Image, ImageTk
from plyer import notification

from modules import (appManager, auth, automation, hotwordDetection, openApi,
                     settings, speak, systemTasks, talk, webOpen)
from modules.modern_components import *

print("Done!")
# except Exception as error:
#     from PIL import Image, ImageTk
#     showerror("Error",error)
#     print(error)
#     pass

def main():
    file = "0110110001101111011001110110100101101110.bin"
    with open(file, 'r') as logedin:
        ld = logedin.read()
        ld = int(ld)
        if ld == 0:
            win = tix.Tk()
            app = auth.Login_Window(win)
            win.mainloop()
            if app.logedinVar.get() == "Yes":
                with open(file, 'w') as f:
                    f.write("1")
                root = Tk()
                root.geometry('900x700')
                root.title('Gravia')
                root.iconify()
                root.iconbitmap(r"static\Icons\Gravia.ico")
                # root.overrideredirect(True)
                
                try:
                    gravia(root)
                except Exception as e:
                    print(e)
                    showerror("Error",e)
                    retry = askretrycancel("Error","An unexpected error accoured \nPlease try again later")
                    if retry:
                        try:
                            root.destroy()
                            gravia(root)
                        except Exception as e:
                            with open("errors.txt","a") as ef:
                                ef.write(f"{datetime.datetime.now().strftime('%c')}: {str(e)}\n")
                                print(e)
                                showerror("Error","Sorry, we could not solve this error")
                                exit()

                root.mainloop()

        else:
            root = Tk()
            root.geometry('900x700')
            root.title('Gravia')
            root.iconify()
            root.iconbitmap(r"static\Icons\Gravia.ico")
            # root.overrideredirect(True)

            # try:
            gravia(root)
            # except Exception as e:
            #     print(e)
            #     showerror("Error",e)
            #     retry = askretrycancel("Error","An unexpected error accoured \nPlease try again later")
            #     if retry:
            #         try:
            #             root.destroy()
            #             gravia(root)
            #         except Exception as e:
            #             with open("errors.log","a") as ef:
            #                 ef.write(f"{datetime.datetime.now().strftime('%c')}: {str(e)}\n")
            #                 print(e)
            #                 showerror("Error","Sorry, we could not solve this error")
            #                 exit()

            root.mainloop()

class gravia:
    def __init__(self, parent):
        print("Starting GUI")
        self.root = parent
        # titleBar = CreateModernTitlebar(self.root,title_text = 'Gravia' , bg = "white" , fg = 'black')
        # titleBar.resizeable = True
        # titleBar.packBar()
        clear = lambda: os.system('cls')
        clear()

        # Getting user info
        user_data = open('UserData.json')
        self.user_info = json_util.loads(user_data.read())

        # Variables
        self.listen = BooleanVar(value=False)
        self.handfreeModevar = IntVar()
        self.queryvar = StringVar()
        self.Iboxvar = StringVar()

        top_menu_frame = Frame(self.root, bg="white", bd=0)
        top_menu_frame.pack(side=TOP,fill=X)

        MenuLabel = Button(top_menu_frame, text="⁝", bg="white", command=self.menu, font="helvetica 16 bold",padx=5, borderwidth=0)
        MenuLabel.pack(side=LEFT,padx=3)

        self.timeLabel = Label(top_menu_frame,text=datetime.datetime.now().strftime("%c"), bg="white",fg="dark green", font="Digital-7 20 bold")
        self.timeLabel.pack(side=RIGHT,pady=2)
        self.timeLabel.after(1000, lambda : Thread(target=self.clock).start())

        # Statusbar
        self.statusbar_frame = Frame(self.root, borderwidth=0, bg="white")
        self.statusbar_frame.pack(side=BOTTOM, fill=X)
        self.statusvar = StringVar()
        self.sbar = Label(self.statusbar_frame,textvariable=self.statusvar, anchor="w", borderwidth=0, bg="white", font="Lucida 10 bold")
        self.sbar.pack(side=LEFT)

        bFrame = Frame(self.root, borderwidth=2, relief=RAISED, bg="white", bd=0)
        bFrame.pack(side=BOTTOM, fill=X)

        self.outputBox = Text(self.root,bg="white",fg="black",font=("cascadia code", 14), state="disabled", bd=0)
        self.outputBox.pack(fill=BOTH, expand=True)
        self.outputBox.tag_configure('right', justify='right')
        self.OlOf()

        self.Ibox = EntryWithPlaceholder(bFrame,placeholder="Ask anything to Gravia...",textvariable=self.Iboxvar, font="lucida 12", bd=0)
        self.Ibox.pack(padx=2,pady=0,fill=X, side=LEFT, expand=True)
        self.Ibox.bind("<Key>", lambda e: Thread(target=self.swap_button).start())
        self.Ibox.bind("<Return>", self.send_through_Ibox)

        img1 = Image.open("static\Icons\Mic.png")
        img1 = img1.resize((30,30),Image.ANTIALIAS)
        self.micImage = ImageTk.PhotoImage(img1)
        self.listenButton = Button(bFrame, state="normal", image=self.micImage, borderwidth=0, bg="white", disabledforeground="black", command=lambda: Thread(target=self.makeTrue).start())
        # self.listenButton.bind("<Double-Button>",)
        self.listenButton.micImage = self.micImage
        self.listenButton.pack(pady=5,side=RIGHT)

        self.engine = pyttsx3.init('sapi5')
        # getting details of current voice
        voices = self.engine.getProperty('voices')
        # print(voices[0])
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 170)

        # Thread(target=self.reminders).start()
        # Thread(target=self.welcome_notification()).start()
        # Thread(target=self.wishMe()).start()

    def displayOutput(self,audio, wordwrap=True):
        list = ["ok", "hey", "gravy", 'gravia']
        for i in list:
            audio = audio.replace(i, "", 1)
        self.outputBox.config(state="normal")
        if wordwrap:
            textaudio = wrap(audio, width=35)
            text = '\n'.join(textaudio)
            try:
                self.outputBox.insert(END, f"{text}\n")
            except Exception:
                self.outputBox.insert(END, f"{text}\n")
        else:
            try:
                self.outputBox.insert(END, f"{audio}\n")
            except Exception:
                self.outputBox.insert(END, f"{audio}\n")
        self.outputBox.config(state="disabled")
        self.outputBox.see("end")

    def mainspeakfunc(self, audio):
        self.engine.say(audio)
        try:
            self.engine.runAndWait()
        except Exception: 
            self.engine.runAndWait()
            self.engine.endLoop()

    def speak(self, audio, wordwrap=True):
        # Thread(target=lambda: self.mainspeakfunc(audio)).start()
        self.mainspeakfunc(audio)
        Thread(target=lambda:self.displayOutput(audio)).start()
        
 
    def makeTrue(self):
        self.takeCommand()
        self.exmain()

    def welcome_notification(self):
        notification.notify(
            title="Gravia",
            message = f"Welcome to Gravia, {self.user_info['firstname']}",
            app_icon= "static\\Icons\\Gravia icon.ico",
            timeout=1,
        )
    
    def OlOf(self):
        import requests
        sleep(1.5)
        try:
            r = requests.get("https://www.google.com")
            self.statusvar.set("Online")
        except Exception: 
            showwarning("No Internet", "Looks like you have no internet connection please kindly try to connect internet, otherwise some features may not work")
            self.statusvar.set("Offline")

    def nextupdate(self):
        showwarning("Themes","More themes are not awailaible")
        showinfo("Update","More themes are comming soon in next update")

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        gd = [
            "Every morning is a new blessing, a second chance that life gives you because you’re so worth it. Have a great day ahead. Good morning!",
            "Get up early in the morning and don’t forget to say thank you to God for giving you another day! Good morning!",
            "Good morning, my friend! Life gives us new opportunities every day, so hoping today will be full of good luck and prosperity for you!",
            "Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good morning!",
            "Good morning, baby. Having you by my side makes me very happy.",
        ]

        goodf = [
            "With a deep blue sky over my head and a relaxing wind around me, the only thing I am missing right now is the company of you. I wish you a refreshing afternoon!"
            "You must be so tired after a long day, but do you what? The day is still so young and full of positive energy for you to absorb. Good afternoon!",
            "The day has come a halt realizing that I am yet to wish you a great afternoon. My dear, if you thought you were forgotten, you’re so wrong. Good afternoon!",
            "Good afternoon! May the sweet peace be part of your heart today and always and there is life shining through your sigh. May you have much light and peace.",
            "I wish I were with you this time of the day. We hardly have a beautiful afternoon like this nowadays. Wishing you a peaceful afternoon!"
        ]

        goode = [
            "Good evening! I hope you had a good and productive day. Cheer up!",
            "No matter how bad your day has been, the beauty of the setting sun will make everything serene. Good evening.",
            "May the setting sun take down all your sufferings with it and make you hopeful for a new day. Good evening!",
            "Thank you for making my days beautiful and evenings full of joy. You are the reason behind all my smiles and laughs. Wishing you a good evening.",
            "It doesn’t matter how hectic your day was, you can’t help admiring the beauty of this evening. I hope you are having a good time right now! Good evening!",
        ]

        gdm = random.choice(gd)
        gdg = random.choice(goodf)
        gde = random.choice(goode)

        if hour >= 0 and hour < 12:
            self.speak(f"Good Morning! {self.user_info['firstname']}")
            notification.notify(
                title="Good Morning",
                message=gdm,
                app_icon="static\\Icons\\wish-list.ico",
                timeout=10,
            )

        elif hour >= 12 and hour < 17:
            self.speak(f"Good Afternoon {self.user_info['firstname']} ")
            notification.notify(
                title="Good Afternoon",
                message=gdg,
                app_icon="static\\Icons\\wish-list.ico",
                timeout=10,
            )

        else:
            self.speak(f"Good Evening {self.user_info['firstname']}")
            notification.notify(
                title="Good Evening",
                message=gde,
                app_icon="static\\Icons\\wish-list.ico",
                timeout=10,
            )

    def reminders(self):
        time = datetime.datetime.now().strftime("%H.%M")
        if time >= "8.00" and time < "9.00":
            notification.notify(
                title="Gravia Reminder",
                message="It's bath time, work will be done later, \nBathing can improve heart health. \nTaking a bath may help you to breathe easier.\nYour brain and nervous system can benefit from bathing.",
                app_icon=r"static\Icons\reminder icon.ico",
                timeout=8,
            )

        elif time >= "19.30" and time < "20.30":
            notification.notify(
                title="Gravia Reminder",
                message="It is your dinner time so you should go to dinner",
                app_icon=r"static\Icons\Dinner icon.ico",
                timeout=8,
            )

        elif time >= "17.30" and time < "18.00":
            notification.notify(
                title="Playing (Gravia Reminder)",
                message="It's time to play, you should go play with your friends",
                app_icon=r"static\Icons\playing reminder icon.ico",
                timeout=8,
            )

        elif time >= "22":
            notification.notify(
                title="Gravia Reminder",
                message="Today a lot of work is done, now is the time to do the rest of the sleep later, and I also need some rest so good night sir",
                app_icon=r"static\Icons\sleep.ico",
                timeout=10,
            )
        sleep(5*60)
        self.reminders()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.statusvar.set("Listening...")
            winsound.PlaySound(r"static\sound clips\Click.wav",winsound.SND_FILENAME)
            r.pause_threshold = 0.9
            audio = r.listen(source)
            winsound.PlaySound(r"static\sound clips\End.wav",winsound.SND_ASYNC)
        try:
            self.statusvar.set("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            self.queryvar.set(query)
            self.outputBox.config(state="normal")
            self.outputBox.insert('end', f"{query}\n", 'right')
            self.outputBox.config(state="disabled")

        except Exception as e:
            winsound.PlaySound(r"static\sound clips\Error.wav",winsound.SND_ASYNC)
            self.speak("Sorry, I can not hear that")
            pass
        
    def exmain(self):
        if self.queryvar.get() != None:
            self.statusvar.set("Fetching & printing results....")
            self.listenButton.config(state=DISABLED)
            
            query = self.queryvar.get().lower()
            # Logic for executing tasks based on query
            webQuery = webOpen.webOpen(query, self.OlOf, self.statusvar, self.speak)
            if webQuery.status == False:
                normalTalk = talk.Talk(query, self.statusvar, self.speak)
                if normalTalk.status == False:
                    openapi = openApi.Api(query,self.statusvar,self.speak, self.engine.setProperty)
                    if openapi.status == False:
                        automate = automation.AutoMate(query, self.speak, self.takeCommand)
                        if automate.status == False:
                            systemTask = systemTasks.Tasks(query, self.statusvar, self.speak)
                            if systemTask.status == False and "open" in query or "close" in query:
                                try:
                                    app = appManager.Manager(query,self.speak ,self.statusvar)
                                    if app.openr != None:
                                        self.speak(app.openr)
                                except appManager.AppNotFound:
                                    self.speak("App not found")
                                    pass
                                except appManager.AppNotOpen:
                                    self.speak("Unable to open application")
                                    pass
                                except appManager.ApllicationAlreadyClosed:
                                    self.speak("Application is already closed or not running")
                                    pass
            self.OlOf()
            self.listenButton.config(state=NORMAL)
            # Thread(target = self.OlOf()).start()

    def ManageHandsFreeMode(self):
        if self.handfreeModevar.get() == 1:
            self.HFML = Label(self.statusbar_frame, text="HandsfreeMode (activated)", anchor="e", borderwidth=0, bg="white", font="Lucida 10 bold")
            self.HFML.pack(side=RIGHT)
            question = askyesno("HandsFreeMode","Do you want to remove listen button ?")
            if question:
                self.listenButton.pack_forget()
            
            hotwordDetection.Detect(self.takeCommand)
        else:
            print(4)
            self.HFML.config(text="HandsfreeMode (deactivated)")
            self.HFML.after(3*1000,lambda:self.HFML.pack_forget())
            self.listenButton.pack()

    def clock(self):
        self.timeLabel.config(text=datetime.datetime.now().strftime("%c"))
        self.timeLabel.update()
        self.timeLabel.after(1000, self.clock)

    def logout(self):
        with open('login.txt', 'w') as lgfile:
            lgfile.write("0")
        self.root.destroy()
        os.startfile(__file__)
    
    def opensetting(self):
        s = settings.Settings(self.root)
        s.mainloop()


    def menu(self, e=None):
        myFont = "helvetica 12"
        position = pyautogui.position()
        menuWindow = Toplevel()
        menuWindow.geometry(f"+{position.x}+{position.y}")
        menuWindow.overrideredirect(True)
        menuWindow.config(bg="white",cursor="hand2",borderwidth=2, relief=RIDGE)
        logout_Button = Button(menuWindow, text="Login out", bg="white", borderwidth=0, font=myFont, command=self.logout)
        hf_mode_Button = Checkbutton(menuWindow, text="Handsfree mode", font=myFont, borderwidth=0, bg="white", onvalue=1, offvalue=0, variable=self.handfreeModevar, command= lambda : self.ManageHandsFreeMode())
        settings_Button = Button(menuWindow, text="⚙️ Setting", bg="white", borderwidth=0, font=myFont,command=self.opensetting)
        logout_Button.pack(anchor="w")
        hf_mode_Button.pack(anchor="w")
        settings_Button.pack(anchor="w")
        self.root.bind("<Button-1>",lambda e:menuWindow.destroy())

    def send_through_Ibox(self, e=None):
        self.queryvar.set(self.Iboxvar.get())
        self.listenButton.config(image=self.micImage, command=lambda: Thread(target=self.makeTrue).start())
        self.outputBox.config(state="normal")
        self.outputBox.insert('end', f"{self.Iboxvar.get()}\n", 'right')
        self.outputBox.config(state="disabled")
        self.Iboxvar.set("")
        self.exmain()

    def swap_button(self, e=None):
        snd_button_image = Image.open("static\Icons\Send.png")
        snd_button_image = snd_button_image.resize((30,30),Image.ANTIALIAS)
        sndImage = ImageTk.PhotoImage(snd_button_image)
        self.listenButton.config(image=sndImage, command=lambda : Thread(target=self.send_through_Ibox).start())
        self.listenButton.sndImage = sndImage

if __name__ == '__main__':
    main()
