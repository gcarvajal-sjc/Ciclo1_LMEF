# Requerimiento: Programa que recibe dos numeros enteros y reporta si la suma de ellos es positiva

# Objetivo: Reportar solament si es positiva la suma de los numeros ingresados

# Algoritmo
# 1.Cargar desde teclado los numeros
# 2.Sumar los dos numeros y guardar resultado
# 3.Comparar si el resultado es > 0 entonces
# 3.a reportamos que la sumatoria es positiva
# 3.b reportamos el resultado y es negativo

a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))
c = a+b
if c > 0:
    print('la sumatoria es positiva')
else:
    print(f"El resultado fue {c}, y es un numero negativo")
