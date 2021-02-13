from tkinter import *
import tkinter as tk
import pyperclip
import re
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("900x900")
canvas = tk.Canvas(root, width=900, height=900)
canvas.grid(columnspan=3, rowspan=3)
pass_details = StringVar()
myList = []



bg = PhotoImage(file="logo.png")
my_label=Label(root,image=bg)
my_label.place(x=0,y=0 ,  relwidth=1, relheight=1)

def see_wifi_pass():
    import subprocess
    global myList
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    myList.append("------------------------")
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            if not re.search('[A-Z]', results[0]) or not re.search('[a-z]', results[0]) or not re.search('[0-9]', results[0]):
                myList.append("Wifi-->" + i)
                # myList.append("--")
                myList.append("Password-->" +results[0]+"| Weak")
                myList.append("------------------------")
            else:
                myList.append("Wifi-->" + i)
                # myList.append("--")
                myList.append("Password-->" +results[0]+"| Strong")
                myList.append("------------------------")
        except IndexError:
            myList.append("Wifi-->" +i)
            # myList.append("--")
            myList.append("")
