class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre  # Atributo protegido (con un guion bajo)
        self._precio = precio  # Atributo protegido (con un guion bajo)
        self._cantidad = cantidad  # Atributo protegido (con un guion bajo)

    def obtener_precio(self):
        return self._precio

    def obtener_nombre(self):
        return self._nombre

    def obtener_cantidad(self):
        return self._cantidad

    def mostrar_info(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla 

    def mostrar_info(self):
        return f"{self._nombre} - Talla: {self._talla}, Precio: ${self._precio}, Stock: {self._cantidad}"

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla 

    def mostrar_info(self):
        return f"{self._nombre} - Talla: {self._talla}, Precio: ${self._precio}, Stock: {self._cantidad}"

class Inventario:
    def __init__(self):
        self._prendas = [] 

    def agregar_prenda(self, prenda):
        self._prendas.append(prenda)

    def mostrar_inventario(self):
        print("Inventario disponible:")
        for prenda in self._prendas:
            print(prenda.mostrar_info())

camisa_hombre = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon_hombre = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
falda_mujer = RopaMujer("Falda de Mujer", 28.00, 15, "S")
blusa_mujer = RopaMujer("Blusa de Mujer", 22.00, 40, "M")
zapatos_hombre = RopaHombre("Zapatos de Hombre", 60.00, 25, "42")
zapatos_mujer = RopaMujer("Zapatos de Mujer", 50.00, 20, "38")

inventario = Inventario()
inventario.agregar_prenda(camisa_hombre)
inventario.agregar_prenda(pantalon_hombre)
inventario.agregar_prenda(falda_mujer)
inventario.agregar_prenda(blusa_mujer)
inventario.agregar_prenda(zapatos_hombre)
inventario.agregar_prenda(zapatos_mujer)

inventario.mostrar_inventario()

def procesar_compra(inventario):
    total = 0
    while True:
        nombre_producto = input("Ingrese el nombre del producto que desea comprar (o 'salir' para finalizar): ")
        if nombre_producto.lower() == 'salir':
            break
        cantidad = int(input(f"¿Cuántos {nombre_producto} desea comprar? "))
        
        encontrado = False
        for prenda in inventario._prendas:
            if prenda.obtener_nombre().lower() == nombre_producto.lower():
                if prenda.obtener_cantidad() >= cantidad:
                    prenda._cantidad -= cantidad  # Reducir el stock
                    total += prenda.obtener_precio() * cantidad
                    print(f"Compra realizada: {cantidad} {prenda.obtener_nombre()} por ${prenda.obtener_precio() * cantidad}")
                    encontrado = True
                else:
                    print(f"No hay suficiente stock de {nombre_producto}. Stock disponible: {prenda.obtener_cantidad()}")
                break

        if not encontrado:
            print(f"Producto {nombre_producto} no encontrado.")
    
    print(f"Total de la compra: ${total}")

procesar_compra(inventario)
