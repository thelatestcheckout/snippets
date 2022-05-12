from datetime import datetime
import time
from webbrowser import open
import os
from pyautogui import(click, hotkey, typewrite, press, moveTo, locateOnScreen)


def _web(phone_number):
    open("https://web.whatsapp.com/send?phone=" +
         phone_number + "&text=")


def send_message(message, phone_number, wait_time):
    _web(phone_number)
    time.sleep(7)
    time.sleep(wait_time - 7)
    for char in message:
        if char == "\n":
            hotkey("shift", "enter")
        else:
            typewrite(char)
    press("enter")
    time.sleep(5)
    hotkey("command", "w")


def sendwhatsappmessage(phone_number, message, time_hour, time_minutes, wait_time):
    print("Enter")
    current_time = time.localtime()
    time_left = datetime.strptime(f"{time_hour}:{time_minutes}:0", "%H:%M:%S") - datetime.strptime(f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
                                                                                                   "%H:%M:%S")
    sleep_time = time_left.seconds - wait_time
    print("Whatsapp scheduler started")
    time.sleep(sleep_time)
    send_message(message, phone_number, wait_time)
    print("Whatsapp scheduler ended")


phone_number = "+91xxxxxx"
message = "Good morning."
time_hour = 1
time_minutes = 32
wait_time = 10
sendwhatsappmessage(phone_number, message, time_hour,
                    time_minutes, wait_time)
