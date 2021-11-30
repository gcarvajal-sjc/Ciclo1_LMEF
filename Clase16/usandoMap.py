import random

# Map basico
# Construir nuestro propio map

# Map consiste en que vamos a recibir una funcion y coleccion o iterable
# y retorno c/u de los elementos de la coleccion despues de aplicales la funcion (retornamos coleccion)

# Requerimiento: -> se necesita aplicar a toda la coleccion un incremento
# de 2 decimas. El docente quiere ayudar con 2 decimas de una actividad
# a los estudiantes por las dificultades presentadas (sumar 2 decimas a cada elemento)

notas = [3.5, 3.0, 4.4, 3.2, 1.0, 3.8, 2.1, 3.7, 4.0]

# # Imperativo
# print('Notas antes de bonificacion: ', notas)
# for i in range(len(notas)):
#     notas[i] = round(notas[i] + 0.2, 2)
# print('Notas despues de bonificacion: ', notas)

# Declarativo


def mapBasico(funcion, coleccion):
    return [funcion(elemento) for elemento in coleccion]  # comprension listas


def bonificacion(nota):
    return round(nota + 0.2, 2)


def bonificacionCondicionada(nota):
    return round(nota + 0.2, 2) if nota <= 3.5 else nota


def penalidad(nota):
    return round(nota - 0.1, 2)


def bonificacionPorcentual(nota):
    return round(nota + nota * 0.15, 2)


# Solucion al requerimiento de forma declarativa (map basico)
print('Notas antes de bonificacion: ', notas)
print('Notas despues de bonificacion: ', mapBasico(bonificacion, notas))
print('Notas despues de penalidad: ', mapBasico(penalidad, notas))
print("Notas condicionadas: ", mapBasico(bonificacionCondicionada, notas))
print('Estado notas -> ', notas)

# 5 + (8+12) <- Algo asi es lo que se hace en la linea 46: (8+12) es el mapBasico(bonificacionPorcentual,notas)) y 5 es el mapBasico que incluye penalizacion de lo que se hizo en (8+12)

# Requerimiento bonificacion basada en nota actual y luego penalidad a todo el grupo
print("Requerimiento:", mapBasico(
    penalidad, mapBasico(bonificacionPorcentual, notas)))

# Ejemplo funciones lambda para la penalidad
print("Notas despues de la penalidad lambda: ",
      mapBasico(lambda x: round(x - 0.1, 2), notas))

# Requerimientos planteados:
# Notas de estudiantes y sacar promedios

# Generar aleatoriamente los casos para los requerimientos planteados

# Generar notas de estudiantes aleatoriamente


def generarNotasGrupoAleatorias():
    notasPosibles = (0, 1, 2, 3, 4, 5, 3.3, 3.8, 4.1, 2.4)
    cortesSemestre = 4
    numeroEstudiantes = 8
    grupoEstudiantes = []
    for _ in range(numeroEstudiantes):
        grupoEstudiantes.append([notasPosibles[random.randint(
            0, len(notasPosibles)-1)] for _ in range(cortesSemestre)])
    return grupoEstudiantes


# Generar el caso
grupoEstudiantes = generarNotasGrupoAleatorias()
print('Notas del grupo: ', grupoEstudiantes)
[print(estudiante) for estudiante in grupoEstudiantes]


def promedio(notasEstudiante):
    return round(sum(notasEstudiante)/len(notasEstudiante), 2)


print("Promedio de cada estudiante: ", mapBasico(promedio, grupoEstudiantes))


# Requerimientos planteados:
# Recibir info de un usuario y crear el codigo compuesto por el nombre, apellido e identificacion

def generarIdentificacion():
    numeroCaracteres = 5
    id = str()
    for _ in range(numeroCaracteres):
        id += str(random.randint(0, 9))
    return id


def generarPersonasAleatorias():
    nombresPosibles = ('Ana', 'Luis', 'Juan', 'Pedro',
                       'Daniel', 'Maria Camila', 'Natalia')
    apellidosPosibles = ('Roa', 'Arrieta', 'Vanegas', 'Cely',
                         'Mendoza',  'Rodriguez', 'Alfaro')
    numeroPersonas = 8
    grupoPersonas = []
    for _ in range(numeroPersonas):
        nombre = nombresPosibles[random.randint(0, len(nombresPosibles)-1)]
        apellido = apellidosPosibles[random.randint(
            0, len(apellidosPosibles)-1)]
        id = generarIdentificacion()
        grupoPersonas.append([nombre, apellido, id])
    return grupoPersonas


grupoPersonas = generarPersonasAleatorias()
[print(persona)for persona in grupoPersonas]  # list comprehension


def generarCodigo(persona):
    return persona[0][0:2]+persona[1][-2:]+persona[2][0:2]


print('Codigos generados: ', mapBasico(generarCodigo, grupoPersonas))


# Utilizando el map de python
print(list(map(generarCodigo, grupoPersonas)))
