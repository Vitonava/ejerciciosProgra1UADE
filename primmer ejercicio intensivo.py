def main():
    listanros = [1,5,6,7,12,23,54,100]
    suma = 0
    
    for nro in listanros:
        suma = suma + nro
    print (f'suma de los numeros en lista = {suma}')
    
    #calculo el promedio
    prom = (suma*len(listanros)) / 100
    
    print(f'el promedio de los numeros leidos es: {prom}')
    
    print(f'numeros mayores al promedio')
    
    for elemento in listanros:
        if elemento > prom:
            print(elemento)
    
if __name__ == '__main__':
    main()