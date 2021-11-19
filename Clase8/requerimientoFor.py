# Requerimiento: Escribir una funcion que valide que un correo electronico
# ingresado solamente tenga una arroba, mostrar en pantalla la posicion de
# las arrobas que esten sobrando.

# Objetivo: Numero valido de arrobas en un correo (unica arroba)

# #Algoritmo
# 1. Ingresar correo electronico
# 2. Iniciar contador de arrobas
# 3. Recorrer todos los caracteres que constituyen el correo
# 3.a si encontramos una @ incrementa contador de arrobas
# 4. Revisar el numero de arrobas y reportar si el correo es valido en este contexto.

# Traduccion Python

def validarCorreo(email):
    contadorArrobas = 0

    # Forma usando subindice
    # for i in range(len(email)):
    #     if email[i] == '@':
    #         contadorArrobas += 1
    #         if contadorArrobas > 1:
    #             return f'Hay una arroba sobrante en la posicion {i}'

    # Forma cargando en una variable cada elemento
    # contadorPosicion = 0
    # for letra in email:
    #     if letra == '@':
    #         contadorArrobas += 1
    #         if contadorArrobas > 1:
    #             return f'Hay {contadorPosicion} arroba(s) sobrante(s)'
    #         contadorPosicion += 1

    # Forma utilizando enumerate

    for i, letra in enumerate(email):
        if letra == '@':
            contadorArrobas += 1
            if contadorArrobas > 1:
                return f'Hay una arroba sobrante en la posicion {i}'

    if contadorArrobas == 1:
        return f'El correo tiene el numero correcto de arrobas'
    elif contadorArrobas == 0:
        return f'El correo no tiene diferencicado el dominio. 0 arrobas encotradas'
    elif contadorArrobas > 1:
        return f'El correo tiene {contadorArrobas -1} arroba(s) de sobra'


print('jose@msn.com', validarCorreo('jose@msn.com'))
print('jose@@msn.com', validarCorreo('jose@@msn.com'))
print('jose@3@@msn.com', validarCorreo('jose@3@@msn.com'))
print('jose@33@msn.com', validarCorreo('jose@33@msn.com'))
print('jose@3333@##msn.com', validarCorreo('jose@3333@##msn.com'))
print('jose@123msn.com', validarCorreo('jose@123msn.com'))
