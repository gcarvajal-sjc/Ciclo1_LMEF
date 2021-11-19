# Distancia entre dos puntos del plano cartesiano

# def nombreFuncion(listadoParametros):
# pass

def distanciaEuclidiana(X1, Y1, X2, Y2):
    resultado = (((X2-X1) ** 2) + ((Y2-Y1)**2)) ** (1/2)
    return resultado


print("La distancia euclidiana de los puntos del plano cartesiano es",
      distanciaEuclidiana(2, 3, 4, 5))

formula = distanciaEuclidiana(4, 59, 16, 7)
print("La distancia euclidiana de los puntos del plano cartesiano es", formula)

X1 = 23
X2 = 34
Y1 = 3
Y2 = 9

formula = distanciaEuclidiana(X1, X2, Y1, Y2)
print("La distancia euclidiana de los puntos del plano cartesiano es", formula)
