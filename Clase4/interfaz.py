def bienvenida():

    print('------------------------------------------')
    print('Bienvenido Aplicacion Calculo de Impuestos')
    print('------------------------------------------')


def recogerPrecio4Productos():
    producto1 = int(input('Ingrese precio producto1: '))
    producto2 = int(input('Ingrese precio producto2: '))
    producto3 = int(input('Ingrese precio producto3: '))
    producto4 = int(input('Ingrese precio producto4: '))
    return producto1, producto2, producto3, producto4


def reporte(valorTotal):
    return f"Precio final de compra: {valorTotal}"
    # return "Precio final de compra:"+str(valorTotal)


def despedida():
    print('--------------------')
    print('Finalizacion Exitosa')
    print('--------------------')
