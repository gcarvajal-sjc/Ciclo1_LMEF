# Requerimiento: Escribir un programa que le permita al usuario ingresar
# cuantos numeros quiera y al final reportar cuantos de esos numeros
# son multiplos de 5 y cuantos son multiplos de 3, recordar que hay numeros
# que pueden ser multiplos de ambos.

# Objetivo -> Reportar cantidad de multiplos de 5 y multiplos de 3
# entre los numeros ingresados

# #Algorito (pseudocodigo)
# 1. Inicializar contadores
# 2. Mientras el usuario quiera ingresar numeros
# 2.a Capturar el numero
# 2.b Revisar si es multiplo de 3 y de 5 y actualizar contadores
# 3. Cuando el usuario reporte que no va a entrar mas numeros informar
# cuantos de los numeros ingresados fueron multiplos de 5 y cuantos de 3.

# Traduccion a Phyton
contadorMultiplos3 = 0
contadorMultiplos5 = 0
quiereIngresarNumeros = True

while quiereIngresarNumeros:
    numero = int(input('Ingrese un numero: '))
    if numero % 3 == 0:
        contadorMultiplos3 += 1
    if numero % 5 == 0:
        contadorMultiplos5 += 1
    # respuesta = input("Desea continuar? (s/n)")
    # if respuesta == 'n':
    #     quiereIngresarNumeros = False
    quiereIngresarNumeros = input("Desea continuar? (s/n)") != 'n'

print(
    f"Multiplos de 5: {contadorMultiplos5} y Multiplos de 3: {contadorMultiplos3}")
