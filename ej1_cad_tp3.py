"""
Desarrollar una función que determine si una cadena de caracteres es capicúa. 
Escribir además un programa que permita verificar su funcionamiento solicitándole 
al usuario valores hasta que el mismo sea vacío.
"""

def es_capicua(texto): 
    """
    obj: determinar si una cadena de caracteres es capicúa
    entrada(parametro): cad de caracteres
    salida: True o False
    """
    if texto == texto[::-1]:
        return True
    else: 
        return False
    
def main():
    cad = input("ingrese un texto: ")

    while len(cad) > 0:
        if es_capicua(cad):
            print(f'la cadena: {cad} es capicua')
        else: 
            print(f'la cadena: {cad} no es capicua')        
        cad = input("ingrese otro texto: ")

if __name__ == "__main__": 
    main()