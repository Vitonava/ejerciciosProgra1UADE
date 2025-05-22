"""
Suma de números: crea un programa que lea una lista de tuplas, donde cada tupla contiene dos números enteros, y calcule la suma de los números en cada tupla. Por ejemplo, si llamamos a la función con la lista de tuplas [(1, 2), (3, 4), (5, 6)], la función devolverá el valor 21, que es la suma de los números en todas las tuplas.
"""

def main():
    lTuplas =[(1,2),(6,5),(8,9),(4,7),(3,2)]
    suma= 0
    for n1, n2 in lTuplas:
        suma += n1 + n2

    print(f'\t\tLa suma de los números en la lista de tuplas es: {suma}')   

if __name__ == "__main__":
    main()