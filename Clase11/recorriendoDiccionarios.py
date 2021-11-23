import pprint as pp  # pretty print

# Nomina -> Lista grande (prime nivel)
# Empleado -> Lista con 2 o 3 valores: Nombres, salario, impuesto

nominaContenedoresMixtos = [
    {'Nombre': 'Ana', 'Salario': 14000},
    {'Nombre': 'Maria Fernanda', 'Salario': 20000},
    {'Nombre': 'Camila', 'Salario': 124000},
    {'Nombre': 'Luis', 'Salario': 2214000}
]

# Recorrer lista de diccionarios (subindices)
for i in range(len(nominaContenedoresMixtos)):
    print(f"Subindice: {i}")
    print(f"Nombre Empleado: {nominaContenedoresMixtos[i]['Nombre']}")
    print(f"Salario: ${nominaContenedoresMixtos[i]['Salario']}")
    print("-------------")


# Ordenamientos
salarios = [1000, 20022, 201, 3942]
print("Primera vesion de salarios: ", salarios)
print("Mayor salario", max(salarios))
salarios = sorted(salarios, reverse=True)
print("Version ordenada de salarios: ", salarios)

# Funcion que retorna un atributo del elemento de la coleccion (compuesta)


def retornarSalarioEmpleado(id, nominaContenedoresMixtos):
    return nominaContenedoresMixtos[id]['Salario']

# Usamos lambda para resumir la funcion de la linea 29 en una sola linea
# Necesitamos envolver la funcion para mandarselo a la funcion sorted para que ordene toda la nomina
# lambda es como decir el 'def' es una funcion sin nombre
# lambda parametros de entrada: parametros de salida

# La linea 44 al salvar el documento lo vuelve funcion automaticamente por eso esta
# commented out.
#retornoSalario = lambda id, nominaContenedoresMixtos : nominaContenedoresMixtos[id]['Salario']


def retornoSalario(
    id, nominaContenedoresMixtos): return nominaContenedoresMixtos[id]['Salario']


print("Salario consultado: ", retornarSalarioEmpleado(0, nominaContenedoresMixtos))
print("Salario consultado: ", retornarSalarioEmpleado(-1, nominaContenedoresMixtos))
print("-------------")
print("Salario consultado: ", retornoSalario(0, nominaContenedoresMixtos))
print("Salario consultado: ", retornoSalario(-1, nominaContenedoresMixtos))


print('Base de datos de nomina sin ordenar:')
pp.pprint(nominaContenedoresMixtos)

# Ordenando la nomina por salario usando sorted.
# Organizar a la lista nominaContenedoresMixtos, le tenemos que mandar una funcion lambda
# la vamos a envoler para enviarla, sorted tiene un campo 'key' por defecto recibe cada elemento del iterable
# En este caso el iterable es la lista de la nomina. Sorted recibe por cada elemento de la coleccion lo recibe
# como un valor, ie llamado por ejemplo elemento (linea 56) (algo asi como un diccionario) y le decimos porque
# quiere que ordene, ie por salario y de menor a mayor -> usando reverse=True
nominaContenedoresMixtos = sorted(
    nominaContenedoresMixtos, key=lambda elemento: elemento['Salario'], reverse=True)
print('Base de datos nomina ordenada salario descendente')
pp.pprint(nominaContenedoresMixtos)

print("-------------")

nominaContenedoresMixtos = sorted(
    nominaContenedoresMixtos, key=lambda elemento: elemento['Nombre'])
print('Base de datos nomina ordenada por nombre descendente')
pp.pprint(nominaContenedoresMixtos)

# Ordenamientos -> bubble sort, quick sort, selection, radix sort, merge sort

# Recorrer un diccionario
print("-------------")
diccionarioAna = nominaContenedoresMixtos[0]
for llave, valor in diccionarioAna.items():
    print("Llave -> ", llave, "Valor -> ", valor)

print("-------------")
for i, llave in enumerate(diccionarioAna.keys()):
    print(i, 'Llave -> ', llave)

print("-------------")
for i, valor in enumerate(diccionarioAna.values()):
    print(i, 'Valor -> ', valor)
