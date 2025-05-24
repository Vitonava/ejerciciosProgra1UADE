import os
def cargarAlumnos(nombreArchivo):
    """
    cargar los alumnos en un archivo
    """
    try:
        rutaActual = os.path.dirname(__file__)
        rutaArchivo = os.path.join(rutaActual, nombreArchivo)
        with open(rutaArchivo, 'w', encoding='UTF-8') as arch:
            bandera = True
            while bandera:
                legajo = int(input("ingrese el legajo del alumno (-1 para terminar la carga): "))
                while legajo != -1:
                    nombre = input("ingrese el nombre del alumno: ")
                    turno = input("ingrese el turno del alumno(m,t,n): ")
                    registro = f'{legajo};{nombre};{turno}\n'
                    arch.write(registro)
                    legajo = int(input("ingrese el legajo del alumno (-1 para terminar la carga): "))
                bandera = False
    except Exception as e:
        print("Error al abrir el archivo: ", e)