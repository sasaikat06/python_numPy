import pyautogui
import time


for i in range(1,100):
    time.sleep(0.5)
    pyautogui.typewrite("Hello, Whats Up!!!")

    time.sleep(1)
    pyautogui.press('enter')
    
