import pyautogui

class AutoMate:
    def __init__(self, query, speak=None) -> None:
        self.query = query
        self.status = True

        if 'wi-fi' in self.query:
            pyautogui.click(x=1680, y=1100)

        elif 'messages' in self.query or 'show menu bar' in self.query:
            pyautogui.hotkey("win","a")

        elif 'type' in self.query or 'write' in self.query:
            sb = self.query.replace('type', '', 1)
            sb = self.query.replace('write', '', 1)
            sb = self.query.replace('gravy', '', 1)
            sb = self.query.replace('gravia', '', 1)
            sb = self.query.replace('ok', '', 1)
            sb = self.query.replace('hey', '', 1)
            pyautogui.write(sb)

        elif 'open start' in self.query:
            pyautogui.press("win")

        elif 'press enter' in self.query:
            pyautogui.press("enter")
        
        else:
            if 'spacebar' in self.query:
                pyautogui.press("space")

            elif 'next page' in self.query or "page down" in self.query:
                pyautogui.press("pagedown")

            elif 'previous page' in self.query or "page up" in self.query:
                pyautogui.press("pageup")

            elif 'open search' in self.query:
                pyautogui.hotkey("ctrl", "f")

            elif 'rotate ' in self.query and 'left' in self.query:
                pyautogui.hotkey("ctrl", "alt", "left")
                speak("Done")
            elif 'rotate ' in self.query and 'right' in self.query:
                pyautogui.hotkey("ctrl", "alt", "right")
            elif 'rotate ' in self.query and 'down' in self.query or 'bottom' in self.query:
                pyautogui.hotkey("ctrl", "alt", "down")
            elif 'rotate screen to top side' in self.query or 'rotate screen to up side' in self.query or 'rotate screen to normal' in self.query:
                pyautogui.hotkey("ctrl", "alt", "up")

            elif 'open task view' in self.query or 'start task view' in self.query or 'show task view' in self.query:
                pyautogui.click(x=462, y=741)   

            elif 'volume up' in self.query:
                print("Volume Uped")
                pyautogui.press("volumeup")
            elif 'volume down' in self.query:
                pyautogui.press("volumedown")

            elif 'mute' in self.query:
                pyautogui.press("volumemute")

            elif 'show options' in self.query or 'right click options' in self.query:
                pyautogui.press("apps")
            else:
                if 'browse back' in self.query or 'brouse back' in self.query:
                    pyautogui.press("browseback")
                elif 'browser forward' in self.query or 'brouse forward'in self.query:
                    pyautogui.press("browserforward")
                elif 'refresh' in self.query:
                    pyautogui.press("browserrefresh")
                elif 'home' in self.query:
                    pyautogui.press("browserhome")
                else:
                    if 'bookmark' in self.query:
                        pyautogui.press("browserfavorites")     
                    else:
                        self.status = False

if __name__ == '__main__':
    a = AutoMate("wsdsdd", speak=lambda q:print(q), takeCommand="Yo")
    print(a.status)