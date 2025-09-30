import tkinter as tk
from tkinter import ttk

CRC_POR_USD = 503.55
CRC_POR_EUR = 540.00

def agregar_caracter(c):
    pantalla.insert(tk.END, c)

def limpiar():
    pantalla.delete(0, tk.END)
    resultado.config(text="")

def convertir():
    try:
        cant = float(pantalla.get().replace(',', '.'))
        moneda = moneda_var.get()
        if moneda == "Colones":
            usd = cant / CRC_POR_USD
            eur = cant / CRC_POR_EUR
            res = f"{cant:.2f} CRC = {usd:.2f} USD = {eur:.2f} EUR"
        elif moneda == "Dólares":
            crc = cant * CRC_POR_USD
            eur = crc / CRC_POR_EUR
            res = f"{cant:.2f} USD = {crc:.2f} CRC = {eur:.2f} EUR"
        else:      
            crc = cant * CRC_POR_EUR
            usd = crc / CRC_POR_USD
            res = f"{cant:.2f} EUR = {crc:.2f} CRC = {usd:.2f} USD"
        resultado.config(text=res)
    except:
        resultado.config(text="Error: Ingresa número válido")

ventana = tk.Tk()
ventana.title("Conversor Colones / USD / EUR")

pantalla = tk.Entry(ventana, font=("Arial",16), width=20)
pantalla.grid(row=0, column=0, columnspan=4)

botones = [
    "7", "8", "9", ".",
    "4", "5", "6", ",",
    "1", "2", "3", "C",
    "0"
]

fila = 1
col = 0
for b in botones:
    cmd = limpiar if b == "C" else lambda x=b: agregar_caracter(x)
    tk.Button(ventana, text=b, width=5, height=2, command=cmd).grid(row=fila, column=col)
    col += 1

    if col > 3:
        col = 0
        fila += 1

moneda_var = tk.StringVar(value="Colones")
ttk.OptionMenu(ventana, moneda_var, "Colones", "Colones", "Dólares", "Euros").grid(row=fila, column=1, columnspan=2)

tk.Button(ventana, text="Convertir", width=12, height=2, command=convertir).grid(row=fila, column=3)

resultado = tk.Label(ventana, font=("Arial",14), fg="red")
resultado.grid(row=fila+1, column=0, columnspan=4, pady=10)

ventana.mainloop()