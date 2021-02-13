from tkinter import *
import tkinter as tk
import pyperclip
import re
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("900x900")
pass_details = StringVar()
myList = []
strength= []
data = []


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

def show_wifi_pass():
    def listToString(s):
        # initialize an empty string
        myStr = ""

        # traverse in the string
        for ele in s:
            myStr = myStr +  ele + "\n"

            # return string
        return myStr
    myStr = listToString(myList)
    pass_details.set(myStr)


def copytoclipboard():
    password = pass_details.get()
    pyperclip.copy(password)
    
    def show_strength():
    def listToString(s):
        # initialize an empty string
        mystr = ""

        # traverse in the string
        for ele in s:
            mystr = mystr +  ele + "\n"

            # return string
        return mystr
    mystr = listToString(strength)
    strength_details.set(mystr)
    
Label(root, text="Get Your Saved Wifi Passwords", bg="white",font= "Helvetica 20" ).place(x = 270,y = 200)
Button(root, text="Initiate Process Now",bg="lightblue",width='20' ,height='1',font="Raleway",command=see_wifi_pass).place(x = 382, y = 282)
Button(root, text="Show all saved wifi passwords",width='25' ,height='1',font="Raleway", bg="lightblue",command=show_wifi_pass).place(x = 360, y = 330)
Entry(root, textvariable=pass_details , bg="light steel blue").place(width=600, height=80, x = 180, y = 370)
Button(root, text="Copy to clipbord",bg="lightblue",width='20' ,height='1',font="Raleway",command=copytoclipboard).place(x = 590, y = 460)

root.mainloop()
