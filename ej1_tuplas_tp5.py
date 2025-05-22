"""
Crear una variable utilizando tuplas que sea capaz de almacenar los valores de las cartas de la baraja española 
(48 cartas; del 1 al 12 de basto, copa, espada y oro).

a. Crear una función que retorne una lista con una determina cantidad de cartas seleccionadas al azar que será 
recibida como parámetro (junto con la variable que se creó el mazo).

b. Utilizando la función anterior, obtenga 10 cartas del mazo e indique la cantidad de cartas que son de oro.
"""
import random

def seleccionar_cartas(mazo, cantidad_cartas):
    lista_cartas = []
    while len(lista_cartas) < cantidad_cartas:
        i = random.randint(0, len(mazo) - 1)
        carta = mazo[i]
        if carta not in lista_cartas:
            lista_cartas.append(carta)
    return lista_cartas

def leerOro(carta):
    if carta[1] == "oro":
        return True
    return False

def main():
    baraja = ["basto", "copa", "espada", "oro"]
    numeros = list(range(1, 13))
    mazo = tuple((numero, palo) for palo in baraja for numero in numeros) 
    """# es lo mismo que 
    for palo in palos:
        for numero in range(1, 13):
            mazo.append((numero, palo))
    mazo = tuple(mazo)
    # o
    mazo = tuple()
    for palo in baraja:
        for numero in range(1, 13):
            mazo += ((numero, palo),)
    """
    print("\n\t\tCartas seleccionadas al azar:\n")
    lCartas = seleccionar_cartas(mazo, random.randint(1, 10))
    for i in lCartas:
        print(i, end="\t")
    print("\n\t\tCantidad de cartas seleccionadas al azar: ", len(lCartas))
    cantidad_cartas = 10
    print("\n\t\tCantidad de cartas seleccionadas: ", cantidad_cartas)
    lista_cartas = seleccionar_cartas(mazo, cantidad_cartas)
    for c in lista_cartas:
        print(c)
    cantidad_oro = sum(1 for carta in lista_cartas if leerOro(carta))
    print("\n\t\tCantidad de cartas de oro: ", cantidad_oro)

if __name__ == "__main__":
    main()