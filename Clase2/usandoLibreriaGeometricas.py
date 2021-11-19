from libreriaGeometricas import distanciaEuclidiana # aca esto hace que no tengo que usar el alias y usar el punto junto a la funcion
import libreriaGeometricas as lg

altura = 12
base = 20

print("El area del triangulo es", lg.areaTriangulo(base, altura))
print("El area del circulo es", lg.areaCirculo(12))
print("La distancia euclidiana es", distanciaEuclidiana(45, 2, 3, 1))
