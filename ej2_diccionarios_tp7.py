"""
Escriba un programa que ingrese (por teclado) los datos de diez personas (nombre, edad, genero, dirección, teléfono), 
los almacene en un diccionario y los muestre. 
Al realizar dicha muestra, destacar la persona más joven en edad.
"""

def main():
    personas = {}
    while len(personas) < 3:
        nombre = input("ingrese el nombre de la persona: ")
        edad = int(input("ingrese la edad de la persona: "))
        genero = input("ingrese el genero de la persona: ")
        direccion = input("ingrese la direccion de la persona: ")
        telefono = input("ingrese el telefono de la persona: ")
        personas[nombre] = {
            "edad": edad,
            "genero": genero,
            "direccion": direccion,
            "telefono": telefono
        }
    print(f'\t\t persona mas joven: ')
    for nombre, datos in personas.items():
        edad = datos["edad"]
        if edad == min([datos["edad"] for datos in personas.values()]):
            print(f'\t\t{nombre} - {datos}')

if __name__ == "__main__":
    main()