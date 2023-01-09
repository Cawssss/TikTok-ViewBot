import pyautogui
import time
import os
import requests
import pyperclip
import pyautogui

lien = input(https://www.tiktok.com/@the_nml/video/7186470103289056555?is_from_webapp=1&sender_device=pc&web_id=7186469709465224746)

for i in range (200):

    os.system("start tiktok")
    time.sleep(1)
    pyperclip.copy(f"{lien}")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(300)
    os.system("taskkill /IM tiktok.exe")
