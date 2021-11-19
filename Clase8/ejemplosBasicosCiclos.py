# Objetivo: mostrar en pantalla los 20 primeros numeros enteros

# #Algoritmo:
# 1. Mostrar el num 1
# 2. Mostrar el num 2
#  . ...
# 3. Finalizar cuando los 20 numeros han sido mostrados

# #Traduccion
# print(1)
# print(2)
# ...
# print(20)


# Primera Variante: range(limSuperior) -> LimInferior: 0, Avance: 1 (por defecto)
# Segunda Variante: range (limInferior, limSuperior)-> Avance: 1
# Tercera Variante: range(limiteInferior, limSuperior, Avance)


# Tener en cuenta las variantes:
# Primera variante:
num = 1
for num in range(20):
    print(num+1, end='-')

# Segunda variante:
num = 1
for num in range(1, 21):
    print(num, end='/')

# Tercera variante:
num = 1
for num in range(1, 21, 2):
    print(num, end='-')

# Usando while
x = 1
while x <= 20:
    print(x)
    x += 1
