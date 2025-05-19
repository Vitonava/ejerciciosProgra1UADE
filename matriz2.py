"""
Suma de Filas y Columnas: crear una función que tome una matriz como entrada y
devuelva una lista con la suma de cada fila y otra lista con la suma de cada columna.
"""
def suma_filas_columnas(matriz):
    """Devuelve la suma de cada fila y cada columna de la matriz, sin usar sum()."""
    suma_filas = []
    suma_columnas = [0] * len(matriz[0])

    for fila in matriz:
        suma_fila = 0
        for i in range(len(fila)):
            suma_fila += fila[i]
            suma_columnas[i] += fila[i]
        suma_filas.append(suma_fila)

    return suma_filas, suma_columnas

def main():     
    # Definimos una matriz de ejemplo
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    suma_filas, suma_columnas = suma_filas_columnas(matriz)
    
    print("Suma de filas:", suma_filas)
    print("Suma de columnas:", suma_columnas)
if __name__ == "__main__":
    main()