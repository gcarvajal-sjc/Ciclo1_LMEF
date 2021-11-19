# PRIMER EJERCICIO
# Escribir un programa que solicite ingresar 10 notas de alumnos y nos
# informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

# Objetivo: Reportar notas diciendo cuantos alumnos tienen notas mayores a 7 y cuantos menores.

# #Algoritmo:
# 1. Recoger 10 notas en una lista
# 2. Mirar cuantas notas son mayores o iguales a 7
# 2.b Sino contar cuantas son menores
# 3. Reportar

# Traduccion -> Python

# listaNotas = []
# mayoresQueSiete = 0
# menoresQueSiete = 0


# for i in range(10):
#     notas = float(input('Ingrese una nota: '))
#     listaNotas.append(notas)
#     if listaNotas[i] >= 7.0:
#         mayoresQueSiete += 1
#     else:
#         menoresQueSiete += 1
# print(
#     f'El numero de notas mayores de siete son: {mayoresQueSiete} y el numero de notas menores de siete son: {menoresQueSiete}')


# SEGUNDO EJERCICIO con while
# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

# Objetivo: Calcular el promedio de altura de un grupo de personas

# #Algoritmo:
# 1. Iniciar hipotesis altura = True
# 2. Mientras altura -> Coleccionar el conjunto de alturas en una lista
# 3. Si altura = false -> calcular el promedio de las alturas

# Traduccion -> Python

# ingresarAltura = True
# listaAltura = []
# while ingresarAltura:
#     altura = float(input('Ingrese altura: '))
#     listaAltura.append(altura)
#     ingresarAltura = input('Desea continuar (s/n)') != 'n'
# promedio = round(sum(listaAltura)/len(listaAltura), 2)
# print(f'El promedio de las alturas de las personas es: {promedio}')


# TERCER EJERCICIO con while
# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100
# y $500, realizar un programa que lea los sueldos que cobra cada
# empleado e informe cuántos empleados cobran entre $100 y $300 y
# cuántos cobran más de $300. Además el programa deberá informar el
# importe que gasta la empresa en sueldos al personal.

# Objetivo: Reportar cuantos empleados de una empresa ganan entre $100-$300
# cuantos ganan mas de $300, y la suma de todos los sueldos

# Algoritmo

# 1. Recibir los sueldos en una lista hasta que no haya que ingresar mas
# 2. Reportar cuantos de esos sueldos estan entre $100 - $300
# 3. Reportar cuantos son mayores a $300
# 4. Reportar el monto total de los sueldos

# Traduccion -> Python

# listaSueldos = []
# ingresarSueldos = True
# entre100Y300 = 0
# mayor300 = 0

# while ingresarSueldos:
#     sueldo = int(input('Ingrese sueldo: '))
#     listaSueldos.append(sueldo)
#     ingresarSueldos = input('Desea continuar (s/n)') != 'n'
#     if sueldo >= 100 and sueldo <= 300:
#         entre100Y300 += 1
#     if sueldo > 300:
#         mayor300 += 1
#     monto = sum(listaSueldos)

# print(f'Numero de empleados con sueldo entre $100-$300: {entre100Y300}')
# print(f'Numero de empleados con sueldo mayor a $300: {mayor300}')
# print(f'La empresa paga un total de ${monto} en sueldos al mes')


# CUARTO EJERCICIO con while
# Realizar un programa que imprima 25 términos de la serie
# 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)

# Objetivo: imprimir 25 numeros de 11 en 11

# #Algoritmo
# 1. Iniciar variable para acumular los numeros de la lista
# 2. Declarar una hipotesis para usar mientras verdadero
# 3. Crear una lista vacia a la cual se le va a ir añadiendo los numeros
# 4. Ir sumando hasta que el numero 11 se haya sumado 25 veces
# 5. Imprimir la lista de los 25 numeros

# Traduccion -> Python
# num = 0
# veces25 = True
# serie = []

# while veces25:
#     num += 11
#     serie.append(num)
#     if num == 275:
#         break
# print(f"La serie del numero 11 es: {serie}")

# EJERCICIO 5 While
# Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en
# pantalla 8 - 16 - 24, etc.

