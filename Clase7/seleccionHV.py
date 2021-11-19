# Objetivo:  Aprobar o rechachar hv de desarrolladores con unos lineamientos especificos.

# Algoritmo:
# 1. Estandarizar la info -> Algunos valores tipo string que son cantidades
# 2. Revisar si cumple el promedio alto de años de experiencia
# 2.a Si no  lo cumple, revisar si cumple con lo minimo (ambas -> conjuncion o 'y' logico):
#     - Promedio minimo de experiencia
#     - Escolaridad y timepo de egreso
# 3. Dependiendo de las revisiones, reportar si se aprueba o se rechaza

# Traduccion -> Python

candidato1 = {
    "nombreCompleto": "Juan Perez",
    "documentoIdentidad": "60257818",
    "expJava": 1.5,
    "expPascal": '3+',
    "expNET": 0,
    "nivelEstudios": 0,
    "añosEgreso": 0
}

candidato2 = {
    "nombreCompleto": "Estudiante Mintic",
    "documentoIdentidad": "50257818",
    "expJava": '3+',
    "expPascal": 0,
    "expNET": '3+',
    "nivelEstudios": "Profesional",
    "añosEgreso": '2+'
}


def estandarizarAlfanumberico(valorAlfanumerico):

    # Estandarizacion: usamos isintance(v,t) v=variable and t= type returns TRUE/FALSE
    # Revision de tipos y parseo
    # Retorno

    valorNumerico = float()
    if isinstance(valorAlfanumerico, str):
        valorNumerico = float(valorAlfanumerico[0])
    else:
        valorNumerico = float(valorAlfanumerico)
    return valorNumerico

# Modularizacion requerimiento


def probarCandidato(candidato):
    expJava = estandarizarAlfanumberico(candidato["expJava"])
    expPascal = estandarizarAlfanumberico(candidato["expPascal"])
    expNET = estandarizarAlfanumberico(candidato["expNET"])
    aEgreso = estandarizarAlfanumberico(candidato["añosEgreso"])

    experienciaPromedio = sum((expJava, expPascal, expNET)) / 3

    if experienciaPromedio >= 2.5:
        return f"El candidato {candidato['nombreCompleto']} ha sido aprobado"
    elif experienciaPromedio >= 1.5 and aEgreso >= 2:
        return f"El candidato {candidato['nombreCompleto']} ha sido aprobado"
    else:
        return f"El candidato {candidato['nombreCompleto']} ha sido rechazado"


print(probarCandidato(candidato1))
print(probarCandidato(candidato2))


# experienciaJava = float()
# if isinstance(candidato1["expJava"], str):
#     experienciaJava = float(candidato1["expJava"][0])
# else:
#     experienciaJava = float(candidato1["expJava"])

# expJava = estandarizarAlfanumberico(candidato2["expJava"])
# expPascal = estandarizarAlfanumberico(candidato2["expPascal"])
# expNET = estandarizarAlfanumberico(candidato2["expNET"])
# aEgreso = estandarizarAlfanumberico(candidato2["añosEgreso"])

# experienciaPromedio = sum((expJava, expPascal, expNET)) / 3

# if experienciaPromedio >= 2.5:
#     print("El candidato ", candidato2["nombreCompleto", " ha sido aprobado"])
# elif experienciaPromedio >= 1.5 and aEgreso >= 2:
#     print(f"El candidato {candidato2['nombreCompleto']} ha sido aprobado")
# else:
#     print(f"El candidato {candidato2['nombreCompleto']} ha sido rechazado")
