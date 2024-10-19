import os

productos = []

def cargar_datos():
    if os.path.exists('productos.txt'):
        with open('productos.txt', 'r') as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })

def guardar_datos():
    with open('productos.txt', 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def añadir_producto():
    nombre = input('Introduce el nombre del producto: ')
    while True:
        try:
            precio = float(input('Introduce el precio del producto: '))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico válido para el precio.")
    
    while True:
        try:
            cantidad = int(input('Introduce la cantidad disponible: '))
            break
        except ValueError:
            print("Por favor, introduce un número entero válido para la cantidad.")
    
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos disponibles.")

def actualizar_producto():
    nombre = input('Introduce el nombre del producto que deseas actualizar: ')
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']}")
            print("Deja el campo en blanco si no quieres modificarlo.")
            
            nuevo_nombre = input(f"Introduce el nuevo nombre [{producto['nombre']}]: ").strip() or producto['nombre']
            
            while True:
                try:
                    nuevo_precio = input(f"Introduce el nuevo precio [{producto['precio']}]: ").strip()
                    nuevo_precio = float(nuevo_precio) if nuevo_precio else producto['precio']
                    break
                except ValueError:
                    print("Por favor, introduce un valor numérico válido para el precio.")
            
            while True:
                try:
                    nueva_cantidad = input(f"Introduce la nueva cantidad [{producto['cantidad']}]: ").strip()
                    nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto['cantidad']
                    break
                except ValueError:
                    print("Por favor, introduce un número entero válido para la cantidad.")
            
            producto.update({'nombre': nuevo_nombre, 'precio': nuevo_precio, 'cantidad': nueva_cantidad})
            print(f"Producto '{nombre}' actualizado correctamente.")
            return
    print(f"No se encontró un producto con el nombre '{nombre}'.")

def eliminar_producto():
    nombre = input('Introduce el nombre del producto que deseas eliminar: ')
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"No se encontró un producto con el nombre '{nombre}'.")

def menu():
    cargar_datos()
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()
