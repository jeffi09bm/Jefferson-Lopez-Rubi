nombre ="Jeff"
edad = 15
alto = 1.70

print(nombre)
print(edad)
print(alto)

print(f"Mi nombre es {nombre}, tengo {edad} años y mido {alto} metros.")
print("mi nombre es " + nombre + ", tengo " + str(edad) + " años y mido " + str(alto) + " metros.")
print("mi nombre es ", nombre, ", tengo ", edad, " años y mido ", alto, " metros.")

numero = 10
print(numero)
numero = 25
print(numero)

precio_str = "99.99"
precio_float = float(precio_str)

print(type(precio_str))
print(type(precio_float))

cantiadad_str = "5"
cantidad_int = int(cantiadad_str)
total = precio_float * cantidad_int
print(f"El total es: {total}")

es_mayor_de_edad = True
tiene_licencia = True
print(f"Es mayor de edad: {es_mayor_de_edad}, Tiene licencia: {tiene_licencia}")

num1 = 10
num2 = 20
num3 = 30

suma_total = num1 + num2 + num3
promedio = suma_total / 3
print(f"La suma total es: {suma_total}, El promedio es: {promedio}")
