import datetime 
import os  
import random
import smtplib  
import subprocess  
import time
import json
import requests
import webbrowser  
import pyjokes
import pyttsx3 
import speech_recognition as sr
import wikipedia 
import wolframalpha
import psutil
import speedtest
import pywhatkit
import pyautogui
import ctypes
from plyer import notification

def welcome_notification():
    notification.notify(
        title = "Gravia",
        message = "Welcome to Gravia",
        app_icon = r"Icons\Gravia icon.ico",
        timeout = 1,
    )

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
# print(voices)
engine.setProperty('voice', voices[1].id)   
engine.setProperty('rate', 130)   

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.
 
def wishMe():
        hour=int(datetime.datetime.now().hour)
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

        if hour>=0 and hour<12:
            speak("Good Morning!")
            notification.notify(
                title = "Good Morning",
                message = gdm,
                app_icon = "Icons\\wish-list.ico",
                timeout = 10,
            )

        elif hour>=12 and hour<17:
            speak("Good Afternoon ")
            notification.notify(
                title = "Good Afternoon",
                message = gdg,
                app_icon = "Icons\\wish-list.ico",
                timeout = 10,
            )

        else:
            speak("Good Evening ")
            notification.notify(
                title = "Good Evening",
                message = gde,
                app_icon = "Icons\\wish-list.ico",
                timeout = 10,
            )

        speak("I am Gravia 1 point two")
        speak("How may I help you ")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def sendEmail(to, Krishna):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Enter your email.com', 'Krishna 2021')
    server.sendmail('Enter your email.com', to, content)
    server.close()

