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


# Funcion para calcular el area del cuadrado

def areaCuadrado(lado):
    formula = lado**2
    return formula


def promedio4(valor1, valor2, valor3, valor4):
    promedio = sum((valor1, valor2, valor3, valor4)) / \
        len((valor1, valor2, valor3, valor4))
    promedio = round(promedio, 2)
    return promedio


def suma3Valores(a=0, b=0, c=0):  # aca estamos dando un valor predeterminado a las variables
    sumatoria = a+b+c
    return sumatoria


def diferencia3Valores(a=0, b=0, c=0):
    diferencia = a-b-c
    return diferencia
