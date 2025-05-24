"""
Se tienen dos archivos con los datos de los alumnos inscriptos para rendir un examen. Cada registro contiene:

Número de legajo

Nombre

Turno (M: Mañana; T: Tarde; N: Noche)

Existe un registro por cada alumno. Los archivos se encuentran ordenados por número de legajo. Se solicita obtener un archivo único con los inscriptos para el examen en el que conste la misma información, el que también debe quedar ordenado por número de legajo. Debido a errores en la carga de datos puede haber alumnos que aparezcan inscriptos en más de un turno. Esos alumnos deberán mostrarse por pantalla en un listado de inconsistencias, y no se grabarán en el archivo de salida. Al finalizar el proceso informar la cantidad de registros grabados y la cantidad de inconsistencias halladas.

Se adjuntan dos archivos llamados alumnos1.txt y alumnos2.txt, ambos con formato CSV (valores separados por punto y coma). Los mismos han sido creados con codificación UTF8, por lo que deberá agregarse el parámetro encoding="UTF8" en el momento de su apertura. El programa debe servir para estos archivos o cualquier otro que respete el mismo formato.
"""
import os 

def cargarAlumnos(nombreArchivo, listaAlu):
    """
    cargar los alumnos en un archivo
    """
    try:
        rutaActual = os.path.dirname(__file__)
        rutaArchivo = os.path.join(rutaActual, nombreArchivo)
        with open(rutaArchivo, 'w', encoding='UTF-8') as arch:
            bandera = True
            while bandera:
                for alumno in listaAlu:
                    legajo = int(alumno[0])
                    nombre = alumno[1]
                    turno = alumno[2]
                    registro = f'{legajo};{nombre};{turno}\n'
                    arch.write(registro)
                bandera = False
    except Exception as e:
        print("Error al abrir el archivo: ", e)

def filtrarAlumnos(nomArch):
    try:
        rutaDirectorio = os.path.dirname(__file__)
        rutaArchivo = os.path.join(rutaDirectorio, nomArch)
        with open(rutaArchivo, 'r', encoding = 'UTF-8') as arch:
            alumnos = {}
            inconsistencias = 0
            for linea in arch:
                legajo, nombre, turno = linea.strip().split(';')
                legajo = int(legajo)
                if legajo in alumnos:
                    inconsistencias += 1
                else:
                    alumnos[legajo] = (nombre, turno)
            print(f'\t\talumnos cargados: \n')
            for legajo, tuplaNombreTurno in alumnos.items(): 
                if legajo in alumnos:
                    nombre, turno = tuplaNombreTurno
                    print(f'legajo: {legajo}, nombre: {nombre}, turno: {turno}')
            print(f'Cantidad de registros grabados: {len(alumnos)}')
            print(f'Cantidad de inconsistencias: {inconsistencias}')    
    except Exception as e:
        print("Error al abrir el archivo: ", e)

def ordenarAlumnos(nombreArchivo):
    """
    ordenar los alumnos por legajo y 
    """
    try:
        rutaDirectorio = os.path.dirname(__file__)
        rutaArchivo = os.path.join(rutaDirectorio, nombreArchivo)
        with open(rutaArchivo, 'r', encoding='UTF-8') as arch:
            alumnos = []
            for linea in arch:
                legajo, nombre, turno = linea.strip().split(';')
                legajo = int(legajo)
                alumnos.append((legajo, nombre, turno))
            # ordenar la lista de alumnos por legajo
            # alumnos.sort(key=lambda x: x[0]) # metodo para ordenar por legajo
            # otro metodo para ordenar por legajo
            for i in range(len(alumnos)):
                for j in range(i + 1, len(alumnos)):
                    if alumnos[i][0] > alumnos[j][0]:
                        alumnos[i], alumnos[j] = alumnos[j], alumnos[i]            
            return alumnos
    except Exception as e:
        print("Error al abrir el archivo: ", e)

def main():
    # genero una lista de alumnos para tomar como ejemplo
    """listaAlumnos = [(1234, 'Juan', 'M'), (2345, 'Pedro', 'T'), (3456, 'Maria', 'N'), (4567, 'Ana', 'M'), (5678, 'Jose', 'T'), (6789, 'Luis', 'N'), (7890, 'Laura', 'M'), (8901, 'Carlos', 'T'), (9012, 'Lucia', 'N'), (1234, 'Javier', 'M')]"""
    listaAluOrd = ordenarAlumnos('alumnos1.txt')
    cargarAlumnos('alumnos1.txt', listaAluOrd)

    filtrarAlumnos('alumnos1.txt')

if __name__ == "__main__":
    main()