# Objetivo: Mostrar los numero multiplos del 8 hasta 500

# #Algoritmo:
# 1. Inicializar una variable para acumular los numeros de la lista
# 2. Iniciar una lista vacia
# 3. Declarar una hipotesis verdadera
# 4. Ir sumando de 8 en 8 hasta 500
# 5. Imprimir la serie

# Traduccion -> Python
# numero = 0
# serie = []
# multiploOcho = True

# while multiploOcho:
#     numero += 8
#     serie.append(numero)
#     if numero == 504:
#         break
# print("La serie de numeros multiplos de 8 hasta 504 es: ", serie)

# EJERCICIO 6 While
# Realizar un programa que permita cargar dos listas de 15 valores cada
#  una. Informar con un mensaje cuál de las dos listas tiene un valor
#  acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas
#  iguales") Tener en cuenta que puede haber dos o más estructuras
# repetitivas en un algoritmo.

# Objetivo: Hacer un programita que reporte cual lista de dos tiene el mayor
# valor acumulado o si son iguales.

# Algoritmo
# 1. Cargar dos listas c/u de 15 valores
# 2. Hacer la sumatoria de cada lista
# 3. Comparar los valores totales de las listas
# 4. Reportar

# # Traduccion -> Python
# listaUno = []
# listaDos = []
# contador = 0
# cargarLista = True

# while cargarLista:
#     numLista1 = int(input('Ingrese un numero Lista1: '))
#     listaUno.append(numLista1)
#     contador += 1
#     if contador == 15:
#         break

# contador = 0
# while cargarLista:
#     numLista2 = int(input('Ingrese un numero Lista2: '))
#     listaDos.append(numLista2)
#     contador += 1
#     if contador == 15:
#         break

# if sum(listaUno) > sum(listaDos):
#     print("Lista 1 Mayor")
# if sum(listaUno) < sum(listaDos):
#     print("Lista 2 Mayor")
# if sum(listaUno) == sum(listaDos):
#     print("Listas Iguales")


# EJERCICIO 8 con for
# Confeccionar un programa que lea n pares de datos, cada par de datos
#  corresponde a la medida de la base y la altura de un triángulo. El
# programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

# Objetivo: Crear un programa que lee n pares de datos, por cada par de
# datos retorna el area del triangulo. Reportar cuanto vale la base, la
# altura, y el area. Reportar la cantidad de triangulos cuya area es mayor a 12

# Algoritmo:
# Preguntar la cantidad de triangulos que quiere trabajar
# Crear un ciclo que haga lo siguiente por cada triangulo:
# Almacenar la base y altura
# Calcular el area del triangulo para la cantidad de pares de datos
# Reportar base, altura y area de cada triangulo
# Reportar cuantos triangulos tienen area mayor que 12

# # Traduccion -> Python

# numeroTriangulos = int(input('Ingrese cuantos triangulos va a trabajar? '))
# areaMayorDoce = 0
# for i in range(numeroTriangulos):
#     base = int(input('Ingrese el valor de la base: '))
#     altura = int(input('Ingrese el valor de la altura: '))
#     area = (base*altura) / 2
#     if area > 12:
#         areaMayorDoce += 1
#     print(f'Base del triangulo{i} es: {base}, altura {altura}, area {area}')
# if areaMayorDoce >= 1:
#     print(f'El numero de triangulos con area mayor a 12 son: {areaMayorDoce}')


# EJERCICIO 9 With for
# Desarrollar un programa que solicite la carga de 10 números e imprima
# la suma de los últimos 5 valores ingresados.

# Objetivo: Cargar 10 numeros y sumar los cinco ultimos

# Algoritmo:
# Cargar 10 numeros
# Usando range podemos sumar los ultimos cinco
# Reportar

# sumatoria = 0

# for i in range(10):
#     numero = int(input('Entre un numero: '))
#     if i >= 5:
#         sumatoria = sumatoria + numero

# print('La suma de los ultimos 5 numeros es: ', sumatoria)

# EJERCICIO 10  Desarrollar un programa que muestre la tabla de
# multiplicar del 5 (del 5 al 50)

