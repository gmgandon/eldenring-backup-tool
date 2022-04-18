
from difflib import restore
from importlib.resources import path
from logging import exception
from ntpath import join
from optparse import Values
import sys
import tkinter as tk
from tkinter import *
import time
import os
import shutil
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from os import listdir, path
from turtle import update




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
        initialfile= 'ER0000',
        filetypes=filetypes
    )


    origin_box.delete(0, END)
    origin_box.insert(0, filename)

def backup_file():
    filename = asksaveasfilename(
        filetypes = [('Elden Ring save files','*.sl2')],
        defaultextension='.sl2',
        title='Select backup file',
        initialdir= destinationdir(),
        initialfile= 'ER0000'
    )

    
    destination_box.delete(0, END)
    destination_box.insert(0, filename)

def pathCheck(origin, destination):
    if origin == '' or destination == '':
        return False
    else: 
        return True
        


def nameCheck(description, destination):
    if description != '':
        return(destination[:-4])+" "+(description_box.get())+(destination[-4:])
    else:
        return(destination[:-4])+ " " + (time.asctime().replace(":", "-"))+(destination[-4:])

def backupSaveFile():
    origin = origin_box.get()
    destination = destination_box.get()
    description = description_box.get()
    actualdestination = nameCheck(description, destination)

    if pathCheck(origin,destination):
        print(origin, actualdestination)
        print (description_box.get())
        boton_label.config(text= 'Done!')
        with open ('settings.txt', "w") as settings:
            settings.write(f"{origin}\n{destination}\n")
    else:
        boton_label.config(text= 'Check your settings!')

def restoreSaveFile():
    origin = origin_box.get()
    destination = destination_box.get()
    description = ''
    actualdestination = nameCheck(description, destination)

    if pathCheck(origin,destination):
        print(origin, actualdestination)
        print (description_box.get())
        boton_label.config(text= 'Done!')
        with open ('settings.txt', "w") as settings:
            settings.write(f"{origin}\n{destination}\n")
    else:
        boton_label.config(text= 'Check your settings!')

    print(destination, f"{destination}/{combo.get()}")


def updateComboList(combo):
    folder = (destinationdir().split('/'))
    realfolder = '/'.join(folder[:-1])
    listedfiles = os.listdir(realfolder)
    combo['value'] = tuple(listedfiles)


    
    


#path info
currentpath= (os.path.dirname(sys.argv[0]))
settingsfile= currentpath+'\settings.txt'
defaultpath = (os.path.expanduser('~')) + '\Appdata\Roaming\EldenRing'

#set window
root= tk.Tk()
root.title("Elden Ring Backup tool")
root.iconbitmap(currentpath+'\icon.ico')
root.resizable(False, False)

#set notebook
tabcontrol = ttk.Notebook(root, height=200, width=300)

#set tabs
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tab3 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text='Back up')
tabcontrol.add(tab2, text='Settings')
tabcontrol.add(tab3, text='Restore')
tabcontrol.pack(expand=1, fill="both")




#description
description_label= tk.Label(tab1, text='Description:')
description_label.place(x=20, y=10)

description_box= ttk.Entry(tab1)
description_box.place(x=20, y=40, width=200)

#boton
boton_label = tk.Label(tab1, text=' ')
boton_label.place(x=117, y= 130)

boton = ttk.Button(tab1, text="Backup now", command=backupSaveFile)
boton.place(x= 100, y= 100)

#origin
origin_label= tk.Label(tab2, text='Save file:')
origin_label.place(x=20, y=10)

origin_box= ttk.Entry(tab2)
origin_box.place(x=20, y=40, width=200)
origin_box.insert(0, origindir())

botonorigin = ttk.Button(tab2, text="...", command=save_file)
botonorigin.place(x= 250, y= 38, width=25)

#destino
destination_label = tk.Label(tab2, text='backup location')
destination_label.place(x=20, y=70)

destination_box= ttk.Entry(tab2)
destination_box.place(x=20, y=90, width=200)
destination_box.insert(0, destinationdir())

botondestination = ttk.Button(tab2, text="...", command=backup_file)
botondestination.place(x= 250, y= 88, width=25)

botonsave = ttk.Button(tab2, text='Save settings', command=savesettings)
botonsave.place(x=100, y=150, width=80)

#set file selection
selected_file = tk.StringVar()
selected_file.set('Select a save to restore')
combo = ttk.Combobox(tab3, width=100, height=150, state='readonly', textvariable= selected_file)
combo.place(x=20, y=40, width=200)
try:
    updateComboList(combo)
except:
    pass
restorebutton = ttk.Button(tab3, text= 'Restore this save', command= restoreSaveFile)
restorebutton.place(x= 90, y= 100)

restore_label = tk.Label(tab3, text=' ')
restore_label.place(x=117, y= 130)





root.mainloop()