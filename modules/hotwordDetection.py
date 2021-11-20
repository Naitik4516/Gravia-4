import speech_recognition as sr
from threading import Thread

def listen():
    print("listening")

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
            r.non_speaking_duration = 0.2
            r.operation_timeout = 1
            r.adjust_for_ambient_noise(source,duration=0.8)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') 
            print(query)
            if "gravia" in query:
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDetected")
                listenfunc()

        except Exception as e:
            self.detector(listenfunc)

        self.detector(listenfunc)

if __name__ == '__main__':
    Detect(listen)