from tkinter import *
from GUI_Utrecht import toonVenster1
from GUI_Ander import toonVenster2

#gegevens voor main scherm
root = Tk()
root.title('Reizigersinformatie')
root.geometry('790x596')
root.resizable(width=False, height=False)
bg_image = PhotoImage(file ='background.png')
x = Label (image = bg_image)
x.grid(row = 0, column = 0)


#button1(huidig station)
button1 = Button(master=root, text='Reisinformatie Huidig Station', command=toonVenster1, background='#01236a', foreground='white', font=('Verdana', 13))
button1.place(x=110, y=400)

#button2(ander station)
button2 = Button(master=root, text='Reisinformatie Ander Station', command=toonVenster2, background='#01236a', foreground='white', font=('Verdana', 13))
button2.place(x=400, y=400)

root.mainloop()
