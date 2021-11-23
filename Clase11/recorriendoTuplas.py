# Ejemplo para tuplas -> Coleccionar info y que no se modifique
# Obtuvimos coordenadas de un punto
valor_x = 12
valor_y = 23
punto1 = (valor_x, valor_y, 'La Candelaria')

valor_x = 121
valor_y = 231
punto2 = (valor_x, valor_y, 'Chapinero')

puntosRecogida = [punto1, punto2]

puntosRecogida = tuple(puntosRecogida)

print('Tupla con el punto 1', punto1)
print('Tipo de dato del punto 1', type(punto1))

print('Tupla con el punto 2', punto2)
print('Tipo de dato del punto 2', type(punto2))

print('Puntos de recogida son: ', puntosRecogida)

# Recorriendo la tupla de tuplas
print('Monstrando puntos de recogida')

for i, punto in enumerate(puntosRecogida):
    print(i+1, " ", punto)


print('Mostrando puntos de recogida con subindice')
for i in range(len(puntosRecogida)):
    print(i+1, " ", puntosRecogida[i])

print('Mostrando componentes de los puntos de recogida y sector')
for i, punto in enumerate(puntosRecogida):
    print(i+1, "Componente en X: ", punto[0])
    print(i+1, "Componente en Y: ", punto[1])
    print(i+1, "Sector: ", punto[2])

print("Mostrando componente en Y de los puntod de recogida con subindice")
for i in range(len(puntosRecogida)):
    print(i+1, "Coordenada en Y: ", puntosRecogida[i][1])
