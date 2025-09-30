import random
numero_suerte = random.randint(1,100)
numero_usuario = 0

while numero_suerte != numero_usuario:
    numero_usuario = int(input("ingrese un numero"))

print(f"usted gano, el numero era el {numero_suerte}")