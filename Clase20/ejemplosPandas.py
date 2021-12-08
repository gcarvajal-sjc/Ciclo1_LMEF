# Librerias
import numpy as np
import pandas as pd
import random

from pandas.core.accessor import PandasDelegate

# Series -> Columnas
# Dataframes -> Hoja de calculo

# Construir series: Tienen dos argumentos principales que uno manda en el
# siguiente orden: 1. Los contenidos de las celdas de la columna, y el 2do
# el nombre de cada fila (sino se le define pandas lo resuelve solo)
serie = pd.Series([33, 44, 55], index=['Fila1', 'Fila2', 'Fila3'])
print(serie)
print('Valores de la serie(columna)')
print(serie.values)
print('Tipo de coleecion de los valores: ', type(serie.values))
print('Indices de la serie(columna)')
print(serie.index)

# Partiendo de un diccionario
diccionario = {'Carlos': 5, 'Pedro': 4.8, 'Juan': 5.0}
serieDiccionario = pd.Series(diccionario)
print('Serie a partir de diccionario')
print(serieDiccionario)
print('Indice', serieDiccionario.index)
print('Valores', serieDiccionario.values)

# Dataframe -> varias series
numEstudiantes = 10
nombres = ['carlos', 'pedro', 'juan', 'natalia', 'valentina', 'camila']
codigos = ['asjhd7', 'asjhd8', 'asjhd9', 'asjhd2', 'asjhd1']
estado = ['matriculado', 'suspendido', 'becado']
# notacion de list comprehension con for sencillo. Hacer algo cierto
# numero de veces pero no necesito llevar un conteo, no necesito tener
# una memoria auxiliar que me este cargando la info -> entonces no
# necesito el 'i', solo necesito que algo suceda cierto numero de veces
# Cinco veces selecciona aletoria% un nombre y los acumula en una lista.
# y esa lista se le manda a la serie, como no se le especifica un indice y
# solo se le manda una lista, se va a convertir en una columna que es
# serie1 y automaticamente va a tener unos autonumericos, lo mismo para serie2
serie1 = pd.Series([random.choice(nombres) for _ in range(5)])
serie2 = pd.Series([random.randint(100, 200)for _ in range(5)])
serie3 = pd.Series([random.choice(estado)
                   for _ in range(5)], index=[0, 1, 2, 3, 55])  # 55 is out of range therefore it solves it as NaN
print(serie1)
print(serie2)
print(serie3)
diccionarioSeries = {'Nombres': serie1, 'Puntaje': serie2}
# Si las dos series tienen el mismo tamańo se puede armar el dataframe.
# Los indices tienen que ser comunes (osea que tengan el mismo numero de datos)
# df = pd.DataFrame(serie1, serie2)
df = pd.DataFrame(diccionarioSeries)
df['Estado'] = serie3
df['Codigo'] = pd.Series(codigos)
print('Nombres columnas')
print(df.columns)
df.columns.name = 'Estudiantes'
df.index.name = 'Autonumerico'
df_original = df.copy()
df.set_index('Codigo', inplace=True)
print(df)
print()
print()
print('Original')
print(df_original)
