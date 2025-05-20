def sumarElementos(mat):
    """
    obj: sumar los elementos de la segunda columna
    entrada: matriz
    salid: suma de los elmentos de la columna
    """
    suma = 0
    for fila in mat:
        suma += fila[1]
    return suma
            

def main():
    matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    
    print(f'suma de las columnas del medio: {sumarElementos(matriz)}')
    


if __name__ == '__main__':
    main()