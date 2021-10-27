# -*- coding: utf-8 -*-
#!/usr/bin/python3

import tkinter as tk
from tkinter import font as tkfont

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

font_1_1 = tkfont.Font(family="Verdana", size=48, weight="bold")
font_1_2 = tkfont.Font(family="Arial", size=64, weight="bold")

root.wm_title("PCPH  HUB")
root.geometry("800x480")
root.minsize(600, 400)
root.configure(bg="#3838B8")
root.attributes("-fullscreen", True)


frame_1 = tk.Frame(root, bg="#3838B8")
frame_1.pack(fill="both", expand=True)

name_1 = tk.StringVar()

label_1 = tk.Label(frame_1, text="Enter your PIN",
                font=font_1_1,
                fg="#B8B838",
                bg="#3838B8")
label_1.place(relx=0.5, rely=0.25, anchor="c")

entry_1 = tk.Entry(frame_1, textvariable=name_1,
                font=font_1_2,
                width=4,
                bg="#B8B8F8")
entry_1.place(relx=0.5, rely=0.5, anchor="c")
entry_1.focus_set()
entry_1.bind("<Return>", to_nextscreen)


frame_2 = tk.Frame(root, bg="#3838B8")

label_2 = tk.Label(frame_2, text="Second Window",
                   font="Verdana 48 bold",
                   fg="#B8B838",
                   bg="#3838B8")
label_2.place(relx=0.5, rely=0.25, anchor="c")


root.bind("<Shift-Up>", switch_to_fullscreen)
root.bind("<Shift-Down>", switch_from_fullscreen)
root.bind("<Escape>", to_firstscreen)

root.mainloop()
