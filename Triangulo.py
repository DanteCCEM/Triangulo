import math


def calcular_area_triangulo(lado1, lado2, lado3):
    # Calcula el semiperímetro
    s = (lado1 + lado2 + lado3) / 2

    # Calcula el área usando la fórmula de Herón
    area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

    return area
