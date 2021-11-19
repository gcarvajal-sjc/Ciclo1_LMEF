# Funcion para calcular el area del circulo
def areaCirculo(radio):
    pi = 3.1416
    radioCuadrado = radio**2
    area = pi*radioCuadrado
    return area

# Funcion para calcular la distancia entre dos puntos del plano cartesiano


def distanciaEuclidiana(X1, Y1, X2, Y2):
    resultado = (((X2-X1) ** 2) + ((Y2-Y1)**2)) ** (1/2)
    return resultado

# Funcion para calcular el area del triangulo


def areaTriangulo(base, altura):
    formula = (base*altura)/2
    return formula
