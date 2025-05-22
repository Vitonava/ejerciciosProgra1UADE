"""
Escribir un programa que dadas dos tuplas de tres elementos, 
realice el producto de cada elemento existente en la primera tupla con todos los restantes del segundo y 
almacene cada resultado en otra tupla. 
Por ejemplo, el producto escalar entre (1, 2, 3) y (4, 5, 6); debería retornar: ((4, 5, 6),(8, 10, 12), (12, 15, 18)).
"""
def prod_tuplas(t1,t2):
    """
    Realiza el producto de cada elemento existente en la primera tupla con todos los restantes del segundo y 
    almacena cada resultado en otra tupla.
    """
    prod = (
        (t1[0]*t2[0], t1[0]*t2[1], t1[0]*t2[2]),
        (t1[1]*t2[0], t1[1]*t2[1], t1[1]*t2[2]),
        (t1[2]*t2[0], t1[2]*t2[1], t1[2]*t2[2])
    )

    return prod

def main():
    tupla1 = (1,2,3)
    tupla2 = (8,4,6)
    print(f'\t\tProducto de las tuplas {tupla1} y {tupla2}:')
    resultado = prod_tuplas(tupla1, tupla2)
    print(f'\t\t{resultado}\t\n')


if __name__ == "__main__":
    main()