"""
Escriba un programa para generar una función (utilizando filter) y lambdas para separar los números pares e impares de una lista de números.
La función debe retornar dos valores resultantes.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lPar = list(filter(lambda n: n % 2 == 0,lista))
lImpar = list(map(lambda n: n*2,list(filter(lambda n: n % 2 != 0,lista))))

print(f'la lista de números pares es: {lPar}')
print(f'la lista de números impares multiplicados por 2 es: {lImpar}')