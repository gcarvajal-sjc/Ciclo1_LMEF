from functools import reduce
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
# 2. Colleccionar las transacciones de los cajeros de los modelos solicitados
# 3. Filtrar las transferencias de las transacciones
# 4. Obtener las transacciones que se realizaron en el ultimo trimestre(Marzo, Abril, Mayo de 2021)


def requerimiento1(caso):

    def esModelo101(modelo):
        return modelo == 101

    def esModelo2017(modelo):
        return modelo == 2017

    def cajerosModelosRequeridos(modelo):
        return any([esModelo101(modelo), esModelo2017(modelo)])

    #print('Cajeros con toda la info de los modelos solicitados')
    # Por cada pareja llave/valor(caso1.items), en x queda cargado cada pareja llave/valor
    # extraigo le mando a la funcion de predicado exclusivamente ese campo que es 'modeloCajero'

    # Version usando predicados
    # listadoCajerosModelos = list(filter(lambda x: cajerosModelosRequeridos(x[1]['modeloCajero']), caso1.items()))
    # pp.pprint(listadoCajerosModelos)
    #print('Numero de cajeros con el modelo solicitado -> ', len(listadoCajerosModelos))

    # Version usando las expresiones directamente osea de forma explicita
    cajerosModelo = list(filter(
        lambda x: x[1]['modeloCajero'] == 101 or x[1]['modeloCajero'] == 2017, caso.items()))
    # pp.pprint(cajerosModelo)
    #print('Numero de cajeros con el modelo solicitado -> ', len(cajerosModelo))

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

    # 2. Coleccionar las transacciones de los cajeros de los modelos solicitados

    listaListaTransacciones = list(
        map(lambda x: x[1]['transacciones'], cajerosModelo))
    # pp.pprint(listaListaTransacciones)

    # Concatenar los elementos de casda lista en una sola lista con reduce

    # Tenemos una lista vacia y una lista de diccionarios con las transacciones
    # Entonces empieza la funcion reduce -> la lista esta vacia y se encuentra
    # un diccionario, entonces le pega todos los elementos que hay en esa lista
    # (de diccionarios)  a la lista vacia, despues hay otra lista de diccionarios
    # entoces se carga otra lista de diccionarios y asi se va acumulado sucesivamente

    listaTransacciones = reduce(lambda acumulador=list(
    ), elemento=dict(): acumulador+elemento, listaListaTransacciones)
    # pp.pprint(listaTransacciones)

    # 3. Filtrar las transferencias de las transacciones
    # Es una lista de diccionarios ->cada elemento de la
    # lista(listaTransacciones) es el que esta en x (en x queda un diccionario)
    # transferencias = list(filter(
    #     lambda x: x['tipoMovimiento'] == 'transferencia', listaTransacciones))
    # con el predicado (mismo ejemplo de las lineas 93-98)

    def esTransferencia(transaccion):
        return transaccion['tipoMovimiento'] == 'transferencia'

    transferencias = list(filter(esTransferencia, listaTransacciones))
    # print('--------------------------')
    # print('Listado de transferencias')
    # pp.pprint(transferencias)

    # 4. Obtener las transacciones que se realizaron en el ultimo trimestre(Marzo, Abril, Mayo de 2021)

    def perteneceAlUltimoTrimestre(transaccion):
        # Trimestre actual va desde 03-2021, al 05-2021 (marzo a mayo)
        fecha = transaccion['fechaMovimiento']
        return any([fecha[3:] == '03-2021', fecha[3:] == '04-2021', fecha[3:] == '05-2021'])

    transferenciasUltimoTrimestre = tuple(filter(
        perteneceAlUltimoTrimestre, transferencias))
    # print()
    # print()
    # print()
    # print('Respuesta del requerimiento')
    # pp.pprint(transferenciasUltimoTrimestre)

    # Retornar la informacion extraida
    return transferenciasUltimoTrimestre

# REQ 1: Haciendolo de forma procedural estructurado
# 1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
# de modelo 101,2017


def req1Procedural(caso):
    # Recorrer el diccionario con todos los cajeros
    transaccionesCajeros = list()
    for idCajero, infoCajero in caso.items():
        if infoCajero['modeloCajero'] == 101 or infoCajero['modeloCajero'] == 2017:
            for transaccion in infoCajero['transacciones']:
                if transaccion['tipoMovimiento'] == 'transferencia':
                    if transaccion['fechaMovimiento'][3:] == '03-2021' or transaccion['fechaMovimiento'][3:] == '04-2021' or transaccion['fechaMovimiento'][3:] == '05-2021':
                        transaccionesCajeros.append(transaccion)

    return transaccionesCajeros


# Consulta del requerimiento 1 aplicada a varios casos
# Llamado a las soluciones imperativas

print("-----------Caso 1")
resultadoProcedural = req1Procedural(caso1)
pp.pprint(resultadoProcedural)

# Llamados a las soluciones declarativas (clase17)
print("-----------Caso 1")
resultadoDeclarativo = requerimiento1(caso1)
pp.pprint(resultadoDeclarativo)

print('Num proc -> ', len(resultadoProcedural))
print('Num decl -> ', len(resultadoDeclarativo))
print('Iguales') if resultadoProcedural == list(resultadoDeclarativo) else print(
    'Diferentes')

# # Consulta del requerimiento 1 aplicada a varios casos
# print("-----------Caso 2")
# print(requerimiento1(caso2))
