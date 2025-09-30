from tkinter import *
root = Tk()

cuadro = Frame()
cuadro1 = Frame()
cuadro2 = Frame()

cuadro.config(width=50, height=50, bg="")
cuadro.grid(row=0, column=0)

cuadro1.config(width=50, height=50, bg="red")
cuadro1.grid(row=0, column=2)

cuadro2.config(width=50, height=50, bg="red")
cuadro2.grid(row=0, column=4)

root.mainloop()