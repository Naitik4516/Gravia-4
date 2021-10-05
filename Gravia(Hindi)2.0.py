import datetime  # pip install datetime
import json
import os  # pip install os
import random
import shutil
import smtplib  # pip install smtplib
import subprocess  # pip install subprocess         "All moduels install by pip like these so first of install all moduels"
import sys
import time
import webbrowser  # pip install webbrowser
from urllib.request import urlopen
import bs4
import feedparser
import playsound
import psutil
import pyautogui
import pyjokes
import pytemperature
import pyttsx3  # pip install pyttsx3
import pywhatkit
import requests
import shutdown
import speech_recognition as sr  # pip install speechRecognition
import speedtest
import wikipedia  # pip install  wikipedia
import win32com.client as wincl
import winshell
import wolframalpha
import ctypes
from bs4 import BeautifulSoup
from clint.textui import progress
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def speak(output):
    toSpeak = gTTS(text=output, lang='hi', slow=False)
    file = "gravia.mp3 "
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("शुभ प्रभात")

        elif hour >= 12 and hour < 17:
                speak("नमस्कार")

        else:
            speak("सुसंध्या")

        speak("मैं ग्रेविया 2.0 हूं, मैं आपकी कैसे मदद कर सकती हूं")

def reminders():
    tm = int(datetime.datetime.now().hour)
    if tm >= 9 and tm < 10:
        speak("कृष्णा यह तुम्हारे नहाने और नाश्ता करने का टाइम हो रहा है")

    elif tm >= 17 and tm < 18:
        speak("कृष्णा यह तुम्हारे खेलने का टाइम हो रहा है क्या तुम बाहर खेलने नहीं जा रहे?")
    elif tm >= 20 and tm < 21:
        speak("यह आपके खाना खाने का टाइम हो रहा है आपको खाना खाने जाना चाहिए")

    elif tm >= 22:
        speak("यह टाइम आपके सोने का है बहुत रात हो चुकी है आज के लिए बस यह बहुत काम हो गया अब मैं भी थक गई हूं तो हमें रेस्ट लेना चाहिए थोड़ा आप भी सो लो, शुभ रात्रि और अच्छे सपने")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("सुन रही हूं...")
        r.pause_threshold = 0.5 
        audio = r.listen(source)
    try:
        # print("समझ रही हूं")
        query = r.recognize_google(audio, language='hi-in')
        print(f"                                                                                        {query}\n")

    except Exception:
        print("कृपया, दोबारा कहैं...")
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
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    reminders()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'विकिपिडिया ' in query:  # if wikipedia found in the query then this block will be executed
            speak('ठीक है अभी देखती हूं')
            query = query.replace("wikipedia", "")
            # We can change sentances that read our A.I.
            results = wikipedia.summary(query, sentences=2)
            speak("विकिपीडिया के अनुसार")
            speak(results)
            print(results)

        elif 'प्ले' in query:
            song = query.replace('प्ले', '')
            speak(f"{song} चल रहा है")
            pywhatkit.playonyt(song)

        elif 'यूट्यूब में सर्च करो' in query:
            V = query.replace('', 'यूट्यूब में सर्च करो')
            speak(f"यूट्यूब पर {V} वाली वीडियो चल रही है")
            pywhatkit.playonyt(V)

        elif 'यूट्यूब में खोजो' in query:
            B = query.replace('', 'यूट्यूब में खोजो')
            speak(f"यूट्यूब पर {V} वाली वीडियो चल रही है")
            pywhatkit.playonyt(B)

        elif 'यूट्यूब खोलो ' in query or 'यूट्यूब चालू':
            speak("ठीक है, आप youtube पर जा रहे हैं। कृपया एक पल के लिए प्रतीक्षा करें")
            print("खुल रहा है .....")
            webbrowser.open("https://www.youtube.com/")

        elif 'इंस्टाग्राम' in query:
            speak("ठीक है, यहाँ आप इंस्टाग्राम पर जा रहे हैं। कृपया एक पल के लिए प्रतीक्षा करें\n")
            print("खुल रहा है .....")
            webbrowser.open("https: // www.instagram.com/")

        elif 'गूगल' in query:
            speak("ठीक है, यहाँ आप google पर जा रहे हैं। कृपया एक क्षण प्रतीक्षा करें\n")
            print("खुल रहा है .....")
            webbrowser.open("https://google.com/")

        elif 'ट्रांसलेटर' in query or "ट्रांसलेट" in query:
            speak(
                "ठीक है गूगल ट्रांसलेट ऐप खुल रहा है कृपया कुछ समय पर प्रतिकस्या  करें\n")
            print("खुल रहा है .....")
            webbrowser.open("https://translate.google.com/")

        elif 'स्तककोवेरफ़्लो' in query:
            speak(
                "ठीक है, यहाँ आप स्तककोवेरफ़्लो पर जा रहे हैं। कृपया एक क्षण प्रतीक्षा करें\n")
            print("खुल रहा है .....")
            webbrowser.open("https://stackoverflow.com/")

        elif 'जीमेल ' in query:
            speak("ठीक है, यहाँ आप जीमेल पर जा रहे हैं। कृपया एक क्षण प्रतीक्षा करें\n")
            print("खुल रहा है .....")
            webbrowser.open("https: // mail.google.com/mail/u/0 /  # inbox")

        elif 'होत्सतार' in query:
            speak("ठीक है, यहाँ आप होत्सतार पर जा रहे हैं । कृपया एक क्षण प्रतीक्षा करें\n")
            print("खुल रहा है .....")
            webbrowser.open("https://www.w3schools.com/")

        elif 'amazon' in query:
            speak("ठीक है, यहाँ आप amazon पर जा रहे हैं। कृपया एक क्षण प्रतीक्षा करें\n")
            print("खुल रहा है .....")
            webbrowser.open("https://www.amazon.com/")

        elif 'facebook' in query:
            print("खुल रहा है .....")
            speak(
                "ठीक है, यहाँ आप facebook पर जा रहे हैं। कृपया एक क्षण प्रतीक्षा करें\n")
            webbrowser.open("https://www.facebook.com/")

        elif 'w3school' in query:
            speak("ठीक है, यहाँ आप w3school पर जा रहे हैं। कृपया एक क्षण प्रतीक्षा करें")
            print("खुल रहा है ........")
            webbrowser.open("https://www.w3schools.com/")

        elif 'code with harry' in query:
            speak(
                "ठीक हे। यहाँ code with harry youtube चैनल खुल रहा है। कृप्या कुछ क्षण प्रतीक्षा करें")
            print("खुल रहा है ........")
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")

        elif 'techno gamerz' in query or 'techno gamers' in query:
            speak(
                "ठीक आहे। यहाँ techno gamerz youtube चैनल खुल रहा है। कृप्या कुछ क्षण प्रतीक्षा करें")
            print("खुल रहा है ........")
            webbrowser.open("https://www.youtube.com/channel/UCX8pnu3DYUnx8qy8V_c6oHg")

        elif 'beast boy shub' in query or 'beast boy shubh' in query:
            speak(
                "ठीक आहे। यहाँ beast boy shub youtube चैनल खुल रहा है। कृप्या कुछ क्षण प्रतीक्षा करें")
            print("खुल रहा है ........")
            webbrowser.open("https://www.youtube.com/channel/UCI86prlqXhbkREDMTaORvLQ")

        elif 'technology gyan' in query:
            speak("ठीक आहे। यहाँ technology gyan youtube चैनल खुल रहा है। कृप्या कुछ क्षण प्रतीक्षा करें")
            print("खुल रहा है ........")
            webbrowser.open("https://www.youtube.com/channel/UC1tVU8H153ZFO9eRsxdJlhA")

        elif 'make joke horror' in query:
            speak("ठीक आहे। यहाँ make joke horror youtube चैनल खुल रहा है। कृप्या कुछ क्षण प्रतीक्षा करें")
            print("खुल रहा है ........")
            webbrowser.open("https://www.youtube.com/channel/UC2gdpnWv_ve_RCWtvftkJ7g")

        elif 't series' in query or 'tseries' in query:
            speak("ठीक आहे। यहाँ T-series  youtube चैनल खुल रहा है। कृप्या कुछ क्षण प्रतीक्षा करें ")
            print("खुल रहा है ........")
            webbrowser.open("https://www.youtube.mommentcom/user/tseries")

        elif 'sound of lion' in query:
            soundPath="G:\\Python Projects\\Gravia\\sound effects\\sound of lion.wav"
            speak("ये रही शेर की आवाज ")
            os.startfile(soundPath)

        elif 'play movie' in query or 'play film' in query:
            os.startfile("G:\\Movies")

        elif 'the time' in query:
            time=datetime.datetime.now().strftime('%I:%M %p')
            speak(f'आबी {time} बज रहे। ')
            print(time)

        elif 'date' in query:
            strDate=datetime.datetime.now().strftime("%d:%m:%y")
            speak(f"आज {strDate} हे ")
            print(f"आज {strDate} हे ")

        elif "which day it is" in query or "What day is today" in query:
            strDay=datetime.datetime.now().strftime("%A")
            speak(f"आज {strDay} हे ")
            print(f"आज {strDay} हे ")

        elif "What year is it " in query:
            stryear=datetime.datetime.now().strftime("%Y")
            speak(f"{stryear} चल रहा है")
            print(f"{stryear} चल रहा है")

        elif "bye" in query:
            speak("अलविदा। अधिक रोमांचक चीजों के लिए चेकआउट ग्रैवीया")
            exit()

        elif 'email to Krishna' in query:
            try:
                speak("में इसमे क्या लिखूँ?")
                content=takeCommand()
                to="Enter your email.com"
                sendEmail(to, content)
                speak("ईमेल भेज दिया गया है !")
            except Exception as e:
                print(e)
                speak("मैं यह ईमेल नहीं भेज पा रही हूं")

        elif 'क्या हाल है?' in query or 'क्या हाल चल हैं' in query or 'केसे हो' in query or 'केसी हो' in query:
            speak("बस, ठीक हूँ ")
            speak("ओर आप केसे हैं")

        elif 'what is today' in query:
            tdy=datetime.datetime.now().strftime("%c")
            speak(tdy)
            print(tdy)

        elif 'fine' in query or "good" in query:
            speak("यह जानकर खुशी हुई कि आप ठीक हैं")

        elif "what's your name" in query or "What is your name" in query:
            assname="Gravia"
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'I am bored' in query or 'bore' in query:
            speak("तो में आपकी क्या मदत कर सकती हूँ क्या में आप के लिए एक गाना चलाउन या फिर कोई मूवी चलाउन या कोई जोक सुनाऊँ ")

        elif 'baba ke kharate' in query or 'baba ki kharate' in query or 'Baba ke kharate' in query or 'Baba ki kharate' in query:
            os.startfile(
                "G:\\Python Projects\\Gravia\\sound effects\\grandpa.wav")
            speak("ये हैं बाबा के खराते ")
            time.sleep(3)

        elif 'amma ke kharate' in query or 'amma ki kharate' in query or 'Amma ke kharate' in query or 'Amma ki kharate' in query:
            os.startfile(
                "G:\\Python Projects\\Gravia\\sound effects\\grandma.wav")
            speak("ये हैं बाबा के खराते। ")

        elif 'exit' in query:
            speak("मुझे अपना समय देने के लिए धन्यवाद")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("मुझे कृष्ण ने बनाया हे वहे बहुत अच्छे हैं। ")

        elif 'joke' in query:
            # os.startfile("C:\\Users\\Sandeep\\Downloads\\mixkit-light-applause-with-laughter-audience-512.wav")
            # speak(pyjokes.get_joke())
            speak("आभी कृष्ण जोक माजूल बना रहे हैं मुझे लगतहे वो जलधी बन जाएगा ")

        elif "calculate" in query:
            app_id="RJAY23-HLLLTY5H64"
            client=wolframalpha.Client(app_id)
            indx=query.lower().split().index('calculate')
            query=query.split()[indx + 1:]
            res=client.query(' '.join(query))
            answer=next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query:
            query=query.replace("search", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("अगर आप बात करते हैं तो निश्चित रूप से आप इंसान हैं।")
            os.startfile(
                "C:\\Users\\Sandeep\\Downloads\\mixkit-cartoon-voice-laugh-343.wav")

        elif "why you came to world" in query:
            speak("कृष्ण को धन्यवाद। इसके अलावा यह एक रहस्य है")
            os.startfile(
                "C:\\Users\\Sandeep\\Downloads\\mixkit-conference-audience-clapping-strongly-476.wav")

        elif "what are you doing" in query:
            speak("कुछ नहीं केवल आपसे बात कर रही हूँ ")
            speak("और तुम क्या कर रहे हो")

        elif "I do" in query:
            pass

        elif 'stop listening for 2 hours' in query:
            speak("ओके .")
            vact=7200
            time.sleep(vact)
            print(vact)

        elif 'stop listening for 1 hours' in query:
            speak("ओके .")
            h=2600
            time.sleep(h)
            print(h)

        elif 'stop listening for 30 minutes' in query:
            speak("ओके .")
            time.sleep(1800)

        elif 'stop listening for 20 minutes' in query:
            speak("ओके .")
            th20=1800
            time.sleep(th20)
            print(th20)

        elif 'stop listening for 10 minutes' in query:
            speak("ओके .")
            min=600
            time.sleep(min)
            print(min)

        elif 'stop listening for 5 minutes' in query:
            speak("ओके .")
            m=300
            time.sleep(m)
            print(f"I am not listening your commands for{m} seconds")

        elif 'stop listening for 2 minutes' in query:
            speak("ओके .")
            i=120
            time.sleep(i)
            print("i")

        elif 'stop listening for 1 minutes' in query:
            speak("ओके .")
            n=60
            time.sleep(n)
            print(n)

        elif 'stop listening for 30 seconds' in query:
            speak("ओके .")
            sec=30
            time.sleep(sec)
            print(sec)

        elif 'stop listening for 10 seconds' in query:
            speak("ओके .")
            time.sleep(10)

        elif 'is love' in query:
            speak("यह 7वीं इंद्रिय है जो अन्य सभी इंद्रियों को नष्ट कर देती है")

        elif "who are you" in query:
            speak("मैं कृष्ण द्वारा बनाया गया आपकी आभासी सहायक हूं")

        elif 'reason for you' in query:
            speak("मुझे कृष्णा द्वारा माइनर प्रोजेक्ट के रूप में बनाया गया था")

        elif 'change background' in query:
            try:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                        0,
                                                        "C:\\Windows\\WinSxS\\amd64_microsoft-windows-shell-wallpaper-theme1_31bf3856ad364e35_10.0.18362.1_none_a937730822266138",
                                                        0)
                speak("बैकग्राउंड सुकसेसफुल्ली चेंज हो गया हे ")

            except Exception as e:
                print(str(e))

        elif 'news' in query:
            try:
                jsonObj=urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data=json.load(jsonObj)
                i=1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))
                print("काम नहीं कर रहा")
                speak("माफ करें ये अभी काम नहीं कर रहा")

        elif 'lock window' in query:
            speak("locking the device")
            os.system("shutdown -1")

        elif 'shutdown ' in query:
            speak("ठीक हे !System shudowning please wait")  # shutdown=y
            print("यदि आप पीसी को शट्डाउन करना कहते हैं तो y दवाएं ओर अगर आप gravia को बंद करना कहते हैं तो न दवाएं। ")
            speak("यदि आप पीसी को शट्डाउन करना कहते हैं तो y दवाएं ओर अगर आप gravia को बंद करना कहते हैं तो न दवाएं। ")
            choice=input("Please confirm to shutdown the pc (y or n)\n")
            if choice == 'n':
                exit()
            else:
                os.system("shutdown /s /t 1")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "where is" in query:
            query=query.replace("where is", "")
            location=query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "restart" in query:
            speak("Restarting")
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            con=input("अगर आप कहते हैं तो 'y' दवाएं ओर अगर नहीं तो न दवाएं")
            if con == "y":
                subprocess.call(["shutdown", "/l"])
            else:
                continue

        elif "chatbot" in query or '3.0' in query:
            speak("क्षमा करें, यह version अभी उपलब्ध नहीं है, लेकिन कार्य प्रगति पर है।")
            print("Sorry, This version is not yet available, but work is in progress.")

        elif 'What are your functions' in query or 'What is your functions' in query:
            speak("में बहुत सारी चीज कर सकती हूँ। जेसे, में गाने चल सकती हूँ ओर कोई भी एप या वेबसाईट खोल सकती हूँ, ओर पीसी को सुतड़ों ओर भी बहुत कुछ, ओर अधिक जानकारी के लिए मेरा डेमो देखें ")

        elif 'what is your birthday' in query or 'what is your date of bith' in query or 'When does your birthday come' in query or 'What is your birthday date' in query or 'your birthday' in query or 'When were you' in query or 'when you were born' in query:
            speak("मेरा जन्म १० फरवरी २०२१ को हुआ था, जिसका समय १३:५२:३२ था")
            print("मेरा जन्म १० फरवरी २०२१ को हुआ था, जिसका समय १३:५२:३२ था")

        elif "weather" in query:
            api_key="675001e5325417f1e97ace33821a9f77"
            base_url="http://api.openweathermap.org/data/2.5/weather?"
            speak(" शहर का नाम ")
            print("City name : ")
            city_name=takeCommand()

            complete_url=base_url + "appid=" + api_key + "&q=" + city_name
            response=requests.get(complete_url)
            x=response.json()

            if x["cod"] != "404":
                y=x["main"]
                current_temperature=y["temp"]
                current_pressure=y["pressure"]
                current_humidiy=y["humidity"]
                current_temperature_celcius=pytemperature.k2c(
                    current_temperature)
                z=x["weather"]
                weather_description=z[0]["description"]

                # print following values
                print(" Temperature (in kelvin unit) = " +
                                str(current_temperature) +
                    "\n atmospheric pressure (in hPa unit) = " +
                                str(current_pressure) +
                    "\n humidity (in percentage) = " +
                                str(current_humidiy) +
                    "\n description = " +
                                str(weather_description))

                speak("तापमान " + str(current_temperature) + "डिग्री केलकिऊस हे" + " और वायु दाब" + str(current_pressure) + "hpa हे" + \
                      " और ह्यूमिडिटी " + str(current_humidiy) + "पर्सेन्ट रहेगी =" + " और आज मॉसम " + str(weather_description) + "रहेगा")

            else:
                print(" City Not Found ")

        elif "send message " in query:
                # You need to create an account on Twilio to use this service
            try:
                account_sid='ACdf65a010a8f2a92f8d2aeb900397bb59'
                auth_token='4445ca232dacaf9e7d1c871c520aab19'
                client=Client(account_sid, auth_token)

                message=client.messages \
                                .create(
                                    body=takeCommand(),
                                    from_='Sender No',
                                    to='Receiver No'
                                )

                print(message.sid)
            except Exception as e:
                print("Something went wrong unaible to send message")

        elif "open wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        elif 'where i am' in query or 'where we are' in query or 'find my location' in query or 'trace my location' in query:
            speak("Wait i check now")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.giojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                state=geo_data['state']
                country=geo_data['country']
                speak(f"Right now we are in {city},{state},{country}")
                print(f"Right now we are in {city},{state},{country}")
            except Exception as e:
                speak(
                    "क्षमा करें, मैं समझ नहीं पा रही हूं कि हम कहां हैं, शायद नेटवर्क की समस्या के कारण")
                pass

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("में शुर नहीं हूँ , हो सकता है कि आप मुझे कुछ समय दें")

        elif 'को बंद करो  yourself' in query:
            speak("ठीक हे में अपनेआप को बंद कर रही हूँ ")
            exit()

        elif "i love you" in query:
            speak("यह समझना कठिन है")

        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"सर, हमारे सिस्टम में {percentage} बैटरी है")
            if percentage >= 75 and percentage <= 99:
                speak("हमारे पास काम जारी रखने के लिए काफी पावर है")

            elif percentage == 100:
                speak("हमारे पास पूरी पावर  है")

            elif percentage >= 45 and percentage <= 70:
                speak("हमें सिस्टम की बैटरी को चार्जिंग पे लगा दे न चाहिए ")

            elif percentage >= 15 and percentage < 35:
                speak("हमारे पास ज्यादा बैटरी  नहीं है, इसलिए अब हमें अपनी बैटरी चार्ज करने की ज़्रुरत है")

            elif percentage <= 15:
                speak("चेतावनी! हमारे पास बहुत कम बैटरी  है पीसी को चार्जर से कनेक्ट करें अन्यथा पीसी बंद होने जा रहा है")

        elif 'search for' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("विकईपेड़ी के अनुसार")
            print(results)
            speak(results)

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'show options' in query or 'right click options' in query:
            speak("ठीक हे दिखारही हूँ ...")
            pyautogui.press("apps")

        elif "इंटरनेट स्पीड" in query:
            st=speedtest.Speedtest()
            up=st.upload
            dw=st.download
            speak(f"इंटरनेट डोनलोडिंग की स्पीड {dw} बिट्स है और अपलोडिंग की स्पीड  {up} बिट्स है")

        elif "Internet speed in mbps" in query:
            try:
                os.system('cmd /k "speed test"')
            except:
                speak("कोई इंटरनेट कनेक्शन नहीं है!")
                print("कोई इंटरनेट कनेक्शन नहीं है!")

        elif 'wi-fi' in query:
            speak("ठीक हे ")
            pyautogui.click(x=1196, y=745)

        elif 'messages' in query or 'show menu bar' in query:
            speak("ठीक हे ")
            pyautogui.click(x=1334, y=741)

        elif 'write' in query or 'voice typing' in query or 'type' in query:
            speak("What should i write in it ?")
            wrote=takeCommand()
            pyautogui.write(wrote, interval=0.12)

        elif 'open start' in query:
            speak("ठीक हे ")
            pyautogui.press("win")

        elif 'press enter' in query:
            speak("ठीक हे ")
            pyautogui.press("enter")

        elif 'browse back' in query or 'brouse back' in query:
            speak("ठीक हे ")
            pyautogui.press("browseback")

        elif 'browser forward' in query or 'brouse forward':
            speak("ठीक हे ")
            pyautogui.press("browserforward")

        elif 'refresh' in query:
            speak("ठीक हे ")
            pyautogui.press("browserrefresh")

        elif 'home' in query:
            speak("ठीक हे ")
            pyautogui.press("browserhome")

        elif 'bookmarks' in query or 'bookmark' in query:
            speak("ठीक हे ")
            pyautogui.press("browserfavorites")

        elif 'spacebar' in query:
            speak("ठीक हे ")
            pyautogui.press("space")

        elif 'next page' in query or "page down" in query:
            speak("ठीक हे ")
            pyautogui.press("pagedown")

        elif 'previous page' in query or "page up" in query:
            speak("ठीक हे ")
            pyautogui.press("pageup")

        elif 'open search' in query:
            speak("ठीक हे ")
            pyautogui.hotkey("ctrl", "f")

        elif 'rotate screen to left side' in query:
            speak("ठीक हे ")
            pyautogui.hotkey("ctrl", "alt", "left")

        elif 'rotate screen to right side' in query:
            speak("ठीक हे ")
            pyautogui.hotkey("ctrl", "alt", "right")

        elif 'rotate screen to down side' in query or 'rotate screen to bottom' in query:
            speak("ठीक हे ")
            pyautogui.hotkey("ctrl", "alt", "down")

        elif 'rotate screen to top side' in query or 'rotate screen to up side' in query or 'rotate screen to normal' in query:
            speak("ठीक हे ")
            pyautogui.hotkey("ctrl", "alt", "up")

        elif 'open task view' in query or 'start task view' in query or 'show task view' in query:
            speak("ठीक हे ")
            pyautogui.click(x=462, y=741)

        elif "what is" in query or "who is" in query:
            client=wolframalpha.Client("RJAY23-HLLLTY5H64")
            res=client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("कोई परिणाम नहीं")

        elif 'open zoom' in query:
            zoompath="C:\\Users\\Sandeep\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            speak("ठीक हे Zoom claud meeting is खुल रहा है। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile(zoompath)
            time.sleep(4)

        elif 'zomm ko band kar do' in query:
            speak("ठीक हे, बंद हो रहा हे...")
            os.system("taskkill /f /im zoom.exe")

        elif 'pycharm' in query:
            try:
                pycharmPath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
                speak("ठीक हे Pycharm Community Edition खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
                os.startfile(pycharmPath)
                time.sleep(4)
            except Exception as e:
                speak("Pycharm नहीं खुल पारा, शायद यहे पहले से ही खुल रहा हे ")

        elif 'open antivirus' in query:
            # antivirusPath="C:\\Program Files\\SecuraShield Ultimate AP\\ssavgui.exe"
            speak("एंटिवाइरस अभी चालू नहीं")
            # os.startfile(antivirusPath)
            time.sleep(4)

        elif 'पोएरशेल' in query:
            speak("ठीक हे windows powershell खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            subprocess.run("powershell.exe")
            time.sleep(4)

        elif 'सीएमडी' in query or "कमांड परोंट" in query or "कमांड फोरम" in query:
            speak("ठीक हे command promt खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            subprocess.run("cmd.exe")
            time.sleep(4)

        elif 'दिस पीसी' in query:
            speak("ठीक हे This PC खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")
            time.sleep(4)

        elif 'कंट्रोल पैनल' in query:
            speak("ठीक हे control panel खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")
            time.sleep(4)

        elif 'फाइल इक्स्प्लोरर ' in query:
            speak("ठीक हे file explorer खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\Users\\Sandeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.lnk")
            time.sleep(4)

        elif 'कैलक्यूलेटर' in query:
            speak("ठीक हे calculator खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            subprocess.run("calc.exe")
            time.sleep(4)

        elif 'पेंट' in query:
            speak("ठीक हे paint खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.system("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
            time.sleep(4)

        elif 'स्टेप रीकॉर्डर' in query:
            speak("ठीक हे Step recorder खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk")
            time.sleep(4)

        elif 'मीडिया प्लेयर' in query:
            speak("ठीक हे मीडिया प्लेयर खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Windows Media Player.lnk")
            time.sleep(4)

        elif 'कैरिक्टर' in query:
            speak("ठीक हे charactor map खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\System Tools\\Character Map.lnk")
            time.sleep(4)

        elif 'टास्क मैनेजर' in query:
            speak("ठीक हे टास्क मैनेजर खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")
            time.sleep(4)

        elif 'टेबल चीटर' in query:
            speak("ठीक हे table cheter program by Krishna  खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile("C:\\Users\\Sandeep\\PycharmProjects\\firstProg\\table cheater.py")
            time.sleep(4)

        elif 'नोटपैड' in query:
            speak("ठीक हे notepad खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            subprocess.run("notepad.exe")
            time.sleep(4)

        elif 'डौंलोड्स' in query:
            downloadsPath="Downloads"
            speak("ठीक हे !")
            os.startfile(downloadsPath)
            time.sleep(4)

        elif 'फ़ायरफ़ॉक्स' in query:
            firefoxPath="C:\\Program Files\\Mozilla Firefox"
            speak("ठीक हे opening firefox now. Please wait for a momment")
            os.startfile(firefoxPath)

        elif 'वस कोड ' in query or "विसुअल स्टूडियो कोड":
            vscodePath = "C:\\Users\\Sandeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("ठीक हे code is opening here now. Happy coding.")
            os.startfile(vscodePath)

        elif 'गरयावीय अपना कोड' in query:
            graviaPath = r"G:\Programming\Python Projects\Gravia\Gravia(Hindi)2.0.py"
            speak("में अपना सोर्स कोड दिखा रह हूँ")
            os.startfile(graviaPath)
            time.sleep(4)

        elif 'फोटो व्यूअर' in query:
            photoviwerPath="C:\\Program Files\\Windows Photo Viewer"
            speak("ठीक हे opening photo viwer now. Please wait for a momment")
            os.startfile(photoviwerPath)
            time.sleep(4)

        elif 'वर्ड खोलो ' in query or 'वर्ड चालू करो' in query or "एमएस वर्ड" in query:
            wordPath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk"
            speak("ठीक हे ,Ms word 2010 खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile(wordPath)
            time.sleep(4)

        elif 'पावर पॉइंट खोलो' in query or "पावर पिंट चालू" in query:
            PowerPointPath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010.lnk"
            speak("Ms power point 2010 खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile(PowerPointPath)
            time.sleep(4)

        elif 'एक्सेल खोलो' in query or 'एक्सेल स्टार्ट करो' in query:
            exelPath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010.lnk"
            speak("Ms exel खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile(exelPath)
            time.sleep(4)

        elif 'क्रोम को खोलो ' in query or 'क्रोम खोलो' in query:
            chromePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("Chrome browser खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile(chromePath)
            time.sleep(4)

        elif 'एज खोलो' in query or 'एज स्टार्ट करो' in query:
            edgePath="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            speak("Microsoft Edge browser खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile(edgePath)
            time.sleep(4)

        elif 'मूवी' in query or "फिल्म":
            moviesPath="G:\\Movies"
            speak("ठीक हे अभी मूवी दी कहती हूँ।")
            os.startfile(moviesPath)
            time.sleep(4)

        elif 'व्हाट्सप्प खोलो' in query or 'व्हाट्सप्प खोलो' in query:
            WhatsAppPath="C:\\Users\\Sandeep\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak("Whatsapp खुल रहा हे। कृप्या कुछ क्षण प्रतीक्षा करें")
            os.startfile(WhatsAppPath)
            time.sleep(10)

        elif "अबे" in query:
            speak("अबे बोले तो")

        elif "अरे" in query:
            speak("क्या अरे नहीं, अरे क्या")

        elif "यार" in query:
            speak("हाँ यार बोल क्या बदत करून तेरी")        

        elif "साले" in query or "कुत्ते" in query or "उल्लू" in query or "चुटिया" in query or "भैंस" in query or "कुत्ता" in query or "बोसडीके" in query or"भोसडीके" in query or"भएनचोट" in query or"मदारचोट " in query or "मादरजात" in query or"चोट" in query or "हारामी" in query or "हरामखोर" in query:
            speak("ओए गाली केसे बकव बए साले कुत्ते हारामी अबे तेरी माँ की")            

        elif 'हैलो' in query:
            speak("हां, सर कृपया बोलें और बताएं कि मैं आपकी कैसे मदद कर सकता हूं।")

        elif "नमस्ते" in query:
            speak("नमस्ते, में हूँ ग्रविया बिलिए में आपकी किस तरह मदत कर सकती हूँ")

        elif "राधे राधे" in query:
            speak("राधे राधे, में हूँ ग्रविया बिलिए में आपकी किस तरह मदत कर सकती हूँ")

        elif "राम राम" in query:
            speak("राम राम, में हूँ ग्रविया बिलिए में आपकी किस तरह मदत कर सकती हूँ")

        elif "गोवा के फोटो" in query:
            goa_photosPath="G:\\Photos&vidios\\goa"
            speak("ठीक हे showing....")
            os.startfile(goa_photosPath)
            time.sleep(4)

        elif 'फ़ोटोज़ दिखाओ' in query or 'फोटो दिखाओ' in query:
            photosPath="G:\\Photos&vidios"
            speak("ठीक है मैं आपको दिखा रहा हूं। कृपया प्रतीक्षा करें मैं इसे खोलती  हूं .....")
            os.startfile(photosPath)
            time.sleep(4)

        elif 'पाइथन प्रोजेक्ट्स' in query:
            projectPath="G:\\Python Projects"
            speak("ठीक है मैं आपको दिखा रहा हूं। कृपया प्रतीक्षा करें मैं इसे खोलती  हूं .....")
            os.startfile(photosPath)
            time.sleep(4)

        elif 'गरवीआ' in query:
            speak("हाँ बोलिए ")
            takeCommand()

        elif 'नोटपैड को बंद करो' in query:
            speak("ठीक हे, में इसे बंद कर रही हूँ। ")
            os.system("taskkill /f /im notepad.exe")

        elif 'व्हाट्सप्प को बंद करो' in query:
            speak("ठीक हे, में इसे बंद कर रही हूँ। ")
            os.system("taskkill /f /im whatsapp.exe")

        elif 'कोड को बंद करो' in query or 'विसुअल स्टूडियो को बंद करो' in query:
            speak("ठीक हे, में इसे बंद कर रही हूँ। ")
            os.system("taskkill /f /im code.exe")

        elif 'पायचर्म को बंद करो ' in query:
            speak("ठीक हे, में इसे बंद कर रही हूँ। ")
            os.system("taskkill /f /im PyCharm.exe")

        elif 'क्रोम  को बंद करो ' in query:
            speak("ठीक हे, में इसे बंद कर रही हूँ। ")
            os.system("taskkill /f /im Chrome.exe")

        elif 'एज को बंद करो ' in query:
            speak("ठीक हे, में इसे बंद कर रही हूँ। ")
            os.system("taskkill /f /im edge.exe")

        elif 'एंटिवाइरस को बंद करो ' in query:
            speak("ठीक हे, में इसे बंद कर रही हूँ। ")
            os.system("taskkill /f /im sssavgui.exe")

        elif 'टेबल' in query:
            speak("आप कॉनसी टेबल देखना चाहते हैं ")
            tlb=takeCommand()
            speak(f"ये रही {tlb} की टेबल ")
            for table in range(1, 11):
                print(tlb, "x", table, "=", tlb*table)
            speak("अगर आपको टेबल डोरेक्ट देखनी तो आप नॉले सकते हैं की 18 की टेबल या कुछ भी।")
