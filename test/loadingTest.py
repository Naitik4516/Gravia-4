from tkinter import * 
from tkinter.ttk import *
import threading

floating_window = Tk()
floating_window.geometry('+650+350')
floating_window.wm_overrideredirect(True)

# Progress bar widget
progress = Progressbar(floating_window, orient = HORIZONTAL,
            length = 200, mode = 'determinate')

# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    floating_window.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    floating_window.update_idletasks()
    time.sleep(1)

    progress['value'] = 100
    floating_window.update_idletasks()
    time.sleep(1)

    progress['value'] = 150
    floating_window.update_idletasks()
    time.sleep(1)
    progress['value'] = 200

    floating_window.destroy()

progress.pack()

# This button will initialize
# the progress bar
# Button(floating_window, text = 'Start', command = bar).pack(pady = 10)
threading.Thread(target=bar,daemon=True).start()

# infinite loop
mainloop()