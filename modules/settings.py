from tkinter import *
try:
    from modern_components import CreateModernTitlebar, ScrolledFrame
except ModuleNotFoundError:
    from .modern_components import CreateModernTitlebar, ScrolledFrame
from tkinter.ttk import Combobox
from tkinter import ttk
from datetime import date

# In future add custom background foreground changer

class SettingsButton(Button):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, kwargs)
        bg = "#E5E7E9"
        self.config(text=text, fg="black", anchor="w", bg="#E5E7E9", bd=0, activebackground="#909497",
                    activeforeground="black", highlightthickness=0, width=18, font=("arial", 14),  padx=10, pady=5,)
        self.bind("<Enter>", lambda e: self.config(bg="gray"))
        self.bind("<Leave>", lambda e: self.config(bg=bg))
        self.bind("<FocusIn>", self.Focus)
        self.bind("<FocusOut>", self.FocusOut)
        self.pack(fill=X)

    def Focus(self, e):
        self.config(bg="gray")

    def FocusOut(self, e):
        self.config(bg="white")

class Settings(Toplevel):
    def __init__(self, root, **kwargs) -> None:
        """
        # It creates a setting window
        """
        super().__init__(root, kwargs)
        self.title("Gravia - Settings")
        self.geometry("1000x600")
        self.iconbitmap("static\\icons\\settings.ico")

        self.root = root
        self.dark_bg_color = "black"
        self.dark_fg_color = "white"
        self.bg_color = "white"
        self.fg_color = "black"
        self.date = date.today()
        # CreateModernTitlebar(self, "Settings","#1C2833","white").packBar()
        self.config(bg=self.bg_color, bd=0)
        # Frames

        # Main Frame
        self.sidebar = Frame(self, bg="#E5E7E9")
        self.sidebar.pack(side=LEFT, fill=Y)

        # Section Frame
        self.GeneralFrame = ScrolledFrame(self, background=self.bg_color)
        self.ProfileFrame = ScrolledFrame(self, background=self.bg_color)
        self.AppearenceFrame = ScrolledFrame(self, background=self.bg_color)
        self.AboutFrame = ScrolledFrame(self, background=self.bg_color)

        # Modifying Frames
        self.GeneralFrame.interior.config(padx=12)
        self.ProfileFrame.interior.config(padx=12)
        self.AppearenceFrame.interior.config(padx=12)
        self.AboutFrame.interior.config(padx=12)

        # Buttons
        self.GeneralButton = SettingsButton(
            self.sidebar, "General", command=self.general)
        self.ProfileButton = SettingsButton(
            self.sidebar, "Profile", command=self.profile)
        self.AppearenceButton = SettingsButton(
            self.sidebar, "Appearence", command=self.appearence)
        self.AboutButton = SettingsButton(
            self.sidebar, "About", command=self.About)

        # Page Headings
        Label(self.GeneralFrame.interior, text="General", font="lucida 22 bold",
              bg=self.bg_color, fg=self.fg_color).pack(anchor="nw", pady=20)
        Label(self.ProfileFrame.interior, text="Profile", font="lucida 22 bold",
              bg=self.bg_color, fg=self.fg_color).pack(anchor="nw", pady=20)
        Label(self.AppearenceFrame.interior, text="Appearence", font="lucida 22 bold",
              bg=self.bg_color, fg=self.fg_color).pack(anchor="nw", pady=20)
        Label(self.AboutFrame.interior, text="About", font="lucida 22 bold",
              bg=self.bg_color, fg=self.fg_color).pack(anchor="nw", pady=20)


        self.frame_list = [self.GeneralFrame, self.ProfileFrame,
                    self.AppearenceFrame, self.AboutFrame]

        # Loading Content
        self.generalContent()
        self.profileContent()
        self.appearenceContent()
        self.aboutContent()

    def general(self):
        self.unpack()
        self.GeneralFrame.pack(fill=BOTH, expand=TRUE)
        self.update()

    def profile(self):
        self.unpack()
        self.ProfileFrame.pack(fill=BOTH, expand=TRUE)
        self.update()

    def appearence(self):
        self.unpack()
        self.AppearenceFrame.pack(fill=BOTH, expand=TRUE)
        self.update()

    def About(self):
        self.unpack()
        self.AboutFrame.pack(fill=BOTH, expand=TRUE)
        self.update()

    def unpack(self):
        self.GeneralFrame.pack_forget()
        self.ProfileFrame.pack_forget()
        self.AppearenceFrame.pack_forget()
        self.AboutFrame.pack_forget()

    def swap_mode(self, e=None):
        theme = self.color_theme.get()

        if theme == "light":
            self.bg_color = "white"
            self.fg_color = "black"
            self.config(bg=self.bg_color)
            self.sidebar.config(bg="#E5E7E9")
            for buttons in self.sidebar.winfo_children():
                buttons.configure(bg="#E5E7E9", fg="black")
            self.GeneralButton.bind("<Leave>", lambda e: self.GeneralButton.config(bg="#E5E7E9"))
            self.ProfileButton.bind("<Leave>", lambda e: self.ProfileButton.config(bg="#E5E7E9"))
            self.AppearenceButton.bind("<Leave>", lambda e: self.AppearenceButton.config(bg="#E5E7E9"))
            self.AboutButton.bind("<Leave>", lambda e: self.AboutButton.config(bg="#E5E7E9"))
            self.root.config(background="white")
            for frames in self.frame_list:
                frames.configure(background=self.bg_color)
                frames.canvas.configure(background=self.bg_color)
                frames.interior.configure(background=self.bg_color)
                for child in frames.interior.winfo_children():
                    child.configure(background=self.bg_color,
                                    foreground=self.fg_color)
            for things in self.root.winfo_children():
                things.configure(background=self.bg_color)
                for child_things in things.winfo_children():
                    try:
                        child_things.configure(background=self.bg_color,
                                    foreground=self.fg_color)
                    except Exception:
                        pass
        else:
            self.sidebar.config(bg="#283747")
            self.root.config(background=self.dark_bg_color)
            for buttons in self.sidebar.winfo_children():
                buttons.configure(bg="#283747", fg="white")
            self.GeneralButton.bind("<Leave>", lambda e: self.GeneralButton.config(bg="#283747"))
            self.ProfileButton.bind("<Leave>", lambda e: self.ProfileButton.config(bg="#283747"))
            self.AppearenceButton.bind("<Leave>", lambda e: self.AppearenceButton.config(bg="#283747"))
            self.AboutButton.bind("<Leave>", lambda e: self.AboutButton.config(bg="#283747"))
            for frames in self.frame_list:
                frames.configure(background=self.dark_bg_color)
                frames.canvas.configure(background=self.dark_bg_color)
                frames.interior.configure(background=self.dark_bg_color)
                for child in frames.interior.winfo_children():
                    child.configure(background=self.dark_bg_color,
                                    foreground=self.dark_fg_color)
            for things in self.root.winfo_children():
                things.configure(background=self.dark_bg_color)
                for child_things in things.winfo_children():
                    try:
                        child_things.configure(background=self.dark_bg_color,
                                    foreground=self.dark_fg_color)
                    except Exception:
                        pass

    def generalContent(self):
        Label(self.GeneralFrame.interior, text="Comming Soon...", font="lucida 22 bold",bg=self.bg_color,fg=self.fg_color).pack(anchor=CENTER, side=BOTTOM, pady=200, padx=250)    

    def profileContent(self):
        Label(self.ProfileFrame.interior, text="Comming Soon...", font="lucida 22 bold",bg=self.bg_color,fg=self.fg_color).pack(anchor=CENTER, side=BOTTOM, pady=200, padx=250)    


    def appearenceContent(self):
        color_label = Label(self.AppearenceFrame.interior, text="Color",
                            bg=self.bg_color, fg=self.fg_color, font="lucida 15")
        color_label.pack(side="left", anchor="n",padx=(0,5))

        self.color_theme = StringVar(value="light")
        color_combobox = Combobox(self.AppearenceFrame.interior, values=[
                                  "dark", "light"], state="readonly", font="lucida 10", textvariable=self.color_theme)
        color_combobox.pack(side="left", anchor="n",pady=(4,0),ipady=1)
        apply_button = Button(self.AppearenceFrame.interior, text="Apply",
                              font="helvetica 9", padx=5, command=self.swap_mode)
        apply_button.pack(side="left", anchor="n",padx=5, pady=(3,0))

    def aboutContent(self):
        content = """Gravia is open source project creted by Naitik Singhal in 2021.
Naitik Singhal (Krishna) was born on 2 february 2009.
He is a very smart and intelligent boy because he creates a `Gravia` a virtual assistant which can do - 
    • Simple User-friendly Gui
    • Open and close destktop applications
    • Open websites
    • Play any music
    • Play or search in youtube
    • Calculate mathematics equations
    • Weather reporting
    • Temperature calculating
    • Real-life News Reporting
    • Login System
    • Answer any question
    • Perform System Tasks i.e. - Calculate system battery, change pc wallpaper, shutdown, restart, logout, sleep, etc.
    • Automate system or browser
    • And have more exciting features and were come me in future
          """

        sub_title = Label(self.AboutFrame.interior, text="Gravia 4.1", bg=self.bg_color, fg=self.dark_fg_color, font="lucida 12 bold")
        sub_title.place(y=60)
        contentLabel = Text(self.AboutFrame.interior, bg=self.bg_color, fg=self.fg_color, font="lucida 10", borderwidth=0, width=90)
        contentLabel.insert(INSERT, content)
        contentLabel.config(state="disabled")
        contentLabel.pack(side=LEFT,anchor="sw",pady=5,padx=3)



if __name__ == '__main__':
    root = Tk()
    root.geometry('1000x600')
    root.title("Setting")
    # self.root.minsize(800,600)

    window = Settings(root)

    root.mainloop()
