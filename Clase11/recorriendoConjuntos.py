conjunto = set()
conjunto.add('elemento1')
conjunto.add('elemento2')

print('Mostrar inicializacion del conjunto: ', conjunto)
print(type(conjunto))

# Eliminar repetciones usando conjuntos
lista = ['elemento1', 'elemento1', 'elemento2', 'elemento1']
listaSinRepeticiones = list(set(lista))
print('Version lista sin repetciones', listaSinRepeticiones)

# Eliminar repeticiones usando listas

lista = ['elemento1', 'elemento1', 'elemento2', 'elemento1']
listaSinRepeticiones2 = []
for elemento in lista:
    if not elemento in listaSinRepeticiones2:
        # if elemento not in listaSinRepeticiones2:  -> otra notacion de la misma linea 18
        listaSinRepeticiones2.append(elemento)
print('Lista_2 sin repeticiones', listaSinRepeticiones2)


conjuntoAnimales = {'Perro', 'Gato', 'Caballo', 12}
print('Conjunto de anmiales', conjuntoAnimales)

print('Recorrido por los elementos del conjunto')
for animal in conjuntoAnimales:
    print(animal)
