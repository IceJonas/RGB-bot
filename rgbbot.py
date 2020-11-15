from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Cords
y1 = 1170
x1 = 775
x2 = 925
x3 = 1080
x4 = 1240

# Click fallið sem fær inn staðsetninguna á pixelinum frá while
# lykkjunni og ýtir á músina.
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
# Takkinn q er notaður til að slökkva á forritinu
# Bæta við if setningum til að bæta við fleirrum pixelum
# Hér er bara skoðað fyrir R ekki fyrir G B

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(x1,y1)[0] == 0:
        click(x1,y1)
    if pyautogui.pixel(x2,y1)[0] == 0:
        click(x2,y1)
    if pyautogui.pixel(x3,y1)[0] == 0:
        click(x3,y1)
    if pyautogui.pixel(x4,y1)[0] == 0:
        click(x4,y1)
