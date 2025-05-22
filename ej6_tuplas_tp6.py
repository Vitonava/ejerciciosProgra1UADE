"""
Cálculo de promedio: crea un programa que lea una lista de tuplas, donde cada tupla contiene el nombre de un estudiante y una lista de calificaciones, y calcule el promedio de calificaciones de cada estudiante. Por ejemplo, si llamamos a la función con la lista de tuplas [( 'Juan', [9, 8, 7]), ('Maria', [10, 9, 10]), ('Pedro', [8, 7, 9])], la función devolverá la lista [( 'Juan', 8.0), ('Maria', 9.67), ('Pedro', 8.0)], que contiene el nombre de cada estudiante y su promedio de calificaciones en forma de tuplas.
"""
def sacarPromedios(listaTuplas):
    """
    objetivo: calcular los promedios de las notas de los alumnos.
    entrada: lista de tuplas con el nombre del alumno y una lista de notas.
    salida: lista de tuplas con el nombre del alumno y su promedio de notas.
    """
    lProm = []
    for aulmno, notas in listaTuplas:
        total = sum(notas)
        promedio = total / len(notas)
        lProm.append((aulmno, round(promedio,2)))
    return lProm

def main():
    lista = [('pepe',[1,2,3]),('valentina',[10,9,10]),('mateo', [7,4,6]),('vito',[8,9,8])]

    listaConPromedios = sacarPromedios(lista)
    print(f'\t\tlista de alumnos:\n{lista}')
    print(f'\n')
    print(f'\t\tlista con promedios:\n{listaConPromedios}')

if __name__ == "__main__":
    main()