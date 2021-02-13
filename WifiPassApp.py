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
