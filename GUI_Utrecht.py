from tkinter import *
from NSapi import *
#functie om scherm aan te maken
def reisInfoMenu():
    root = Tk()
    root.geometry('790x596')
    root.resizable(width=False, height=False)
    root.title('Reisinformatie Huidig Station')
    root.iconbitmap('ns.ico')
    root.configure(background='#ffcf1a')
    root.columnconfigure(0,minsize=790)
    root.rowconfigure(1,minsize=550)

    reisinfo = StringVar(master=root, value='')
    #functie om reisinformatie op te halen uit NSapi.py en weer te geven in listbox
    def tooninfo():
        w.delete(0,END)
        for vertrektijd in reisinformatie('ut'):
            w.insert(END,vertrektijd)
    #button om vertrektijden op te halen
    button1 = Button(master=root, text='Haal Vertrektijden op', command=tooninfo, background='#01236a', foreground='white', font=('Verdana', 13))
    button1.grid(row=0)
    #aanmaken listbox met  scrollbar
    w = Listbox(root, listvariable=reisinfo,font='Monaco')
    scrollbar = Scrollbar(w)
    scrollbar.pack(side=RIGHT, fill=Y)
    w.config(yscrollcommand=scrollbar.set)
    w.grid(row=1,sticky=E+W+S+N)
    scrollbar.config(command=w.yview)

    mainloop()
