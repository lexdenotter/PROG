from tkinter import *
from NSapi import *

#functie om venster aan te maken
def toonVenster1():
    root = Tk()
    root.geometry('790x596')
    root.resizable(width=False, height=False)
    root.title('Reisinformatie Huidig Station')
    root.configure(background='#ffcf1a')
    button1 = Button(master=root, text='Haal Vertrektijden op', command=aanroep, background='#01236a', foreground='white', font=('Verdana', 13))
    button1.place(x=10, y=10)
    button1.pack()

#functie om de functie reisinformatie aan te roepen
def aanroep():
    return reisinformatie('ut')

