from tkinter import *
import win32gui
import win32con
from ctypes import windll

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
            self._title_bar = Frame(self._win,bd=1,bg=bg)
    
            self._title_text = Label(self._title_bar,text=title_text,bg=bg,fg=fg,font=self.font_style)
            self._title_text.pack(side=LEFT,padx=4,pady=3)
            self._title_text.bind("<B1-Motion>",self._drag)
    
            self._close_btn = Button(self._title_bar,text = '\u2715',bd=0,bg=bg,fg=fg,width=3,font=self.font_style,command=lambda: quit())
            self._close_btn.pack(side=RIGHT,fill=Y)
            self._maximize_btn = Button(self._title_bar,text="🗖",bd=0,bg=bg,fg=fg,width=3,font=self.font_style,command=self._maximize_win)
            self._maximize_btn.pack(side=RIGHT,fill=Y)
            self._minimize_btn = Button(self._title_bar,text="_",bd=0,bg=bg,fg=fg,width=3,font=self.font_style,command=self._minimize)
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

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x500+100+90")
    titleBar = CreateModernTitlebar(root,title_text = 'Hello,World!' , bg = "dark blue" , fg = 'white')
    titleBar.resizeable = True
    titleBar.packBar()
    root.mainloop()