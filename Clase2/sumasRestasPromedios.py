"""Algoritmo que reciba cuatro numeros y reporte la diferencia de los dos primeros, 
reporte el producto del tercero y el cuarto, y reporte el promedio de los cuatro
numeros"""

# Objetivo general: Reportar computos numericos del enunciado

# Algoritmo:
# 1. Almacenar los cuatro numeros en variables para procesar
# 2. Calcular la diferencia de los dos numeros y almacenarla
# 3. Calcular el producto del tercero y el cuarto
# 4. Calcular promedio de los cuatro numeros
# 5. Reportar resta
# 6. Reportar producto
# 7. Reportar promedio

# Traduccion

n1 = 1
n2 = 2
n3 = 3
n4 = 48

variable_1 = n1+n2
print("la suma de los dos primeros numeros es", variable_1)

variable_2 = n3*n4
print("el producto de los numeros 3 y 4 es", variable_2)

# la sumatoria y len reciben una coleccion por eso van los dobles parentesis
promedio = sum((n1, n2, n3, n4))/len((n1, n2, n3, n4))
print("el promedio de los numeros es", promedio)

# Reportar el promedio descartando el menor de los numeros

menor = min((n1, n2, n3, n4))
promedio = (sum((n1, n2, n3, n4)) - menor)/(len((n1, n2, n3, n4))-1)
promedio_round = round(promedio, 2)

print("el promedio de los numeros es", promedio)
print("el promedio redondeado es:", promedio_round)
