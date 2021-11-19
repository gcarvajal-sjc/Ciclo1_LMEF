# Objetivo -> Determiar si se apureba o se rechaza un credito, retornado la respuesta
# en un diccionarion con una estructura especifica.

# #Algoritmo
# 1. Estandarizacion de las variables
# 2. Reflejar arbol de decisiones de la entidad bancaria
# 3. Retornar el dictamen del arbol de decisiones

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


def prestamo(informacion):

    # Estandarizacion
    id_prestamo = informacion['id_prestamo']

    # #Primera forma
    # casado = bool()
    # if informacion['casado']== 'Si':
    #     casado = True
    # else:
    #     casado = False

    # #Segunda forma
    # casado = False
    # if informacion[casado]== 'Si':
    #     casado = True

    # ----------------------
    # Casado
    # Tercera forma
    casado = informacion['casado'] == "Si"

    # ----------------------
    # Dependientes

    # dependientes = estandarizarAlfanumberico(informacion['dependientes'])

    # Condicional en una sola linea Python (bonus)
    # if condicion:
    #     (h,v -> return) -> h means haga si es v -> verdadero
    # else:
    #     (h,f -> return)  -> h means haga si es f -> falso
    # (h,v) if condicion else (h,f)

    # Segunda forma
    dependientes = informacion['dependientes'] if isinstance(
        informacion['dependientes'], int) else 3

    # ----------------------
    # Graduado

    graduado = informacion['educacion'] == 'Graduado'

    # ----------------------
    # Independiente

    independiente = informacion['independiente'] == 'Si'

    # ----------------------
    # Semiurbana

    semiurbana = informacion['tipo_propiedad'] == 'Semi Urbana'

    # Copias de los campos del diccionario que no necesitan estandarizacion

    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazo_prestamo']
    h_c = informacion['historia_credito']

    decision = False
    # Arbol de decisiones
    if h_c:
        # Cuando el cliente tiene historial crediticio
        if i_c > 0 and i_d/9 > c_p:
            # cumple ingresos de codeudor e ingresos de solicitante
            decision = True
        else:
            if dependientes > 2 and independiente:
                decision = i_c/12 > c_p
            else:
                decision = c_p < 200
    else:
        # Cuando no tiene el cliente historial crediticio
        if independiente:
            if not(casado and dependientes > 1):
                if i_d/10 > c_p or i_c/10 > c_p:
                    decision = c_p < 180
                else:
                    decision = False
            else:
                decision = False
        else:
            # Trabajador dependiente
            if not(semiurbana) and dependientes < 2:
                if graduado:
                    decision = i_d/11 > c_p and i_c/11 > c_p
                else:
                    decision = False
            else:
                decision = False

    # Diccionario con la decision del prestamo

    diccionarioDecision = {
        'id_prestamo': id_prestamo,
        'aprobado': decision
    }

    return(diccionarioDecision)

# Seccion principal -> pruebas


# Casos de prueba
diccionario1 = dict(id_prestamo='RETOS2_001',
                    casado='No',
                    dependientes=1,
                    educacion='Graduado',
                    independiente='Si',
                    ingreso_deudor=4692,
                    ingreso_codeudor=0,
                    cantidad_prestamo=106,
                    plazo_prestamo=360,
                    historia_credito=1,
                    tipo_propiedad='Rural')

diccionario2 = dict(id_prestamo='RETOS2_002',
                    casado='No',
                    dependientes='3+',
                    educacion='No Graduado',
                    independiente='No',
                    ingreso_deudor=1830,
                    ingreso_codeudor=0,
                    cantidad_prestamo=100,
                    plazo_prestamo=360,
                    historia_credito=0,
                    tipo_propiedad='Urbano')

diccionario3 = dict(id_prestamo='RETOS2_003',
                    casado='No',
                    dependientes='0',
                    educacion='No Graduado',
                    independiente='No',
                    ingreso_deudor=3748,
                    ingreso_codeudor=1668,
                    cantidad_prestamo=110,
                    plazo_prestamo=360,
                    historia_credito=1,
                    tipo_propiedad='Semiurbano')

# Correr las pruebas
print(prestamo(diccionario1))
print(prestamo(diccionario2))
print(prestamo(diccionario3))
