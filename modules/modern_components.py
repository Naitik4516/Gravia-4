from ctypes import windll
from tkinter import *
from tkinter import ttk

import win32con
import win32gui
from PIL import Image, ImageTk
from ttkwidgets import AutoHideScrollbar


class CreateModernTitlebar():
        """
        Ex:
            root = Tk()
            titleBar = CustomTitle(root,title_text = 'Hello,World!' , bg = "#000000" , fg = '#ffffff')
            titleBar.resizeable = True
            titleBar.packBar()
            self._win.mainloop()
    
            Note:
                    Try to Give Color value in Hex and the 3rd car should be number
                        #7a4e7a
                           ↑ (this one)                  
        """
        resizeable = True
        font_style = ('Candara',13)
        
    
        def __init__(self,win,title_text='Custom Title Bar',bg='#ffffff',fg="#000000"):  
            # deactivating main title bar
            self._win = win
            win.title(title_text)
    
            # props
            self.bg = bg
            self._maximized = False
            self._win_width = win.winfo_width()
            self._win_height = win.winfo_height()
            self._scr_width = win.winfo_screenwidth()
            self._scr_height = win.winfo_screenheight()
            self._addWidget(title_text,bg,fg)
            
        def packBar(self):
            self._title_bar.pack(fill=X)
            self._checkAbility()
            self._win.overrideredirect(1)
            self._finilize()
    
        def _checkAbility(self):
            if not self.resizeable:
                self._maximize_btn.config(state=DISABLED)
            else:
                self._resizey_widget.pack(side=BOTTOM,ipadx=.1,fill=X)
                self._resizex_widget.pack(side=RIGHT,ipadx=.1,fill=Y)
    
        def _maximize_win(self):
            if not self._maximized:
                self._past_size = self._win.geometry()
                self._win.geometry(f"{self._scr_width}x{self._scr_height}+{0}+{0}")
                self._maximize_btn.config(text = '🗗')
            else:
                self._win.geometry(self._past_size)
                self._maximize_btn.config(text = '🗖')
            self._maximized = not self._maximized
    
    
        def _minimize(self):
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    
        
        def _setIconToTaskBar(self,mainWindow):
            GWL_EXSTYLE = -20
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_TOOLWINDOW = 0x00000080
            # Magic
            hwnd = windll.user32.GetParent(mainWindow.winfo_id())
            stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            stylew = stylew & ~WS_EX_TOOLWINDOW
            stylew = stylew | WS_EX_APPWINDOW
            res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
        
            mainWindow.wm_withdraw()
            mainWindow.after(10, lambda: mainWindow.wm_deiconify())
    
        def _addWidget(self,title_text,bg,fg):
            self._title_bar = Frame(self._win,bd=1,bg=bg, pady=2)
    
            self._title_text = Label(self._title_bar,text=title_text,bg=bg,fg=fg,font=self.font_style)
            self._title_text.pack(side=LEFT,padx=4,pady=3)
            self._title_text.bind("<B1-Motion>",self._drag)
    
            self._close_btn = Button(self._title_bar,text = '\u2715',bd=0,bg=bg,fg=fg,width=3,font=self.font_style,command=lambda: exit())
            self._close_btn.pack(side=RIGHT,fill=Y)
            self._maximize_btn = Button(self._title_bar,text="🗖",bd=0,bg=bg,fg=fg,width=3,font=self.font_style,command=self._maximize_win)
            self._maximize_btn.pack(side=RIGHT,fill=Y)
            self._minimize_btn = Button(self._title_bar,text="–",bd=0,bg=bg,fg=fg,width=3,font=self.font_style,command=self._minimize)
            self._minimize_btn.pack(side=RIGHT,fill=Y)
            self._title_bar.bind('<Button-1>', self._drag)
    
            self._resizex_widget = Frame(self._win,cursor='sb_h_double_arrow')
            self._resizex_widget.bind("<B1-Motion>",self._resizex)
    
            self._resizey_widget = Frame(self._win,cursor='sb_v_double_arrow')
            self._resizey_widget.bind("<B1-Motion>",self._resizey)
    
            self._hover_effect()
    
        def _hover_effect(self):
            try:
                num = int(self.bg[3]) - 1
                newbg = self.bg.replace(self.bg[3],str(num))
            except:
                newbg = "#c7ebe8"
    
            def change_bg(which_one,bg = newbg):
                which_one.config(bg=bg)
            def restore_bg(which_one):
                which_one.config(bg=self.bg)
            self._maximize_btn.bind('<Enter>',lambda event: change_bg(self._maximize_btn))
            self._maximize_btn.bind('<Leave>',lambda event: restore_bg(self._maximize_btn))
            self._minimize_btn.bind('<Enter>',lambda event: change_bg(self._minimize_btn))
            self._minimize_btn.bind('<Leave>',lambda event: restore_bg(self._minimize_btn))
            self._close_btn.bind('<Enter>',lambda event: change_bg(self._close_btn,bg='#db2730'))
            self._close_btn.bind('<Leave>',lambda event: restore_bg(self._close_btn))
    
    
        def _finilize(self):
            self._win.after(10, lambda: self._setIconToTaskBar(self._win))
    
        def _drag(self,event):
            xwin = self._win.winfo_x()
            ywin = self._win.winfo_y()
            startx = event.x_root
            starty = event.y_root
    
            ywin = ywin - starty
            xwin = xwin - startx
    
            def _move_window(event): # runs when window is dragged
    
                self._win.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')
    
    
            def _release_window(event): # runs when window is released
                self._win.config(cursor="arrow")
                
            self._title_bar.bind('<B1-Motion>', _move_window)
            self._title_bar.bind('<ButtonRelease-1>', _release_window)
            self._title_text.bind('<B1-Motion>', _move_window)
            self._title_text.bind('<ButtonRelease-1>', _release_window)
    
    
        def _resizex(self,event):
    
            xwin = self._win.winfo_x()
    
            difference = (event.x_root - xwin) - self._win.winfo_width()
    
            if self._win.winfo_width() > 150 : # 150 is the minimum width for the window
                try:
                    self._win.geometry(f"{ self._win.winfo_width() + difference }x{ self._win.winfo_height() }")
                except:
                    pass
            else:
                if difference > 0: # so the window can't be too small (150x150)
                    try:
                        self._win.geometry(f"{ self._win.winfo_width() + difference }x{ self._win.winfo_height() }")
                    except:
                        pass
    
    
        def _resizey(self,event):
    
            ywin = self._win.winfo_y()
    
            difference = (event.y_root - ywin) - self._win.winfo_height()
    
            if self._win.winfo_height() > 150: # 150 is the minimum height for the window
                try:
                    self._win.geometry(f"{ self._win.winfo_width()  }x{ self._win.winfo_height() + difference}")
                except:
                    pass
            else:
                if difference > 0: # so the window can't be too small (150x150)
                    try:
                        self._win.geometry(f"{ self._win.winfo_width()  }x{ self._win.winfo_height() + difference}")
                    except:
                        pass

