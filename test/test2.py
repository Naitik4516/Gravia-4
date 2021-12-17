from modules import talk
from modules import systemTasks
from modules import appManager
from modules import automation
from modules import openApi
from modules import systemTasks
from modules import webOpen

speak = lambda q: print(q)

olf = lambda : print("Done")

query = input("Enter your query \n")
if query != None:    
    query = query.lower()
    webQuery = webOpen.webOpen(query, OlOf, statusvar=None, speak)
    if webQuery.status == False:
        normalTalk = talk.Talk(query, statusvar=None, speak)
        if normalTalk.status == False:
            openapi = openApi.Api(query,statusvar=None,speak, engine.setProperty)
            if openapi.status == False:
                automate = automation.AutoMate(query, speak, input)
                if automate.status == False:
                    systemTask = systemTasks.Tasks(query, statusvar=None, speak)
                    if systemTask.status == False and "open" in query or "close" in query:
                        try:
                            app = appManager.Manager(query,speak ,statusvar=None)
                            if app.openr != None:
                                speak(app.openr)
                        except appManager.AppNotFound:
                            speak("App not found")
                            pass
                        except appManager.AppNotOpen:
                            speak("Unable to open application")
                            pass
                        except appManager.ApllicationAlreadyClosed:
                            speak("Application is already closed or not running")
                            pass