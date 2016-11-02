from tkinter import *
from NSapi import *

#functie om scherm aan te maken
def toonVenster2():
    root = Tk()
    root.geometry('790x596')
    root.resizable(width=False, height=False)
    root.title('Reisinformatie Ander Station')
    root.configure(background='#ffcf1a')