# #Algoritmo:
# 1. Iniciar una variable con el numero 5
# 2. Empezar a ciclar para que multiplique desde el 5 hasta el 50
# 3. Reportar

# tabla = 5
# for i in range(5,11):
#     resultado = tabla * i
#     print(f'{tabla}*{i}={resultado}')

# EJERCICIO 11  Confeccionar un programa que permita ingresar un valor
#  del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los
# primeros 12 términos) Ejemplo: Si ingreso 3 deberá aparecer en
# pantalla los valores 3, 6, 9, hasta el 36.

# Algoritmo
# Recoger un numero del 1 al 10
# Ciclar ese numero para que muestre la tabla de multiplicar los 12 primero terminos
# Reportar

# numero = int(input('Ingrese un numero del 1 al 10: '))

# for i in range(1, 13):
#     resultado = numero * i
#     print(f'{numero}*{i}={resultado}')


# EJERCICIO 12:  Realizar un programa que lea los lados de n triángulos,
#  e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres
# lados iguales), isósceles (dos lados iguales), o escaleno (ningún
# lado igual)
# b) Cantidad de triángulos de cada tipo.

# #Algoritmo
# 1. Guardar cuantos triangulos desea analizar
# 2. Entrar los valores de los tres lados
# 3a. Mirar si  todos los lados son iguales es equilatero, incrementar la variable equilatero
# 3b. Mirar si cualquiera de los dos lados son inguales es isoceles, incrementar la variable isoceles
# 3c. Mirar si todos los lados son diferentes, incrementar la variable escaleno
# 4. Reportar cuantos triangulos hay de cada uno

# equilatero = 0
# isoceles = 0
# escaleno = 0

# numeroTriangulos = int(input('Cuantos triangulos desea analizar? '))

# for i in range(numeroTriangulos):
#     ladoUno = int(input('Entre el valor del primer lado: '))
#     ladoDos = int(input('Entre el valor del segundo lado: '))
#     ladoTres = int(input('Entre el valor del tercer lado: '))
#     if ladoUno == ladoDos and ladoTres == ladoUno:
#         equilatero += 1
#     elif ladoDos == ladoTres or ladoUno == ladoTres or ladoDos == ladoUno:
#         isoceles += 1
#     else:
#         escaleno += 1

# print(f'Cantidad de triangulos equilateros: {equilatero}')
# print(f'Cantidad de triangulos isoceles: {isoceles}')
# print(f'Cantidad de triangulos escalenos: {escaleno}')

# EJERCICIO 13: Escribir un programa que pida ingresar coordenadas (x,y)
# que representan puntos en el plano. Informar cuántos puntos se han
# ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar
# el programa se pide que se ingrese la cantidad de puntos a procesar.

# Algoritmo:
# 1. Almacenar cuantas veces va a entrar las coordenadas
# 2. Para cada par de puntos mirar(osea un for)
# 2.a Si la coordenada x es positiva y y es positiva -> 1er cuadrante, incrementar variable primer
# 2.b Si la coordenada x es negativa y y es positiva -> 2do cuadrante, incrementar variable segundo
# 2.c Si la coordenada x es negativa y y es negativa -> 3er cuadrante, incrementar variable tercer
# 2.d Si la coordenada x es positiva y y es negativa -> 4to cuadrante, incrementar variable cuarto
# # 3. Reportar

# primer = 0
# segundo = 0
# tercer = 0
# cuarto = 0
# numeroCoordenadas = int(input('Ingrese el numero de coordenadas a evaluar: '))

# for i in range(numeroCoordenadas):
#     x = int(input('Ingrese valor coordenada x: '))
#     y = int(input('Ingrese valor coordenada y: '))
#     if x > 0 and y > 0:
#         primer += 1
#     if x < 0 and y > 0:
#         segundo += 1
#     if x < 0 and y < 0:
#         tercer += 1
#     if x > 0 and y < 0:
#         cuarto += 1

# print(f'There is/are {primer} coordinate(s) on the first quadrant')
# print(f'There is/are {segundo} coordinate(s) on the first quadrant')
# print(f'There is/are {tercer} coordinate(s) on the first quadrant')
# print(f'There is/are {cuarto} coordinate(s) on the first quadrant')
