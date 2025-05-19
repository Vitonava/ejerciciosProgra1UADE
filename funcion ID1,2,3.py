"""
Crear una lista y asignarla a otra variable diferentes. Luego, imprimir los IDs de ambas
variables y comprobar si son iguales o diferentes. ¿Qué puedes concluir sobre el comportamiento de Python en este caso?
 
Crear una función que reciba dos números enteros como parámetros. Ambos valores recibidos como parámetros se deben modificar.
Imprimir los IDs de ambos números antes, durante y después de la llamada a la función.
¿Cuál es la relación entre los IDs antes y después de la llamada a la función?
 
Crear una función que reciba una lista como parámetro.
Dentro de la función, crear una nueva lista y asignarla a la variable original.
Imprimir los IDs de ambas listas antes y después de la asignación dentro de la función.
¿Qué puedes concluir sobre el comportamiento de Python en este caso?
"""
def main():
    lista1 = [1,2,3,6,4,8,7,4,9]
    lista2 = lista1
    
    print(id(lista1),id(lista2))

if __name__ == '__main__':
    main()