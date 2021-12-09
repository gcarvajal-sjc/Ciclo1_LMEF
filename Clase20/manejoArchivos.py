import random
import pprint as pp
import json

# Crear archivos de texto plano

numEstudiantes = 10
nombres = ['carlos', 'pedro', 'juan', 'natalia', 'valentina', 'camila']
codigos = ['asjhd1', 'asjhd2', 'asjhd3', 'asjhd4', 'asjhd5',
           'asjhd7', 'asjhd8', 'asjhd9', 'asjhd6', 'asjhd0']
estado = ['matriculado', 'suspendido', 'becado', 'egresado', 'posgrado']

# Cuando uno va a crear un archivo se usa la funcion open() Y se le da
# la ruta donde va a estar el archivo en quotes inside the () y el
# modo que queremos que se cree el archivo leer, escribir, agregar
# El archivo queda en la misma carpeta donde esta el script

# manejadorArchivo = open('estudiantes.txt', 'w')

# # Generar un archivo con 10 estudiantes generados aleatoriamente
# for i in range(numEstudiantes):
#     infoEstudiante = str()
#     infoEstudiante += codigos[i] + ' '
#     infoEstudiante += random.choice(nombres) + ' '
#     infoEstudiante += random.choice(estado) + '\n'
#     manejadorArchivo.write(infoEstudiante)

# manejadorArchivo.close()

# Para no tener que abrir y cerrar el archivo manualmente, esta la
# palabra reservada with que genera un bloque de codigo.

try:
    with open('estudiantes.txt', 'w') as manejadorArchivo:

        # Generar un archivo con 10 estudiantes generados aleatoriamente
        for i in range(numEstudiantes):
            infoEstudiante = str()
            infoEstudiante += codigos[i] + ' '
            infoEstudiante += random.choice(nombres) + ' '
            infoEstudiante += random.choice(estado) + '\n'
            manejadorArchivo.write(infoEstudiante)
except:
    print('Fallo realizando la escritura')


# Leer archivos de texto plano y cargarlo en diccionario
diccionarioArchivo = dict()
try:
    with open('estudiantes.txt') as manejadorArchivo:
        # Generar un archivo con 10 estudiantes generados aleatoriamente
        for linea in manejadorArchivo:
            # strip will remove the \n in the output
            registro = linea.strip().split(' ')
            diccionarioArchivo[registro[0]] = {
                'Nombre': registro[1], 'Estado': registro[2]}
except:
    print('Fallo realizando la lectura')
print('Contenido del diccionario')
pp.pprint(diccionarioArchivo)


# Modificar el archivo
try:
    with open('estudiantes.txt', 'a') as manejadorArchivo:
        estudianteNuevo = 'asjh12 john casado\n'
        manejadorArchivo.write(estudianteNuevo)
except:
    ('Error modificando el archivo de estudiantes')

# Hay funciones que nos permite descargar toda la info que tenemos en un
# archivo de json a partir de la info del archivo txt

# para ver este archivo es mejor abrirlo en firefox le
# hace drag desde finder
with open('estudiantes.json', 'w') as f:
    json.dump(diccionarioArchivo, f)

# Leer del archivo json
diccionarioJson = dict()
with open('lectura.json') as manejadorArchivo:
    diccionarioJson = json.load(manejadorArchivo)
print('Diccionario JSON')
pp.pprint(diccionarioJson)
