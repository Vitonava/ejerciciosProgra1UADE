"""1.  Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30).
Debes usar una matriz para su parametrización y una función para la recuperación del dato."""

def diasMes(mes):
    """Devuelve la cantidad de días del mes indicado usando una matriz."""
    # Matriz con [número de mes, días]
    matriz_meses = [
        [1, 31],
        [2, 28],
        [3, 31],
        [4, 30],
        [5, 31],
        [6, 30],
        [7, 31],
        [8, 31],
        [9, 30],
        [10, 31],
        [11, 30],
        [12, 31]
    ]
    for fila in matriz_meses:
        if fila[0] == mes:
            return fila[1]
    return "Mes inválido"
    
def main():
    mes = int(input("Ingrese un número de mes (1-12): "))
    dias = diasMes(mes)
    if isinstance(dias, str):
        print(dias)
    else:
        print(f"El mes {mes} tiene {dias} días.")

if __name__ == "__main__":  
    main()