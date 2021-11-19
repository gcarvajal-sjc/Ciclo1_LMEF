# Definir una funcion que retorna una variable booleana True si el año
# es bisiesto, o false si no es bisiesto.

# Algoritmo
# 1. Recibir año e inicializar la variable como False, asumiendo que el anio no es bisiesto
# 2. Mirar si anio/4 es modulo 0 entonces va al paso 3 sino va al paso 6.
# 3. MIrar si anio/100 es modulo 0 entonces va al paso 4 sino va al paso 6.
# 4. Mirar si anio/400 es modulo 0 entonces va al paso 5 sino va al paso 6.
# 5. Mirar si la bandera de la variable anio es True, si si entonces retorna el anio es bisiesto
# 6. Si el valor de la bandera de la variable anio es False, entonces retorna el anio no es bisiesto


from typing import Tuple


def calcularBisiesto(anio):
    aniobisiesto = False

    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                aniobisiesto = True
        else:
            aniobisiesto = True

    if aniobisiesto == True:
        return f"El anio {anio} es bisiesto"
    else:
        return f"El anio {anio} no es bisiesto"


print(calcularBisiesto(2020))
print(calcularBisiesto(2800))
print(calcularBisiesto(2400))
print(calcularBisiesto(2000))
print(calcularBisiesto(2500))
print(calcularBisiesto(2300))
