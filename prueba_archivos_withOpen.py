import os

try:
    rutaDirectorio = os.path.dirname(__file__)
    rutaArchivo = os.path.join(rutaDirectorio, 'archivo1.txt')

    with open(rutaArchivo, 'r') as arch: # Usando with no es necesario cerrar el archivo manualmente
        for linea in arch:
            print(linea.strip())

except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"Error de entrada/salida: {e}")