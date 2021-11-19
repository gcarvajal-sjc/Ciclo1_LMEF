# Precio final de venta de productos cargados sin IVA

# Algoritmo:
# 1. Cargar el precio sin IVA de cada producto
# 2. Cargar el valor del IVA (porcentaje, float)
# 3. Inicializamos un acumulador para el impuesto de cada producto
# 4. Calcular el IVA del primer producto y sumarlo al acumulador
# 5. Calcular el IVA del 2do producto y sumarlo al acumulador
# 6. Calcular el IVA del 3er producto y sumarlo al acumulador
# 7. Calcular el IVA del 4to producto y sumarlo al acumulador
# 8. Calculamos el valor total de los productos
# 9. Sumamos al valor total de los productos el acumulado de impuestos

from logica import precioFinalVenta as pfv
from interfaz import bienvenida as bv, despedida
from interfaz import recogerPrecio4Productos as r4p
from interfaz import reporte as rp
from interfaz import despedida as dp
from logica import precioFinalVenta2 as pfv2


# producto1 = 1200000
# producto2 = 1500000
# producto3 = 350000
# producto4 = 4000000

# Interaccion
# print('------------------------------------------')
# print('Bienvenido Aplicacion Calculo de Impuestos')
# print('------------------------------------------')

bv()

# producto1 = int(input('Ingrese precio producto1: '))
# producto2 = int(input('Ingrese precio producto2: '))
# producto3 = int(input('Ingrese precio producto3: '))
# producto4 = int(input('Ingrese precio producto4: '))

producto1, producto2, producto3, producto4 = r4p()

# Logica que nos llevamos al script logica.py
#precioFinalVenta = pfv(producto1, producto2, producto3, producto4)

precioFinalVenta = pfv2(producto1, producto2, producto3, producto4)

# Interaccion2


# print("El valor total de los productos es: $", precioFinalVenta)
print(rp(precioFinalVenta))
# print('--------------------')
# print('Finalizacion Exitosa')
# print('--------------------')
dp()
