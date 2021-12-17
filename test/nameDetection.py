import speech_recognition as sr


def speechRecognize():   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-in')
        # if "graveyard" in query or "gravy" in query:
        #     query.replce("gravy","gravia")
        #     query.replce("graveyard","gravia")
        print(f"User said: {query}\n") 

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        s = speechRecognize()
        if "gravia" in s:
            print("\t\t\t\t\t\t\t\t\t\t\tDetected")