#el modulo OS proporciona funcionalidades del sistema operativo, entorno
import os
from os.path import isfile

print("directorio actua: ", os.getcwd())
path = os.getcwd()
print("Path absoluto: ", os.path.abspath((path)))
print("Directorio base: ", os.path.basename(path))
print("Saber si existe dir: ", os.path.exists(path))
print("Ultimo acceso: ", os.path.getatime(path))
print("Tamaño: ", os.path.getsize(path))
print("Es archivo? ", os.path.isfile(path))
print("Es directorio? ", os.path.isdir(path))