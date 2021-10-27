# -*- coding: utf-8 -*-
#!/usr/bin/python3

import time
import tkinter as tk
from tkinter import font as tkfont


class Node:
    def __init__(self, num=0):
        self.__num = num
        self.__power_applied = False

    def get_num(self):
        return self.__num

    def get_power_applied(self):
        return self.__power_applied

    def set_power_applied(self, power):
        self.__power_applied = power


node = Node()


def switch_to_fullscreen(event):
    root.attributes("-fullscreen", True)

def switch_from_fullscreen(event):
    root.attributes("-fullscreen", False)

def to_nextscreen(event):
    if len(name_1.get()) > 3:
        name_1.set("")
        frame_1.pack_forget()
        frame_2.pack(fill="both", expand=True)
        # root.attributes("-fullscreen", True)

def to_firstscreen(event):
    frame_2.pack_forget()
    frame_1.pack(fill="both", expand=True)
    # root.attributes("-fullscreen", True)


root = tk.Tk()

root.wm_title("PCPH  HUB")
root.geometry("800x600")
root.minsize(800, 600)
root.configure(bg="#3838B8")
root.attributes("-fullscreen", True)

color_front = "#B8B838"
color_back = "#3838B8"
color_entry_back = "#B8B8F8"

frame_1 = tk.Frame(root, bg=color_back)
frame_1.pack(fill="both", expand=True)

name_1 = tk.StringVar()

font_1_1 = tkfont.Font(family="Verdana", size=48, weight="bold")
font_1_2 = tkfont.Font(family="Arial", size=64, weight="bold")

label_1 = tk.Label(frame_1, text="Enter your PIN",
                font=font_1_1,
                fg=color_front,
                bg=color_back)
label_1.place(relx=0.5, rely=0.25, anchor="c")

entry_1 = tk.Entry(frame_1, textvariable=name_1,
                font=font_1_2,
                width=4,
                bg=color_entry_back)
entry_1.place(relx=0.5, rely=0.5, anchor="c")
entry_1.focus_set()
entry_1.bind("<Return>", to_nextscreen)


frame_2 = tk.Frame(root, bg=color_back)

name_2_1 = tk.StringVar()
name_2_2 = tk.StringVar()
name_2_3_1 = tk.StringVar(value="HH")
name_2_3_2 = tk.StringVar(value="MM")
name_2_3_3 = tk.StringVar(value="SS")
name_2_4_1 = tk.StringVar(value="HH")
name_2_4_2 = tk.StringVar(value="MM")
name_2_4_3 = tk.StringVar(value="SS")

label_2_0 = tk.Label(frame_2,
                     font=("Verdana", 48),
                     fg=color_front,
                     bg=color_back,
                     bd=10)
label_2_0.place(relx=0.975, rely=0.025, anchor= 'ne')

def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label_2_0.config(text=text_input)
    label_2_0.after(100, digitalclock)

digitalclock()

label_2_1 = tk.Label(frame_2,
                     text="Power Hub #",
                     font="Verdana 24",
                     fg=color_front,
                     bg=color_back)
label_2_1.place(relx=0.35, rely=0.3, anchor='s')

entry_2_1 = tk.Entry(frame_2,
                     textvariable=name_2_1,
                     font=tkfont.Font(family="Verdana", size=32, weight="bold"),
                     width=2,
                     bg=color_entry_back)
entry_2_1.place(relx=0.35, rely=0.3, anchor='n')

label_2_2 = tk.Label(frame_2,
                     text="AMP Max",
                     font="Verdana 24",
                     fg=color_front,
                     bg=color_back)
label_2_2.place(relx=0.65, rely=0.3, anchor='s')

entry_2_2 = tk.Entry(frame_2,
                     textvariable=name_2_2,
                     font=tkfont.Font(family="Verdana", size=32, weight="bold"),
                     width=2,
                     bg=color_entry_back)
entry_2_2.place(relx=0.65, rely=0.3, anchor='n')

label_2_5 = tk.Label(frame_2,
                     text="Power is OFF",
                     font="Verdana 24",
                     fg=color_front,
                     bg=color_back)
label_2_5.place(relx=0.5, rely=0.5, anchor='s')

def power_button():
    pass

button_2_1 = tk.Button(frame_2,
                       text="Push to ON",
                       font="Verdana 32",
                       bg="Green",
                       fg="Magenta",
                       command=power_button)
button_2_1.place(relx=0.5, rely=0.5, anchor='n')

labelframe_2 = tk.LabelFrame(frame_2,
                             bg=color_back,
                             fg=color_front,
                             height=160,
                             width=650,
                             bd=4,
                             font="Verdana 24",
                             text="OR Set Up Timer")
labelframe_2.place(relx=0.5, rely=0.7, anchor='n')

label_2_3 = tk.Label(labelframe_2,
                     bg=color_back,
                     fg=color_front,
                     font="Verdana 16",
                     text="Set Time")
label_2_3.place(relx=0.25, rely=0.25, anchor='c')

entry_2_3_1 = tk.Entry(labelframe_2,
                       width=2,
                       textvariable=name_2_3_1,
                       font="Courier 32",
                       bg=color_entry_back)
entry_2_3_1.place(relx=0.1, rely=0.65, anchor='c')

entry_2_3_2 = tk.Entry(labelframe_2,
                       width=2,
                       textvariable=name_2_3_2,
                       font="Courier 32",
                       bg=color_entry_back)
entry_2_3_2.place(relx=0.25, rely=0.65, anchor='c')

entry_2_3_3 = tk.Entry(labelframe_2,
                       width=2,
                       textvariable=name_2_3_3,
                       font="Courier 32",
                       bg=color_entry_back)
entry_2_3_3.place(relx=0.4, rely=0.65, anchor='c')

label_2_4 = tk.Label(labelframe_2,
                     bg=color_back,
                     fg=color_front,
                     font="Verdana 16",
                     text="Countdown")
label_2_4.place(relx=0.75, rely=0.25, anchor='c')

entry_2_4_1 = tk.Entry(labelframe_2,
                       width=2,
                       textvariable=name_2_4_1,
                       font="Courier 32",
                       bg=color_entry_back)
entry_2_4_1.place(relx=0.6, rely=0.65, anchor='c')

entry_2_4_2 = tk.Entry(labelframe_2,
                       width=2,
                       textvariable=name_2_4_2,
                       font="Courier 32",
                       bg=color_entry_back)
entry_2_4_2.place(relx=0.75, rely=0.65, anchor='c')

entry_2_4_3 = tk.Entry(labelframe_2,
                       width=2,
                       textvariable=name_2_4_3,
                       font="Courier 32",
                       bg=color_entry_back)
entry_2_4_3.place(relx=0.9, rely=0.65, anchor='c')


root.bind("<Shift-Up>", switch_to_fullscreen)
root.bind("<Shift-Down>", switch_from_fullscreen)
root.bind("<Escape>", to_firstscreen)

root.mainloop()
