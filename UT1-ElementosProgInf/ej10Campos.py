# Sabiendo que un campo de futbol mide entre 90 y 120 m de largo
# y entre 45 y 90 m de ancho, comprueba si una superficie puede
# corresponder a la estimacion indicada de campos de futbol.

superficie = float(input("Introduce la superficie en metros cuadrados (1-99999): "))
numero_campos = int(input("Introduce el numero estimado de campos: "))

superficie_minima = 90 * 45
superficie_maxima = 120 * 90

campos_validos = (
    1 <= superficie <= 99999
    and numero_campos > 0
    and superficie_minima <= superficie / numero_campos <= superficie_maxima
)

print(campos_validos)