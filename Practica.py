#1 Saludo Personalizado
nombre = input("¿Cual es tu nombre? ")
print(f"Hola,{nombre}. ¡Bienvenido a Python!")

#2 Cálculo Simple
num1 = 5
num2 = 3
print(num1+num2,
    num1-num2,
    num1*num2,
    num1/num2)

#3 Conversión de Temperatura
gradc = float(input("Ingresa la temperatura en celsius "))
gradf = (gradc * (9/5)) + 32
print(f"{gradc} Grados es igual a {gradf} Grados")

#4
nombre= ("Eydan")
apellido= ("Araya")
edad= 16
print(f"Hola, mi nombre es {nom} {ape}, tengo {eda} años.")

#5
numEntero = int(input("Ingresa un numero entero. "))
if numEntero  % 2 == 0:
    print (f"El numero {numEntero} es par")
else:
    print (f"El numero {numEntero} es impar")

#6

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if (num1 >= num2) and (num1 >= num3):
    mayor = num1
elif (num2 >= num1) and (num2 >= num3):
    mayor = num2
else:
    mayor = num3

print(f"El número mayor es: {mayor}")

#7
for i in range(1, 11):
    print(i)

#8
suma = 0
i = 1
while i <= 50:
    suma += i 
    i += 1    
print("La suma es:", suma)

#9
contrasena = "python123"
contrasena_ingresada = input("Ingrese la contraseña: ")
if contrasena_ingresada == contrasena:
    print("Acceso concedido")
else:
    print("Acceso denegado")

#10
numero = int(input("cual tabla deseas ver: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#11
def calcular_area(base, altura):
    return base * altura

area = calcular_area(5, 3)
print(f"El área del rectángulo es: {area}")

#12
def invertir_cadena(cadena):
    return cadena[::-1]

texto = "Hola Mundo"
texto_invertido = invertir_cadena(texto)
print(f"La cadena invertida es: {texto_invertido}")

#13
def es_primo(numero):
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False
    
    # Verificar divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

#15
ef lista_compras():
    lista = ["pan", "leche", "huevos", "manzanas", "arroz"]
    # Imprime el tercer artículo (índice 2)
    print("Tercer artículo:", lista[2])
    # Añade un nuevo artículo al final e imprime la lista completa
    lista.append("aceite")
    print("Lista completa:", lista)

if __name__ == "__main__":
    main()
    datos_personales()
    lista_compras()
# ...existing code...

#16
def calcular_promedio():
    # Lista de 5 números flotantes
    numeros = [3.14, 2.71, 1.618, 4.2, 5.55]
    
    # Calcular el promedio
    promedio = sum(numeros) / len(numeros)
    
    # Imprimir la lista y el resultado
    print("Lista de números:", numeros)
    print(f"El promedio es: {promedio:.2f}")

# Llamar a la función
calcular_promedio()

#17
def eliminar_duplicados():
    # Lista original con elementos duplicados
    lista_original = [1, 2, 2, 3, 4, 4, 5]
    
    # Convertir a conjunto para eliminar duplicados y luego volver a lista
    lista_sin_duplicados = list(set(lista_original))
    
    # Imprimir resultados
    print("Lista original:", lista_original)
    print("Lista sin duplicados:", lista_sin_duplicados)

# Llamar a la función
eliminar_duplicados()

#18
print("ingrese una palabra para contar sus vocales :")
palabra = input ()
contador_vocales = sum(1 for letra in palabra if letra. lower () in AEIOUaeiouáéíóú")
print("la palabra "+ palabra + " tiene " + str (contador_vocales) + "vocales".)
