# Programación Tradicional

import statistics


def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


def calcular_desviacion_estandar(temperaturas):
    desviacion = statistics.stdev(temperaturas)
    return desviacion


def main():
    print("Ingrese las temperaturas diarias para determinar el promedio semanal y la desviación estándar.")
    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    desviacion = calcular_desviacion_estandar(temperaturas)

    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")
    print(f"La desviación estándar de las temperaturas es: {desviacion:.2f} °C")


if __name__ == "_main_":
    main()

#Utiliza funciones separadas (ingresar_temperaturas_diarias y calcular_promedio_semanal)
#para manejar la entrada de datos y el cálculo del promedio.
#La lógica está organizada en funciones que se llaman secuencialmente
#desde la función main().