import random
# A
def listaNrosAzar(cant = random.randint(1,9)):
    """
    Genera una lista de números aleatorios entre 1 y 100.
    :param cant: Cantidad de números a generar.
    :return: Lista de números aleatorios.
    """
    lA = [random.randint(1000, 9999) for _ in range(cant)]
    return lA

# B

def sumaLista(l):
    """
    calcula la suma de los números en una lista.
    """
    suma = sum(l)
    return suma 

# C 

def eliminarNumero(elemento, lista): 
    """
    Elimina un número de una lista. pasado por teclado.
    """
    for numero in lista:
        if numero == elemento:
            lista.remove(numero)
    return lista

# D
def esCapicua(lista):
    """
    Verifica si una lista es capicúa.
    """
    lista2 = lista[::-1]
    if lista == lista2: 
        return True
    else:
        return False

def main():
    # Genera una lista de números aleatorios de 4 digitos.
    listaAzar = listaNrosAzar()
    print("Lista de números aleatorios:", listaAzar)    

    # Calcula la suma de los números en la lista.
    sumLista = sumaLista(listaAzar)
    print("La suma de los números de la lista es:", sumLista)

    # Elimina un número de la lista.
    numEliminar = int(input("Ingrese un número a eliminar de la lista: "))
    listaAzar = eliminarNumero(numEliminar, listaAzar)
    print("Lista después de eliminar el número:", listaAzar)

    # Verifica si la lista es capicúa.
    if esCapicua(listaAzar):
        print("La lista es capicúa.")
    else:
        print("La lista no es capicúa.")

if __name__ == "__main__":
    main()