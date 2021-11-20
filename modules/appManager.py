from os import startfile, system, path
import subprocess

HOME_DIR = path.expanduser('~')

class AppNotFound(Exception):
    pass

class AppNotOpen(Exception):
    pass

class ThroughError():
    def __init__(self,message, *args: object) -> None:
            super().__init__(*args)
            return message

class ApllicationAlreadyClosed(Exception):
    pass
        

def open(appName):    
    try:
        if 'pycharm' in appName:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            startfile(pycharmPath)

        elif 'antivirus' in appName:
            
            antivirusPath = r"C:\Program Files\SecuraShield AVCP\ssavgui.exe"
            startfile(antivirusPath)

        elif 'powershell' in appName:
            
            subprocess.run("powershell.exe")

        elif 'cmd' in appName or "command promt" in appName:
            subprocess.run("cmd.exe")

        elif 'this pc' in appName:       
            startfile(f"{HOME_DIR}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")

        elif 'control panel' in appName:        
            startfile(f"{HOME_DIR}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")

        elif 'file explorer' in appName:      
            startfile(f"{HOME_DIR}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.lnk")

        elif 'calculator' in appName:       
            subprocess.run("calc.exe")
            print("calculator is opening here now. Please wait for a momment")

        elif 'paint' in appName:
            
            system(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
            print(
                "calculator is opening here now. Please wait for a momment")

        elif 'step recorder' in appName:
            
            startfile(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk")
            print(
                "Step recorder is opening here now. Please wait for a momment")

        elif 'media player' in appName:
            
            startfile(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Windows Media Player.lnk")
            print(
                "calculator is opening here now. Please wait for a momment")

        elif 'charactor map' in appName:
            print(
                "charactor map is opening here now. Please wait for a momment")
            startfile(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\System Tools\\Character Map.lnk")

        elif 'calculator' in appName:
            print(
                "calculator is opening here now. Please wait for a momment")
            startfile(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")

        elif 'table cheater' in appName:
            startfile(
                f"{HOME_DIR}\\PycharmProjects\\firstProg\\table cheater.py")
            print(
                "table cheter program by Krishna  is opening here now. Please wait for a momment")

        elif 'notepad' in appName:
            
            subprocess.run("notepad.exe")
            print(
                "notepad is opening here now. Please wait for a momment")

        elif 'downloads' in appName or 'download' in appName:
            
            startfile("Downloads")
            print("Opening downloads folder")

        elif 'firefox' in appName:
            firefoxPath = "C:\\Program Files\\Mozilla Firefox"
            startfile(firefoxPath)
            print("opening firefox now. Please wait for a momment")

        elif 'code' in appName or 'vs code' in appName or 'visual studio code' in appName:
            
            vscodePath = f"{HOME_DIR}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            startfile(vscodePath)
            print("code is opening here now. Happy coding.")

        elif 'Gravia code' in appName:
            
            graviaPath = "G:\\Python Projects\\Gravia\\Gravia(Eng.)1.0.py"
            startfile(graviaPath)
            print("I my code")

        elif 'Photo viwer' in appName:
            photoviwerPath = "C:\\Program Files\\Windows Photo Viewer"
            print(
                " opening photo viwer now. Please wait for a momment")
            startfile(photoviwerPath)

        elif "start Need For Speed" in appName or "play need for speed" in appName:
            
            gamePath = "C:\\Program Files (x86)\\EA GAMES\\Need for Speed Most Wanted PC Demo\\speedDemo.exe"
            startfile(gamePath)
            print(
                ",Starting ready for racing zuummmmmm,zuummmmmm,zuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuum")

        elif 'word' in appName:
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk"
            startfile(wordPath)
            print("Ms word is opening here now. Please wait for a momment")

        elif 'powerpoint' in appName or 'power point' in appName:           
            PowerPointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010.lnk"
            startfile(PowerPointPath)
            print("Ms power point 2010 is opening here now. Please wait for a momment")

        elif 'exel' in appName:            
            exelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010.lnk"
            startfile(exelPath)
            print("Ms exel is opening here now. Please wait for a momment")

        elif 'chrome' in appName:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            print("Chrome browser is opening here now. Please wait for a momment")
            startfile(chromePath)

        elif 'edge' in appName:          
            edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            startfile(edgePath)
            print(
                "Microsoft Edge browser is opening here now. Please wait for a momment")

        elif 'play Movies' in appName:
                moviesPath = "G:\\Movies"
                print("Sure movie list is showing")
                startfile(moviesPath[0])

        elif 'whatsapp' in appName or 'whattsapp' in appName or 'whatsup' in appName:        
            try:
                WhatsAppPath = f"{HOME_DIR}\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                startfile(WhatsAppPath)
                print("Whatsapp is opening here now. Please wait for a momment")
            except Exception:
                return "Sorry it is Microsoft store application. Tha means I have no acces on this"

        elif "show goa photos" in appName:
            try:
                
                goa_photosPath = "G:\\Photos&vidios\\goa"
                print("showing....")
                startfile(goa_photosPath)
            except Exception:
                ThroughError("A bad news, We found that all photos and vidios are corropted by noaa ransomeware.")

        elif 'show photos' in appName:
            try:
                
                photosPath = "G:\\Photos&vidios"
                print("I showing you.Please wait I open it.....")
                startfile(photosPath)
            except Exception:
                startfile("Pictures")
                raise ThroughError("A bad news, We found that all photos and vidios are corropted by noaa ransomeware. But I have some fhotos in your pictures media library")

        elif 'python projects' in appName:   
            projectPath = "G:\\Programming\\Python Projects"
            print("I showing you.Please wait I open it.....")
            startfile(projectPath)

        else:
            raise AppNotOpen()
    except Exception as e:
        print(e)
        raise AppNotFound()

def close(appName):
    if 'notepad' in appName:
        try:
            system("taskkill /f /im notepad.exe")
        except Exception:
            raise ApllicationAlreadyClosed("Notepad is not opened, it is already close")
     
    elif 'whatsapp' in appName:
        try:  
            system("taskkill /f /im whatsapp.exe")
        except Exception:
            raise ApllicationAlreadyClosed("Whatsapp is not opened, it is already close")
            
    elif 'vs code' in appName or 'visual studio' in appName:
        try:            
            system("taskkill /f /im code.exe")
        except Exception:
            raise ApllicationAlreadyClosed("Visual studio code is not opened, it is already close")
            
    elif 'pycharm' in appName:
        try:          
            system("taskkill /f /im PyCharm.exe")          
        except Exception:
            ApllicationAlreadyClosed()
            
    elif 'chrome' in appName:
        try:           
            system("taskkill /f /im Chrome.exe")
        except Exception:
            raise ApllicationAlreadyClosed()
            
    elif 'edge' in appName:
        try:   
            system("taskkill /f /im msedge.exe")
        except Exception:
            raise ApllicationAlreadyClosed()
            
    elif 'antivirus' in appName:
        try:
            system("taskkill /f /im sssavgui.exe")
        except Exception as e:
            print(e)
            raise ApllicationAlreadyClosed()

class Manager:
    def __init__(self,appName) -> None:
        if "open" in appName :
            app = appName.replace("open ","")
            print(app)
            self.openr = open(app)
        elif "close" in appName:
            appc = appName.replace("close ","")
            close(appc)
        else:
            app = appName.replace("open ","")
            print(app)
            self.openr = open(app)



if __name__ == '__main__':
    m = Manager("open whatsapp")