numeros = (1,2,3,4,5,6,7,8)
for numero in numeros:
    print (numero)
    if numero % 2 ==0:
        print("el numero es par")
    else:
        print("el numero es impar")

lista = ("manzana","pera","mora","uva")

for fruta in lista:
    print(fruta)




numeros = (1,2,3,4,5)
suma = 0

for numero in numeros:
    suma += numero
print (suma)




texto= "El universo se creó con el Big Bang, un evento que ocurrió hace aproximadamente 13.8 mil millones de años, cuando el universo se expandió rápidamente desde un punto increíblemente pequeño, denso y caliente."
contador = 0
vocales = ["a","e","i","o","u"]

for vocal in vocales:
    for letra in texto:
        if letra.lower() == vocal:
            contador +=1
    print(f"La letra {vocal} aparece {contador} veces")



while True:
    opc = input("""
1 = Manzana 
2 = Pera
3 = Sandia
""")
    if opc == "1":
        print("usted escogio manzana")
        break
    elif opc == "2":
        print("usted escogio pera")
        break
    elif opc == "3":
        print("usted escogio sandia")
        break
    else:
        print("seleccione opcion valida")




num_suerte = 12
num_usuario = 0
while num_suerte != num_usuario:
    num_usuario = int(input("ingrese un numero"))

print(f"usted gano, el numero era"[num_suerte])
