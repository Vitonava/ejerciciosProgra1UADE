"""
Crea un programa que vaya leyendo las frases que el usuario teclea y las guarde en un fichero de texto llamado “frases.txt”. Terminará cuando la frase introducida sea "fin" (esa frase no deberá guardarse en el fichero).
"""
import os
def cargarFrases(nombreArchivo):
    try:
        rutaDirectorio = os.path.dirname(__file__)
        rutaArchivo = os.path.join(rutaDirectorio, nombreArchivo)
        with open(rutaArchivo, 'w') as arch:
            bandera = True
            while bandera:
                frase = input("ingrese una frase ('fin' para terminar): ")
                while frase != 'fin':
                    arch.write(f'{frase}\n')
                    frase = input("ingrese una frase ('fin' para terminar): ")
                bandera = False
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrarFrases(nombreArchivo):
        try:
            with open(nombreArchivo, 'r') as arch:
                for linea in arch:
                    print(linea.strip())
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as e:
            print(f"Error inesperado: {e}")

def main():
    cargarFrases('frases.txt')
    mostrarFrases('frases.txt')

if __name__ == "__main__":
    main()