# Requerimiento: Se solicita una funcion que recoja la informacion de una
# cantidad determinada de empleados. Se espera recibir el nombre del
# empleado y el salario del empleado (dolares). Retornar cuales empleados
# deben pagar impuestos (salario superior a 10,000 USD) en una lista.
# En otra lista mostrar toda la nomina ingresada y mostrar el salario
# promedio de los empleados registrados. Agregar en el listado de los empleados
# que pagan impuestos, el valor correspondiente (5%)

# #Algoritmo:
# 1. Mientras el usuario este ingresando nomina (quiera continuar):
# 2. Coleccionar el empleado ingresado
# 3. Revisar si el empleado tiene un salario superior a 10,000 -> agregarlo en
#    el listado de los que pagan impuestos.
# 4. Calcular el salario promedio
# 5. Mostrarlo en pantalla
# 6. Retornar las listas correspondientes (empleados y empleadosImpuestos).

# Traduccion Python

def impuestosEmpleados():

    # Colecciones
    bdEmpleados = []
    empleadosImpuestos = []

    # El usuario esta especificando la nomina
    mainloop = True
    while mainloop:
        infoEmpleado = input(
            'Ingrese el nombre y salario (nom salario): ').split(' ')
        infoEmpleado[-1] = int(infoEmpleado[-1])

        # Coleccionar empleado
        bdEmpleados.append(infoEmpleado)

        # Revisar si debe pagar impuestos
        if bdEmpleados[-1][-1] > 10000:
            # Coleccion (lista) empleados que pagan impuestos
            empleadosImpuestos.append(bdEmpleados[-1].copy())
            # empleadosImpuestos.append(list(bdEmpleados[-1]))
            # Agregar los impuestos en la penultima posicion
            empleadosImpuestos[-1].insert(-1,
                                          empleadosImpuestos[-1][-1] * 0.05)

        if input("Ha terminado el registro? (s/n) ").lower() == 's':
            mainloop = False

    # Calcular salario promedio general
    salarioPromedio = 0
    for empleado in bdEmpleados:
        salarioPromedio += empleado[-1]
    salarioPromedio = salarioPromedio/len(bdEmpleados)
    print(f'El salario promedio de la nomina ingresada es {salarioPromedio}')

    # Retornar los listados solictados
    return bdEmpleados, empleadosImpuestos


# Seccion principal
nomina, detalleEmpleadosPagaImpuestos = impuestosEmpleados()
print('---- Nomina Completa ----')
for i, empleado in enumerate(nomina):
    print(f'{i+1}) {empleado}')

print('---- Empleados que pagan impuestos ----')
for i, empleado in enumerate(detalleEmpleadosPagaImpuestos):
    print(f'{i+1}) {empleado}')
