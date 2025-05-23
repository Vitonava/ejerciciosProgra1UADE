"""
leer desde el teclado los datos correspondientes a los alumnos de un curso (legajo, nombre) y grabarlos en un archivo csv.
cada dato se separa con ; (punto y coma)
el fin de datos se indica con un legajo -1
"""
import os

def filtrarAlumnos(rutaArchivo):
    try:
        with open(rutaArchivo, 'r') as file: 
            for linea in file:
                legajo, nombre = linea.strip().split(';')
                if int(legajo) < 1000:
                    print(f'legajo: {legajo}, nombre: {nombre}')
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")

def cargarAlumno(nombreArchivo):
    try:
        rutaDirectorio = os.path.dirname(__file__)
        rutaArchivo = os.path.join(rutaDirectorio, nombreArchivo)
        with open(rutaArchivo, 'w') as archivo:
            bandera = True
            while bandera:
                legajo = int(input("Ingrese el legajo del alumno (o -1 para terminar): "))
                if legajo != -1:
                    nombre = input("Ingrese el nombre del alumno: ")
                    registro = f'{str(legajo)};{nombre}\n'
                    archivo.write(registro)
                else:
                    bandera = False
    except FileNotFoundError:
        print("El archivo no existe")
    except IOError:
        print("Error de entrada/salida")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else:
        filtrarAlumnos(rutaArchivo)


def main():
    cargarAlumno('alumnos.txt')
    
if __name__ == "__main__":
    main()        