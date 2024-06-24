# Programación Orientada a Objetos (POO)

class ClimaSemana:
    def _init_(self):
        self.temperaturas = []

    def ingresar_temperatura_diaria(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

    def calcular_promedio_temperatura_maxima(self):
        promedio_max = max(self.temperaturas)
        return promedio_max

    def calcular_promedio_temperatura_minima(self):
        promedio_min = min(self.temperaturas)
        return promedio_min

def main():
    clima_semana = ClimaSemana()
    print("Ingrese las temperaturas diarias para determinar el promedio semanal y promedios de temperatura máxima y mínima.")
    clima_semana.ingresar_temperatura_diaria()
    promedio_semanal = clima_semana.calcular_promedio_semanal()
    promedio_maximo = clima_semana.calcular_promedio_temperatura_maxima()
    promedio_minimo = clima_semana.calcular_promedio_temperatura_minima()

    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f} °C")
    print(f"El promedio de temperatura máxima es: {promedio_maximo:.2f} °C")
    print(f"El promedio de temperatura mínima es: {promedio_minimo:.2f} °C")

if __name__ == "_main_":
    main()

   #Define una clase ClimaSemana
    #que encapsula la lista
    #de temperaturas y métodos
    #para ingresar las  temperaturas
    #y calcular el promedio
    #semanal.Esto fomenta
    #el encapsulamiento y la
    #cohesión de los datos y
    #las operaciones  relacionadas.