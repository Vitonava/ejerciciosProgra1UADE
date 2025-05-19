lista = [i**2 for i in range(1,5)] # Genera una lista de los cuadrados de los números del 1 al 4
print(lista) # Imprime la lista 

listaPares = [i**2 for i in range(1,10) if i % 2 == 0] # Genera una lista de los números pares del 1 al 9
print(listaPares) # Imprime la lista de números pares   


a = 55555

aCortado = a//10 # Divide el número por 10 y lo convierte a entero
print(aCortado) # Imprime el número cortado