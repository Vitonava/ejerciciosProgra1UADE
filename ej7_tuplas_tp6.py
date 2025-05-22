"""
Cálculo de áreas: crea un programa que lea una lista de tuplas, donde cada tupla contiene el nombre de una figura geométrica (cuadrado, rectángulo, triángulo y círculo) y sus dimensiones, y calcule el área de cada figura. Por ejemplo, si llamamos a la función con la lista de tuplas [('cuadrado', 4), ('rectángulo', 5, 10), ('triángulo', 6, 8), ('círculo', 3)], la función devolverá la lista [( 'cuadrado', 16), ('rectángulo', 50), ('triángulo', 24), ('círculo', 28.27)], que contiene el nombre de cada figura y su área en forma de tuplas.
"""
def calcularArea(figura):
    """
    objetivo: calcular el area de cada figura.
    entrada: figura con su nombre y dimensiones.
    salida: tupla con el nombre de la figura y su area.
    """
    if figura[0].strip() == 'cuadrado':
        lado = figura[1]
        area = lado ** 2
    elif figura[0].strip() == 'rectangulo':
        base = figura[1]
        altura = figura[2]
        area = base * altura
    elif figura[0].strip() == 'triangulo':
        base = figura[1]
        altura = figura[2]
        area = (base * altura)/2
    elif figura[0].strip() == 'circulo':
        radio = figura[1]
        area = 3.14 * (radio**2)
    else:
        area = 0
    return (figura[0], round(area, 2))


def main():
    listaFiguras = [('cuadrado', 4), ('rectangulo', 5, 10), ('triangulo', 6, 8), ('circulo', 3)]
    listaAreas = []
    for fig in listaFiguras:
        area = calcularArea(fig)
        listaAreas.append(area)
    print(f'\t\tLista de figuras:\n{listaFiguras}')
    print(f'\n')
    print(f'\t\tLista con áreas:\n{listaAreas}')



if __name__ == '__main__':
    main()  