"""
Desarrolle un programa que almacene datos de canciones en formato MP3: 
Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). 
Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. 
Debe interrumpirse la carga cuando el artista ingresado sea vacío.
"""
def genCanciones():
    """
    Genera una lista de canciones con datos aleatorios.
    """
    canciones = []
    artista = input("Ingrese el nombre del artista (o presione Enter para salir): ")
    while artista != "":
        cancion = {}
        cancion["artista"] = artista
        cancion["titulo"] = input("Ingrese el título de la canción: ")
        cancion["duracion"] = float(input("Ingrese la duración de la canción (en segundos): "))
        cancion["tamaño"] = int(input("Ingrese el tamaño del fichero (en KB): "))
        canciones.append(cancion)
        artista = input("Ingrese el nombre del artista (o presione Enter para salir): ")
    return canciones

def main():
    """
    Función principal que ejecuta el programa.
    """
    canciones = genCanciones()
    print(f'\t\tDatos de las canciones ingresadas:\n')
    for cancion in canciones:
        print(f"\t\tArtista: {cancion['artista']}")
        print(f"\t\tTítulo: {cancion['titulo']}")
        print(f"\t\tDuración: {cancion['duracion']} segundos")
        print(f"\t\tTamaño: {cancion['tamaño']} KB")
        print("\n")

if __name__ == "__main__":
    main()