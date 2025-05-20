"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra", cuya longitud no se conoce. 
Realizar un programa para obtener ambas claves, donde la primera se construye con los dígitos ubicados en posiciones impares de la clave maestra 
y la segunda con los dígitos ubicados en posiciones pares. Los dígitos se numeran desde la izquierda. 
Ejemplo: Si clave maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89
"""

def obtenerClave1(claveMaestra):
    """
    obj: devolver posiciones pares de la clave maestra
    entrada(parametro): clave maestra
    salida: clave 1
    """
    clave1 = claveMaestra[::2]
    return clave1

def obtenerClave2(claveMaestra):
    """ 
    obj: devolver posiciones impares de la clave maestra
    entrada(parametro): clave maestra
    salida: clave 2
    """
    clave2 = claveMaestra[1::2]
    return clave2

def main(): 
    claveM = input("ingrese la clave maestra: ")

    while claveM != "": 
        if claveM.isdigit():
            c1 = obtenerClave1(claveM)
            c2 = obtenerClave2(claveM)
            print(f'la clave 1 es: {c1}')
            print(f'la clave 2 es: {c2}')
        else:
            print("la clave maestra no puede contener letras...")
        claveM = input("ingrese otra clave maestra: ")

if __name__ == '__main__': 
    main()