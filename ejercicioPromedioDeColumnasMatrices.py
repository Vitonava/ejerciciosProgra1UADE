"""
**c)** Escribe una función que reciba una matriz y devuelva una lista con el promedio de cada columna.
"""
def promColumnas(mat):
    """
    obj: devover el promedio de cada una de las columnas.
    entrada: matriz
    salida: lista con promedios 
    """
    prom = []
    for columna in range(len(mat[0])): # esto recorre las columnas, len(mat[0]) es la cantidad de columnas en este caso 3
        total = 0  # Reiniciar total para cada columna
        for fila in mat: # esto recorre las filas
            total += fila[columna]
        promedio = total / len(mat)
        prom.append(promedio)
    return prom

def main():
    matriz = [
    [1, 2,3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    promedios = promColumnas(matriz)
    print(f'promedio de las columnas: \ncol 1: {promedios[0]}\ncol 2: {promedios[1]}\ncol 3: {promedios[2]}')
    
if __name__ == '__main__':
    main()