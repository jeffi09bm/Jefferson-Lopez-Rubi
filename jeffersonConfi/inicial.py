from tkinter import *
root = Tk()

cuadro = Frame()
cuadro1 = Frame()
cuadro2 = Frame()
cuadro3 = Frame()
cuadro4 = Frame()
cuadro5 = Frame()

cuadro.config(width=50, height=50, bg="blue")
cuadro.grid(row=0, column=0)

cuadro1.config(width=50, height=50, bg="blue")
cuadro1.grid(row=0, column=1)

cuadro2.config(width=50, height=50, bg="blue")
cuadro2.grid(row=0,column=2)

cuadro3.config(width=50, height=50, bg="blue")
cuadro3.grid(row=2,column=1)

cuadro4.config(width=50, height=50, bg="blue")
cuadro4.grid(row=3,column=1)

cuadro5.config(width=50, height=50, bg="blue")
cuadro5.grid(row=3,column=0)

root.mainloop()