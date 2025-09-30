Lista = [1,2,3,4,5]
Tupla = (10,20,30,40,50)
cadena = "python"
conjuntos = {1,2,3,4,5,6}
diccionario = {1:{"Nombre":"Diana",
                "Telefono":"465464",
                "edad":18},
                2:{}}
range(0,10,2)

with open("archivo.txt", "r") as archivo:
    pass


# Definir una lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción desde el inicio hasta el índice 6 (sin incluir)
porcion1 = mi_lista[:6]
print(porcion1)  # Imprime [1, 2, 3, 4, 5, 6]

# Obtener una porción desde el índice 7 hasta el final
porcion2 = mi_lista[7:]
print(porcion2)  # Imprime [8, 9, 10]

# Obtener una porción desde el índice 2 hasta el índice 8 (sin incluir)
porcion3 = mi_lista[2:8]
print(porcion3)  # Imprime [3, 4, 5, 6, 7, 8]

# Utilizar índices negativos para contar desde el final
porcion4 = mi_lista[-5:-1]
print(porcion4)  # Imprime [6, 7, 8, 9]

# Obtener toda la lista (equivalente a lista[:])
copia_completa = mi_lista[:]
print(copia_completa)  # Imprime [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción con un paso (cada segundo elemento)
porcion_con_paso = mi_lista[::2]
print(porcion_con_paso)  # Imprime [1, 3, 5, 7, 9]





lista_numeros = [1, 2, 3, 4, 5]#lista de el 1 al 5
lista_strings = ['apple', 'banana', 'cherry']#lista de frutas
lista_mixta = [1, 'dos', True, 4.5]#lista mixto

primer_elemento = lista_numeros[0]
segundo_elemento = lista_strings[1]
ultimo_elemento = lista_mixta[-1]

long = len(lista_mixta)#cuenta los elementos en una lista
print(long)

lista_numeros.append(6)#agrega el numero 6 a la lista

lista_strings.insert(1, "orange")#inserta elemento en el espacio numero 1 

ultimo_elemento = lista_numeros.pop()#Elimina y retorna el último elemento de la lista de números
lista_strings.remove("banana")# Elimina la primera ocurrencia de "banana" de la lista de strings


lista_numeros.sort()#Elimina y retorna el último elemento de la lista de números

lista_mixta.reverse()  # Invierte el orden de los elementos en la lista mixta



#1 - Crear una lista con 4 frutas
#2 - Acceder al elemento 0
#3 - Agregar kiwi al final
#4 - Agregar pera en posición 2
#5 - Eliminar el kiwi
#6 - Imprimir toda la lista

frutas= ["fresa","banano","uva","píña"]

primer_elemento = frutas[0]

frutas.append("kiwi")

frutas.insert(2, "pera")

frutas.remove("kiwi")

print(frutas)

# Creación de una tupla
coordenadas = (3, 7)

# Acceso a elementos
x = coordenadas[0]  # x es igual a 3

# Longitud de la tupla
longitud = len(coordenadas)  # longitud es igual a 2

# Desempaquetado de tuplas
a, b = coordenadas  # a es igual a 3, b es igual a 7

# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2  # tupla_concatenada es igual a (1, 2, 3, 'a', 'b', 'c')

# Creación de un objeto range
mi_rango = range(0, 10, 2)

# Iteración sobre el rango
for numero in mi_rango:
    print(numero)  # Imprime 0, 2, 4, 6, 8

# Convertir el rango en una lista
lista_mi_rango = list(mi_rango)  # lista_mi_rango es igual a [0, 2, 4, 6, 8]

# Verificar si un valor está en el rango
esta_en_rango = 3 in mi_rango  # devuelve False