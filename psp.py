import tkinter as guipsp
from tkinter import filedialog
from tkinter import messagebox as mesajverici
from pathlib import Path as pathpsp
import shutil as selam
file123 = ""
window = guipsp.Tk() #tuff
başlık="PSP Memory Stick Initializer"
window.title(başlık)
window.geometry("300x250")

sts123=guipsp.Label(window, text="Ready-Choose your MiniSD/Memory Stick")
sts123.pack(pady=10)

def ne_yazıcagimi_bilemedim():
    global file123
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


#buton1
button=guipsp.Button(window, text="Choose Memory Stick", command=ne_yazıcagimi_bilemedim)
button.pack(pady=10)
#buton2
ragequit=guipsp.Button(window,text="Quit" , command=window.destroy)
ragequit.pack()

def diskbilgileri():
    bilgi=selam.disk_usage(file123)
    mesajverici.showinfo(
    "Disk Information",
    f"Total: {bilgi.total / 1024**3:.2f} GB\n"
    f"Used : {bilgi.used  / 1024**3:.2f} GB\n"
    f"Free: {bilgi.free   / 1024**3:.2f} GB\n"
    #2f'ledim çok büyük depolamalarda sıkıntı çıkabiliyor'
    )


diskbilgisi=guipsp.Button(window,text="Disk Info" , command=diskbilgileri)
diskbilgisi.pack()





window.mainloop()
