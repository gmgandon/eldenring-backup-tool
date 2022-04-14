from cProfile import label
from cgitb import text
from msilib.schema import Icon
from operator import truediv
import time
import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog as fd
from tkinter.messagebox import showinfo


defaultpath = (os.path.expanduser('~')) + '\Appdata\Roaming\EldenRing'

#backuppath = r"D:\Juegos\ER backup\ER0000" + (time.asctime().replace(":", "-")) + ".sl2"



#shutil.copy(r"C:\Users\Guido\AppData\Roaming\EldenRing\76561198102024189\ER0000.sl2", backuppath)

#exit()

#datos de la ventana
main_window= tk.Tk()
main_window.title("Elden Ring Backup tool")
main_window.config(width=300, height=250)
main_window.resizable(False , False)


def getfilename():
    deftaultname= 'ER0000'
    description = description_box.get()

    if description != '' :
        return description
    else:
        return deftaultname + (time.asctime().replace(":", "-"))

def save_file():
    filetypes = [('Elden Ring save files','*.sl2')]

    filename = fd.askopenfilename(
        title='Select save file',
        initialdir=defaultpath,
        filetypes=filetypes
    )

    showinfo(
        title='Selected file',
        message=filename
    )
    origin_box.insert(0, filename)

def backup_file():
    filename = fd.asksaveasfilename(
        filetypes = [('Elden Ring save files','*.sl2')],
        defaultextension='.sl2',
        title='Select backup file',
        initialdir= '/',
        initialfile= getfilename()

    )

    showinfo(
        title='Selected file',
        message=filename
    )    
    destination_box.insert(0, filename)

def backupSaveFile():
    origin = origin_box.get()
    destination = destination_box.get()
    shutil.copy(origin, destination)
    boton_label.config(text= 'Done!')



#description
description_label= tk.Label(text='Description:')
description_label.place(x=20, y=10)

description_box= ttk.Entry()
description_box.place(x=20, y=40, width=200)


#box y boton origen
origin_label= tk.Label(text='Save file:')
origin_label.place(x=20, y=70)

origin_box= ttk.Entry()
origin_box.place(x=20, y=100, width=200)

botonorigin = ttk.Button(text="...", command=save_file)
botonorigin.place(x= 250, y= 98, width=25)



#destino
destination_label = tk.Label(text='backup location')
destination_label.place(x=20, y=130)

destination_box= ttk.Entry()
destination_box.place(x=20, y=160, width=200)

botondestination = ttk.Button(text="...", command=backup_file)
botondestination.place(x= 250, y= 158, width=25)

#boton
boton_label = tk.Label(text=' ')
boton_label.place(x=117, y= 230)

boton = ttk.Button(text="Backup now", command=backupSaveFile)
boton.place(x= 100, y= 200)









main_window.mainloop()