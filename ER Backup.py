


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

currentpath= (os.path.dirname(sys.argv[0]))
settingsfile= currentpath+'\settings.txt'
defaultpath = (os.path.expanduser('~')) + '\Appdata\Roaming\EldenRing'


#backuppath = r"D:\Juegos\ER backup\ER0000" + (time.asctime().replace(":", "-")) + ".sl2"



#shutil.copy(r"C:\Users\Guido\AppData\Roaming\EldenRing\76561198102024189\ER0000.sl2", backuppath)

#exit()

#directory settings:
if path.exists(settingsfile) == False:
    with open (settingsfile, "w") as settings:
        settings.write('\n\n')
        erpath = ''
        destpath = ''
else:
    with open (settingsfile, 'r') as settings:
        data= settings.readlines()
        erpath = data[0].replace('\n','')
        destpath = data[1].replace('\n','')

    

#datos de la ventana
root= tk.Tk()
root.title("Elden Ring Backup tool")
root.config(width=300, height=250)
root.resizable(False , False)
root.option_add('*tearOff', False)



def getfilename():
    defaultname= 'ER0000'
    description = description_box.get()

    if description != '' :
        return defaultname + description
    else:
        return defaultname + (time.asctime().replace(":", "-"))

def setts():
    settingswindow = Toplevel()
    settingswindow.title('Settings')
    settingswindow.geometry('300x200')
    pass
    
def origindir():
    if erpath == '':
        return defaultpath
    else:
        return erpath

def destinationdir():
    if destpath == '':
        return '/'
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
    #destination = f'{destination_box.get()[:-4]}{getfilename()}{destination_box.get()[-4::]}'
    destination = destination_box.get()
    print(origin, destination)
    boton_label.config(text= 'Done!')
    with open (settingsfile, "w") as settings:
        settings.write(f"{origin}\n{destination_box.get()}\n")



#menu
menubar = Menu(root)
root.config(menu=menubar)

#add items to the menu
menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
#add dropdown items
menu_file.add_command(label='Settings...', command=setts)
menu_file.add_separator()
#menubar.add_cascade(menu=menu_edit, label='Edit')


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
origin_box.insert(0, origindir())

botonorigin = ttk.Button(text="...", command=save_file)
botonorigin.place(x= 250, y= 98, width=25)


#destino
destination_label = tk.Label(text='backup location')
destination_label.place(x=20, y=130)

destination_box= ttk.Entry()
destination_box.place(x=20, y=160, width=200)
destination_box.insert(0, destinationdir())

botondestination = ttk.Button(text="...", command=backup_file)
botondestination.place(x= 250, y= 158, width=25)


#boton
boton_label = tk.Label(text=' ')
boton_label.place(x=117, y= 230)

boton = ttk.Button(text="Backup now", command=backupSaveFile)
boton.place(x= 100, y= 200)









root.mainloop()