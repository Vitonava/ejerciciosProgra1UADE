"""
Escriba un programa para encontrar números divisibles por 3 de una lista de números usando Lambda
"""

def main():
    lista = [1,6,8,5,26,4,45,56,65,515]
    lNDivTres = list(filter(lambda n: n%3 == 0, lista))

    print(f'los numeros divisibles por 3 de la lista pasada son: \n{lNDivTres}')


if __name__ == '__main__':
    main()