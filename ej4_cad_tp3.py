def detLong(palabra):
    cantidad = 0
    for letra in palabra:
        if (letra.isalnum()):
            cantidad += 1
    return cantidad

def filtrarPalabras(cadena, cantCar):
    lPalabras = cadena.split()
    
    cadFinal = [palabra for palabra in lPalabras if detLong(palabra)>= cantCar]
    
    return " ".join(cadFinal)

def main():
    c = input("ingrese una cadena de caracteres: ")
    n = int(input("ingrese la cantidad de letras que deben tener las palabras"))
    print(f'las palabras filtradas son: {filtrarPalabras(c,n)}')
if __name__ == '__main__':
    main()