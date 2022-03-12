import pyautogui
import time
import os
import requests
import pyperclip
import pyautogui

lien = input("Link of your tiktok video : ")

for i in range (200):

    os.system("start tiktok")
    time.sleep(1)
    pyperclip.copy(f"{lien}")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(300)
    os.system("taskkill /IM tiktok.exe")
