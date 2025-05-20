"""
Escribir una función filtrarPalabras() que reciba una cadena de caracteres conteniendo una frase y un entero N,
y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original.
Escribir también un programa paraverificar el comportamiento de la misma.
"""
"""
def filtrarPalabras(cadena, cantCar):
    
    lPalabras = cadena.split()
    cadFinal = ""
    for palabra in lPalabras:
        if (len(palabra) >= cantCar):
            cadFinal += + " " + palabra
    return cadFinal"""

def detLong(palabra):
    cantidad = 0
    for letra in palabra:
        if (letra.isalNum()):
            cantidad += 1
    return cantidad

def filtrarPalabras(cadena, cantCar):
    lPalabras = cadena.split()
    
    cadFinal = [palabra for palabra in lPalabras if detLong(palabra)>= cantCar]
    
    return ",".join(cadfinal)

def main():
    c = input("ingrese una cadena de caracteres: ")
    n = int(input("ingrese la cantidad de letras que deben tener las palabras"))
    print(f'las palabras filtradas son: {filtrarPalabras(c,n)}')
if __name__ == '__main__':
    main()