"""
En  la  República  de  Elbonia  se  realizaron  recientemente  elecciones  primarias  tendientes  a 
renovar parcialmente las cámaras de representantes. Se presentaron varios partidos políti-
cos,  y  dentro  de  ellos  una  serie  de  alianzas  o  coaliciones  compitieron  para  alzarse  con  la 
victoria. Los resultados de la elección se encuentran en un archivo que contiene un registro 
por  cada  voto  escrutado.  El  archivo  tiene  formato  CSV  (valores  separados  por  punto  y 
coma). Cada registro está formado por el nombre de un partido político seguido por el nú-
mero de alianza que recibió el voto, por ejemplo:
Unidos Podemos;3
significa que  el partido  “Unidos  Podemos”  recibió  un voto  en  su  lista  N°  3.  La  cantidad de 
alianzas dentro de cada partido es variable, dependiendo de las corrientes internas de cada 
agrupación.
Se solicita escribir un programa para determinar los resultados finales de la elección. El par-
tido ganador será el que acumule más sufragios sin importar qué alianza haya recibido cada 
voto. Imprimir un gráfico de barras (representado por asteriscos) ordenado de mayor a me-
nor  según  el  porcentaje  de  votos  cosechado  por  cada  partido.  El  informe  debe  incluir  el 
nombre del mismo, el gráfico de barras y el porcentaje obtenido.
Además, y sólo para el partido más votado, deben desglosarse los votos obtenidos según la 
alianza  o  coalición, también  en  un  gráfico  de  barras  con  los  mismos  datos  anteriores  pero 
referido a las alianzas dentro del partido ganador. Ejemplo:
Unión del Pueblo ********** 54.32%
Unidad Republicana ***** 25.17%
Más País ** 12.01 %
[ . . . ]
Partido ganador: Unión del Pueblo
Lista 11 ******* 64.47%
Lista 7 **** 25.11%
Lista 19 * 3.33%
[ . . . ]
Se suministra un archivo a modo de ejemplo llamado RESULTADOS.TXT. El archivo no está 
ordenado  por  ningún  criterio  particular.  El  programa  debe  funcionar  para  este  archivo  o 
cualquier otro con la misma estructura
"""
import os

def leerVotos(nombreArchivo):
    rutaActual = os.path.dirname(__file__)
    rutaArchivo = os.path.join(rutaActual, nombreArchivo)
    votos = [] # lista de tuplas (partido, lista)
    try:
        with open(rutaArchivo, 'r') as arch:
            for linea in arch:
                if linea:
                    partido, lista = linea.strip().split(';')
                    votos.append((partido, lista)) 
        return votos  
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")

def contarVotos(listaTuplaVotos):
    conteo = {} 
    for partido, lista in listaTuplaVotos:
        conteo[partido] = conteo.get(partido, 0) + 1 # si no esta la clave se le inicializa el valor en 0 y se le suma 1
    return conteo

def mostrarGraficoBarras(diccionarioConteo, totalVotos):
    print(f'resultasdos de los partidos\n')

    elem = list(diccionarioConteo.items())

    for i in range(len(elem)):
        for j in range(i + 1, len(elem)):
            if elem[i][1] < elem[j][1]:
                elem[i], elem[j] = elem[j], elem[i]

    for partido, cantVotos in elem:
        porcentaje = (cantVotos / totalVotos) * 100
        asteriscos = '*' * int(porcentaje)
        print(f'{partido}\t{asteriscos} {porcentaje:.2f}%')

def main():
    dVotos = leerVotos('Resultados2.txt')
    diccionario = contarVotos(dVotos)
    print(mostrarGraficoBarras(diccionario, len(dVotos)))


if __name__ == "__main__":
    main()