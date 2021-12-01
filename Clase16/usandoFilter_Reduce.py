# Filter: Aplica una funcion para revisar el contenido de cada posicion
# del iterable y con base en lo que revise dependiendo del requerimeinto y
# la logica que ejecuta deja un contenedor exactamente igual o un contenedor
# mas pequeno, deja los que le cumplan la funcion. La funcion retorna un booleno
# y la funcion se llama predicado.

# Requerimiento: Coleccion con las notas aprobadas para luego obtener el
# promedio de los que pasaron la materia

from functools import reduce
import random


notas = [3.5, 3.0, 4.4, 3.2, 1.0, 3.8, 2.1, 3.7, 4.0]

# Predicado:


def aprobo(nota):
    # if nota>-3:
    #     return True
    # else:
    #     return False
    return nota >= 3


coleccionNotasAprobadas = tuple(filter(aprobo, notas))
print(coleccionNotasAprobadas)


def promedio(notasEstudiante):
    return round(sum(notasEstudiante)/len(notasEstudiante), 2)


print('Promedio de los aprobados ', promedio(tuple(filter(aprobo, notas))))

# Notacion lambda
print('Notacion Lambda ->', tuple(filter(lambda x: x >= 3.0, notas)))

# Requerimiento 1: agregar una edad aleatoria al grupo de personas que tenenmos
# Requerimiento 2: Filtrar unicamente los menores de edad

grupoPersonas = [
    ['Luis', 'Roa', '54048'],
    ['Luis', 'Alfaro', '87539'],
    ['Luis', 'Rodríguez', '14697'],
    ['Luis', 'Vanegas', '49084'],
    ['Juan', 'Vanegas', '28854'],
    ['Pedro', 'Alfaro', '41835'],
    ['Juan', 'Alfaro', '18405'],
    ['Juan', 'Arrieta', '85322']
]

print(grupoPersonas)


def generarEdadAleatoria():
    return random.randint(10, 45)


# Notacion lambda
# grupoPersonasAmpliado = list(
#     map(lambda x: [x[0], x[1], x[2], generarEdadAleatoria()], grupoPersonas))

grupoPersonasAmpliado = list(
    map(lambda x: [x[0:], generarEdadAleatoria()], grupoPersonas))

print('------------------------------------------')
print('Coleccion ampliada', grupoPersonasAmpliado)

# Req 2 -> Obtener personas menores de edad


def esMenorDeEdad(persona):
    return persona[-1] <= 18


personasMenoresEdad = list(filter(esMenorDeEdad, grupoPersonasAmpliado))

print('---------------------------')
print('Menores de Edad')
[print(persona) for persona in personasMenoresEdad]

# Reduce -> Devuelve solo un elemento, puede ser una coleccion que salga
# de acumular informacion. Ejemplo una coleccion de numeros y quiero sumarlos

# Sumatoria de una coleccion de numeros

numeros = list(range(1, 10))
print('Lista generada ', numeros)
# Reduce recibe dos parametros: un acumulador que es buena idea inicializarlo
# un 2do elemento que se llama elemento  y retorna lo que se haga con el
# elemento y el acumulador sobre la coleccion
print('Resultado reduce es -> ', reduce(lambda elemento=0,
      acumulador=0: elemento+acumulador, numeros))

# Req: Concatenar en una cadena todos los nombres del listado de personas
print(reduce(lambda nombresConcatenados='',
      persona='': nombresConcatenados + ' ' + persona,  map(lambda x: x[0], grupoPersonas)))
