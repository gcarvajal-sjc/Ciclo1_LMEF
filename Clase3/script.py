# Algoritmo para probar las funciones de la libreriaGeomArit

from libreriaGeomArit import suma3Valores as s3
from libreriaGeomArit import diferencia3Valores as d3

# Primero probar la funcion de suma de tres numeros

print("La suma de los tres numeros es", s3(3, 4, 5))

# Podemos enviar parametros por nombre

print(s3(b=9, c=3, a=3))  # aca manda los parametros por nombre

# aca manda los parametros por posicion. No bota error porque el valor de c=0 que viene de la libreria
print(s3(23, 43))

# Segundo probar la funcion de diferencia de tres numeros

print(d3(4, 5, 6))

print(d3(23, 43))

print(d3(c=9, a=18))
