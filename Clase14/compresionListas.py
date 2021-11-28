# -> List Comprehension: Generar colecciones de forma resumida

# Requeriemiento: solicitar un numero y presentar todos los numeros
# impares hasta el numero ingresado (incluido)

# Satisfacer de manera convencional el requerimiento:
# n = int(input("Ingrese un numero: "))
# for i in range(1, n+1):
#     if i % 2 != 0:
#         print(i, end=' ')

# # Generar colecciones con list comprehension
# n = int(input("Ingrese un numero: "))
# # Generar todos los numeros hasta el valor n ingresado
# # list(range(n+1)) #Solucon con conversion de contenedores
# # Solucion comprension de listas
# coleccion = [i for i in range(1, n+1) if i % 2 != 0]
# print(coleccion)
# [print(i, end=' ') for i in range(1, n+1) if i % 2 != 0]
# print('--------------')


# # Generar un diccionario donde la llave sea un numero y el valor sea ese
# # numero elevado al cuadrado hasta el valor ingresado-> en una sola linea
# n = int(input("Ingrese un numero: "))
# cuadrados = {i: i**2 for i in range(1, n+1) if i % 2 == 0}
# print(cuadrados)

# # Ahora en una sola linea:
# print({i: i**2 for i in range(1, int(input('Ingrese un numero: '))+1) if i % 2 == 0})

# Requerimiento: Solicitar al usuario una serie de palabras (separadas por
# espacios) y mostrar solamente las que tengan vocales abiertas (a,e,o)

# # Algoritmo:
# 1. Solicitar palabras al usuario
# 2. Separar las palabras por espacios
# 3. Para c/u de las palabras que tienen vocales abiertas:
# 4. Mostrar palabra en pantalla

# # Solucion linea a linea (Unidad 1-3)
# print('Ingrese las palabras separadas por espacios:')
# entradaUsuario = input('Entrada -> ')
# palabras = entradaUsuario.split(' ')
# conjuntoVocalesCerradas = set()
# conjuntoVocalesCerradas.add('i')
# conjuntoVocalesCerradas.add('u')
# for palabra in palabras:
#     tieneVocalesCerradas = False
#     for letra in palabra:
#         if letra in conjuntoVocalesCerradas:
#             tieneVocalesCerradas = True
#     if not tieneVocalesCerradas:
#         print(palabra)

# Solucion comprensio de listas
print('Ingrese las palabras a revisar separadas por espacios')

# Predicado -> es una funcion que solo devuelve falso o verdadero


def tieneVocalesCerradas(palabra):
    hipotesisTieneVocalesCerradas = False
    for letra in palabra:
        if letra in {'i', 'u'}:
            hipotesisTieneVocalesCerradas = True
    return hipotesisTieneVocalesCerradas


# Comprension de listas para el requerimiento
[print(palabra) for palabra in input(
    'Entrada -> ').split(' ') if not tieneVocalesCerradas(palabra)]
