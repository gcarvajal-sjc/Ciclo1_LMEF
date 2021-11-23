# Requerimiento: Recibimos una red o grafo y se requiere obtener la matriz
# de distancias correspondientes para computos de optimizacion.

# Altenativas de codificacion

# Ejemplos de coleecion
# 1. Lista de listas representado la red:
# - La lista general es la red, y cada posicion de la lista son los nodos

red = [
    ['A', 8, 11],
    ['B', 7, 8],
    ['C', 9, 5.5],
    ['D', 9, 7],
    ['E', 10, 10]
]

# 2. En la primera posicion de cada una de las listas esta la etiqueta y
# las coordenadas en una tupla para que no cambien
red = [
    ['A', (8, 11)],
    ['B', (7, 8)],
    ['C', (9, 5.5)],
    ['D', (9, 7)],
    ['E', (10, 10)]
]

# 3. Una lista de tuplas
red = [
    ('A', (8, 11)),
    ('B', (7, 8)),
    ('C', (9, 5.5)),
    ('D', (9, 7)),
    ('E', (10, 10))
]

# 4. Tal vez no necesitamos el autonumerico. Entonces el diccionario permite
# personalizar la etiqueta

red = {
    'A': (8, 11),
    'B': (7, 8),
    'C': (9, 5.5),
    'D': (9, 7),
    'E': (10, 10)
}


# Distancia euclidiana (2D)


def distanciaEUC_2D(punto1, punto2):
    return ((punto1[0]-punto2[0])**2 + (punto1[1]-punto2[1])**2)**(1/2)


# Ejemplo distancia entre A y B
distanciaA_B = {'A-B': int(distanciaEUC_2D(red['A'], red['B']))}


# 5. Red diccionario anidado

red = {
    'A': {'x': 8, 'y': 11},
    'B': {'x': 7, 'y': 8},
    'C': {'x': 9, 'y': 5.5},
    'D': {'x': 9, 'y': 7},
    'E': {'x': 10, 'y': 10}
}

# Distancia euclidiana (2D) Version2 usando el diccionario anidado definido en linea 62


def distanciaEUC_2DV2(punto1, punto2):
    return ((punto1['x']-punto2['x'])**2 + (punto1['y']-punto2['y'])**2)**(1/2)


# Funcion para el calculo de la matriz de costos usando diccionario anidado

def calcularMatrizCostos(red):
    matrizCostos = dict()
    M = 9999999
    for nombre_i, punto_i in red.items():
        for nombre_j, punto_j in red.items():
            costo = int()
            if nombre_i != nombre_j:
                #costo = int(distanciaEUC_2D(red[nombre_i], red[nombre_j]))
                costo = int(distanciaEUC_2DV2(red[nombre_i], red[nombre_j]))
                matrizCostos[nombre_i+"-"+nombre_j] = costo
            # else: para no poner nada en distancia del mismo punto y evitar que el codigo se quede en un loop midiendo la distancia a si mismo
            #     costo = M
    return matrizCostos


# Matriz de costos donde van a estar los costos entre los nodos
# Generalizar para calcular todas las posibles conexiones
# matrizCostos = dict()
# M = 9999999
# for nombre_i, punto_i in red.items():
#     for nombre_j, punto_j in red.items():
#         costo = int()
#         if nombre_i != nombre_j:
#             costo = int(distanciaEUC_2D(red[nombre_i], red[nombre_j]))
#             matrizCostos[nombre_i+"-"+nombre_j] = costo
#         # else: para no poner nada en distancia del mismo punto y evitar que el
#         # codigo se quede en un loop midiendo la distancia a si mismo
#         #     costo = M


matrizCostos = calcularMatrizCostos(red)
[print(llave, ' ', valor) for llave, valor in matrizCostos.items()]

print('--------------')
print(matrizCostos)
