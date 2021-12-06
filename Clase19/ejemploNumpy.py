# libreria para arreglos o matrices
import numpy as np
import random

# Crear coleccines tipo numpy -> arreglos
arreglo1 = np.array([[1, 2], [3, 4]])
print(arreglo1)
print('Tipo', type(arreglo1))


arreglo2 = np.array([[1, 2], [3, 4, 5, 6]])
print(arreglo2)
print('Tipo', type(arreglo2))

lista = [[1, 2, 4], [4, 5, 6]]
arreglo3 = np.array(lista)
print('Tipo', type(arreglo3))

# Arreglos se pueden generar usando rangos, con valores aleatorios, con
# seleccion de valores aleatorios.
arregloGenerado = np.zeros(5)
print(arregloGenerado)

matrizGenerada = np.zeros((3, 4))
print(matrizGenerada)

matrizGenerada = np.ones((5, 5))
print(matrizGenerada)

arregloRango = np.arange(1, 6, 2)
print(arregloRango)

arregloAleatorio = np.random.randint(-5, 5, size=7)
print(arregloAleatorio)

matrizAleatoria = np.random.randint(-5, 5, size=(7, 7))
print(matrizAleatoria)

departamentos = ['valle', 'tolima', 'cesar', 'atlantico']
arregloDepartamentos = np.random.choice(
    departamentos, size=3, p=[0.1, 0.1, 0.6, 0.2])  # p = probabilidad
print(arregloDepartamentos)

matrizDepartamentos = np.random.choice(
    departamentos, size=(3, 4), p=[0.1, 0.1, 0.6, 0.2])
print(matrizDepartamentos)

requerimientoJahleel = np.array(departamentos)
np.random.shuffle(requerimientoJahleel)
print('Sin repeticiones y orden aleatorio', requerimientoJahleel)

# Consultas (recorrer extraer partes del contenedor)
matrizAleatoria = np.random.randint(-5, 5, size=(6, 4))
print(matrizAleatoria)

# # Consultar tamaño
# print("Numero de filas ->", len(matrizAleatoria))
# print("Numero de columnas ->", len(matrizAleatoria[0]))
# print("Forma de la matriz ->", np.shape(matrizAleatoria))
# print("Tipo de la forma ->", type(np.shape(matrizAleatoria)))

# Acceder a valores o a posiciones
print("Valor de la esquina superior izq ->", matrizAleatoria[0, 0])
print("Valor de la diagonal ->", matrizAleatoria[2, 2])

submatriz = matrizAleatoria[1:4, 1:]
print(submatriz)

# Recorridos for-> con variables auxiliares o temporales, con subindices
print("Recorrido 1 de la matriz aleatoria")
for fila in matrizAleatoria:
    for columna in fila:
        print(columna, end=' ')
    print()
print("Recorrido 2 de la matriz aleatoria")
for i in range(len(matrizAleatoria)):
    for j in range(len(matrizAleatoria[i])):
        print(matrizAleatoria[i, j], end=' ')
    print()


# Consultas (recorrer extraer partes del contenedor)
matrizAleatoria = np.random.randint(3, size=(3, 3))
print(matrizAleatoria)

# Operaciones (Las columnas son el eje 0 ->eje Y, y las filas el eje 1 -> eje X)
sumatoriaColumnas = np.sum(matrizAleatoria, axis=0)
print(sumatoriaColumnas)

sumatoriaFilas = np.sum(matrizAleatoria, axis=1)
print(sumatoriaFilas)

print('Sumatoria de toda la matriz', np.sum(matrizAleatoria))

print("Diagonal de la matriz:")
print(matrizAleatoria.diagonal())
print('La transpuesta (para visualizaciones)')  # Las filas las vuelve columnas
print(matrizAleatoria.transpose())

print("Espejo de las columnas")
print(np.fliplr(matrizAleatoria))

# El espejo sirve si queremos la diagonal contraria y pedimos nuevamente la diagonal
print("Diagonal contraria")
print(np.fliplr(matrizAleatoria).diagonal())

print("Efecto sobre la matriz original")
print(matrizAleatoria)

print('Ubicacion de los valores iguales a 2')
print(np.where(matrizAleatoria == 2))
