# Hibrido programacion funcional en Python:
# 1. Minimizar las asignaciones a variables (cambios de estado de las variables)
# 2. Tratamos a las funciones como variables: - Funciones de primera clase
#                                            - Funciones de orden superior: pueden recibir construir o devolver funciones. Se busca que no accedan a estados globales.
# 3. Minimizar el acceso a estados globales

# Calculadora estilo programacion funcional
# Una funcion que reciben o retornan funciones son funciones de orden superior
def operacion(signo):
    if signo == '+':
        def suma(a=0, b=0):
            return a+b
        return suma
    elif signo == '-':
        def resta(a=0, b=0):
            return a-b
        return resta
    elif signo == '*':
        def multiplicacion(a=0, b=0):
            return a*b
        return multiplicacion
    elif signo == '/':
        def division(a=0, b=1):
            return a//b
        return division
    else:
        def f(a=0, b=0):
            return (a, b)
        return f


def calculadora(signo, a, b):
    # # Construir o solicitar a otra funcion la construccion del proceso que debe hacer
    # funcionAplicar = operacion(signo)

    # # Aplicar funcion construida en tiempo de ejecucion
    # return funcionAplicar(a, b)

    # Mas resumido que las lineas de la 33 a la 37

    return operacion(signo)(a, b)


# Utilizar funcion
print(calculadora('+', 7, 8))
print(calculadora('-', 7, 8))
print(calculadora('*', 7, 8))
print(calculadora('/', 7, 8))
print(calculadora('+adfdf', 7, 8))

# Utilizar funcion recogiendo info del teclado
print(calculadora(input('Signo -> '), int(input('a = ')), int(input('b = '))))


