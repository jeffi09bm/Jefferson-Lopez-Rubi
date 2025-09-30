def bienvenida(nombre, idioma = "español"):
    if idioma == "español":
        print(f"hola, {nombre}")
    elif idioma == "ingles":
        print(f"hello, {nombre}")
bienvenida("Jefferson")