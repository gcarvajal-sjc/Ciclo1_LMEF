# Definir una funcion que calcula el area del circulo

def areaCirculo(radio):
    pi = 3.1416
    radioCuadrado = radio**2
    area = pi*radioCuadrado
    return area


area = round(areaCirculo(9), 2)
print("El area del circulo es", area)
