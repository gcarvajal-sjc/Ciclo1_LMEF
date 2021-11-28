# Guardar cada uno de los elementos de una coleccion
# tipo cadena en un diccionario

# Vesion con los conocimientos de la unidad 1-3
cadena = 'hola'
diccionarioCadena = dict()
# diccionarioCadena['primerValor'] = cadena[0]
# diccionarioCadena['segundoValor'] = cadena[1]
# diccionarioCadena['tercerValor'] = cadena[2]
# diccionarioCadena['cuartoValor'] = cadena[3]
# print(diccionarioCadena)

# Segunda forma
# por cada letra que hay en la variable cadena agreguele un
# elemento al diccionario pero como hay que resolver se le pone un contador
# enumerate va a sacar cada uno de los elementos de cadena y los guarda en letra
# pero ademas le pone un contador que arranca en zero
# for i, letra in enumerate(cadena):
#     diccionarioCadena['Valor' + str(i)] = letra
# print('------------')
# print(diccionarioCadena)

# Generando coleccion de indices  (o llaves para el diccionario)
llaves = list(range(len(cadena)))
print("Las llaves del futuro diccionario")
print(llaves)
print("Valores del futuro diccionario")
print(cadena)
# Necesitariamos una coleccion de tuplas tipo tupla
print("Mostrar tuplas que constituiran el diccionario")
for i in range(len(cadena)):
    print((llaves[i], cadena[i]))

# la funcion zip resume la parte del for de lineas 31/32 en una sola linea
# y crea tuplas de la informacion
coleccionTuplas = zip(llaves, cadena)
print('Resultado del zip: ', tuple(coleccionTuplas))

diccionarioCadena = dict(zip(range(len(cadena)), cadena))
print(diccionarioCadena)

# Ilustrando un poco de ZIP
nombres = ['juan', 'luis', 'ana']
edades = ['12', '15', '22']
tipoSangre = ['A+', 'O+', 'AB+']

listadoPacientes = list(zip(nombres, edades, tipoSangre))
print(listadoPacientes)

# Zip de diferentes coleccoines, vea que la coleccion palabra manda
# sobre la cantidad de tuplas que se arman en el zip, ya que el numero
# de elementos en las colecciones es diferente.
# nombres = ['juan', 'luis', 'ana']
# edades = ('12', '15', '22')
# tipoSangre = ['A+', 'O+', 'AB+']
# palabra = "Tripulante"

# listadoPacientes = list(zip(nombres, edades, tipoSangre, palabra))
# print(listadoPacientes)

# Colecciones que podemos extraer del diccionario
print("Llaves del diccionario: ", diccionarioCadena.keys())
print("Valores del diccionario: ", diccionarioCadena.values())
print("Valores del diccionario: ", diccionarioCadena.items())
