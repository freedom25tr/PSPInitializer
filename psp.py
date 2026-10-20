import tkinter as guipsp
from tkinter import filedialog
from pathlib import Path as pathpsp
#merhaba muharrem hocam
window = guipsp.Tk() #tuff
başlık="PSP Memory Stick Initializer"
window.title(başlık)
window.geometry("300x150")

sts123=guipsp.Label(window, text="Ready-Choose your MiniSD/Memory Stick")
sts123.pack(pady=10)

def ne_yazıcagimi_bilemedim():
    file123=filedialog.askdirectory()
    if isinstance(file123, str) and len(file123) > 0:
        psp=pathpsp(file123) / "PSP"
        psp.mkdir(exist_ok=True)
        fileslop=["GAME", "SAVEDATA", "PHOTO", "MUSIC", "VIDEO" , "SEPLUGINS" , "ISO" , "THEME"]
        for file in fileslop:
            (psp / file).mkdir(exist_ok=True)
        sts123.config(text="PSP folders created successfully.")
    else:
        sts123.config(text="Cancelled.") #hi to whoever reading this

button=guipsp.Button(window, text="Choose Memory Stick", command=ne_yazıcagimi_bilemedim)
button.pack(pady=10)

ragequit=guipsp.Button(window,text="Quit" , command=window.destroy)
ragequit.pack()

window.mainloop()
