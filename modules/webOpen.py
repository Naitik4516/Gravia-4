import webbrowser
import pywhatkit
import wikipedia

class webOpen:
    def __init__(self,webquery,statusfunc=None,statusvar=None,speak=None) -> None:
        self.status = True
        if 'according wikipedia' in webquery or "ask wikipedia about" in webquery:  # if wikipedia found in the webquery then this block will be executed
            statusvar.set("Searching...")
            webquery = webquery.replace("according to wikipedia", "")
            webquery = webquery.replace("ask wikipedia about", "")
            speak('Searching Wikipedia...')
            # We can change sentences that read our A.I.
            results = wikipedia.summary(webquery, sentences=2)
            speak("According to Wikipedia")
            statusvar.set("Getting & Printing...")
            statusvar.set("Speaking...")
            speak(results)
            print(results)

        elif 'play' in webquery:
            statusvar.set("Playing...")
            song = webquery.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            statusvar.set("Online...")

        elif 'youtube' in webquery:
            if webquery == "youtube" or webquery == "open youtube":
                statusvar.set("Opening...")
                webbrowser.open("https://www.youtube.com/")
                speak("Opening youtube")
                statusvar.set("Searching...")
            else:
                statusvar.set("Searching...")
                v = webquery.replace('search in youtube','',1)
                v = webquery.replace('search on youtube','',1)
                v = webquery.replace('youtube','',1)
                v = webquery.replace('gravia','',1)
                pywhatkit.playonyt(v,open_video=False)
                speak('getting that from youtube')
                statusvar.set("Online...")

        elif 'open instagram' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.instagram.com/")
            speak(
                "here you go to instagram. opening please wait for a moment\n")
            print("Opening.....")

        elif 'open google' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.google.com/")
            print("Opening.....")
            speak("opening www.google.com . Search any thing that you want. Indian also called it. Google baabaa 😄\n")

        elif 'open translator' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://translate.google.com")
            speak(
                "google translate is opening her now. opening... please wait for a moment\n")
            print("Opening")

        elif 'open spotify' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.stackoverflow.com")
            speak("here you go to spotify. Listen music, be happy")
            print("Opening.....")

        elif 'open gmail' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://mail.google.com")
            speak(
                "here you go to gmail. Lets checkout some new mails\n")
            print("Opening.....")

        elif 'open hotstar' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.hotstar.com")
            speak(
                "Opening hotstar. Lets Watch tv shows, movies, cartoons and more\n")
            print("Opening.....")

        elif 'open amazon' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.amazon.in")
            speak(
                "here you go to amazon. Lets watch or purchase some awesome things\n")
            print("Opening.....")

        elif 'open facebook' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.facebook.com")
            print("Opening.....")
            speak("Opening facebook.")

        elif 'open w3 schools' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.w3schools.com")
            speak("here is W3schools.com . Learn code and become a master")
            print("Opening...")

        elif 'code with harry' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
            speak("Here is code with harry youtube channel. Beast channel for learn code for free in hindi 🤩")
            print("Opening...")

        elif 'techno gamerz' in webquery or 'techno gamers' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.youtube.com/channel/UCX8pnu3DYUnx8qy8V_c6oHg")
            speak(" here is techno gamerz youtube channel is opening. You know it is my favorite YouTube channel")
            print("Opening...")

        elif 'beast boy shub' in webquery or 'beast boy shubh' in webquery:
            statusvar.set("Opening...")
            webbrowser.open(
                "https://www.youtube.com/channel/UCI86prlqXhbkREDMTaORvLQ")
            speak(" here is beast boy shub youtube channel is opening. I hate this channel 😤")
            print("Opening...")

        elif 'technology gyan' in webquery:
            statusvar.set("Opening...")
            webbrowser.open(
                "https://www.youtube.com/channel/UC1tVU8H153ZFO9eRsxdJlhA")
            speak(" technology gyan youtube channel is opening. Please wait for a moment")
            print("Opening...")

        elif 'make joke horror' in webquery:
            statusvar.set("Opening...")
            webbrowser.open(
                "https://www.youtube.com/channel/UC2gdpnWv_ve_RCWtvftkJ7g")
            speak("make joke horror youtube channel is opening. Watch animated horror stories 👻")
            print("Opening...")

        elif 'sound clip' in webquery:
            statusvar.set("Opening...")
            webbrowser.open("https://www.youtube.com/user/tseries")
            speak(" T-series youtube channel is opening. best youtube channel for music 🎵🎶🎧")
            print("Opening...")  

        else:
            self.status = False

        if statusfunc!=None:
            statusfunc()

if __name__ == '__main__':
    from tkinter import Tk, StringVar
    
    root = Tk()
    root.geometry('500x400')
    
    svar = StringVar()
    
    s = lambda q: print(q)
    a = webOpen("search tech burner in youtube",statusvar=svar, speak=s)
    a = bool(a)
    if a == True:
        print("Y")
    else:
        print("N")
    
    root.mainloop()