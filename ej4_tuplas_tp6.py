"""
Juego de cartas: crea una función que genere aleatoriamente una mano de cinco cartas de una baraja de póker. Cada carta debe ser representada por una tupla que contenga un número y un palo.
"""
import random
def generarMano(lista):
    """
    obj: generar una mano de cartas aleatorias.
    entrada: lista con las cartas de la baraja
    salida: lista con las cartas de la mano
    """
    mano = []
    while len(mano) < 5:
        num = random.randint(1,48)
        mano.append(lista[num])
    return mano

def main():
    baraja = [('corazones', 1), ('corazones', 2), ('corazones', 3), ('corazones', 4), ('corazones', 5), ('corazones', 6), ('corazones', 7), ('corazones', 8), ('corazones', 9), ('corazones', 10), ('corazones', 11), ('corazones', 12), ('corazones', 13),
              ('diamantes', 1), ('diamantes', 2), ('diamantes', 3), ('diamantes', 4), ('diamantes', 5), ('diamantes', 6), ('diamantes', 7), ('diamantes', 8), ('diamantes', 9), ('diamantes', 10), ('diamantes', 11), ('diamantes', 12), ('diamantes', 13),
              ('tréboles', 1), ('tréboles', 2), ('tréboles', 3), ('tréboles', 4), ('tréboles', 5), ('tréboles', 6), ('tréboles', 7), ('tréboles', 8), ('tréboles', 9), ('tréboles', 10), ('tréboles', 11), ('tréboles', 12), ('tréboles',13),
              ('picas' ,1) ,('picas' ,2) ,('picas' ,3) ,('picas' ,4) ,('picas' ,5) ,('picas' ,6) ,('picas' ,7) ,('picas' ,8) ,('picas' ,9) ,('picas' ,10) ,('picas' ,11) ,('picas' ,12) ,('picas' ,13)]
    
    manoAleatoria = generarMano(baraja)
    print(f'\t\tMano de cartas:\n{manoAleatoria}')

if __name__ == "__main__":
    main()  