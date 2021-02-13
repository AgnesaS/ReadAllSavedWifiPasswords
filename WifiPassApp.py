from tkinter import *
import tkinter as tk
import pyperclip
import re
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

#krijimi i root dritares 
root = tk.Tk()
root.geometry("900x900") #dimensionet e dritares
pass_details = StringVar()
myList = []
strength= []
data = []

#Vendosja dhe pershtatja e nje logoje ne background
bg = PhotoImage(file="logo.png")
my_label=Label(root,image=bg)
my_label.place(x=0,y=0 ,  relwidth=1, relheight=1)

#funksioni per gjetjen e wifi-ve dhe fjalekalimeve perkatese
def see_wifi_pass():
    import subprocess
    global myList
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n') #komanda per gjetjen e profileve(wifi-ve)
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    myList.append("------------------------")
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n') #komanda per gjetjen e fjalekalimeve
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            if not re.search('[A-Z]', results[0]) or not re.search('[a-z]', results[0]) or not re.search('[0-9]', results[0]): #kondita per kriteret e kompleksitetit te fjalekalimit
                myList.append("Wifi-->" + i)
                # myList.append("--")
                myList.append("Password-->" +results[0]+"| Weak")
                myList.append("------------------------")
            else:
                myList.append("Wifi-->" + i)

                myList.append("Password-->" +results[0]+"| Strong")
                myList.append("------------------------")
        except IndexError:
            myList.append("Wifi-->" +i)
           
            myList.append("")

#funksioni per shnderrimin ne str te variables myList e cila permbane ciftin wifi-fjalekalim
def show_wifi_pass():
    def listToString(s):
        # inicializimi i nje stringu bosh
        myStr = ""

        # iterimi neper string
        for ele in s:
            myStr = myStr +  ele + "\n"

            # kthimi i stringut
        return myStr
    myStr = listToString(myList)
    pass_details.set(myStr)

#funksioni per kopjimin e fjalekalimeve
def copytoclipboard():
    password = pass_details.get()
    pyperclip.copy(password)

#funksioni per shnderrimin ne str te te variables strength e cila permbane kompleksitetin e fjalekalimeve
def show_strength():
    def listToString(s):
       # inicializimi i nje stringu bosh
        mystr = ""

      # iterimi neper string
        for ele in s:
            mystr = mystr +  ele + "\n"

       # kthimi i stringut
        return mystr
    mystr = listToString(strength)
    strength_details.set(mystr)

#funksioni per krijimin e grafit
def graph():
    strength1 = strength_details.get()
    strength2= strength1.split()
    for i in strength2:
        if i=='Weak':
            data.append(20)
        elif i=='Strong':
            data.append(60)
    plt.bar([1,2,3,4], data)
    plt.show()
    
Label(root, text="Get Your Saved Wifi Passwords", bg="white",font= "Helvetica 20" ).place(x = 270,y = 200)
Button(root, text="Initiate Process Now",bg="lightblue",width='20' ,height='1',font="Raleway",command=see_wifi_pass).place(x = 382, y = 282)
Button(root, text="Show all saved wifi passwords",width='25' ,height='1',font="Raleway", bg="lightblue",command=show_wifi_pass).place(x = 360, y = 330)
Entry(root, textvariable=pass_details , bg="light steel blue").place(width=600, height=80, x = 180, y = 370)
Button(root, text="Copy to clipbord",bg="lightblue",width='20' ,height='1',font="Raleway",command=copytoclipboard).place(x = 590, y = 460)
Button(root, text="Show graph",bg="lightblue",width='20' ,height='1',font="Raleway",command=graph).place(x = 590, y = 500)


root.mainloop()
