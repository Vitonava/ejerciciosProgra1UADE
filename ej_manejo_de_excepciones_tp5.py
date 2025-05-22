"""
Desarrollar una función para ingresar a través del teclado un número. La función rechazará cualquier ingreso inválido de datos utilizando excepciones y mostrará la razón exacta del error. Devolver el valor ingresado cuando éste sea correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""
def cargarNumero(): #ej1
    bandera = True

    while bandera:
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Error: Debe ingresar un numero entero.")

"""
Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un número real. Devolver None si alguna de las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error.
"""
def sumaReal(n1,n2):
    try:
        result = float(n1) + float(n2)
        return result
    except ValueError:
        print("Error: Debe ingresar un numero real.")
        return None

"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como parámetro. Los nombres de los meses deberán obtenerse de una tupla de cadenas de caracteres inicializada dentro de la función. Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a través de excepciones.

"""
def informarNombreMes(mes):
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    try:
        return meses[mes - 1]
    except IndexError:
        print("Error: Mes inválido.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except TypeError:
        print("Error: Debe ingresar un número entero.")
    except:
        print("Error: Ocurrió un error inesperado.")

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("\t\tTP 5: Manejo de excepciones")
    print("\t\t-------------------------------\n")
    print("\t\tEjercicio 1: Cargar un numero")
    print("\t\t-----------------------------\n")

    numero = cargarNumero()
    print(f"\t\tEl numero ingresado es: {numero}")

    print("\t\tEjercicio 2: Sumar dos numeros reales")
    print("\t\t--------------------------------\n") 
    n1 = input("Ingrese el primer numero real: ")
    n2 = input("Ingrese el segundo numero real: ")
    resultado = sumaReal(n1, n2)
    if resultado is not None:
        print(f"\t\tLa suma de {n1} y {n2} es: {resultado:.2f}")
    else:
        print("\t\tNo se pudo realizar la suma debido a un error en los datos ingresados.")
    
    print("\t\tEjercicio 3: Informar nombre del mes")
    print("\t\t--------------------------------\n")
    mes = int(input("Ingrese el numero del mes (1-12): "))
    while mes < 1 or mes > 12:
        print("Error: Debe ingresar un numero entre 1 y 12.")
        mes = int(input("Ingrese el numero del mes (1-12): "))
    
    nombre_mes = informarNombreMes(mes)
    if nombre_mes:
        print(f"\t\tEl mes {mes} es: {nombre_mes}")
    else:
        print("\t\tNo se pudo obtener el nombre del mes debido a un error en el numero ingresado.")

if __name__ == "__main__":
    main()
