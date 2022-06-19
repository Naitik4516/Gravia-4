import playsound, os, gtts, googletrans, pyttsx3, threading

class Google_Speak:
    language = "en"
    slow = False
    lang_check = True

    def translate_speak(self, text, To, From='auto'):
        translator = googletrans.Translator()
        self.language = To
        self.speak(translator.translate(text,To,From))

    def speak(self, output):
        toSpeak = gtts.gTTS(text=output, lang=self.language, slow=self.slow, lang_check=self.lang_check)
        file = ".mp3"
        toSpeak.save(file)
        playsound.playsound(r".mp3", True)
        os.remove(file)

class MsSpeech:
    engine = pyttsx3.init('sapi5')
    # voices = engine.getProperty('voices') #getting details of current voice\n
    # for i in voices:
    #     print(i)
    """
    engine.setProperty('voice', voices[0].id)   \n
    engine.setProperty('rate', 130)   \n
    """
    def speak(self, audio):
        self.engine.say(audio) 
        self.engine.runAndWait() #Without this command, speech will not be audible to us.
        

if __name__ == '__main__':
    google = Google_Speak()
    # google.language = "en"
    # google.speak("हैलो में गूगल टेक्स्ट-तो-स्पीच बोल रही हूँ ।")
    # google.translate_speak("Hello I am Gravia, How may I hel you.","hi")
    # print(google.language)
    ms = MsSpeech()
    ms.speak("Hello, I am gravia speech api.")
    # google.speak("Hello, I am gravia speech a.p.i.")
    # print("Done!")
    # threading.Thread(target=google.speak, args=("Hello, I am running as a Thread",)).start()
    # print("Raned!")