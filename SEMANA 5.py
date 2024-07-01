# Programa para calcular el área de un triángulo
# utilizando base y altura proporcionadas por el usuario.

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.

    Parameters:
    base (float): La longitud de la base del triángulo.
    altura (float): La altura perpendicular a la base.

    Returns:
    float: El área calculada del triángulo.
    """
    area = 0.5 * base * altura  # Fórmula para calcular el área del triángulo
    return area


# Entrada de datos desde el usuario
base = float(input("Ingrese la longitud de la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Llamada a la función para calcular el área del triángulo
area_triangulo = calcular_area_triangulo(base, altura)

# Mostrar el resultado al usuario
print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo}")