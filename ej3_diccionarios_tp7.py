"""
Hacer un programa que registre 10 alumnos y guarde: nombre, nombre de la asignatura y 4 notas. Calcular y mostrar el promedio de las notas
"""
def calcularPromedio(notas):
    """
    obj: calcular el promedio de las notas.
    entrada: lista con los alumnos y sus notas
    salida: imprime el promedio de las notas
    """
    total = sum(notas)
    promNotas = total / len(notas)

    return promNotas

def main():
    datosAlu = []
    while len(datosAlu) < 3:
        alumno = {}
        alumno['nombre'] = input("ingrese el nombre del alumno: ")
        alumno['asignatura'] = input("ingrese la asignatura del alumno: ")
        notasAlu = []
        while len(notasAlu) < 4:
            nota = float(input("ingrese la nota del alumno: "))
            while nota < 0 or nota > 10:
                print("la nota ingresada no es correcta")
                nota = float(input("ingrese la nota del alumno: "))
            notasAlu.append(nota)
        alumno['notas'] = notasAlu
        datosAlu.append(alumno)
    # completo una lista con las notas de los alumnos 
    listaNotas = [n for alumno in datosAlu for n in alumno['notas']] 

    promedioNotas = calcularPromedio(listaNotas)

    print(f'\t\t promedio de notas:\t {promedioNotas:.2f}')

if __name__ == '__main__':
    main()