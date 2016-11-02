#Import
from tkinter import *
from GUI_Utrecht import *
from GUI_Ander import toonVenster2


#Algemene settings
root = Tk()
root.title('Reizigersinformatie')
root.geometry('790x596')
root.resizable(width=False, height=False)
#bg_image = PhotoImage(file ='background.png')
#x = Label (image = bg_image)
#x.grid(row = 0, column = 0)

#Button reisinfo huidig station
button1 = Button(master=root, text='Reisinformatie Huidig Station', command=reisInfoMenu, background='#01236a', foreground='white', font=('Verdana', 13))
button1.place(x=110, y=400)

#Button reisingo ander station
button2 = Button(master=root, text='Reisinformatie Ander Station', command=toonVenster2, background='#01236a', foreground='white', font=('Verdana', 13))
button2.place(x=400, y=400)

root.mainloop()
