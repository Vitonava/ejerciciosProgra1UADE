"""
Desarrolle un programa que procese una tabla con 10 horarios (hora -de 0 a 23- y minutos) en formato tupla; 
e indique por cada una de ellas: si es AM o PM y cuántos minutos falta para la próxima hora. 
El resultado de AM/PM y la cantidad de minutos se debe almacenar en una lista de tuplas con los valores originales y los resultados. 
Imprimir el resultado final en pantalla.
"""
def main():
    tuplaHorarios = (
        (10, 30) , (12, 0) , (23, 45) , (0, 15) ,
        (13, 0) , (2, 30) , (15, 45) , (4, 15) ,
        (5, 0) , (6, 30)
    )
    print("\t\tHorarios procesados:\n")
    resultados = []
    for horario in tuplaHorarios: # determinar si es AM o PM
        hora, minutos = horario
        if hora < 12:
            ampm = "AM"
        else:
            ampm = "PM"
        # determinar cuántos minutos faltan para la próxima hora
        minutos_faltan = 60 - minutos
        resultados.append((hora, minutos, ampm, minutos_faltan))
    for resultado in resultados:
        hora, minutos, ampm, minutos_faltan = resultado
        print(f"\t\t{hora}: {minutos} - {ampm} - restan {minutos_faltan} minutos para la próxima hora")



if __name__ == "__main__":
    main()  