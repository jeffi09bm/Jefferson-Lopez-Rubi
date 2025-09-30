#   Imprime la lista completa frutas.
lista1 = ["manzana", "banana", "cereza", "dátil"]
print(lista1)
print(lista1[0])
print(lista1[-1])
print(lista1[2])

# Modificación de Listas

colores=["rojo", "verde", "azul"]
colores[1]="amarillo"
print (colores)
colores[-1] = "morado"
print (colores)
colores[1] = "naranja"
print(colores)

# Métodos Básicos de Listas
numeros=[10, 5, 20, 15, 25]
numeros.append(30)
print(numeros)
numeros.remove(5)
print(numeros)
ultimo = numeros.pop()
print(ultimo)
numeros.sort()
print(numeros)

#Longitud de una Lista y Verificación de Elementos
ciudades = ["san jose","alajuela","guanacaste","cartago"]
print(len(ciudades))
esta ="tokio" in ciudades

#Listas con Diferentes Tipos de Datos
mixta = (12,3.14, "hola mundo", True, None)
for elemento in mixta:
    print(type(elemento))
print(mixta)