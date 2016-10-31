from tkinter import *
from  tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title('Reizigersinformatie')

root.geometry('790x596')
root.resizable(width=False, height=False)

bg_image = PhotoImage(file ='lol.png')
x = Label (image = bg_image)
x.grid(row = 0, column = 0)


def toonVenster():
    def close():
        subwindow.withdraw()
    subwindow = Toplevel(master=root)
    button2 = Button(master=subwindow, text='Sluit mij', command=close)
    button2.pack(padx=10, pady=10)

button1 = Button(master=root, text='Reisinformatie Huidig Station', command=toonVenster, background='#01236a', foreground='white', font=('Verdana', 13))
button1.place(x=110, y=400)

button2 = Button(master=root, text='Reisinformatie Ander Station', command=toonVenster, background='#01236a', foreground='white', font=('Verdana', 13))
button2.place(x=400, y=400)

root.mainloop()
