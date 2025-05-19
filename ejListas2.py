"""
2. Escribir funciones para:

a. Generar una lista de 50 números aleatorios del 1 al 100. Utilice comprensión de listas para generar el resultado.

b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.

c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.

Combinar estas tres funciones en un mismo programa."""

import random
def generar_lista_aleatoria(cantidad=50, rango=(1, 100)):
    """
    Genera una lista de números aleatorios entre un rango dado.
    :param cantidad: Cantidad de números a generar.
    :param rango: Rango de los números aleatorios.
    :return: Lista de números aleatorios.
    """
    return [random.randint(rango[0], rango[1]) for _ in range(cantidad)]
def contiene_repetidos(lista):
    """
    Verifica si una lista contiene elementos repetidos.
    """
    return len(lista) != len(set(lista))
def lista_unicos(lista):
    """
    Devuelve una nueva lista con los elementos únicos de la lista original.
    """
    for elemento in lista:
        
        if lista.count(elemento) > 1:
            listaSinRepetidos = [i for i in lista if i != elemento]
    return listaSinRepetidos
#     return list(set(lista))  # Alternativa más sencilla para obtener elementos únicos

def main():
    # Genera una lista de 50 números aleatorios del 1 al 100.
    lista_aleatoria = generar_lista_aleatoria()
    print("Lista aleatoria:", lista_aleatoria)

    # Verifica si la lista contiene elementos repetidos.
    if contiene_repetidos(lista_aleatoria):
        print("La lista contiene elementos repetidos.", len(lista_aleatoria))
    else:
        print("La lista no contiene elementos repetidos.", len(lista_aleatoria))

    # Genera una nueva lista con los elementos únicos de la lista original.
    lista_unicos_resultado = lista_unicos(lista_aleatoria)
    print("Lista con elementos únicos:", lista_unicos_resultado)
    print("Cantidad de elementos únicos:", len(lista_unicos_resultado))

if __name__ == "__main__":
    main()