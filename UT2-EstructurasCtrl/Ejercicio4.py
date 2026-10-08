try:
    nota = float(input("Introduce una nota del 0 al 10: "))
    if not 0 <= nota <= 10:
        print("Error: la nota debe estar entre 0 y 10.")
    elif nota < 5:
        print("Insuficiente")
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")
except ValueError:
    print("Error: introduce un número válido.")
