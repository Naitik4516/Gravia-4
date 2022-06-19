from tkinter import *
from threading import Thread
from time import sleep

class LDS:
    @staticmethod
    def start():
        global splash_root
        splash_root = Tk()
        splash_root.geometry("500x500")
        # splash_root.overrideredirect(True)
        splash_root.eval('tk::PlaceWindow . center')

        logo = PhotoImage(file=r"static\Icons\Gravia logos & animations\Gravia (500x500).png")
        splash_label = Label(splash_root,image=logo)
        splash_label.pack(fill="both", expand=True)
        splash_root.mainloop()

    @staticmethod
    def stop():
        splash_root.destroy()

if __name__ == "__main__":
    root = LDS()
    Thread(target=LDS.start).start()
    print("Starting in 5 seconds...")
    sleep(5)
    print("Starting...")
    LDS.stop()
