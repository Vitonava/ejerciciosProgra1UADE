"""Desarrollar una función que reciba tres números enteros y devuelva el mayor de los tres. Devolver -1 en caso de existir igualdad.
Desarrollar un programa principal que invoque a la función, en el programa principal solicitar los datos al usuario"""

def encontrarMayor(n1,n2,n3):
    """
    objetivo: comparar 3 numeros y encontrar el mas grande.
    en caso de igualdad devuelve un '-1'
    """
    if n1 > n2 and n1 > n3:
        mayor = n1
    elif n2 > n1 and n2 > n3:
        mayor = n2
    elif n3 > n1 and n3 > n2:
        mayor = n3
    elif n1 == n2 or n1 == n3:
        return print("hay una igualdad",-1)
    
    return print("el numero mas grande es: ", mayor)
    
def main():
    a1 = int(input("ingrese un numero: "))
    a2= int(input("ingrese un numero: "))
    a3 = int(input("ingrese un numero: "))
    
    encontrarMayor(a1,a2,a3)
    
if __name__ == '__main__':
    main()