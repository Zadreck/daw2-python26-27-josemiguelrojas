import getpass

# getpass oculta lo que se escribe para que el otro jugador no vea el secreto
secreto = int(getpass.getpass("Introduce el número secreto (no se verá): "))

while True:
    intento = int(input("Adivina el número: "))
    if intento == secreto:
        print("¡Enhorabuena! Has acertado el número.")
        break
    elif secreto > intento:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")