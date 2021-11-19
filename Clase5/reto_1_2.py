'''
Se requiere una funcion que reciba la edad de un grupo de personas, y 
seleccione las personas que son mayores de edad. Si el grupo tiene por lo 
menos dos personas mayores de edad (acudientes), se aprueba su participacion
en un torneo. Adicionalmente, si cumple con el numero de acudientes, mostrar
la edad promedio de los acudientes
'''

# Algoritmo
# 1. Cargar la edad de 4 personas por teclado
# 2. Mirar cuales personas son mayores de edad
# 3. Mirar si al menos dos personas son mayores de edad
# 3.a Si hay dos mayores de edad se les da acceso al torneo
# 3.a.1 Si hay dos mayores de edad reportar la edad promedio de las personas mayores de edad
# 3.b nada

EdadPersona1 = int(input('Ingrese edad persona 1: '))
EdadPersona2 = int(input('Ingrese edad persona 2: '))
EdadPersona3 = int(input('Ingrese edad persona 3: '))
EdadPersona4 = int(input('Ingrese edad persona 4: '))

mayores18 = 0
EdadPromedio = 0

if EdadPersona1 >= 18:
    mayores18 += 1
    EdadPromedio += EdadPersona1
if EdadPersona2 >= 18:
    mayores18 += 1
    EdadPromedio += EdadPersona2
if EdadPersona3 >= 18:
    mayores18 += 1
    EdadPromedio += EdadPersona3
if EdadPersona4 >= 18:
    mayores18 += 1
    EdadPromedio += EdadPersona4

if mayores18 >= 2:
    EdadPromedioTotal = int(EdadPromedio/mayores18)
    print(
        f'La edad promedio del grupo de participantes es {EdadPromedioTotal} años')
