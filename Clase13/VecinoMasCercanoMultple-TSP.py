# Requerimiento: Recibimos una red o grafo y se requiere obtener la matriz
# de distancias correspondientes para computos de optimizacion.

# Distancia euclidiana (2D)

red = {
    'A': (8, 11),
    'B': (7, 8),
    'C': (9, 5.5),
    'D': (9, 7),
    'E': (10, 10)
}


def distanciaEUC_2D(punto1, punto2):
    return int(((punto1[0]-punto2[0])**2 + (punto1[1]-punto2[1])**2)**(1/2)) + 0.5


# Ejemplo distancia entre A y B
distanciaA_B = {'A-B': int(distanciaEUC_2D(red['A'], red['B']))}


# 5. Red diccionario anidado

red = {
    'Armenia': {'x': 8, 'y': 11},
    'Pereira': {'x': 7, 'y': 8},
    'Cali': {'x': 9, 'y': 5.5},
    'Cartago': {'x': 9, 'y': 7},
    'Manizales': {'x': 10, 'y': 10}
}

# Distancia euclidiana (2D) Version2 usando el diccionario anidado definido en linea 62


def distanciaEUC_2DV2(punto1, punto2):
    return int(((punto1['x']-punto2['x'])**2 + (punto1['y']-punto2['y'])**2)**(1/2) + 0.5)


# Funcion para el calculo de la matriz de costos usando diccionario anidado

def calcularMatrizCostos(red):
    matrizCostos = dict()
    for nombre_i, punto_i in red.items():
        for nombre_j, punto_j in red.items():
            costo = int()
            if nombre_i != nombre_j:
                # costo = int(distanciaEUC_2D(red[nombre_i], red[nombre_j]))
                costo = distanciaEUC_2DV2(red[nombre_i], red[nombre_j])
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

# Consultar la estrategia del vecino mas cerano e intentar implementarla
# sobre esta codificacion del problema

# #Algoritmo o pseudocodigo del vecino mas cercano
# 1. Establecer nodo o ciudad de partida(radicado el agente)
# 2. Preparar contenedor de jornadas
# 3. Iniciar el itinerario o el tour en la ciudad de partida establecida
# 4. Mientras tengamos ciudades sin cubrir en los itinerarios:
# 5.     Desde la ultima ciudad del itinerario revisamos las salidas a las demas ciudades
# 6.     Seleccionar la mejor de las salidas
# 7.      Si agregar la ciudad no supera el tiempo maximo de jornada:
# 8.                Agregar la ciudad (mejor de las salidas) al itinerario actual (crecimiento)
# 9.         De lo contrario:
# 10.                Cerrar itinerario con el retorno y agregarlo a las jornadas (dias)
# 11.                Abrir el itinerario con la mejor ciudad que no fue acomodada en el itinerario anterior
# 12     Actualizar las ciudades sin cubrir
# 13. Si el itinerario que estaba en construccion no fue agregado en las jornadas:
# 14.     Agregarlo
# 15. Mostrar las jornadas
# 16. Generar indicadores de las jornadas

# Traduccion a Python
print("-----Algoritmo Heuristico del vecino mas cercano-----")
# Inicializacion del tour y el conjunto de control de ciudades cubiertas
ciudadInicial = "Manizales"
itinerario = list()
itinerario.append(ciudadInicial)
ciudadesSinCubrir = set(red.keys())
ciudadesSinCubrir.remove(ciudadInicial)
jornadasTSP = list()  # Separar en jornadas para regreso del agente viajero
duracionMaxJornada = 9

# Seccion principal del algoritmo (cubrir todas las ciudades como ciclo hamiltoniano)
while len(ciudadesSinCubrir) > 0:
    # Construir el listado con las posibles salidas desde la ultima ciudad ingresada en el itinerario
    listadoSalidas = list()
    for ciudadSalida in ciudadesSinCubrir:
        listadoSalidas.append(
            (ciudadSalida, matrizCostos[itinerario[-1]+'-'+ciudadSalida]))
    listadoSalidas = tuple(listadoSalidas)
    # Seleccionar mejor salida
    mejorSalida = listadoSalidas[0]
    for salida in listadoSalidas:
        if mejorSalida[1] > salida[1]:
            mejorSalida = salida

    # Antes de actualizar itinerario, revisar si es una jornada viable
    duracion = 0
    for i in range(len(itinerario)-1):
        duracion += matrizCostos[itinerario[i]+'-'+itinerario[i+1]]
    duracion += matrizCostos[itinerario[-1]+'-'+mejorSalida[0]]
    duracion += matrizCostos[mejorSalida[0]+'-'+ciudadInicial]
    if duracion <= duracionMaxJornada:
        # Actualizar el itinerario
        itinerario.append(mejorSalida[0])
    else:
        # Cerrar el itinerario actual
        itinerario.append(ciudadInicial)
        # Agregarlo al listado de las jornadas
        jornadasTSP.append(list(itinerario))
        # Abrir nuevo itinerario
        itinerario.clear()
        itinerario = [ciudadInicial, mejorSalida[0]]

    # Actualizar el conjunto (entrando en el intenerario de la ciudad ahora esta cubierta)
    ciudadesSinCubrir.remove(mejorSalida[0])

# Ingresar el ultimo itinerario si hace falta
itinerario.append(ciudadInicial)
if jornadasTSP[-1] != itinerario:
    jornadasTSP.append(list(itinerario))

# Visualizar los itinerarios generados
print("------Itinerarios-------")
[print(jornada) for jornada in jornadasTSP]

# Funcion para calcular duracion de los itinerarios


def calcularDuracion(itinerario, matrizCostos):
    duracion = 0
    for i in range(len(itinerario)-1):
        duracion += matrizCostos[itinerario[i]+'-'+itinerario[i+1]]
    return duracion


# Contenedor ampliado de los itinerarios
print("-----------------------------")
print('Diccionarion Detalle Jornadas')
jornadasDetalle = dict()
for i, jornada in enumerate(jornadasTSP):
    jornadasDetalle[f"Jornada{i+1}"] = {'itinerario': jornada,
                                        'duracion': calcularDuracion(jornada, matrizCostos)}

# Mostar en pantalla
[print(llave, valor) for llave, valor in jornadasDetalle.items()]


# # Cuantificar la calidad de la solucion, tecnicamente eso se llama
# # funcion objetivo 'fo'
# fo = 0
# for i in range(len(itinerario)-1):
#     fo += matrizCostos[itinerario[i]+'-'+itinerario[i+1]]
# print("Funcion objetivo (calidad) solucion: ", fo)
