"""
Mayor Elemento por Columna: implementar una función que tome una matriz como entrada y
devuelva una lista con los mayores elementos de cada columna
"""

def encontrarMayorPorColumna(matriz):
    """Devuelve una lista con el mayor elemento de cada columna de la matriz."""
    if len(matriz) == 0:
        return 'no hay elementos en la matriz'
    
    listaMayores = []  
    for i in range(len(matriz[0])):  # Iterar sobre cada columna
        mayor = matriz[0][i] # Primer elemento de la columna
        for j in range(1, len(matriz)):
            if matriz[j][i] > mayor:
                mayor = matriz[j][i]
        listaMayores.append(mayor)
    return listaMayores

def main(): 
    # Definimos una matriz de ejemplo
    matriz = [
        [100, 285, 314],
        [4, 5888, 6],
        [70, 85, 911]
    ]
    
    mayores = encontrarMayorPorColumna(matriz)
    
    print("Mayores elementos por columna:", mayores)
if __name__ == "__main__":
    main() 