if __name__ == "__main__":
    try:
        clear = lambda: os.system('cls')
        clear()
        welcome_notification()
        wishMe()  

        while True:
                query = takeCommand().lower() #Converting user query into lower case

                # Logic for executing tasks based on query
                if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2) #We can change sentances that read our A.I.
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)   

                elif 'play' in query:
                    song = query.replace('play', '')
                    speak('playing ' + song)
                    pywhatkit.playonyt(song)      

                elif 'youtube' in query:
                    if query=="youtube" or query=="open youtube":
                        webbrowser.open("https://www.youtube.com/")
                        speak("Opening youtube")
                    else:
                        v = query.replace('','search')
                        v = query.replace('','on')
                        v = query.replace('','youtube')
                        v = query.replace('','open')
                        v = query.replace('','in')
                        v = query.replace('','gravia')
                        pywhatkit.playonyt(v)     
                        speak('getting that from youtube')

                elif 'open instagram' in query:
                    webbrowser.open("https://www.instagram.com/")
                    speak("here you go to instagram. opening please wait for a momment\n")
                    print("Opening.....")

                elif 'open google' in query:
                    webbrowser.open("https://www.google.com/")
                    print("Opening.....")
                    speak("opening www.google.com . Search any thing that you want. Indian also called it. Google baabaa\n")

                elif 'open translater' in query:
                    webbrowser.open("https://translate.google.com")
                    speak("google translate is opening her now. opening... please wait for a moment\n")
                    print("Opening")

                elif 'open spotify' in query:
                    webbrowser.open("https://www.stackoverflow.com")
                    speak("Ok. here you go to spotify. Listen music, be happy")
                    print("Opening.....")

                elif 'open gmail' in query:
                    webbrowser.open("https://mail.google.com")
                    speak("Ok. here you go to gmail. Lets checkout some new mails\n")
                    print("Opening.....")

                elif 'open hotstar' in query:
                    webbrowser.open("https://www.hotstar.com")
                    speak("Openinng hotstar. Lets Watch tv shows, movies, cartoons and more\n")
                    print("Opening.....")

                elif 'open amazon' in query:
                    webbrowser.open("https://www.amazon.in")
                    speak("here you go to amazon. Lets watch or purchase some awsome things\n")
                    print("Opening.....")

                elif 'open facebook' in query:
                    webbrowser.open("https://www.facebook.com")
                    print("Opening.....")
                    speak ("Opening facebook. \n")

                elif 'open w3 schools' in query:
                    webbrowser.open("https://www.w3schools.com")
                    speak("here is W3schools.com . Learn code and become a master")
                    print("Opening...")

                elif 'code with harry' in query:
                    webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
                    speak("Here is code with harry youtube channel. Beast chanel for learn code for free in hindi")
                    print("Opening...")

                elif 'techno gamerz' in query or 'techno gamers' in query:
                    webbrowser.open("https://www.youtube.com/channel/UCX8pnu3DYUnx8qy8V_c6oHg")
                    speak(" here is techno gamerz youtube channel is opening. You know it is my favorite yotube channel")
                    print("Opening...")

                elif 'beast boy shub' in query or 'beast boy shubh' in query:
                    webbrowser.open("https://www.youtube.com/channel/UCI86prlqXhbkREDMTaORvLQ")
                    speak(" here is beast boy shub youtube channel is opening. I hate this channel")
                    print("Opening...")

                elif 'technology gyan' in query:
                    webbrowser.open("https://www.youtube.com/channel/UC1tVU8H153ZFO9eRsxdJlhA")        
                    speak(" technology gyan youtube channel is opening. Please wait for a momment")
                    print("Opening...")

                elif 'make joke horror' in query:
                    webbrowser.open("https://www.youtube.com/channel/UC2gdpnWv_ve_RCWtvftkJ7g")     
                    speak("make joke horror youtube channel is opening. Watch animated horror stories")
                    print("Opening...")

                elif 'sound clip' in query:
                    webbrowser.open("https://www.youtube.com/user/tseries") 
                    speak(" T-series youtube channel is opening. best youtube channl for music")
                    print("Opening...")
                
                elif 'sound of lion'in query:
                    soundPath = "sound effects\\mixkit-wild-lion-animal-roar-6.wav"
                    speak("Playing sound")
                    os.startfile(soundPath)
            
                elif 'play movie' in query or 'play film' in query:
                    speak("SOrry I have no movies")

                elif 'time' in query: 
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    speak('Current time is ' + time)
                    print(time)

                elif 'date' in query: 
                    strDate = datetime.datetime.now().strftime("%d:%m:%y")
                    speak(f"Today is {strDate}")
                    print(f"Date is {strDate}")                  

                elif ' day' in query:
                    strDate = datetime.datetime.now().strftime("%A")
                    speak(f"Today is {strDate}")
                    print(f"Date is {strDate}") 

                elif "What year is it " in query or "what year is going now" in query or "what yer it is" in query:
                    stryear = datetime.datetime.now().strftime("%Y")
                    speak(f"{stryear} is going on")
                    print(f"It is going on {stryear}") 
                
                elif "bye" in query: 
                    speak("Bye. Check Out gravia for more exicting things") 
                    exit() 

                elif 'email to Krishna' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "Enter your email.com"   
                        sendEmail(to, content)
                        speak("Email has been sent !")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this email")
        
                elif 'how are you' in query:
                    speak("I am fine, Thank you")
                    speak("How are you, Sir")
        
                elif 'what is today' in query:
                    tdy = datetime.datetime.now().strftime("%c")
                    speak(tdy)
                    print(tdy)

                elif 'fine' in query or "good" in query:
                    speak("It's good to know that you are fine")
        
                elif "change my name to" in query:
                    query = query.replace("change my name to", "")
                    assname = query
        
                elif "change name" in query:
                    speak("What would you like to call me, Sir ")
                    assname = takeCommand()
                    speak("Thanks for naming me")
        
                elif "what's your name" in query or "What is your name" in query:
                    speak("My friends call me")
                    speak(assname)
                    print("My friends call me", assname)

                elif 'I am bored' in query or 'bore' in query:
                    speak("So. What can I do I play music,play movies or Youtube. I also tell you joke.")
                    takeCommand()

                elif 'baba ke kharate' in query or 'baba ki kharate' in query or 'Baba ke kharate' in query or 'Baba ki kharate' in query:
                    os.startfile("G:\\Python Projects\\Gravia\\sound effects\\grandpa.wav")
                    speak("Ye hain Baba ke kharraaatA")
                    time.sleep(3)

                elif 'amma ke kharate' in query or 'amma ki kharate' in query or 'Amma ke kharate' in query or 'Amma ki kharate' in query:
                    os.startfile("G:\\Python Projects\\Gravia\\sound effects\\grandma.wav")
                    speak("Ye hain amma ke kharraaatA")

                elif 'Snore of grandpa' in query or 'Snoring of grandpa' in query or 'Snore of grandfather' in query or 'Snoring of grandfather' in query:
                    os.startfile("G:\\Python Projects\\Gravia\\sound effects\\grandpa.wav")
                    speak("This is grandpa or grandfather's snoring")

                elif 'snore of grandma' in query or 'snoring of grandma' in query or 'Snore of grandmother' in query or 'Snoring of grandmother' in query:
                    os.startfile("G:\\Python Projects\\Gravia\\sound effects\\grandma.wav")
                    speak("This is grandma or grandmother's snoring")

                elif 'exit' in query:
                    speak("Thanks for giving me your time")
                    exit()
        
                elif "who made you" in query or "who created you" in query: 
                    speak("I have been created by Krishna.")
                    
                elif 'joke' in query:
                    os.startfile(r"G:\Programming\Python Projects\Gravia\sound effects\mixkit-light-applause-with-laughter-audience-512.wav")
                    speak(pyjokes.get_joke())
                
                elif "calculate" in query: 

                    app_id = "RJAY23-HLLLTY5H64"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('calculate') 
                    query = query.split()[indx + 1:] 
                    res = client.query(' '.join(query)) 
                    answer = next(res.results).text
                    print("The answer is " + answer) 
                    speak("The answer is " + answer) 
        
                elif 'search' in query:
                    query = query.replace("search", "")        
                    webbrowser.open(query) 
        
                elif "who i am" in query:
                    speak("If you talk then definately you are human.")
                    os.startfile(r"G:\Programming\Python Projects\Gravia\sound effects\mixkit-cartoon-voice-laugh-343.wav")
        
                elif "why you came to world" in query:
                    speak("Thanks to Krishna. further It's a secret")
                    os.startfile(r"G:\Programming\Python Projects\Gravia\sound effects\mixkit-conference-audience-clapping-strongly-476.wav")

                elif "what are you doing" in query:
                    speak("Nothing, just talking to you")
                    speak("And what are you doing")

                elif "I do" in query:
                    pass

                elif 'stop listening for 2 hours' in query:
                    speak("")
                    time.sleep(7200)

                elif 'stop listening for 1 hours' in query:
                    speak("")
                    time.sleep(2600)

                elif 'stop listening for 30 minutes' in query:
                    speak("")
                    time.sleep(1800)

                elif 'stop listening for 20 minutes' in query:
                    speak("")
                    th20 = 1800
                    time.sleep(th20)
                    print(th20)

                elif 'stop listening for 10 minutes' in query:
                    speak("")
                    min = 600
                    time.sleep(min)
                    print(min)

                elif 'stop listening for 5 minutes' in query:
                    speak("")
                    m = 300
                    time.sleep(m)
                    print(f"I am not listening your commands for{m} seconds")

                elif 'stop listening for 2 minutes' in query:
                    speak("")
                    time.sleep(120)

                elif 'stop listening for 1 minutes' in query:
                    speak("")
                    time.sleep(60)

                elif 'stop listening for 30 seconds' in query:
                    speak("")
                    time.sleep(30)

                elif 'stop listening for 10 seconds' in query:
                    speak("")
                    time.sleep(10)
        
                elif 'is love' in query:
                    speak("It is 7th sense that destroy all other senses")
        
                elif "who are you" in query:
                    speak("I am your virtual assistant created by Krishna")
        
                elif 'reason for you' in query:
                    speak("I was created as a Minor project by Mister Krishna ")
        
                elif 'change background' in query:
                    try:
                        ctypes.windll.user32.SystemParametersInfoW(20, 
                                                                0, 
                                                                "C:\\Windows\\WinSxS\\amd64_microsoft-windows-shell-wallpaper-theme1_31bf3856ad364e35_10.0.18362.1_none_a937730822266138",
                                                                0)
                        speak("Background changed succesfully")

                    except Exception as e:
                        print(str(e))
                    
                elif 'news' in query:
                    try:
                        from urllib.request import urlopen
                        jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=ce40662fcb6f4596870bac50bfb6b422''')
                        data = json.load(jsonObj)
                        i = 1
                        
                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============'''+ '\n')
                        
                        for item in data['articles']:
                            
                            print(str(i) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 1
                    except Exception as e:
                        print(str(e))
            
                elif 'lock window' in query:
                    speak("locking the device")
                    os.system("shutdown -1")

                elif 'shutdown ' in query:
                    speak("Okay!System shudowning please wait")
                    print("If you want to shutown press 'y'. \nElse you Want to shutdown gravia press 'n'")
                    speak("If you want to shutown press y else you Want to shutdown gravia press n")
                    choice = input("Please confirm to shutdown the pc (y or n)")
                    if choice == 'n':
                        exit()
                    else:
                        os.system("shutdown /s /t 1")

                elif 'empty recycle bin' in query:
                    try:
                        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                        speak("Recycle Bin Recycled")
                    except Exception:
                        speak("Unaible to empty recycle bin")
                        print(Exception)
                    finally:
                        continue
        
                elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        
                elif "restart" in query:
                    subprocess.call(["shutdown", "/r"])
                    
                elif "hibernate" in query or "sleep" in query:
                    speak("Hibernating")
                    subprocess.call("shutdown / h")
        
                elif "log off" in query or "sign out" in query:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    subprocess.call(["shutdown", "/l"])

                elif "update" in query or "updates" in query:
                    try:
                        f = open("gravia 1.1")
                        # Do something with the file
                    except FileNotFoundError:
                        print("There are no updates available right now")
                        speak("There are no updates available right now")
                    finally:
                        f.close()

                elif "hindi version" in query or '2.0' in query:
                    speak("Sorry, This version is not yet available, but work is in progress. But you can try its developer version")
                    print("It has been done but is not working properly")

                elif 'What are your functions' in query or 'What is your functions' in query:
                    speak("I will do many thing like. I play music. I open any app or website, play movies, pay games, shutdown  pc an much more for more information show my demo ")

                elif 'what is your birthday' in query or 'what is your date of bith' in query or 'When does your birthday come' in query or 'What is your birthday date' in query or 'your birthday' in query or 'When were you' in query or 'when you were born' in query:
                    speak("I was born on 10 february 2021, timing 13:56:32") 
                    print("I was born on 10 february 2021, timing 13:56:32") 

                elif "weather" in query:
                    api_key = "675001e5325417f1e97ace33821a9f77"
                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    speak(" City name ")
                    print("City name : ")
                    city_name = takeCommand()

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

                        speak("Temperature is " +  str(current_temperature) + " and atmospheric pressure is " + str(current_pressure) + "and humidity is" + str(current_humidiy) + "and today is " + str(weather_description))

                    else: 
                        print(" City Not Found ") 
        
                elif "open wikipedia" in query:
                    webbrowser.open("wikipedia.com")
        
                elif "Good Morning" in query:
                    speak("A warm" +query)
                    speak("How are you Mister")
                    speak(assname)

                elif 'security mode' in query or 'on security' in query:
                    speak("Security mode is on. Initially the alarm will ring for confirmation, press q for exit or say stop security mode or off security mode")
                    try:
                        os.startfile("G:\\Python Projects\\security camera\\main.py")

                    except Exception as e:
                        print("Anaible to run security mode please try again later")
                        speak("Anaible to run security mode please try again later")
                        time.sleep(5)

                elif 'off security mode' in query or "stop security" in query:
                    pyautogui.press("q")

                elif 'where i am' in query or 'where we are' in query or 'find my location' in query or 'trace my location' in query:
                    speak("Wait i check now")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        url = 'https://get.giojs.io/v1/ip/geo/'+ipAdd+'.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        state = geo_data['state']
                        country = geo_data['country']
                        speak(f"Right now we are in {city},{state},{country}")
                        print(f"Right now we are in {city},{state},{country}")
                    except Exception as e:
                        speak("Sorry, I can't figure out where we are, probably because of a network issue")
                        pass
                    
                # most asked question from google Assistant
                elif "will you be my gf" in query or "will you be my bf" in query:   
                    speak("I'm not sure about, may be you should give me some time")
        
                elif "how are you" in query:
                    speak("I'm fine, glad you me that")

                elif 'close yourself' in query:
                    speak("Okay I am closing you self. Bye")
                    exit()
        
                elif "i love you" in query:
                    speak("It's hard to understand")

                elif "how much power left" in query or "how much power we have" in query or "battery" in query:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"Sir, our system have {percentage} of battry")
                    if percentage>=75 and percentage<=99:
                        speak("We have enough power to continue the work")

                    elif percentage==100:
                        speak("We have full power")

                    elif percentage>=45 and percentage<=70:
                        speak("We should connect system to charging point to charge the system battery")

                    elif percentage>=15 and percentage<35:
                        speak("We don't have enough,so now we need to charge our battery")

                    elif percentage<=15:
                        speak("Alert! We have very low power connect the pc to the charger otherwise pc is going to shutdown")

                elif 'search for' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'volume up' in query:
                    pyautogui.press("volumeup")

                elif 'volume down' in query:
                    pyautogui.press("volumedown")       

                elif 'mute' in query:
                    pyautogui.press("volumemute")  

                elif 'show options' in query or 'right click options' in query:
                    speak("Okay showing...")
                    pyautogui.press("apps")    

                elif "internet speed" in query:
                    st = speedtest.Speedtest()
                    up = st.upload
                    dw = st.download
                    speak(f"The internet donloading speed is {dw} bits and the uploding speed is {up} bits")

                elif "Internet speed in mbps" in query:
                    pass

                elif 'wi-fi' in query:
                    speak("Okay")
                    pyautogui.click(x=1196,y=745)

                elif 'messages' in query or 'show menu bar' in query:
                    speak("Okay")
                    pyautogui.click(x=1334,y=741)

                elif 'write' in query or 'voice typing' in query:
                    speak("What should i write in it ?")
                    wrote = takeCommand()
                    pyautogui.write(wrote, interval=0.12)

                elif 'type' in query:
                    sb = query.replace('type', '')
                    pyautogui.write(sb, interval=0.05)

                elif 'open start' in query:
                    speak("Okay")
                    pyautogui.press("win") 
                    
                elif 'press enter' in query:
                    speak("Okay")
                    pyautogui.press("enter")

                elif 'browse back' in query or 'brouse back' in query:
                    speak("Okay")
                    pyautogui.press("browseback")

                elif 'browser forward' in query or 'brouse forward':
                    speak("Okay")
                    pyautogui.press("browserforward")

                elif 'refresh' in query:
                    speak("Okay")
                    pyautogui.press("browserrefresh")

                elif 'home' in query:
                    speak("Okay")
                    pyautogui.press("browserhome")

                elif 'bookmarks' in query or 'bookmark' in query:
                    speak("Okay")
                    pyautogui.press("browserfavorites")

                elif 'spacebar' in query:
                    speak("Okay")
                    pyautogui.press("space")

                elif 'next page' in query or "page down" in query:
                    speak("Okay")
                    pyautogui.press("pagedown")

                elif 'previous page' in query or "page up" in query:
                    speak("Okay")
                    pyautogui.press("pageup")

                elif 'open search' in query:
                    speak("Okay")
                    pyautogui.hotkey("ctrl","f")

                elif 'rotate screen to left side' in query:
                    speak("Okay")
                    pyautogui.hotkey("ctrl","alt","left") 

                elif 'rotate screen to right side' in query:
                    speak("Okay")
                    pyautogui.hotkey("ctrl","alt","right") 

                elif 'rotate screen to down side' in query or 'rotate screen to bottom' in query:
                    speak("Okay")
                    pyautogui.hotkey("ctrl","alt","down") 

                elif 'rotate screen to top side' in query or 'rotate screen to up side' in query or 'rotate screen to normal' in query:
                    speak("Okay")
                    pyautogui.hotkey("ctrl","alt","up") 

                elif 'open task view' in query or 'start task view' in query or 'show task view' in query:
                    speak("Okay")
                    pyautogui.click(x=462,y=741)

                elif "what is" in query or "who is" in query:
                    client = wolframalpha.Client("RJAY23-HLLLTY5H64")
                    res = client.query(query)
                    
                    try:
                        print (next(res.results).text)
                        speak (next(res.results).text)
                    except StopIteration:
                        print ("No results")
                    
                elif 'open pycharm' in query:
                    try:
                        pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
                        speak("Okay;Pycharm Community Edition is opening here now. Please wait for a momment")
                        os.startfile(pycharmPath)
                        time.sleep(4)   
                    except Exception as e:
                        speak("Anaible to open pycharm, Maybe it is already open or not installed")

                elif 'open antivirus' in query:
                    antivirusPath = r"C:\Program Files\SecuraShield AVCP\ssavgui.exe"
                    speak(" Antivirus is opening here now.  Please wait for a momment")
                    os.startfile(antivirusPath)
                    time.sleep(4)        

                elif 'open powershell' in query:
                    speak("Okay windows powershell is opening here now. Please wait for a momment")
                    subprocess.run("powershell.exe")
                    time.sleep(4)     

                elif 'open cmd' in query or "command promt" in query:
                    speak("Okay command promt is opening here now. Please wait for a momment")
                    subprocess.run("cmd.exe")
                    time.sleep(4)     

                elif 'open this pc' in query:
                    speak("Okay This PC is opening here now. Please wait for a momment")
                    os.startfile("C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")
                    time.sleep(4)        

                elif 'open control panel' in query:
                    speak("Okay control panel is opening here now. Please wait for a momment")
                    os.startfile("C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")
                    time.sleep(4)            

                elif 'open file explorer' in query:
                    speak("Okay file explorer is opening here now. Please wait for a momment")
                    os.startfile("C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.lnk")
                    time.sleep(4)        

                elif 'open calculator' in query:
                    speak("Okay calculator is opening here now. Please wait for a momment")
                    subprocess.run("calc.exe")
                    time.sleep(4)  

                elif 'open paint' in query:
                    speak("Okay calculator is opening here now. Please wait for a momment")
                    os.system("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
                    time.sleep(4)  

                elif 'open step recorder' in query:
                    speak("Okay Step recorder is opening here now. Please wait for a momment")
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk")
                    time.sleep(4)  

                elif 'open media player' in query:
                    speak("Okay calculator is opening here now. Please wait for a momment")
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Windows Media Player.lnk")
                    time.sleep(4)  

                elif 'open charactor map' in query:
                    speak("Okay charactor map is opening here now. Please wait for a momment")
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\System Tools\\Character Map.lnk")
                    time.sleep(4)  

                elif 'open calculator' in query:
                    speak("Okay calculator is opening here now. Please wait for a momment")
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")
                    time.sleep(4)    

                elif 'open table cheater' in query:
                    speak("Okay table cheter program by Krishna  is opening here now. Please wait for a momment")
                    os.startfile("C:\\Users\\Sandeep\\PycharmProjects\\firstProg\\table cheater.py")
                    time.sleep(4)            

                elif 'open notepad' in query:
                    speak("Okay notepad is opening here now. Please wait for a momment")
                    subprocess.run("notepad.exe")
                    time.sleep(4)       

                elif 'open downloads' in query or 'download' in query:
                    downloadsPath = "Downloads"
                    speak("Okay!")
                    os.startfile(downloadsPath)
                    time.sleep(4)        

                elif 'open firefox' in query:
                    firefoxPath = "C:\\Program Files\\Mozilla Firefox"
                    speak("okay opening firefox now. Please wait for a momment")
                    os.startfile(firefoxPath)

                elif 'open code' in query:
                    vscodePath = "C:\\Users\\Sandeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    speak("Okay code is opening here now. Happy coding.")
                    os.startfile(vscodePath)

                elif 'open Gravia code' in query:
                    graviaPath = "G:\\Python Projects\\Gravia\\Gravia(Eng.)1.0.py"
                    speak("Okay I open my coding")
                    os.startfile(graviaPath)
                    time.sleep(4)        

                elif 'open Photo viwer' in query:
                    photoviwerPath = "C:\\Program Files\\Windows Photo Viewer"
                    speak(" opening photo viwer now. Please wait for a momment")
                    os.startfile(photoviwerPath)
                    time.sleep(4)        

                elif "start Need For Speed" in query or "play need for speed" in query:
                    gamePath = "C:\\Program Files (x86)\\EA GAMES\\Need for Speed Most Wanted PC Demo\\speedDemo.exe"
                    speak("Okay,Starting ready for racing zuummmmmm,zuummmmmm,zuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuum")
                    os.startfile(gamePath)
                    time.sleep(4)        

                elif 'open Word' in query or 'open word' in query:
                    wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk"
                    speak("okay,Ms word 2010 is opening here now. Please wait for a momment")
                    os.startfile(wordPath)
                    time.sleep(4)        

                elif 'open PowerPoint' in query:
                    PowerPointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010.lnk"
                    speak("Ms power point 2010 is opening here now. Please wait for a momment")
                    os.startfile(PowerPointPath)
                    time.sleep(4)        

                elif 'open exel' in query or 'open Exel' in query:
                    exelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010.lnk"
                    speak("Ms exel is opening here now. Please wait for a momment")
                    os.startfile(exelPath)
                    time.sleep(4)        

                elif 'open Chrome'in query or 'open chrome' in query:
                    chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    speak("Chrome browser is opening here now. Please wait for a momment")
                    os.startfile(chromePath)
                    time.sleep(4)        

                elif 'open edge'in query or 'open Edge' in query:
                    edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    speak("Microsoft Edge browser is opening here now. Please wait for a momment")
                    os.startfile(edgePath)
                    time.sleep(4)     
        
                elif 'play Movies' in query:
                    moviesPath = "G:\\Movies"
                    speak("Ok movie list is showing")
                    os.startfile(moviesPath[0])
                    time.sleep(4)        

                elif 'open WhatsApp' in query or 'open whatsapp' in query:
                    WhatsAppPath = "C:\\Users\\Sandeep\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                    speak("Whatsapp is opening here now. Please wait for a momment")
                    os.startfile(WhatsAppPath)
                    time.sleep(10)

                elif 'hello' in query:
                    speak("Yes,Sir please speak and tell how may I help you.")

                elif "show goa photos" in query:
                    goa_photosPath = "G:\\Photos&vidios\\goa"
                    speak("Okay showing....")
                    os.startfile(goa_photosPath)
                    time.sleep(4)        

                elif 'show photos' in query:
                    photosPath = "G:\\Photos&vidios"
                    speak("Okay I showing you.Please wait I open it.....")
                    os.startfile(photosPath)
                    time.sleep(4)        

                elif 'python projects' in query:
                    projectPath = "G:\\Python Projects"
                    speak("Okay I showing you.Please wait I open it.....")
                    os.startfile(photosPath)  
                    time.sleep(4)                  

                elif 'gravia' in query:
                    speak("Yes")
                    takeCommand()

                elif 'close notepad' in query:
                    speak("Okay, I close it")
                    os.system("taskkill /f /im notepad.exe")

                elif 'close whatsapp' in query:
                    speak("Okay, I close it")
                    os.system("taskkill /f /im whatsapp.exe")

                elif 'close vs code' in query or 'close visual studio ' in query:
                    speak("Okay, I close it")
                    os.system("taskkill /f /im code.exe")

                elif 'close pycharm' in query:
                    speak("Okay, I close it")
                    os.system("taskkill /f /im PyCharm.exe")

                elif 'close chrome' in query:
                    speak("Okay, I close it")
                    os.system("taskkill /f /im Chrome.exe")

                elif 'close edge' in query:
                    speak("Okay, I close it")
                    os.system("taskkill /f /im msedge.exe")

                elif 'close antivirus' in query:
                    speak("Okay, I close it")
                    os.system("taskkill /f /im sssavgui.exe")

                elif 'I want to see a table' in query:
                    speak("Which table you want to see or listen?")
                    tlb = takeCommand()
                    speak(f"here is the table of {tlb}")
                    for table in range(1,11):
                        print(tlb,"x",table,"=",tlb*table)

                elif 'table' in query:
                    le = query.replace('table', '')
                    speak(f"Table of {le} is showing...")
                    for tables in range(1,11):
                        print(le,"x",tables,"=",le*tables)

                time = datetime.datetime.now().strftime("%H.%M")
                if time>="8.00" and time<"9.00":
                    notification.notify(
                        title = "Gravia Reminder",
                        message = "It's bath time, work will be done later, \nBathing can improve heart health. \nTaking a bath may help you to breathe easier.\nYour brain and nervous system can benefit from bathing.",
                        app_icon = r"G:\Programming\Python Projects\Gravia\Icons\reminder icon.ico",
                        timeout = 8,
                    )

                elif time>="19.30" and time<"20.30":
                    notification.notify(
                        title = "Gravia Reminder",
                        message = "It is your dinner time so you should go to dinner",
                        app_icon = r"G:\Programming\Python Projects\Gravia\Icons\Dinner icon.ico",
                        timeout = 8,
                    )

                elif time>="17.00" and time<"18.00":
                    notification.notify(
                        title = "Playing (Gravia Reminder)",
                        message = "It's time to play, you should go play with your friends",
                        app_icon = r"G:\Programming\Python Projects\Gravia\Icons\playing reminder icon.ico",
                        timeout = 8,
                    )

                elif time>="22":
                    notification.notify(
                        title = "Gravia Reminder",
                        message = "Today a lot of work is done, now is the time to do the rest of the sleep later, and I also need some rest so good night sir",
                        app_icon = r"G:\Programming\Python Projects\Gravia\Icons\sleep.ico",
                        timeout = 10,
                    )

    except Exception:
        speak("Soory I could't do that")