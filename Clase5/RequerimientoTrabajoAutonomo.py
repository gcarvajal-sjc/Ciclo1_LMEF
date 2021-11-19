# Hacer el mismo ejercicio reto_1_2.py pero modularizado

# Algoritmo
# 1. Saludar
# 2. Pedir datos de la edad y el nombre
# 3. Calcular cuantas personas son mayores de 18
# 4. Reportar si se aprueba
# 5. Reportar si se cumple

from interfaz import bienvenida as bv
from interfaz import pedirInfo as datos
from logica import mayor18 as m18
from logica import reportar

bv()

nombrePersona1, edadPersona1, nombrePersona2, edadPersona2, nombrePersona3, edadPersona3, nombrePersona4, edadPersona4 = datos()

mayores18, edadPromedioTotal = m18(
    edadPersona1, edadPersona2, edadPersona3, edadPersona4)
 
reportar(mayores18, edadPromedioTotal)
