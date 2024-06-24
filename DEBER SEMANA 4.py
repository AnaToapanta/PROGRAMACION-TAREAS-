# tienda.py

class Producto:
    """Clase que representa un producto en la tienda."""

    def _init_(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def _str_(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio}, stock={self.stock})"

    def actualizar_stock(self, cantidad):
        """Actualiza el stock del producto sumando la cantidad proporcionada."""
        self.stock += cantidad

    def vender(self, cantidad):
        """Reduce el stock en la cantidad vendida, si hay suficiente stock."""
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad


class Tienda:
    """Clase que representa una tienda."""

    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto a la tienda."""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra todos los productos disponibles en la tienda."""
        for producto in self.productos:
            print(producto)

    def vender_producto(self, nombre_producto, cantidad):
        """Vende un producto reduciendo su stock."""
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.vender(cantidad)
                print(f"Vendido {cantidad} de {producto.nombre}")
                return
        print(f"Producto {nombre_producto} no encontrado en la tienda")


# Ejemplo de uso
if __name__ == "_main_":
    tienda = Tienda()

    # Crear algunos productos
    p1 = Producto("Manzana", 0.7, 100)
    p2 = Producto("Naranja", 0.80, 80)
    p3 = Producto("Plátano", 0.5, 150)

    # Agregar productos a la tienda
    tienda.agregar_producto(p1)
    tienda.agregar_producto(p2)
    tienda.agregar_producto(p3)

    # Mostrar productos disponibles
    print("Productos disponibles en la tienda:")
    tienda.mostrar_productos()

    # Vender productos
    tienda.vender_producto("Manzana", 10)
    tienda.vender_producto("Plátano", 20)

    # Mostrar productos después de la venta
    print("\nProductos disponibles después de las ventas:")
    tienda.mostrar_productos()