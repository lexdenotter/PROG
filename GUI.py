# Import
from GUI_Utrecht import *
from GUI_Ander import toonVenster2


# Algemene settings
root = Tk()
root.title('Reizigersinformatie')
root.geometry('790x596')
root.resizable(width=False, height=False)
bg_image = PhotoImage(file='background.png')
root.iconbitmap('ns.ico')
x = Label(image=bg_image)
x.grid(row=0, column=0)
root.iconbitmap('ns.ico')

# Button reisinfo huidig station
button1 = Button(master=root, text='Reisinformatie\nUtrecht Centraal', command=reisInfoMenu, background='#01236a', foreground='white', font=('Verdana', 13, 'bold'))
button1.place(x=220, y=400)

# Button reisingo ander station
button2 = Button(master=root, text='Reisinformatie\nAnder Station', command=toonVenster2, background='#01236a', foreground='white', font=('Verdana', 13, 'bold'))
button2.place(x=415, y=400)

root.mainloop()
