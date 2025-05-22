"""
Se debe gestionar los datos de stock de una tienda de comestibles, la información a recoger será: nombre del producto, precio, cantidad en stock. La tienda dispone de 10 productos distintos. El programa debe ser capaz de:

§ Dar de alta un producto nuevo.

§ Buscar un producto por su nombre.

§ Modificar el stock y precio de un producto dado.
"""
def buscarProd(nombre, productos):
    """
    objetivo: buscar un producto por su nombre
    entrada: nombre del producto y diccionario de productos
    salida: diccionario del producto si se encuentra, None si no se encuentra
    """
    return productos.get(nombre.lower())

def modificarDatos(prod):
    """
    objetivo: modificar el stock y precio de un producto dado
    entrada: diccionario del producto dado
    salida: producto modificado (diccionario)
    """
    nuevoPrecio = float(input("Ingrese el precio nuevo del producto: "))
    nuevoStock = int(input("Ingrese el stock nuevo del producto: "))
    prod['precio'] = nuevoPrecio
    prod['stock'] = nuevoStock
    return prod

def main():
    productos = {}  # clave: nombre (en minúsculas), valor: {'precio': float, 'stock': int}
    while len(productos) < 3:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible en stock: "))
        productos[nombre.lower()] = {'nombre': nombre, 'precio': precio, 'stock': cantidad}
    print(f'\t\tDatos de los productos ingresados:\n')
    for prod in productos.values():
        print(f"\t\tNombre: {prod['nombre']}")
        print(f"\t\tPrecio: {prod['precio']}")
        print(f"\t\tCantidad en stock: {prod['stock']}")
        print("\n")
    
    nombreProducto = input("ingrese el nombre del producto a buscar: ")
    prodBuscado = buscarProd(nombreProducto, productos)
    if prodBuscado:
        print(f'\t\tProducto encontrado:\n')
        print(f"\t\tNombre: {prodBuscado['nombre']}")
        print(f"\t\tPrecio: {prodBuscado['precio']}")
        print(f"\t\tCantidad en stock: {prodBuscado['stock']}")
        print("\n")
        modificar = input("¿Desea modificar el stock y precio del producto? (si/no): ")
        if modificar.strip().lower() == 'si':
            nuevoProd = modificarDatos(prodBuscado)
            print(f'\t\tProducto modificado:\n')
            print(f"\t\tNombre: {nuevoProd['nombre']}")
            print(f"\t\tPrecio: {nuevoProd['precio']}")
            print(f"\t\tCantidad en stock: {nuevoProd['stock']}")
            print("\n")
        else:
            print("\t\tNo se realizaron modificaciones.")
    else:
        print("\t\tProducto no encontrado")
    
if __name__ == "__main__":
    main()
