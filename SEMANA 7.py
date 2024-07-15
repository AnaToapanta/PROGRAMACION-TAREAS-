class Archivo:
    def _init_(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto para escritura.")

    def escribir(self, texto):
        self.archivo.write(texto + '\n')
        print(f"Escrito en archivo '{self.nombre_archivo}': {texto}")

    def _del_(self):
        self.archivo.close()
        print(f"Archivo '{self.nombre_archivo}' cerrado.")


class BaseDeDatos:
    def _init_(self, nombre_bd):
        self.nombre_bd = nombre_bd
        self.conectado = False
        self.conectar()

    def conectar(self):
        if not self.conectado:
            # Simula la conexión a la base de datos
            self.conectado = True
            print(f"Conectado a la base de datos '{self.nombre_bd}'.")

    def desconectar(self):
        if self.conectado:
            # Simula la desconexión de la base de datos
            self.conectado = False
            print(f"Desconectado de la base de datos '{self.nombre_bd}'.")

    def _del_(self):
        self.desconectar()


# Uso de la clase Archivo
archivo = Archivo('ejemplo.txt')
archivo.escribir('Hola, mundo!')
archivo.escribir('Esto es un ejemplo de uso de constructores y destructores en Python.')

# Uso de la clase BaseDeDatos
bd = BaseDeDatos('mi_base_de_datos')
# Aquí se realizarían operaciones con la base de datos

# Al final del script, los destructores (_del_) se llamarán automáticamente para limpiar recursos