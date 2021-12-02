from casosGenerados import *

# 1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
# de modelo 101,2017
# 2)Obtener todas las consignaciones realizadas en el último trimestre en los cajeros
# de modelo 101,2017 que se encuentran fuera de servicio
# 3) Todas las transacciones de los cajeros cerrados que pertenecen a la firma integrada
# -> Convencional: Ciclando y con condicionales
# -> Funcional: Map, Filter, Zip o Reduce

# Para visualizar por consola de una forma organizada y automatica
import pprint as pp

# Extraer la informacion de un cajero
# pp.pprint(caso1['25u8sBP'])

# # Extraer transacciones del cajero
# print(type(caso1['25u8sBP']['transacciones']))
# pp.pprint(caso1['25u8sBP']['transacciones'])

# # Primera trasnsaccion del cajero
# print('--------------------Primera trasnsaccion del cajero-------------------')
# print(caso1['25u8sBP']['transacciones'][0])

# REQ 1:
# 1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
# de modelo 101,2017

# Algoritmo para REQ 1:
# 1. Sacar la info de los cajeros modelo 101 y 2017
# 2. Colecconar las transferencias de los cajeros solicitados
# 3. Obtener las que se realizaron en el ultimo trimestre(Marzo, Abril, Mayo de 2021)


def esModelo101(modelo):
    return modelo == 101


def esModelo2017(modelo):
    return modelo == 2017


def cajerosModelosRequeridos(modelo):
    return any([esModelo101(modelo), esModelo2017(modelo)])


print('Cajeros con toda la info de los modelos solicitados')
# Por cada pareja llave/valor(caso1.items), en x queda cargado cada pareja llave/valor
# extraigo le mando a la funcion de predicado exclusivamente ese campo que es 'modeloCajero'

# listadoCajerosModelos = list(filter(lambda x: cajerosModelosRequeridos(x[1]['modeloCajero']), caso1.items()))
# pp.pprint(listadoCajerosModelos)
#print('Numero de cajeros con el modelo solicitado -> ', len(listadoCajerosModelos))

cajerosModelo = list(filter(
    lambda x: x[1]['modeloCajero'] == 101 or x[1]['modeloCajero'] == 2017, caso1.items()))
pp.pprint(cajerosModelo)
print('Numero de cajeros con el modelo solicitado -> ', len(cajerosModelo))


# # Diccionario
# palabra = 'mesopotamia'
# # zip entre dos colecciones: la palabra, y unos valores que son exactamente
# # el mismo numero de las letras que hay en palabras
# diccionario = dict(zip(range(len(palabra)), palabra))
# pp.pprint(diccionario)

# # Ver las llaves, los valores o los items(llave,valor)
# print(diccionario.keys())
# print(diccionario.values())
# print(diccionario.items()) #esto es una tupla