class ModernMenubar:
    def __init__(self, parent) -> None:
        self.root = parent
        self.menuframe = Frame(parent,borderwidth=2,background="#082451",)
        self.menuframe.pack(side=TOP, fill='both')

    def createMenu(self, text):
        newButton  = Label(self.menuframe,text=text,background="#082451",padx=2,fg="white",font="lucida 10 bold")
        newButton.pack(side=LEFT)
        newButton.bind("<Button-1>", self.add_submenu_button)

    def add_submenu_button(self,text=None):
        button = Button(self.submenu,text=text,borderwidth=0,background="#082451",foreground="white")
        button.pack(side=LEFT,padx=5,pady=2)

    def submenu(self, e=None):
        self.submenu = Toplevel(self.root)
        self.submenu.overrideredirect(True)
        self.submenu.mainloop()

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        super().__init__(master, kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class Switch_button(Button):
    def __init__(self, master, size: tuple[int, int], **kwargs):
        super().__init__(master, kwargs)

        self.is_on = True

        # Define our switch function
        def switch(e=None):            
            # Determine is on or off
            if self.is_on:
                self.config(image = off)
                self.is_on = False
            else:
                self.config(image = on)
                self.is_on = True

        # Binding
        self.bind("<Button-1>", switch)

        # Define Our Images
        on_image = Image.open(r"static\Icons\on.png")
        on_image = on_image.resize(size)
        on = ImageTk.PhotoImage(on_image)

        off_image = Image.open(r"static\Icons\off.png")
        off_image = off_image.resize(size)
        off = ImageTk.PhotoImage(off_image)

        self["image"] = on
        self["borderwidth"] = 0

class ScrolledFrame(Frame):
    def __init__(self, master: Misc, autohide:bool = True, bindwithmousewheel:bool = True, background:str = ..., **kwargs) -> None:
        """
        # ScrolledFrame
        Tkinter frame with scrollbars
        ## Autohide
        If you set autohide=True, the scrollbar will automatically hide when it is not needed.
        ## Bind with mouse wheel
        If you turn bindwithmousewheel=True, your scroll bar will bind to the mouse wheel.
        ### Tips
        If you want to change or modify more you need to modify the canvas to modify the can you need write this syntax - canva.config(`Your options here`)

        """
        super().__init__(master, kwargs)

        # Create A Main frame

        # self = Frame(master)

        self.config(bd=0,highlightthickness=0)
        # Create Frame for X Scrollbar

        sec = Frame(self)

        sec.pack(fill=X, side=BOTTOM)

        # Create A Canvas

        self.canvas = Canvas(self, background=background, bd=0, highlightthickness=0)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbars to Canvas

        if autohide:
            x_scrollbar = AutoHideScrollbar(
                sec, orient=HORIZONTAL, command=self.canvas.xview)
            x_scrollbar.pack(side=BOTTOM, fill=X)

            y_scrollbar = AutoHideScrollbar(
                self, orient=VERTICAL, command=self.canvas.yview)
            y_scrollbar.pack(side=RIGHT, fill=Y)
        else:
            x_scrollbar = ttk.Scrollbar(
                sec, orient=HORIZONTAL, command=self.canvas.xview)
            x_scrollbar.pack(side=BOTTOM, fill=X)

            y_scrollbar = ttk.Scrollbar(
                self, orient=VERTICAL, command=self.canvas.yview)
            y_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas

        self.canvas.configure(xscrollcommand=x_scrollbar.set)

        self.canvas.configure(yscrollcommand=y_scrollbar.set)

        self.canvas.bind("<Configure>", lambda e: self.canvas.config(
            scrollregion=self.canvas.bbox(ALL)))

        # Create Another Frame INSIDE the Canvas

        self.interior = Frame(self.canvas, background=background, bd=0, highlightthickness=0)
    
        # Add that New Frame a Window In The Canvas

        self.canvas.create_window((0, 0), window=self.interior, anchor="nw")

        # Binding with mousewheel
        if bindwithmousewheel:
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == '__main__':
    def clicked():
        print("cliked")
    root = Tk() 
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
    b1 = ScrolledFrame(root, background="navy blue", borderwidth=0, highlightthickness=0,)
    b1.interior.config(padx=10)
    sub_title = Label(b1.interior, text="Gravia 4.1", bg="navy blue", fg="white", font="lucida 12 bold")
    sub_title.pack()
    contentLabel = Text(b1.interior, bg="navy blue", fg="white", font="lucida 10", borderwidth=0)
    contentLabel.insert(INSERT, content)
    contentLabel.config(state="disabled")
    contentLabel.pack()
    b1.pack(fill=BOTH, expand=1)
    root.mainloop()
