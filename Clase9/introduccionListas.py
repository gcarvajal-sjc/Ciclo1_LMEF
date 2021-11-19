# Listas -> Primer contenedor general
# Mutable -> cada casilla la podemos modificar
# En cada casilla podemos guardar info de cualquier tipo
# Cada posicion tiene un indice(autonumerico)

# lista = [12, 56, 7.9, 'hola mundo']

# # CRUD -> create read update delete
# # Para update: se usan
# # append() para agregar elementos al final
# # insert(posicion)

# lista.append('mintic')
# print(lista)

# lista.insert(1, 'Elemento')
# print(lista)

# lista.insert(-1, 'Elemento_2')
# print(lista)

# # Para eliminar elementos de la lista se puede usar
# # pop() elimina exactamente el ultimo elemento
# # para eliminar un elemento especifico se le da pop(indice)

# lista.pop()
# print(lista)

# lista.pop(1)
# print(lista)

# REQUERIMIENTO: El usuario va a especificar el numero de ingresos que
# va a realizar. Se va a identiicar de esas entradas cuantos y cuales
# de ellos son numeros son pares y cuales son impares

# Objetivo -> Informar cuantos y cuales son pares de las entradas recibidas

# #Algoritmo
# 1. Solicitar al usuario el numero de entradas a realizar
# 2. Por cada una de las entradas revisar si es numero par o impar
# 3. Si es par o impar, coleccionarlo
# 3.a De lo contrario seguir solicitando las entradas

# Traduccion -> Python
n = int(input('Cuantos numeros va a ingresar? '))
coleccionNumerosPares = []
coleccionNumerosImpares = []
for _ in range(n):  # se ahorra memoria usando el _ porque no se necesita recorrer el indice
    num = int(input('Ingrese Numero: '))
    if num % 2 == 0:
        coleccionNumerosPares.append(num)
    else:
        coleccionNumerosImpares.append(num)
print(
    f'Numero de Pares Ingresados: {len(coleccionNumerosPares)} Coleccion: {coleccionNumerosPares}')
print(
    f'Numero de Impares Ingresados: {len(coleccionNumerosImpares)} Coleccion: {coleccionNumerosImpares}')
