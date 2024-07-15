import os

class Inventario:
    def _init_(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde el archivo."""
        if not os.path.isfile(self.archivo):
            # Si el archivo no existe, crea uno vacío
            open(self.archivo, 'w').close()
            return

        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    nombre, cantidad = linea.strip().split(',')
                    self.productos[nombre] = int(cantidad)
        except FileNotFoundError:
            print("El archivo de inventario no se encontró. Se creará un nuevo archivo.")
        except PermissionError:
            print("No se tienen permisos para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda el inventario en el archivo."""
        try:
            with open(self.archivo, 'w') as file:
                for nombre, cantidad in self.productos.items():
                    file.write(f"{nombre},{cantidad}\n")
        except PermissionError:
            print("No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, nombre, cantidad):
        """Añade un producto al inventario."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()
        print(f"Producto '{nombre}' añadido exitosamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def actualizar_producto(self, nombre, cantidad):
        """Actualiza la cantidad de un producto en el inventario."""
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado exitosamente.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")