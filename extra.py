"""
ts = [
    "Sorry I can't connected",
    "Sorry I am not connected to the Internet",
    "Sorry I can't connect at the momment.Try again in a little bit.",
    "I am not connected to the Internet, So I can't talk you",
    "sorry to saying that I can't connected to the Internet, Try again in a little bit"
]
r = random.choice(ts)
speak(r)
print(r)
"""

"""
elif "write a note" in query:
    speak("What should i write, sir")
    note = takeCommand()
    file = open('gravia.txt', 'w')
    speak("Sir, Should i include date and time")
    snfm = takeCommand()
                                                        #By Krishna - "Usable"
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
         file.write(note)

elif "show note" in query:
speak("Showing Notes")
file = open("gravia.txt", "r")
print(file.read())
speak(file.read(6))
"""
"""
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much second you want to stop gravia from listening commands")
            a = int(takeCommand())
            speak(f"I will not listen your command for {a} seconds.")
            time.sleep(a)
            print(a)
"""

"""
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)       
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
"""
# import pyautogui
# import time
# pyautogui.press("f5")       

####
# def say():
#     z=["Welcome back, Sir","welcome back Krishna","Welcome back Naitik","Welcome back creator","Welcome","Welcome back","Welcome back my owner"]
#     y=random.choice(z)
#     speak(y)
#     print(y)
####

####
#def usrname():
   # speak("What should i call you sir")
  #  uname = takeCommand()
 #   speak("Welcome back Sir")
    #speak(uname)
   # columns = shutil.get_terminal_size().columns
     
  #  print("#####################".center(columns))
  #  print("Welcome ", uname.center(columns))
 #   print("#####################".center(columns))
     
# speak("uname")
####

     


"""

        else:
            s = ["Sorry, I can't catch that",
                "Please speak this again",
                "Something went wrong, please speak this again",
                "Unable to recognise your voice",
                "Uff , I did not hear that, please speak that again",
                "Sorry about that I didn't hear anything.",
                "Sorry to say I did not know about that but I still learning",
                "sorry I am not able to do that"
                "I did not know about that"]
            sya = random.choice(s)
            print(sya)

"""

# import pywhatkit`
# pywhatkit.sendwhatmsg('+918218182326','Hello this is working', 9,48)

"""
import pyautogui
from tkinter import *
root = Tk()
root.geometry("102x59")
Button(root, text="Stop typing", bg="black", fg="white", font="Calibri 6 bold", borderwidth=6, relief=GROOVE).pack(expand=TRUE)
while True:
    wrote = str(input("What should I write? : "))
    pyautogui.write(wrote, interval=0.05)
root.mainloop()

"""

#****************************************************************Modules*************************************************************************
#________________________________Emoji printer_______________________________________
# import emojis 
# emojified = emojis.encode("There is a :snake: in my boot !") 
# print(emojified) 
# or
# from emoji import emojize 
# print(emojize(":thumbs_up:")) 

"""
__________________________________sys_____________________________
import sys 

while True: 
	print("Type 'exit' to exit") 
	response = input() 
	if response == "exit": 
		print("Exiting the program") 
		sys.exit() 
	print("You typed", response) 
"""
"""
_______________________________________turtule_____________________________
import turtle 

myTurtle = turtle.Turtle() 
myWin = turtle.Screen() 

# Turtle to draw a spiral 
def drawSpiral(myTurtle, linelen): 
	myTurtle.forward(linelen) 
	myTurtle.right(90) 
	drawSpiral(myTurtle, linelen-10) 

drawSpiral(myTurtle, 80) 
myWin.exitonclick()
drawSpiral(myTurtle, 80)
#documation of turtle here-https://docs.python.org/2/library/turtle.html

"""
#__________________________________________modules end___________________________________________________________

""" ______________________________________________weather forecasting______________________________________________________
import re
import json
from urllib3 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('Your IP detail\n ')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
"""    
"""
import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
# print(voices)
engine.setProperty('voice', voices[0].id,)
engine.setProperty('rate', 100) 

engine.say("Ye hain amma ke kharraaatA") 
engine.runAndWait()
"""
from datetime import date
import os
# To get all possible colors for the command line, open the command prompt
# and enter the command "color help"
# os.system('color Fd')

