# Calculos de la edad de las personas para ver si son mayores de 18 años

def mayor18(edadPer1, edadPer2, edadPer3, edadPer4):
    mayores18 = 0
    edadPromedio = 0

    if edadPer1 >= 18:
        mayores18 += 1
        edadPromedio += edadPer1
    if edadPer2 >= 18:
        mayores18 += 1
        edadPromedio += edadPer2
    if edadPer3 >= 18:
        mayores18 += 1
        edadPromedio += edadPer3
    if edadPer4 >= 18:
        mayores18 += 1
        edadPromedio += edadPer4
    return mayores18, edadPromedio


def reportar(mayores18, edadPromedio):

    if mayores18 >= 2:
        edadPromedioTotal = int(edadPromedio/mayores18)
        print(
            f'La edad promedio del grupo mayores de 18 años es: {edadPromedioTotal} años')
    else:
        print('Lo sentimos, inscripción no aprobada')
