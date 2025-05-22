"""
Escriba un programa que ingrese (por teclado) los datos de diez personas (nombre, edad, genero, dirección, teléfono), 
los almacene en un diccionario y los muestre. 
Al realizar dicha muestra, destacar la persona más joven en edad.
"""

def sacarMenor(lista):
    """
    obj: recorrer la lista de personas y mostrar la persona más joven del diccionario.
    entrada: lista de personas(diccionarios)
    salida: imprime la persona más joven
    """
    menor = lista[0]
    for elemento in lista:
        if elemento.get('edad') < menor.get('edad'):
            menor = elemento
    return menor

def main():
    personas = []
    while len(personas) < 3:
        nombre = input("ingrese el nombre de la persona: ")
        edad = int(input("ingrese la edad de la persona: "))
        genero = input("ingrese el genero de la persona: ")
        direccion = input("ingrese la direccion de la persona: ")
        telefono = input("ingrese el telefono de la persona: ")
        persona = {
            "nombre": nombre,
            "edad": edad,
            "genero": genero,
            "direccion": direccion,
            "telefono": telefono
        }
        personas.append(persona)
    
    print(f'\t\t persona mas joven: ')
    masJoven = sacarMenor(personas)
    print(f'\t\t{masJoven}')

if __name__ == "__main__":
    main()