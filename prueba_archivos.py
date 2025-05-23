import os

try:
    ruta_Directorio = os.path.dirname(__file__)
    ruta_Archivo = os.path.join(ruta_Directorio, 'archivo1.txt')

    arch = open(ruta_Archivo, 'r')

    for line in arch:
        print(line.strip())
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error de entrada/salida")
finally:
    arch.close()