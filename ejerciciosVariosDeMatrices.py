import random

# 1. Días del mes
def obtenerDiasDelMes(mes, matrizMeses):
    for i in range(len(matrizMeses)):
        if matrizMeses[i][0] == mes:
            return matrizMeses[i][1]

# 2. Crear y mostrar matriz aleatoria
def cargarMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(0, 100))
        matriz.append(fila)
    return matriz

def visualizarMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end="\t")
        print()

# 3. Suma de matrices
def sumaMatrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matrizResultante = []
    for i in range(filas):
        filaResultante = []
        for j in range(columnas):
            sumaElemento = matriz1[i][j] + matriz2[i][j]
            filaResultante.append(sumaElemento)
        matrizResultante.append(filaResultante)
    return matrizResultante

# 4. Producto escalar
def productoEscalar(matriz, numero):
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizResultante = []
    for i in range(filas):
        filaResultante = []
        for j in range(columnas):
            productoElemento = matriz[i][j] * numero
            filaResultante.append(productoElemento)
        matrizResultante.append(filaResultante)
    return matrizResultante

# 5. Suma de filas y columnas
def sumarFilasYColumnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    sumasFila = []
    sumasColumna = [0] * columnas
    for i in range(filas):
        suma = 0
        for s in range(len(matriz[i])):
            suma += matriz[i][s]
        sumasFila.append(suma)
        for j in range(columnas):
            sumasColumna[j] += matriz[i][j]
    return sumasFila, sumasColumna

# 6. Mayor elemento por columna
def encontrarMayoresPorColumna(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    mayoresPorColumna = []
    for j in range(columnas):
        mayor = matriz[0][j]
        for i in range(1, filas):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
        mayoresPorColumna.append(mayor)
    return mayoresPorColumna

# 7. Frases por fila
def obtenerFrases(matriz):
    frases = []
    for fila in range(len(matriz)):
        frase = ''
        for columna in range(len(matriz[fila])):
            frase += matriz[fila][columna] + ' '
        frases.append(frase.strip())
    return frases

# 8. Buscar palabra en matriz
def buscarPalabra(matriz, palabra):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == palabra:
                return True
    return False

# Ejemplo de uso de cada función
def main():
    print("1. Días del mes:")
    mes = 4
    matrizMeses = [
    [1, 31],  # Enero
    [2, 28],  # Febrero
    [3, 31],  # Marzo
    [4, 30],  # Abril
    [5, 31],  # Mayo
    [6, 30],  # Junio
    [7, 31],  # Julio
    [8, 31],  # Agosto
    [9, 30],  # Septiembre
    [10, 31], # Octubre
    [11, 30], # Noviembre
    [12, 31]  # Diciembre
    ]
    print(f"El mes {mes} tiene {obtenerDiasDelMes(mes, matrizMeses)} días.\n")

    print("2. Matriz aleatoria:")
    matrizAleatoria = cargarMatriz(3, 4)
    visualizarMatriz(matrizAleatoria)
    print()

    print("3. Suma de matrices:")
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matriz2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    resultadoSuma = sumaMatrices(matriz1, matriz2)
    visualizarMatriz(resultadoSuma)
    print()

    print("4. Producto escalar:")
    resultadoEscalar = productoEscalar(matriz1, 2)
    visualizarMatriz(resultadoEscalar)
    print()

    print("5. Suma de filas y columnas:")
    sumasFilas, sumasColumnas = sumarFilasYColumnas(matriz1)
    print("Sumas de filas:", sumasFilas)
    print("Sumas de columnas:", sumasColumnas)
    print()

    print("6. Mayor elemento por columna:")
    matrizEjemplo = [
        [8, 12, 9],
        [14, 6, 17],
        [3, 15, 7]
    ]
    mayoresColumnas = encontrarMayoresPorColumna(matrizEjemplo)
    print("Mayores elementos por columna:", mayoresColumnas)
    print()

    print("7. Frases por fila:")
    matrizFrases = [
        ['Hola', 'cómo', 'estás'],
        ['Estoy', 'bien', 'gracias']
    ]
    print(obtenerFrases(matrizFrases))
    print()

    print("8. Buscar palabra en matriz:")
    print(buscarPalabra(matrizFrases, 'bien'))  # True
    print(buscarPalabra(matrizFrases, 'adiós')) # False

if __name__ == "__main__":
    main()