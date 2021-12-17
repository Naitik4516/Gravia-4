import speech_recognition as sr
from threading import Thread

def takeCommand():   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening from take command...")
        audio = r.listen(source)

    try:
        print("Recognizing.from takeCommand..")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 
        if "hi" or "hello" in query: print("Hi hello tata bye bye")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

class Detect:
    def __init__(self, listenfunc) -> None:
        # while True:
        Thread(target=lambda : self.detector(listenfunc)).start()

    def detector(self, listenfunc):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            r.pause_threshold = 0.5
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') 
            print(query)
            if "gravia" in query or "graveyard" in query:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDetected")
                listenfunc()

        except Exception as e:
            self.detector(listenfunc)

        self.detector(listenfunc)

if __name__ == '__main__':
    Detect(listenfunc=takeCommand)