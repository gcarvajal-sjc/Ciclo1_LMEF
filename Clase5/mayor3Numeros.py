# Se requiere una funcion que reciba 3 numeros que son diferentes
# y determine cual es el mayor de ellos. Observacion: los numeros no
# estan ordenados.

# Objetivo -> reportar el mayor numero

# Algoritmo
# 1.Ingresar 3 numeros a, b, y c
# 2.Revisar si a>b
# 3.Si a>b revisar si a>c
# 4.Si a>c print a es el numero mayor de los tres
# 5.Del falso de 3 -> print c es el mayor
# 6.Del falso de 2 -> revisar si b>c
# 7.Si b>c -> print b es el mayor

def calcularMayor3Numeros(a, b, c):

    if a > b:
        if a > c:
            print(a, "a es el mayor numero")
        else:
            print(c, "c es el mayor numero")
    else:
        if b > c:
            print(b, "b es el mayor numero")
        else:
            print(c, "c es el mayor numero")


a = int(input('ingrese 1er numero: '))
b = int(input('ingrese 2do numero: '))
c = int(input('ingrese 3er numero: '))
calcularMayor3Numeros(a, b, c)
