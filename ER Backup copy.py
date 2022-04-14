


from importlib.resources import path
import sys
import tkinter as tk
from tkinter import *
import time
import os
import shutil
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from os import path




#backuppath = r"D:\Juegos\ER backup\ER0000" + (time.asctime().replace(":", "-")) + ".sl2"



#shutil.copy(r"C:\Users\Guido\AppData\Roaming\EldenRing\76561198102024189\ER0000.sl2", backuppath)

#exit()

#directory settings:
if path.exists('settings.txt') == False:
    with open ("settings.txt", "w") as settings:
        settings.write('\n\n')
        erpath = ''
        destpath = ''
else:
    with open ('settings.txt', 'r') as settings:
        data= settings.readlines()
        erpath = data[0].replace('\n','')
        destpath = data[1].replace('\n','')

def savesettings():
    origin = origin_box.get()
    destination = destination_box.get()
    print(origin, destination)
    with open ('settings.txt', "w") as settings:
        settings.write(f"{origin}\n{destination}\n")
    



#datos de settings




def getfilename():
    defaultname= 'ER0000'
    description = description_box.get()

    if description != '' :
        return defaultname + description
    else:
        return defaultname + (time.asctime().replace(":", "-"))

def setts():
    global destination_box, origin_box

    settingswindow = Toplevel()
    settingswindow.title('Settings')
    settingswindow.geometry('300x200')

    #box y boton origen
    origin_label= tk.Label(settingswindow, text='Save file:')
    origin_label.place(x=20, y=10)

    origin_box= ttk.Entry(settingswindow)
    origin_box.place(x=20, y=40, width=200)
    origin_box.insert(0, origindir())

    botonorigin = ttk.Button(settingswindow, text="...", command=save_file)
    botonorigin.place(x= 250, y= 38, width=25)


    #destino
    destination_label = tk.Label(settingswindow, text='backup location')
    destination_label.place(x=20, y=70)

    destination_box= ttk.Entry(settingswindow)
    destination_box.place(x=20, y=90, width=200)
    destination_box.insert(0, destinationdir())

    botondestination = ttk.Button(settingswindow, text="...", command=backup_file)
    botondestination.place(x= 250, y= 88, width=25)

    botonsave = ttk.Button(settingswindow, text='Save settings', command=savesettings)
    botonsave.place(x=180, y=150, width=50)

    
def origindir():
    if erpath == '':
        return defaultpath
    else:
        return erpath

def destinationdir():
    if destpath == '':
        return ''
    else:
        return destpath


def save_file():
    filetypes = [('Elden Ring save files','*.sl2')]

    filename = askopenfilename(
        title='Select save file',
        initialdir=origindir(),
        filetypes=filetypes
    )

    showinfo(
        title='Selected file',
        message=filename
    )
    origin_box.delete(0, END)
    origin_box.insert(0, filename)

def backup_file():
    filename = asksaveasfilename(
        filetypes = [('Elden Ring save files','*.sl2')],
        defaultextension='.sl2',
        title='Select backup file',
        initialdir= destinationdir(),
        initialfile= getfilename()
    )

    showinfo(
        title='Selected file',
        message=filename
    )    
    destination_box.delete(0, END)
    destination_box.insert(0, filename)

def backupSaveFile():
    origin = origin_box.get()
    destination = destination_box.get()
    print(origin, destination)
    boton_label.config(text= 'Done!')
    with open ('settings.txt', "w") as settings:
        settings.write(f"{origin}\n{destination}\n")


#path info
currentpath= (os.path.dirname(sys.argv[0]))
settingsfile= currentpath+'\settings.txt'
defaultpath = (os.path.expanduser('~')) + '\Appdata\Roaming\EldenRing'

#datos de la ventana
root= tk.Tk()
root.title("Elden Ring Backup tool")
root.config(width=300, height=250)
root.resizable(False , False)
root.option_add('*tearOff', False)

#menu
menubar = Menu(root)
root.config(menu=menubar)

#add items to the menu
menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
#add dropdown items
menu_file.add_command(label='Settings...', command=setts)
menu_file.add_separator()



#description
description_label= tk.Label(text='Description:')
description_label.place(x=20, y=10)

description_box= ttk.Entry()
description_box.place(x=20, y=40, width=200)


    


#boton
boton_label = tk.Label(text=' ')
boton_label.place(x=117, y= 230)

boton = ttk.Button(text="Backup now", command=backupSaveFile)
boton.place(x= 100, y= 200)









root.mainloop()