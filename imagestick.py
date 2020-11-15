from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(150,900,1550,1100))
    width, height = pic.size

    for x in range(0,width,15):
        for y in range(0,height,15):

            r,g,b = pic.getpixel((x,y))
            
            if b == 195:
                click(x+150,y+900)
                time.sleep(0.05)
                break
