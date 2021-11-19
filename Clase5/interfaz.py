# Funcion de int

def bienvenida():
    print('---------------------------------------------------')
    print('Bienvenidos a la inscripcion del torneo programitas')
    print('---------------------------------------------------')


def pedirInfo():
    nombrePersona1 = input('Ingrese nombre de la persona 1: ')
    edadPersona1 = int(input('Ingrese edad persona 1: '))
    nombrePersona2 = input('Ingrese nombre de la persona 2: ')
    edadPersona2 = int(input('Ingrese edad persona 2: '))
    nombrePersona3 = (input('Ingrese nombre de la persona 3: '))
    edadPersona3 = int(input('Ingrese edad persona 3: '))
    nombrePersona4 = input('Ingrese nombre de la persona 4: ')
    edadPersona4 = int(input('Ingrese edad persona 4: '))
    return nombrePersona1, edadPersona1, nombrePersona2, edadPersona2, nombrePersona3, edadPersona3, nombrePersona4, edadPersona4
