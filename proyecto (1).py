
import turtle

# Crear la ventana
ventana = turtle.Screen()
ventana.bgcolor("white")  # color de fondo

# Crear la tortuga
flor = turtle.Turtle()
flor.shape("turtle")       # forma de tortuga
flor.color("magenta")      # color inicial
flor.pensize(2)            # grosor del trazo
flor.speed(10)             # velocidad de dibujo

# Función para dibujar un pétalo
def petalo():
    for i in range(2):
        flor.circle(100, 60)   # arco de círculo
        flor.left(120)
        flor.circle(100, 60)
        flor.left(120)

# Dibujar la flor completa (6 pétalos)
for i in range(6):
    petalo()
    flor.right(60)  # girar para el siguiente pétalo

# Dibujar el tallo
flor.color("green")
flor.right(90)
flor.forward(300)

# Finalizar
flor.hideturtle()  # ocultar la tortuga al terminar
turtle.done()
