import winshell
import ctypes
import speedtest
import psutil
from os import system
import subprocess

class Tasks:
    def __init__(self, query, statusvar, speak) -> None:
        self.status,self.statusvar = True, statusvar

        if 'change background' in query:
            self.stausvar.set("Changing...")
            try:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                        0,
                                                        "C:\\Windows\\WinSxS\\amd64_microsoft-windows-shell-wallpaper-theme1_31bf3856ad364e35_10.0.18362.1_none_a937730822266138",
                                                        0)
                speak("Background changed succesfully")

            except Exception as e:
                print(str(e))

        elif 'empty recycle bin' in query:
            try:
                statusvar.set("Cleaning...")
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")
            except Exception:
                speak("Unaible to empty recycle bin")
                print(Exception)

        elif "restart" in query:
            statusvar.set("Restarting...")
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            statusvar.set("Processing...")
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            statusvar.set("Processing...")
            speak("Make sure all the application are closed before sign-out")
            subprocess.call(["shutdown", "/l"])

        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            statusvar.set("Fetching...")
            battery = psutil.sensors_battery()
            percentage = battery.percent 
            charging = battery.power_plugged
            speak(f"Sir, our system have {percentage} of battry")
            if charging != True:
                if percentage >= 75 and percentage <= 99:
                    speak("We have enough power to continue the work")

                elif percentage == 100:
                    speak("We have full power")

                elif percentage >= 45 and percentage <= 70:
                    speak("We should connect system to charging point to charge the system battery")

                elif percentage >= 15 and percentage < 35:
                    speak("We don't have enough,so now we need to charge our battery")

                elif percentage <= 15:
                    speak("Alert! We have very low power connect the pc to the charger otherwise pc is going to shutdown")
            else:
                speak("We have unlimited power as long as the system is on charging")

        elif "internet speed" in query:
            st = speedtest.Speedtest()
            up = st.upload
            dw = st.download
            speak(f"The internet donloading speed is {dw} bits and the uploding speed is {up} bits")

        elif 'lock window' in query:
            self.speak("locking the device")
            system("shutdown -1")

        elif 'shutdown ' in query:
            self.speak("System shudowning please wait !")
            print("If you want to shutown press 'y'. \nElse you Want to shutdown gravia press 'n'")
            self.speak(
                "If you want to shutown press y else you Want to shutdown gravia press n")
            choice = input("Please confirm to shutdown the pc (y or n)")
            if choice == 'n':
                exit()
            else:
                system("shutdown /s /t 1")
        
        else:
            self.status = False

    def __str__(self) -> str:
        return str(self.status)