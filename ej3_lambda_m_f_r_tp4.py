"""
Escriba un programa para contar los números pares e impares en una lista dada de enteros usando Lambda.
"""

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    cantPares = len(list(filter(lambda n: n % 2 == 0, lista)))

    cantImpares = len(list(filter(lambda n: n % 2 != 0, lista)))

    print(f'la cantidad de números pares es: {cantPares}')
    print(f'la cantidad de números impares es: {cantImpares}')


if __name__ == "__main__":
    main()  