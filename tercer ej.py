"""
Desarrollar cada una de las siguientes funciones y escribir un programa principal que permita verificar el funcionamiento de las mismas
Cargar una lista con números al azar de cuatro digitos. La cantidad de elementos también debe ser ingresado por el usuario
Calcular y devolver el producto de todos elementos de la lista
Eliminar todos las apariciones de un elemento de la lista. No utilizar listas auxiliares. El elemento a eliminar se recibe por teclado
Determinar si una lista es capicua
"""
import random

def listaAzar(c):
    """obj: generar una lsita con n numeros al azar"""
    l = []
    while len(l) <= c:
        l.append(random.randint(1000,9999))
    
    return l

"""def esCapicua(l):"""
    

def main():
    cant = int(input("ingrese la cantidad de elementos de la lista: "))
    lista = listaAzar(cant)
    print(lista)
    #calculo el producto de los elementos
    prod = 1
    for elemento in lista:
        prod = prod * elemento
    print(prod)
    
    eliminar = int(input("ingrese un numero a eliminar: "))
    
    for numero in lista:
        if numero == eliminar:
            lista.remove(numero)
            
    print(lista)
    
if __name__ == '__main__':
    main()