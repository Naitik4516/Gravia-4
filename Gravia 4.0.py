from tkinter.messagebox import *
import socket
print("initializing...")
host = socket.gethostname()
hostName = socket.gethostbyname(host)
if hostName == "127.0.0.1":
    showwarning("No Internet", "Looks like you have no internet connection please kindly try to connect internet, otherwise some features may not work ")

try:
    from tkinter import *
    import datetime
    import os
    import random
    import smtplib
    import subprocess
    import json
    import requests
    import webbrowser
    import pyjokes
    import pyttsx3
    import speech_recognition as sr
    import wikipedia
    import wolframalpha
    import psutil
    import pyautogui
    import speedtest
    import pywhatkit
    import ctypes
    from plyer import notification
    from playsound import playsound
    from threading import Thread
except Exception as error:
    showerror("Error",error)
    print(error)
    pass


class gravia:
    def __init__(self, parent) -> None:

        self.root = parent
        clear = lambda: os.system('cls')
        clear()
        self.welcome_notification()
        self.wishMe()

        self.statusbar_frame = Frame(
            self.root, borderwidth=1, relief=RIDGE, bg="white")
        self.statusbar_frame.pack(side=BOTTOM, fill=X)
        self.statusvar = StringVar()
        self.sbar = Label(self.statusbar_frame,
                          textvariable=self.statusvar, anchor="w", borderwidth=0)
        self.sbar.pack(side=LEFT)

        self.outputBox = Text(self.root,bg="#2d2587",fg="white")
        self.outputBox.pack(fill=BOTH, expand=True)
       
        if hostName == "127.0.0.1":
            showwarning(
                "No Internet", "Looks like you have no internet connection please kindly try to connect internet, otherwise some features may not work")
            self.statusvar.set("Offline")
        else:
            self.statusvar.set("Online")

        bFrame = Frame(self.root, borderwidth=2, relief=RAISED)
        bFrame.pack(side=BOTTOM, fill=X)

        self.listen = BooleanVar(False)

        self.listenButton = Button(bFrame, text="Listen", font="lucida 15 bold",
                                   state="normal", command=lambda: Thread(target=self.makeTrue).start())
        self.listenButton.pack(pady=10)

        self.engine = pyttsx3.init('sapi5')
        # getting details of current voice
        voices = self.engine.getProperty('voices')
        # print(voices)
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 150)
    
    def speak(self, audio):
        def m():
            try:
                self.outputBox.insert(END, f"\n{audio}")
            except Exception:
                self.outputBox.insert(END, f"\n{audio}")
            self.engine.say(audio);
            self.engine.runAndWait();
        m()

    
    def makeTrue(self):
        self.listen.set(True)
        self.exmain()

    def welcome_notification(self):
        notification.notify(
            title="Gravia",
            message="Welcome to Gravia",
            app_icon=r"static\\Icons\Gravia icon.ico",
            timeout=1,
        )


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
            self.speak("Good Morning!")
            notification.notify(
                title="Good Morning",
                message=gdm,
                app_icon="static\\Icons\\wish-list.ico",
                timeout=10,
            )

        elif hour >= 12 and hour < 17:
            self.speak("Good Afternoon ")
            notification.notify(
                title="Good Afternoon",
                message=gdg,
                app_icon="static\\Icons\\wish-list.ico",
                timeout=10,
            )

        else:
            # self.speak("Good Evening ")
            notification.notify(
                title="Good Evening",
                message=gde,
                app_icon="static\\Icons\\wish-list.ico",
                timeout=10,
            )

        # self.speak("I am Gravia 1 point two")
        # self.speak("How may I help you ")

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.statusvar.set("Listening...")
            r.pause_threshold = 0.8
            # For removing background noise
            r.adjust_for_ambient_noise(source, duration=0.8)
            audio = r.listen(source)

        try:
            self.statusvar.set("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            self.outputBox.insert(END, f"\nUser said: {query}")

        except Exception as e:
            self.speak("Say that again please")
            self.listenButton.config(state="normal")
            return None
        return query

    def sendEmail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Enter your email.com', 'Krishna 2021')
        server.sendmail('Enter your email.com', to, content)
        server.close()

    def exmain(self):
        self.listenButton.config(state="disabled")
        query = self.takeCommand().lower()  # Converting user query into lower case
        while self.listen.get():
            # Logic for executing tasks based on query
            if 'according wikipedia' in query:  # if wikipedia found in the query then this block will be executed
                self.statusvar.set("Searching...")
                self.speak('Searching Wikipedia...')
                query = query.replace("according to wikipedia", "")
                # We can change sentances that read our A.I.
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia")
                self.statusvar.set("Speaking...")
                self.speak(results)
                print(results)

            elif 'play' in query:
                self.statusvar.set("Playing...")
                song = query.replace('play', '')
                self.speak('playing ' + song)
                pywhatkit.playonyt(song)
                self.statusvar.set("Online...")

            elif 'youtube' in query:
                if query == "youtube" or query == "open youtube":
                    self.statusvar.set("Opening...")
                    webbrowser.open("https://www.youtube.com/")
                    self.speak("Opening youtube")
                    self.statusvar.set("Searching...")
                else:
                    self.statusvar.set("Searching...")
                    v = query.replace('', 'search')
                    v = query.replace('', 'on')
                    v = query.replace('', 'youtube')
                    v = query.replace('', 'open')
                    v = query.replace('', 'in')
                    v = query.replace('', 'gravia')
                    pywhatkit.playonyt(v)
                    self.speak('getting that from youtube')
                    self.statusvar.set("Online...")

            elif 'open instagram' in query:
                self.statusvar.set("Opening...")
                webbrowser.open("https://www.instagram.com/")
                self.speak(
                    "here you go to instagram. opening please wait for a momment\n")
                print("Opening.....")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com/")
                print("Opening.....")
                self.speak(
                    "opening www.google.com . Search any thing that you want. Indian also called it. Google baabaa\n")

            elif 'open translater' in query:
                webbrowser.open("https://translate.google.com")
                self.speak(
                    "google translate is opening her now. opening... please wait for a moment\n")
                print("Opening")

            elif 'open spotify' in query:
                webbrowser.open("https://www.stackoverflow.com")
                self.speak("here you go to spotify. Listen music, be happy")
                print("Opening.....")

            elif 'open gmail' in query:
                webbrowser.open("https://mail.google.com")
                self.speak(
                    "here you go to gmail. Lets checkout some new mails\n")
                print("Opening.....")

            elif 'open hotstar' in query:
                webbrowser.open("https://www.hotstar.com")
                self.speak(
                    "Openinng hotstar. Lets Watch tv shows, movies, cartoons and more\n")
                print("Opening.....")

            elif 'open amazon' in query:
                webbrowser.open("https://www.amazon.in")
                self.speak(
                    "here you go to amazon. Lets watch or purchase some awsome things\n")
                print("Opening.....")

            elif 'open facebook' in query:
                webbrowser.open("https://www.facebook.com")
                print("Opening.....")
                self.speak("Opening facebook.")

            elif 'open w3 schools' in query:
                webbrowser.open("https://www.w3schools.com")
                self.speak(
                    "here is W3schools.com . Learn code and become a master")
                print("Opening...")

            elif 'code with harry' in query:
                webbrowser.open(
                    "https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
                self.speak(
                    "Here is code with harry youtube channel. Beast chanel for learn code for free in hindi")
                print("Opening...")

            elif 'techno gamerz' in query or 'techno gamers' in query:
                webbrowser.open(
                    "https://www.youtube.com/channel/UCX8pnu3DYUnx8qy8V_c6oHg")
                self.speak(
                    " here is techno gamerz youtube channel is opening. You know it is my favorite yotube channel")
                print("Opening...")

            elif 'beast boy shub' in query or 'beast boy shubh' in query:
                webbrowser.open(
                    "https://www.youtube.com/channel/UCI86prlqXhbkREDMTaORvLQ")
                self.speak(
                    " here is beast boy shub youtube channel is opening. I hate this channel")
                print("Opening...")

            elif 'technology gyan' in query:
                webbrowser.open(
                    "https://www.youtube.com/channel/UC1tVU8H153ZFO9eRsxdJlhA")
                self.speak(
                    " technology gyan youtube channel is opening. Please wait for a momment")
                print("Opening...")

            elif 'make joke horror' in query:
                webbrowser.open(
                    "https://www.youtube.com/channel/UC2gdpnWv_ve_RCWtvftkJ7g")
                self.speak(
                    "make joke horror youtube channel is opening. Watch animated horror stories")
                print("Opening...")

            elif 'sound clip' in query:
                webbrowser.open("https://www.youtube.com/user/tseries")
                self.speak(
                    " T-series youtube channel is opening. best youtube channl for music")
                print("Opening...")

            elif 'sound of lion' in query:
                soundPath = "sound effects\\mixkit-wild-lion-animal-roar-6.wav"
                self.speak("Playing sound")
                os.startfile(soundPath)

            elif 'play movie' in query or 'play film' in query:
                self.speak("SOrry I have no movies")

            elif 'time' in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                self.speak('Current time is ' + time)
                print(time)

            elif 'date' in query:
                strDate = datetime.datetime.now().strftime("%d:%m:%y")
                self.speak(f"Today is {strDate}")
                print(f"Date is {strDate}")

            elif ' day' in query:
                strDate = datetime.datetime.now().strftime("%A")
                self.speak(f"Today is {strDate}")
                print(f"Date is {strDate}")

            elif "What year is it " in query or "what year is going now" in query or "what yer it is" in query:
                stryear = datetime.datetime.now().strftime("%Y")
                self.speak(f"{stryear} is going on")
                print(f"It is going on {stryear}")

            elif "bye" in query:
                self.speak("Bye. Check Out gravia for more exicting things")
                exit()

            elif 'email to Krishna' in query:
                try:
                    self.speak("What should I say?")
                    content = self.takeCommand()
                    to = "Enter your email.com"
                    self.sendEmail(to, content)
                    self.speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    self.speak("I am not able to send this email")

            elif 'how are you' in query:
                self.speak("I am fine, Thank you")
                self.speak("How are you, Sir")

            elif 'what is today' in query:
                tdy = datetime.datetime.now().strftime("%c")
                self.speak(tdy)
                print(tdy)

            elif 'fine' in query or "good" in query:
                self.speak("It's good to know that you are fine")

            elif "change my name to" in query:
                query = query.replace("change my name to", "")
                assname = query

            elif "change name" in query:
                self.speak("What would you like to call me, Sir ")
                assname = self.takeCommand()
                self.speak("Thanks for naming me")

            elif "what's your name" in query or "What is your name" in query:
                self.speak("My friends call me")
                self.speak(assname)
                print("My friends call me", assname)

            elif 'I am bored' in query or 'bore' in query:
                self.speak(
                    "So. What can I do I play music,play movies or Youtube. I also tell you joke.")
                self.takeCommand()

            elif 'baba ke kharate' in query or 'baba ki kharate' in query or 'Baba ke kharate' in query or 'Baba ki kharate' in query:
                playsound(
                    "G:\\Python Projects\\Gravia\\sound effects\\grandpa.wav")
                self.speak("Ye hain Baba ke kharraaatA")

            elif 'amma ke kharate' in query or 'amma ki kharate' in query or 'Amma ke kharate' in query or 'Amma ki kharate' in query:
                os.startfile(
                    "G:\\Python Projects\\Gravia\\sound effects\\grandma.wav")
                self.speak("Ye hain amma ke kharraaatA")

            elif 'Snore of grandpa' in query or 'Snoring of grandpa' in query or 'Snore of grandfather' in query or 'Snoring of grandfather' in query:
                os.startfile(
                    "G:\\Python Projects\\Gravia\\sound effects\\grandpa.wav")
                self.speak("This is grandpa or grandfather's snoring")

            elif 'snore of grandma' in query or 'snoring of grandma' in query or 'Snore of grandmother' in query or 'Snoring of grandmother' in query:
                os.startfile(
                    "G:\\Python Projects\\Gravia\\sound effects\\grandma.wav")
                self.speak("This is grandma or grandmother's snoring")

            elif 'exit' in query:
                self.speak("Thanks for giving me your time")
                exit()

            elif "who made you" in query or "who created you" in query:
                self.speak("I have been created by Krishna.")

            elif 'joke' in query:
                os.startfile(
                    r"G:\Programming\Python Projects\Gravia\sound effects\mixkit-light-applause-with-laughter-audience-512.wav")
                self.speak(pyjokes.get_joke())

            elif "calculate" in query:

                app_id = "RJAY23-HLLLTY5H64"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                self.speak("The answer is " + answer)

            elif 'search' in query:
                query = query.replace("search", "")
                webbrowser.open(query)

            elif "who i am" in query:
                self.speak("If you talk then definately you are human.")
                os.startfile(
                    r"G:\Programming\Python Projects\Gravia\sound effects\mixkit-cartoon-voice-laugh-343.wav")

            elif "why you came to world" in query:
                self.speak("Thanks to Krishna. further It's a secret")
                os.startfile(
                    r"G:\Programming\Python Projects\Gravia\sound effects\mixkit-conference-audience-clapping-strongly-476.wav")

            elif "what are you doing" in query:
                self.speak("Nothing, just talking to you")
                self.speak("And what are you doing")

            elif 'is love' in query:
                self.speak("It is 7th sense that destroy all other senses")

            elif "yo " in query:
                self.speak("Yo, what's up")

            elif "i love you" in query:
                self.speak("I live you too")

            elif "who are you" in query:
                self.speak("I am your virtual assistant created by Krishna")

            elif 'reason for you' in query:
                self.speak(
                    "I was created as a Minor project by Mister Krishna ")

            elif 'change background' in query:
                try:
                    ctypes.windll.user32.SystemParametersInfoW(20,
                                                               0,
                                                               "C:\\Windows\\WinSxS\\amd64_microsoft-windows-shell-wallpaper-theme1_31bf3856ad364e35_10.0.18362.1_none_a937730822266138",
                                                               0)
                    self.speak("Background changed succesfully")

                except Exception as e:
                    print(str(e))

            elif 'news' in query:
                try:
                    from urllib.request import urlopen
                    jsonObj = urlopen(
                        '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=ce40662fcb6f4596870bac50bfb6b422''')
                    data = json.load(jsonObj)
                    i = 1

                    self.speak(
                        'here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + '\n')

                    for item in data['articles']:

                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        self.speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:
                    print(str(e))

            elif 'lock window' in query:
                self.speak("locking the device")
                os.system("shutdown -1")

            elif 'shutdown ' in query:
                self.speak("!System shudowning please wait")
                print(
                    "If you want to shutown press 'y'. \nElse you Want to shutdown gravia press 'n'")
                self.speak(
                    "If you want to shutown press y else you Want to shutdown gravia press n")
                choice = input("Please confirm to shutdown the pc (y or n)")
                if choice == 'n':
                    exit()
                else:
                    os.system("shutdown /s /t 1")

            elif 'empty recycle bin' in query:
                try:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    self.speak("Recycle Bin Recycled")
                except Exception:
                    self.speak("Unaible to empty recycle bin")
                    print(Exception)
                finally:
                    continue

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                self.speak("Locating" + location)
                webbrowser.open(
                    "https://www.google.nl/maps/place/"+location+"")

            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                self.speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in query or "sign out" in query:
                self.speak(
                    "Make sure all the application are closed before sign-out")
                subprocess.call(["shutdown", "/l"])

            elif "update" in query or "updates" in query:
                try:
                    f = open("gravia 1.1")
                    # Do something with the file
                except FileNotFoundError:
                    print("There are no updates available right now")
                    self.speak("There are no updates available right now")
                finally:
                    f.close()

            elif "hindi version" in query or '2.0' in query:
                self.speak(
                    "Sorry, This version is not yet available, but work is in progress. But you can try its developer version")
                print("It has been done but is not working properly")

            elif 'What are your functions' in query or 'What is your functions' in query:
                self.speak(
                    "I will do many thing like. I play music. I open any app or website, play movies, pay games, shutdown  pc an much more for more information show my demo ")

            elif 'what is your birthday' in query or 'what is your date of bith' in query or 'When does your birthday come' in query or 'What is your birthday date' in query or 'your birthday' in query or 'When were you' in query or 'when you were born' in query:
                self.speak("I was born on 10 february 2021, timing 13:56:32")
                print("I was born on 10 february 2021, timing 13:56:32")

            elif "weather" in query:
                api_key = "675001e5325417f1e97ace33821a9f77"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                self.speak(" City name ")
                print("City name : ")
                city_name = self.takeCommand()

                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()

                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]

                    # print following values
                    print(" Temperature (in kelvin unit) = " +
                          str(current_temperature) +
                          "\n atmospheric pressure (in hPa unit) = " +
                          str(current_pressure) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

                    self.speak("Temperature is " + str(current_temperature) + " and atmospheric pressure is " + str(
                        current_pressure) + "and humidity is" + str(current_humidiy) + "and today is " + str(weather_description))

                else:
                    print(" City Not Found ")

            elif "open wikipedia" in query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in query:
                self.speak("A warm" + query)
                self.speak("How are you Mister")
                self.speak(assname)

            elif 'security mode' in query or 'on security' in query:
                self.speak(
                    "Security mode is on. Initially the alarm will ring for confirmation, press q for exit or say stop security mode or off security mode")
                try:
                    os.startfile(
                        "G:\\Python Projects\\security camera\\main.py")

                except Exception as e:
                    print("Anaible to run security mode please try again later")
                    self.speak(
                        "Anaible to run security mode please try again later")

            elif 'off security mode' in query or "stop security" in query:
                pyautogui.press("q")

            elif 'where i am' in query or 'where we are' in query or 'find my location' in query or 'trace my location' in query:
                self.speak("Wait i check now")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.giojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    self.speak(f"Right now we are in {city},{state},{country}")
                    print(f"Right now we are in {city},{state},{country}")
                except Exception as e:
                    self.speak(
                        "Sorry, I can't figure out where we are, probably because of a network issue")
                    continue

            # most asked question from google Assistant
            elif "will you be my gf" in query or "will you be my bf" in query:
                self.speak(
                    "I'm not sure about, may be you should give me some time")

            elif "how are you" in query:
                self.speak("I'm fine, glad you me that")

            elif 'close yourself' in query:
                self.speak("I am closing you self. Bye")
                exit()

            elif "i love you" in query:
                self.speak("It's hard to understand")

            elif "how much power left" in query or "how much power we have" in query or "battery" in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                self.speak(f"Sir, our system have {percentage} of battry")
                if percentage >= 75 and percentage <= 99:
                    self.speak("We have enough power to continue the work")

                elif percentage == 100:
                    self.speak("We have full power")

                elif percentage >= 45 and percentage <= 70:
                    self.speak(
                        "We should connect system to charging point to charge the system battery")

                elif percentage >= 15 and percentage < 35:
                    self.speak(
                        "We don't have enough,so now we need to charge our battery")

                elif percentage <= 15:
                    self.speak(
                        "Alert! We have very low power connect the pc to the charger otherwise pc is going to shutdown")

            elif 'search for' in query:
                self.speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia")
                print(results)
                self.speak(results)

            elif 'volume up' in query:
                pyautogui.press("volumeup")

            elif 'volume down' in query:
                pyautogui.press("volumedown")

            elif 'mute' in query:
                pyautogui.press("volumemute")

            elif 'show options' in query or 'right click options' in query:
                self.speak("showing...")
                pyautogui.press("apps")

            elif "internet speed" in query:
                st = speedtest.Speedtest()
                up = st.upload
                dw = st.download
                self.speak(
                    f"The internet donloading speed is {dw} bits and the uploding speed is {up} bits")

            elif "Internet speed in mbps" in query:
                pass

            elif 'wi-fi' in query:
                self.speak("")
                pyautogui.click(x=1196, y=745)

            elif 'messages' in query or 'show menu bar' in query:
                self.speak("")
                pyautogui.click(x=1334, y=741)

            elif 'write' in query or 'voice typing' in query:
                self.speak("What should i write in it ?")
                wrote = self.takeCommand()
                pyautogui.write(wrote, interval=0.12)

            elif 'type' in query:
                sb = query.replace('type', '')
                pyautogui.write(sb, interval=0.05)

            elif 'open start' in query:
                self.speak("")
                pyautogui.press("win")

            elif 'press enter' in query:
                self.speak("")
                pyautogui.press("enter")

            elif 'browse back' in query or 'brouse back' in query:
                self.speak("")
                pyautogui.press("browseback")

            elif 'browser forward' in query or 'brouse forward':
                self.speak("")
                pyautogui.press("browserforward")

            elif 'refresh' in query:
                self.speak("")
                pyautogui.press("browserrefresh")

            elif 'home' in query:
                self.speak("")
                pyautogui.press("browserhome")

            elif 'bookmarks' in query or 'bookmark' in query:
                self.speak("")
                pyautogui.press("browserfavorites")

            elif 'spacebar' in query:
                self.speak("")
                pyautogui.press("space")

            elif 'next page' in query or "page down" in query:
                self.speak("")
                pyautogui.press("pagedown")

            elif 'previous page' in query or "page up" in query:
                self.speak("")
                pyautogui.press("pageup")

            elif 'open search' in query:
                self.speak("")
                pyautogui.hotkey("ctrl", "f")

            elif 'rotate screen to left side' in query:
                self.speak("")
                pyautogui.hotkey("ctrl", "alt", "left")

            elif 'rotate screen to right side' in query:
                self.speak("Done")
                pyautogui.hotkey("ctrl", "alt", "right")

            elif 'rotate screen to down side' in query or 'rotate screen to bottom' in query:
                self.speak("Done")
                pyautogui.hotkey("ctrl", "alt", "down")

            elif 'rotate screen to top side' in query or 'rotate screen to up side' in query or 'rotate screen to normal' in query:
                self.speak("Done")
                pyautogui.hotkey("ctrl", "alt", "up")

            elif 'open task view' in query or 'start task view' in query or 'show task view' in query:
                self.speak("Done")
                pyautogui.click(x=462, y=741)

            elif "what is" in query or "who is" in query:
                client = wolframalpha.Client("RJAY23-HLLLTY5H64")
                res = client.query(query)

                try:
                    print(next(res.results).text)
                    self.speak(next(res.results).text)
                except StopIteration:
                    print("No results")

            if 'open pycharm' in query:
                try:
                    self.statusvar.set("Opening...")
                    pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
                    os.startfile(pycharmPath)
                    self.speak(
                        ";Pycharm Community Edition is opening here now. Please wait for a momment")
                except Exception as e:
                    self.speak(
                        "Anaible to open pycharm, Maybe it is already open or not installed")

            elif 'open antivirus' in query:
                self.statusvar.set("Opening...")
                antivirusPath = r"C:\Program Files\SecuraShield AVCP\ssavgui.exe"
                os.startfile(antivirusPath)
                self.speak(
                    " Antivirus is opening here now.  Please wait for a momment")

            elif 'open powershell' in query:
                self.statusvar.set("Opening...")
                subprocess.run("powershell.exe")
                self.speak(
                    "windows powershell is opening here now. Please wait for a momment")

            elif 'open cmd' in query or "command promt" in query:
                self.speak(
                    "command promt is opening here now. Please wait for a momment")
                subprocess.run("cmd.exe")

            elif 'open this pc' in query:
                self.statusvar.set("Opening...")
                os.startfile(
                    "C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")
                self.speak(
                    "This PC is opening here now. Please wait for a momment")

            elif 'open control panel' in query:
                self.statusvar.set("Opening...")
                os.startfile(
                    "C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")
                self.speak(
                    "control panel is opening here now. Please wait for a momment")

            elif 'open file explorer' in query:
                self.statusvar.set("Opening...")
                os.startfile(
                    "C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.lnk")
                self.speak(
                    "file explorer is opening here now. Please wait for a momment")

            elif 'open calculator' in query:
                self.statusvar.set("Opening...")
                subprocess.run("calc.exe")
                self.speak(
                    "calculator is opening here now. Please wait for a momment")

            elif 'open paint' in query:
                self.statusvar.set("Opening...")
                os.system(
                    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
                self.speak(
                    "calculator is opening here now. Please wait for a momment")

            elif 'open step recorder' in query:
                self.statusvar.set("Opening...")
                os.startfile(
                    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk")
                self.speak(
                    "Step recorder is opening here now. Please wait for a momment")

            elif 'open media player' in query:
                self.statusvar.set("Opening...")
                os.startfile(
                    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Windows Media Player.lnk")
                self.speak(
                    "calculator is opening here now. Please wait for a momment")

            elif 'open charactor map' in query:
                self.speak(
                    "charactor map is opening here now. Please wait for a momment")
                os.startfile(
                    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\System Tools\\Character Map.lnk")

            elif 'open calculator' in query:
                self.speak(
                    "calculator is opening here now. Please wait for a momment")
                os.startfile(
                    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")

            elif 'open table cheater' in query:
                self.statusvar.set("Opening...")
                os.startfile(
                    "C:\\Users\\Sandeep\\PycharmProjects\\firstProg\\table cheater.py")
                self.speak(
                    "table cheter program by Krishna  is opening here now. Please wait for a momment")

            elif 'open notepad' in query:
                self.statusvar.set("Opening...")
                subprocess.run("notepad.exe")
                self.speak(
                    "notepad is opening here now. Please wait for a momment")

            elif 'open downloads' in query or 'download' in query:
                self.statusvar.set("Opening...")
                os.startfile("Downloads")
                self.speak("Opening downloads folder")

            elif 'open firefox' in query:
                self.statusvar.set("Opening...")
                firefoxPath = "C:\\Program Files\\Mozilla Firefox"
                os.startfile(firefoxPath)
                self.speak("opening firefox now. Please wait for a momment")

            elif 'open code' in query or 'open vs code' in query or 'open visual studio code' in query:
                self.statusvar.set("Opening...")
                vscodePath = "C:\\Users\\Sandeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(vscodePath)
                self.speak("code is opening here now. Happy coding.")

            elif 'open Gravia code' in query:
                self.statusvar.set("Opening...")
                graviaPath = "G:\\Python Projects\\Gravia\\Gravia(Eng.)1.0.py"
                os.startfile(graviaPath)
                self.speak("I open my code")

            elif 'open Photo viwer' in query:
                self.statusvar.set("Opening...")
                photoviwerPath = "C:\\Program Files\\Windows Photo Viewer"
                self.speak(
                    " opening photo viwer now. Please wait for a momment")
                os.startfile(photoviwerPath)

            elif "start Need For Speed" in query or "play need for speed" in query:
                self.statusvar.set("Opening...")
                gamePath = "C:\\Program Files (x86)\\EA GAMES\\Need for Speed Most Wanted PC Demo\\speedDemo.exe"
                os.startfile(gamePath)
                self.speak(
                    ",Starting ready for racing zuummmmmm,zuummmmmm,zuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuum")

            elif 'open Word' in query or 'open word' in query:
                self.statusvar.set("Opening...")
                wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk"
                os.startfile(wordPath)
                self.speak(
                    ",Ms word 2010 is opening here now. Please wait for a momment")

            elif 'open PowerPoint' in query:
                self.statusvar.set("Opening...")
                PowerPointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010.lnk"
                os.startfile(PowerPointPath)
                self.speak(
                    "Ms power point 2010 is opening here now. Please wait for a momment")

            elif 'open exel' in query or 'open Exel' in query:
                self.statusvar.set("Opening...")
                exelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010.lnk"
                os.startfile(exelPath)
                self.speak(
                    "Ms exel is opening here now. Please wait for a momment")

            elif 'open chrome' in query:
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                self.speak(
                    "Chrome browser is opening here now. Please wait for a momment")
                os.startfile(chromePath)

            elif 'open edge' in query:
                self.statusvar.set("Opening...")
                edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(edgePath)
                self.speak(
                    "Microsoft Edge browser is opening here now. Please wait for a momment")

            elif 'play Movies' in query:
                self.statusvar.set("Opening...")
                try:
                    moviesPath = "G:\\Movies"
                    self.speak("Sure movie list is showing")
                    os.startfile(moviesPath[0])
                except Exception as e:
                    self.speak("Sorry I have no movies right now")
                    print(e)
                    continue

            elif 'open whatsapp' in query or 'open whattsapp' in query or 'open whatsup' in query:
                self.statusvar.set("Opening...")
                WhatsAppPath = "C:\\Users\\Sandeep\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(WhatsAppPath)
                self.speak(
                    "Whatsapp is opening here now. Please wait for a momment")

            elif 'hello' in query:
                self.speak("Hello, what's up dude")

            elif "show goa photos" in query:
                try:
                    self.statusvar.set("Opening...")
                    goa_photosPath = "G:\\Photos&vidios\\goa"
                    self.speak("showing....")
                    os.startfile(goa_photosPath)
                except Exception:
                    self.speak(
                        "A bad news, We found that all photos and vidios are corropted by noaa ransomeware.")
                    continue

            elif 'show photos' in query:
                try:
                    self.statusvar.set("Opening...")
                    photosPath = "G:\\Photos&vidios"
                    self.speak("I showing you.Please wait I open it.....")
                    os.startfile(photosPath)
                except Exception:
                    os.startfile("Pictures")
                    self.speak(
                        "A bad news, We found that all photos and vidios are corropted by noaa ransomeware. But I have some fhotos in your pictures media library")
                    continue

            elif 'python projects' in query:
                self.statusvar.set("Opening...")
                projectPath = "G:\\Programming\\Python Projects"
                self.speak("I showing you.Please wait I open it.....")
                os.startfile(projectPath)
            
            else:
                self.speak("Sorry I can't do that")
                with open('otherQuery.txt', "r") as o:
                    o.write(query)

            if 'close notepad' in query:
                try:
                    self.statusvar.set("Closing...")
                    self.speak(", I close it")
                    os.system("taskkill /f /im notepad.exe")
                except Exception:
                    self.speak("Notepad is not opened, it is already close")
                    continue

            elif 'close whatsapp' in query:
                try:
                    self.statusvar.set("Closing...")
                    self.speak(", I close it")
                    os.system("taskkill /f /im whatsapp.exe")
                except Exception:
                    self.speak("Whatsapp is not opened, it is already close")
                    continue

            elif 'close vs code' in query or 'close visual studio ' in query:
                try:
                    self.statusvar.set("Closing...")
                    os.system("taskkill /f /im code.exe")
                    self.speak("Fine I close it")
                except Exception:
                    self.speak(
                        "Visual studio code is not opened, it is already close")
                    continue

            elif 'close pycharm' in query:
                try:
                    self.statusvar.set("Closing...")
                    os.system("taskkill /f /im PyCharm.exe")
                    self.speak(", I close it")
                except Exception:
                    self.speak("Pycharm is not opened, it is already close")
                    continue

            elif 'close chrome' in query:
                try:
                    self.statusvar.set("Closing...")
                    self.speak(", I close it. Chrome browser is closing")
                    os.system("taskkill /f /im Chrome.exe")
                except Exception:
                    self.speak("Chrome is not opened, it is already close")
                    continue

            elif 'close edge' in query:
                try:
                    self.statusvar.set("Closing...")
                    self.speak(", I close it")
                    os.system("taskkill /f /im msedge.exe")
                except Exception:
                    self.speak("Notepad is not opened, it is already close")
                    continue

            elif 'close antivirus' in query:
                try:
                    self.statusvar.set("Closing...")
                    self.speak(", I close it")
                    os.system("taskkill /f /im sssavgui.exe")
                except Exception:
                    self.speak("Antivirus is not opened, it is already close")
                    continue

            elif 'I want to see a table' in query:
                self.statusvar.set("Printing...")
                self.speak("Which table you want to see or listen?")
                tlb = self.takeCommand()
                self.speak(f"here is the table of {tlb}")
                for table in range(1, 11):
                    print(tlb, "x", table, "=", tlb*table)

            elif 'table' in query:
                self.statusvar.set("Printing...")
                le = query.replace('table', '')
                self.speak(f"Table of {le} is showing...")
                for tables in range(1, 11):
                    print(le, "x", tables, "=", le*tables)

            else:
                self.speak("Sorry I can't do that")
                with open('otherQuery.txt', "r") as o:
                    o.write(query)

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

            self.listen.set(False)
            self.listenButton.config(state="normal")
            if hostName != "127.0.0.1":
                self.statusvar.set("Online...")
            else:
                self.statusvar.set("Offline...")
                showwarning()


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    root.title('Gravia')

    gravia(root)

    root.mainloop()
