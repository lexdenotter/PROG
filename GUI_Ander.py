from tkinter import *

from NSapi import *

def toonVenster2():
    root = Tk()
    root.geometry('790x596')
    root.resizable(width=False, height=False)
    root.title('Reisinformatie Huidig Station')
    root.configure(background='#ffcf1a')

    button1 = Button(master=root, text='Haal Vertrektijden op', command=aanroeputrecht, background='#01236a', foreground='white', font=('Verdana', 13))
    button1.place(x=10, y=10)
    button1.pack()

    button2 = Button(master=root, text='Haal Vertrektijden op van Tilburg', command=aanroeptilburg, background='#01236a', foreground='white', font=('Verdana', 13))
    button2.place(x=10, y=10)
    button2.pack()

    button3 = Button(master=root, text='Haal Vertrektijden op van Breda', command=aanroepbreda, background='#01236a', foreground='white', font=('Verdana', 13))
    button3.place(x=10, y=10)
    button3.pack()


def aanroeputrecht():
    return reisinformatie('ut')

def aanroeptilburg():
    return reisinformatie('tilburg')

def aanroepbreda():
    return reisinformatie('breda')
