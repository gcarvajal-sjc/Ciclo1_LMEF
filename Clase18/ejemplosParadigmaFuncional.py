# Requerimiento: Se le solicita al usuario una n coordenadas por
# teclado (separadas por espacios). Debe ingresarlas colocando primero
# el nombre del punto que representa la coordenada y a continuacion los
# valores en x y y que componenla coordenada. Coleccionarlas y al
# final aplicar un corrimiento dado a todas las coordenadas.

# Ejemplo:
# 'Bogota' 12.5 4.8
# 'A'         7, 10

# Corrimiento en X -> 1
# Corrimiento en Y -> 2

# 'Bogota' 13.5 6.8
# 'A'         8, 12

# # Algoritmo
# 1. El usuario ingresa la cantidad de puntos solicitados.
# 2. Los puntos deben ser coleccionados en el formato string float float
# 3. Aplicar el corriemiento a c/u de las componentes

# Totalmente Procedural estructurado

# n = 3
# corrimientoX = 4
# corrimientoY = 1
# coleccionPuntos = []
# for _ in range(n):
#     coordenada = input('Ingrese coordenada: ')
#     coordenada = coordenada.split(' ')
#     coordenada[1] = float(coordenada[1])
#     coordenada[2] = float(coordenada[2])
#     coleccionPuntos.append(coordenada)
# print('Coleccion de puntos')
# print(coleccionPuntos)


# for i in range(len(coleccionPuntos)):
#     coleccionPuntos[i][1] += corrimientoX
# print('Coleccion con corriemiento en X aplicado')
# print(coleccionPuntos)

# for i in range(len(coleccionPuntos)):
#     coleccionPuntos[i][2] += corrimientoY
# print('Coleccion con corriemiento en Y aplicado')
# print(coleccionPuntos)

# Funciones de primera clase y de orden superior
# Primera clase


def convertirFormatoSFF(coordenada):
    return [coordenada[0], float(coordenada[1]), float(coordenada[2])]

# variante SFI -> string float integer


def convertirFormatoSFI(coordenada):
    return [coordenada[0], float(coordenada[1]), int(coordenada[2])]

# variante SFI -> string integer integer


def convertirFormatoSII(coordenada):
    return [coordenada[0], int(coordenada[1]), int(coordenada[2])]

# Partir la coordenada entrada como texto


def partirPorEspacios(coordenada):
    return coordenada.split(' ')

# Variante partir por comas


def partirPorComas(coordenada):
    return coordenada.split(',')

# Acumular en una lista las coordenadas


def coleccionarEnLista(lista, elemento):
    return lista.append(elemento)

# Variante coleccionar en Dictionary


def coleccionarEnDiccionario(diccionario, elemento):
    diccionario[elemento[0]+str(elemento[1])+str(elemento[2])] = elemento


# Funcion para coleccionar las coordenadas (funcion de orden superior)

# Recibe la cadena, recibe la coleecion, y le mandamos funciones para
# describirle que tiene que hacer con esa coleccion y esa cadena


def coleccionarCoordenadas(cadenaCoordenada, coleccion, funcionPartido, funcionFormato, funcionColeccion):
    funcionColeccion(coleccion, funcionFormato(
        funcionPartido(cadenaCoordenada)))


n = 3
corrimientoX = 4
corrimientoY = 1
coleccionPuntos = list()
coleccionPuntos = dict()
for _ in range(n):
    #coleccionarCoordenadas(input('Ingrese coordenada: '), coleccionPuntos,partirPorEspacios, convertirFormatoSFF, coleccionarEnLista)

    coleccionarCoordenadas(input('Ingrese coordenada: '), coleccionPuntos,
                           partirPorComas, convertirFormatoSII, coleccionarEnDiccionario)
print('Coleccion de puntos obtenida')
print(coleccionPuntos)

# Aprovechando map y reduce
