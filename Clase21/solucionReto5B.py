# Librerias
import pandas as pd

# Funcion respondiendo al requerimiento


def indicadoresPetroleo(rutaArchivo):
    # Analizar la extension del archivo
    if rutaArchivo[-3:].lower() != 'csv':
        return 'Extension invalida'

    # Si cumple la extension del archivo cargar el archivo en un dataframe para trabajar
    # Hay que tener cuidado porqeu vamos a hablar con capa externa a la aplicacion donde estamos
    try:
        df = pd.read_csv(rutaArchivo, sep=',')
    except:
        return 'Error al leer el archivo de datos'
    # #Salida de diagnostico
    # print('Contenido del dataframe cargado')
    # print(df)
    # print('Nombres de las columnas')
    # print(df.columns)

    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
    df.set_index("Fecha", inplace=True)

    # Calcular la variacion
    variacion = list()
    for i in range(len(df['Ecopetrol'])-1):
        calculo = (
            abs(df['Ecopetrol'][i]-df['Ecopetrol'][i+1])/df['Ecopetrol'][i])*100
        variacion.append(calculo)

    # # Observacion de la variacion (no hace parte del requerimiento)
    # df['Variacion'] = pd.Series(variacion)
    # print(df)  # para ver este print tiene que hacer grayout de linea 25 df.set_index("Fecha", inplace=True)

    # Conversion buscando aprovechas las funciones de pandas
    variacion = pd.Series(variacion)
    promedioVariacion = variacion.mean

    # Promedio de casos de COVID
    promedioCasos = df['Casos'].mean()
    df = df[df['Casos'] <= promedioCasos]
    # print(df)

    # Graficando opcional de los casos acumulados en cada mes despues de la manipulacion
    import matplotlib.pyplot as plt
    dataCasosMes = df['Casos'].groupby(df.index.month).sum()
    dataCasosMes.plot(kind='barh', color='red')
    plt.title('Total casos por mes')
    plt.xlabel('Mes')
    plt.ylabel('Numero de casos')
    plt.show()

    # Graficando opcional del valor medio de la accion de ecopetrol de cada mes despues de la manipulacion

    dataMediaPrecioMes = df['Ecopetrol'].groupby(df.index.month).mean()
    dataMediaPrecioMes.plot(color='green')
    plt.title('Valor Ecopetrol promedio')
    plt.xlabel('Mes')
    plt.ylabel('Valor')
    plt.show()

    # Retorno solicitado
    return {'Promedio Variacion': promedioVariacion, 'Registros Menores': df}


# Seccion principal
print(indicadoresPetroleo('BaseDeDatosReto5.csv'))

# CONTINUA EN 2:10 DEL 16/06/21
