try:
    year = int(input("Año: "))
    if year %4 == 0 and year % 100 != 0 :
        print ("SI es bisiesto")
    else:
        print("NO es bisiesto")
except ValueError:
    print("Debe ser un numero valido")

