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

# b. Determine si una nota está aprobada o no (mayor o igual que 4 aprueba). Retorna True por aprobado; False por desaprobado.
aprobado = lambda nota: nota >= 4

# c. Que dado un número invierta su signo (de positivo a negativo y viceversa)

invertir = lambda nro : nro*-1 

# d. Que dado un nombre determine si su longitud es larga (mayor de 10 caracteres). Retorna True o False.

esLarga = lambda nomAEvaluar: len(nomAEvaluar)>10

#e. Dado un valor numérico retorne True si es positivo o cero; False en caso contrario.

Positivo = lambda nro : nro>=0

#f. Escribe una función que tome dos argumentos: a y b y devuelva la multiplicación de ellos.
 
multiplicacion = lambda n1, n2: n1*n2

#g. Que compare dos valores y retorne True si el primer argumento es mayor que el segundo
esMayor = lambda n1,n2: n1>n2

def main():
    base = float(input("ingrese la base del rectángulo: "))
    altura = float(input("ingrese la altura del rectángulo: "))
    print(f'la superficie del rectángulo es: {supTrianguloRec(base, altura)%2}')  
    nota = float(input("ingrese la nota: "))
    print(f'la nota {nota} es aprobada: {aprobado(nota)}')
    nro = float(input("ingrese un número: "))
    print(f'el número {nro} invertido es: {invertir(nro)}')
    nombre = input("ingrese un nombre: ")
    print(f'el nombre {nombre} es largo: {esLarga(nombre)}')

    nro = float(input("ingrese un número: "))
    print(f'el número {nro} es positivo: {Positivo(nro)}')
    n1 = float(input("ingrese un número: "))
    n2 = float(input("ingrese otro número: "))
    print(f'la multiplicación de {n1} y {n2} es: {multiplicacion(n1, n2)}')
    n1 = float(input("ingrese un número: "))

if __name__ == "__main__":
    main()