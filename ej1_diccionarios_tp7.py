"""
Desarrolle un programa que almacene datos de canciones en formato MP3: 
Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). 
Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. 
Debe interrumpirse la carga cuando el artista ingresado sea vacío.
"""

def main():
    canciones = {}
    salida = True
    while salida:
        artista = input("Ingrese el nombre del artista (o presione Enter para salir): ")
        if artista == "":
            salida = False
        else:
            titulo = input("Ingrese el título de la canción: ")
            duracion = int(input("Ingrese la duración de la canción (en segundos): "))
            tamano = int(input("Ingrese el tamaño del fichero (en KB): "))
            canciones[artista] = (titulo, duracion, tamano)
            
    print("\n\t\tDatos de las canciones ingresadas:\n")
    for artista, datos in canciones.items():
        titulo, duracion, tamano = datos
        print(f"\t\tArtista: {artista}")
        print(f"\t\tTítulo: {titulo}")
        print(f"\t\tDuración: {duracion} segundos")
        print(f"\t\tTamaño: {tamano} KB")
        print("\n")

    
if __name__ == "__main__":
    main()