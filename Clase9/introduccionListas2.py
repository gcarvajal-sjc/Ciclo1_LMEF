# Se va a incluir al requerimeinto del 'introduccionListas.py
# "saber a cual de las entradas corresponde el numero que se entro, para usar el index en lugar del _ "

# REQUERIMIENTO: El usuario va a especificar el numero de ingresos que
# va a realizar. Se va a identiicar de esas entradas cuantos y cuales
# de ellos son numeros son pares y cuales son impares. Ademas necesitamos saber
# a cual de las entradas corresponde

# Objetivo -> Informar cuantos y cuales son pares de las entradas recibidas
# y en que momento de la secuencia fueron ingresados.

# #Algoritmo
# 1. Solicitar al usuario el numero de entradas a realizar
# 2. Por cada una de las entradas revisar si es numero par o impar
# 3. Si es par o impar, coleccionarlo
# 3.a De lo contrario seguir solicitando las entradas

# Traduccion -> Python
n = int(input('Cuantos numeros va a ingresar? '))
coleccionNumerosPares = []
coleccionNumerosImpares = []
for i in range(n):
    num = int(input('Ingrese Numero: '))
    if num % 2 == 0:
        coleccionNumerosPares.append([num, i])
    else:
        coleccionNumerosImpares.append([num, i])

soloNumerosPares = []
for numero in coleccionNumerosPares:
    soloNumerosPares.append(numero[0])

soloNumerosImpares = []
for numero in coleccionNumerosImpares:
    soloNumerosImpares.append(numero[0])


print(
    f'Numero de Pares Ingresados: {len(coleccionNumerosPares)} Coleccion: {soloNumerosPares}')
print(
    f'Numero de Impares Ingresados: {len(coleccionNumerosImpares)} Coleccion: {soloNumerosImpares}')
