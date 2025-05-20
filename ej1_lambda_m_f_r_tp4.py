"""
1. Crear funciones lambda que resuelvan las siguientes problemáticas:

a. Calcule la superficie de un rectángulo

b. Determine si una nota está aprobada o no (mayor o igual que 4 aprueba). Retorna True por aprobado; False por desaprobado.

c. Que dado un número invierta su signo (de positivo a negativo y viceversa)

d. Que dado un nombre determine si su longitud es larga (mayor de 10 caracteres). Retorna True o False.

e. Dado un valor numérico retorne True si es positivo o cero; False en caso contrario.

f. Escribe una función que tome dos argumentos: a y b y devuelva la multiplicación de ellos.

g. Que compare dos valores y retorne True si el primer argumento es mayor que el segundo
"""
# a. Calcule la superficie de un rectángulo
supTrianguloRec = lambda base, altura : (base*altura)/2

def main():
    base = float(input("ingrese la base del rectángulo: "))
    altura = float(input("ingrese la altura del rectángulo: "))
    print(f'la superficie del rectángulo es: {supTrianguloRec(base, altura)%2}')  

if __name__ == "__main__":
    main()