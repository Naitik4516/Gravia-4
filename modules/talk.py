import datetime, winsound, holidays, webbrowser, pyautogui, pyjokes, os, socket, wikipedia, smtplib
from modules import birth_day_calculator
from bson import json_util

class Talk:
    def __init__(self, query,stausvar, speak) -> None:
        self.speak,self.statusvar = speak, stausvar
        self.status = True
        host = socket.gethostname()
        hostName = socket.gethostbyname(host)
        # Getting user info
        user_data = open('UserData.json')
        self.user_info = json_util.loads(user_data.read())
        assname = self.user_info["assistant_name"]

        if 'sound of lion' in query:
            stausvar.set("Playing...")
            soundPath = r"static\sound clips\lion roar.wav"
            winsound.PlaySound(soundPath,winsound.SND_FILENAME)

        elif 'play movie' in query or 'play film' in query:
            self.speak("Sorry I have no movies")

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.speak('Current time is ' + time)
            print(time)

        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%d:%m:%y")
            self.speak(f"Today is {strDate}") 
            print(f"Date is {strDate}")

        elif 'day' in query:
            strDate = datetime.datetime.now().strftime("%A")
            self.speak(f"Today is {strDate}")

        elif "What year is it " in query or "what year is going now" in query or "what yer it is" in query:
            stryear = datetime.datetime.now().strftime("%Y")
            self.speak(f"{stryear} is going on")
            print(f"It is going on {stryear}")

        elif "bye" in query:
            self.speak("Bye. Check Out gravia for more exicting things")
            exit()

        elif "my ip" in query:
            self.speak(hostName)

        elif "host" in query or "what is name of my pc" in query or "what is name of my laptop" in query or "what is name of my computer" in query:
            self.speak(hostName)

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

        elif 'hello' in query:
            self.speak("Hello, what's up dude")

        elif 'what is today' in query:
            in_holidays = holidays.HolidayBase()
            tdy = datetime.datetime.now().strftime("%A %d")
            date = datetime.datetime.now().strftime("%d-%m-%y")
            festival = in_holidays.get(date)
            speak(tdy)
            if "Christmas" in date:
                self.speak(f"Marry {festival}")
            self.speak("Today is {tdy}")
            if festival != None:
                self.speak("Happy {festival}")

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
            self.speak("So. What can I do for you, can I play music or play movies or Youtube. I also tell you joke.")
            self.takeCommand()

        elif 'baba ke kharate' in query or 'baba ki kharate' in query or 'Baba ke kharate' in query or 'Baba ki kharate' in query:
            winsound.PlaySound(r"static\sound clips\grandpa.wav",winsound.SND_FILENAME)
            self.speak("Ye hain Baba ke kharraaatA")

        elif 'amma ke kharate' in query or 'amma ki kharate' in query or 'Amma ke kharate' in query or 'Amma ki kharate' in query:
            winsound.PlaySound(r"static\sound clips\grandma.wav",winsound.SND_FILENAME)
            self.speak("Ye hain amma ke kharraaatA")

        elif 'Snore of grandpa' in query or 'Snoring of grandpa' in query or 'Snore of grandfather' in query or 'Snoring of grandfather' in query:
            winsound.PlaySound(r"static\sound clips\grandpa.wav",winsound.SND_FILENAME)
            self.speak("This is grandpa or grandfather's snoring")

        elif 'snore of grandma' in query or 'snoring of grandma' in query or 'Snore of grandmother' in query or 'Snoring of grandmother' in query:
            winsound.PlaySound(r"static\sound clips\grandma.wav",winsound.SND_FILENAME)
            self.speak("This is grandma or grandmother's snoring")

        elif 'exit' in query:
            self.speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            self.speak("I have been created by Krishna.")

        elif 'hindi joke' in query:
            self.speak("It is with great sadness that I cannot do this because I only know English, but my sister Gravia 2.0 can certainly do this for you.")

        elif 'joke' in query:
            self.speak(pyjokes.get_joke(category="all"))
            winsound.PlaySound(r"static\sound clips\mixkit-light-applause-with-laughter-audience-512.wav",winsound.SND_FILENAME)

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)

        elif "who i am" in query:
            self.speak("If you talk then definately you are human.")
            winsound.PlaySound(r"static\sound clips\mixkit-cartoon-voice-laugh-343.wav",winsound.SND_FILENAME)

        elif "why you came to world" in query:
            self.speak("Thanks to Krishna. further It's a secret")
            winsound.PlaySound(r"static\sound clips\audience-clapping-strongly-476.wav",winsound.SND_FILENAME)

        elif "what are you doing" in query:
            self.speak("Nothing, just talking to you")
            self.speak("And what are you doing")

        elif 'is love' in query:
            self.speak("It is 7th sense that destroy all other senses")

        elif "yo " in query:
            self.speak("Yo, what's up")

        elif "i love you" in query:
            self.speak("I love you too. My dear!")

        elif "who are you" in query:
            self.speak("I am your virtual assistant created by Krishna")

        elif 'reason for you' in query:
            self.speak("I was created as a Minor project by Mister Krishna ")           

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            self.speak("Locating" + location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")
        
        elif "update" in query or "updates" in query:
            try:
                f = open("gravia 4.1")
                # Do something with the file
            except FileNotFoundError:
                print("There are no updates available right now")
                self.speak("There are no updates available right now")
            finally:
                f.close()

        elif "hindi version" in query or '2.0' in query:
            self.speak("Sorry, This version is not yet available, but work is in progress. But you can try its developer version")
            print("It has been done but is not working properly")

        elif 'What are your functions' in query or 'what is your functions' in query:
            self.speak("I will do many thing like. I play music. I open any app or website, play movies, pay games, shutdown  pc an much more for more information show my demo ")

        elif 'what is your birthday' in query or 'what is your date of bith' in query or 'when does your birthday come' in query or 'what is your birthday date' in query or 'your birthday' in query or 'when were you' in query or 'when you were born' in query:
            self.speak("I was born on 10 february 2021, timing 13:56:32")
            print("I was born on 10 february 2021, timing 13:56:32")

        elif "open wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            self.speak("A warm" + query)
            self.speak("How are you Mister")

        elif 'security mode' in query or 'on security' in query:

            self.speak("Security mode is on. Maybe Initially the alarm will ring for confirmation, press q for exit or say stop security mode or off security mode")
            try:
                os.startfile("..\\security camera\\main.py")

            except Exception as e:
                self.speak("Anaible to run security mode please try again later")

        elif 'off security mode' in query or "stop security" in query:
            pyautogui.press("q")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            self.speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            self.speak("I'm fine, glad you me that")

        elif 'close yourself' in query:
            self.speak("I am closing you self. Bye")
            exit()

        elif "i love you" in query:
            self.speak("It's hard to understand")

        elif 'search for' in query:
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia")
            print(results)
            self.speak(results)
        
        elif "how old" in query or "your age" in query:
            birthday_calc = birth_day_calculator.findAge(10, 2, 2021)
            birthday = birthday_calc.get()
            speak(f"I am {birthday[0]} years, {birthday[1]} months and {birthday[2]} days old ")

        elif 'table' in query:
            self.statusvar.set("Printing...")
            number = [int(word) for word in query.split() if word.isdigit()]
            le =  number[0]
            self.speak(f"Table of {le} is showing...")
            for tables in range(1, 11):
                self.speak(le, "x", tables, "=", le*tables)

        # elif 'I want to see a table' in query:
        #     self.statusvar.set("Printing...")
        #     self.speak("Which table you want to see or listen?")
        #     tlb = self.takeCommand()
        #     self.speak(f"here is the table of {tlb}")
        #     for table in range(1, 11):
        #         print(tlb, "x", table, "=", tlb*table) 

        else:
            self.status = False

    def sendEmail(self, to, content):
        self.statusvar.set("Conecting to server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        self.statusvar.set("Emailing in process...")
        server.ehlo()
        server.starttls()
        server.login('Enter your email.com', 'Krishna 2021')
        self.statusvar.set("Sending...")
        server.sendmail('Enter your email.com', to, content)
        server.close()
        self.statusvar.set("Sent!")

if __name__ == '__main__':
    print(Talk("cfgfg",None,lambda q:print(q)))
    a = Talk("cfgfg",None,lambda q:print(q))
    print(bool(a.status), type(a.status))