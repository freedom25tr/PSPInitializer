import tkinter as guipsp
from tkinter import filedialog
from pathlib import Path as pathpsp

window = guipsp.Tk() #tuff
title123="PSP Memory Stick Initializer"
window.title(title123)
window.geometry("300x150")

sts123=guipsp.Label(window, text="Ready-Choose your MiniSD/Memory Stick")
sts123.pack(pady=10)

def pspchoose123():
    global file123, psp
    file123=filedialog.askdirectory()
    if isinstance(file123, str) and len(file123) > 0:
        psp = pathpsp(file123) / "PSP"
        psp.mkdir(exist_ok=True)
        fileslop=["GAME", "SAVEDATA", "PHOTO", "MUSIC", "VIDEO" , "SEPLUGINS" , "ISO" , "THEME"]
        for file in fileslop:
            (psp / file).mkdir(exist_ok=True)
        sts123.config(text="PSP folders created successfully.")
    else:
        sts123.config(text="Cancelled.") #hi to whoever reading this

button = guipsp.Button(window, text="Choose Memory Stick", command=pspchoose123)
button.pack(pady=10)

ragequit = guipsp.Button(window,text="Quit" , command=window.destroy)
ragequit.pack()

window.mainloop()
