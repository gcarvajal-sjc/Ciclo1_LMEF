'''
Se calculan las tres distancias usando la funcion de
distancia euclidiana.
Se saca el promedio de las tres distancias
Se calcula la distancia min
Se calcula la distancia max
'''

import libreriaGeomArit as lg

# Calcular la primera distancia
d1_2 = lg.distanciaEuclidiana(3, 4, 6, 6)

# Calcular la segunda distancia
d2_3 = lg.distanciaEuclidiana(6, 6, 7, 8)

# Calcular la tercera distancia
d3_4 = lg.distanciaEuclidiana(7, 8, 6, 5.5)

# Calcular promedio
promedio = lg.suma3Valores(d1_2, d2_3, d3_4)/len((d1_2, d2_3, d3_4))
print('promedio', promedio)

# Calcular distancia min
distanciaMin = min((d1_2, d2_3, d3_4))
print('distancia min', distanciaMin)

# Calcular distancia max
distanciaMax = max((d1_2, d2_3, d3_4))
print('distancia max', distanciaMax)
