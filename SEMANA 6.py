# Definición de la Clase Vehículo (superclase)
class Vehiculo:
    def init(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.modelo = modelo  # Atributo público
        self.__precio = 0  # Atributo privado inicializado en 0

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.__precio}")


# Definición de la Clase Coche (subclase que hereda de Vehículo)
class Coche(Vehiculo):
    def init(self, marca, modelo, puertas):
        super().init(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        print(
            f"Coche - Marca: {self.marca}, Modelo: {self.modelo}, Puertas: {self.puertas}, Precio: ${self.get_precio()}")


# Definición de la Clase Motocicleta (subclase que hereda de Vehículo)
class Motocicleta(Vehiculo):
    def init(self, marca, modelo, cilindrada):
        super().init(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        print(
            f"Motocicleta - Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada}, Precio: ${self.get_precio()}")


# Creación de objetos y demostración de polimorfismo
if __name__ == "main":
    # Creación de objetos de tipo Coche y Motocicleta
    coche1 = Coche("Toyota", "Corolla", 4)
    coche1.set_precio(25000)

    moto1 = Motocicleta("Honda", "CBR600RR", "600cc")
    moto1.set_precio(12000)

    # Llamada a método mostrar_info de cada objeto
    coche1.mostrar_info()
    moto1.mostrar_info()