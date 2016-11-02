from tkinter import *
from NSapi import *

def toonVenster2():
    root = Tk()
    root.geometry('790x650')
    root.resizable(width=False, height=False)
    root.title('Reisinformatie Ander Station')
    root.configure(background='#01236a')
    root.columnconfigure(0,minsize=790)
    root.rowconfigure(2,minsize=550)
    #dropdownmenuopties
    OPTIONS = [
    "Utrecht",
    "Den Bosch",
    "Amsterdam Centraal"
    ]
    #dropdownmenu
    variable = StringVar(root)
    variable.set(OPTIONS[0]) # default value
    w = OptionMenu(root, variable, *OPTIONS)
    w.grid(row=0, sticky=E+W+S+N)
    w.configure(background='#ffcf1a')
    reisinfo = StringVar(master=root, value='')
    #reisgegevensophalen
    def tooninfo():
        w.delete(0,END)
        for vertrektijd in reisinformatie(variable.get()):
            w.insert(END,vertrektijd)
    #aktiebutton
    button = Button(root, text="Haal reisgegevens op", command=tooninfo)
    button.grid(row=1, sticky=E+W+S+N)
    #aanmaken listbox met  scrollbar
    w = Listbox(root, listvariable=reisinfo,font='Monaco')
    scrollbar = Scrollbar(w)
    scrollbar.pack(side=RIGHT, fill=Y)
    w.config(yscrollcommand=scrollbar.set)
    w.grid(row=2,sticky=E+W+S+N)
    w.configure(background='#ffcf1a')
    scrollbar.config(command=w.yview)

    mainloop()