"""                                                                                            
        elif "update assistant" in query:                                                        
            speak("After downloading file please replace this file with the downloaded one")     
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)       
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
"""

""" __________________________________Notification maker_________________
from plyer import notification
import datetime

notification.notify(
    title = "Gravia Reminder",
    message = "",
    app_icon = "G:\\Python Projects\\Gravia\\Icons\\playing reminder icon.ico",
    timeout = 10,
    )


"""
"""
import requests
import pytemperature
def weather():
            api_key = "675001e5325417f1e97ace33821a9f77"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = input("City name: ")

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
            response = requests.get(complete_url)  
            x = response.json() 

            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"]
                a =  pytemperature.k2c(current_temperature)
                z = x["weather"] 
                weather_description = z[0]["description"] 

                # print following values 
                print(" Temperature (in kelvin unit) = " +
                                str(current_temperature))
                
                print(" Temperature (in celcius unit) = " +
                                str(a))

weather()
"""
""" Not working
import pyttsx3
import requests
import json
import time

url = ('https://newsapi.org/v2/top-headlines?'
	'country = in&'
	'apiKey =')

url +='ce40662fcb6f4596870bac50bfb6b422'


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)

sound = engine.getProperty ('voices');
engine.setProperty('voice', 'sound[1].id')


try:
	response = requests.get(url)
except:
	engine.say("can, t access link, plz check you internet ")

news = json.loads(response.text)


for new in news['articles']:
	print("##############################################################\n")
	print(str(new['title']), "\n\n")
	engine.say(str(new['title']))
	print('______________________________________________________\n')

	engine.runAndWait()

	print(str(new['description']), "\n\n")
	engine.say(str(new['description']))
	engine.runAndWait()
	print("..............................................................")
	time.sleep(2)
"""
"""
from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews.set_lang('en')
# googlenews.set_period('7d')
# googlenews.set_time_range('03/29/2021', '03/29/2021')
googlenews.set_encode('utf-8')
googlenews.search('Aligarh')
result = googlenews.page_at(2)
print(results)
"""
"""
try:
                jsonObj = urlopen('''https://newsapi.org/v2/everything?q=tesla&from=2021-02-28&sortBy=publishedAt&apiKey=ce40662fcb6f4596870bac50bfb6b422''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    # speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
except Exception as e:
                print(str(e))
                print("काम नहीं कर रहा")
                # speak("माफ करें ये अभी काम नहीं कर रहा")
"""
"""
import os    
import time    
second = 0    
minute = 0    
hours = 0    
while(True):    
    print("Simple Stopwatch(in Python) Created By Krishna...")    
    print('\n\n\n\n\n\n\n')    
    print('\t\t\t\t-------------')    
    print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))    
    print('\t\t\t\t-------------')    
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        hour+=1;    
    os.system('cls')   
"""

# ________________________________Another way to speak_________________________----
# engine = pyttsx3.init('sapi5')
# voices= engine.getProperty('voices') #getting details of current voice
# # print(voices)
# engine.setProperty('voice', voices[0].id)   
# engine.setProperty('rate', 130)   

# def speak(audio):
#     engine.say(audio) 
#     engine.runAndWait() #Without this command, speech will not be audible to us.

"""__________________________________________________To search anything on google__________________________________________________-
import webbrowser
a = input()
webbrowser.open("https://www.google.com/search?q=" + a + "")
"""
"""
import webbrowser
a = input("Enter what you want to search \n")
webbrowser.open("https://www.youtube.com/results?search_query=" + a + "")
"""
"""
import webbrowser
a = input()
webbrowser.open("https://www.google.com/maps/place/" + a + "")
"""
"""
import webbrowser
a = input()
webbrowser.open("https://www.amazon.com/s?k=" + a + "")
"""
"""
import webbrowser
a = input()
webbrowser.open(f"https://translate.google.com/?sl=auto&tl=hi&text={a}&op=translate")
"""
"""
# import module
from geopy.geocoders import Nominatim

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")


# Latitude & Longitude input
Latitude = "25.594095"
Longitude = "85.137566"

location = geolocator.reverse(Latitude+","+Longitude)

address = location.raw['address']

# traverse the data
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')
print('City : ', city)
print('State : ', state)
print('Country : ', country)
print('Zip Code : ', zipcode)
"""

print("Yo")