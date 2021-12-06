# Librerias de soporte
import numpy as np
import random

# Requerimiento general -> Simulacion de dos robots jugando tres en raya
# Requerimientos especificos -> Jugdor O
#                           -> Jugador X
#                           -> Sistema que controlael tablero que modifican los jugadores(bots)

# Codificacion
# Tablero -> matriz de numpy
# Jugador 0 ->1
# Jugador X -> 10
# Posicion libre del tablero -> 0
# Interfaz ->mostrar el tablero con X, O , _


# Interaccion
def mostrarTablero(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == 1:
                print('O', end=' ')
            if casilla == 10:
                print('X', end=' ')
            elif casilla == 0:
                print('_', end=' ')
        print()  # Separar las filas del tablero
    print()  # Separar el tablero en la pantalla

# Logica


def formatoCV(casillasVacias):
    listaFilas = list(casillasVacias[0])
    listaColumnas = list(casillasVacias[1])
    listaCV = list(zip(listaFilas, listaColumnas))
    return listaCV


def jugadorX(tablero):
    casillasVacias = np.where(tablero == 0)
    listaCV = formatoCV(casillasVacias)
    casillaElegida = random.choice(listaCV)
    tablero[casillaElegida] = 10


def jugadorO(tablero):
    casillasVacias = np.where(tablero == 0)
    listaCV = formatoCV(casillasVacias)
    casillaElegida = random.choice(listaCV)
    tablero[casillaElegida] = 1


def estadoTablero(tablero):
    # Gana el jugador O
    ganaFila = 3 in np.sum(tablero, axis=1)
    ganaColumna = 3 in np.sum(tablero, axis=0)
    ganaDiagonal = 3 == np.sum(tablero.diagonal())
    ganaDiagonalContraria = 3 == np.sum(np.fliplr(tablero).diagonal())
    if any([ganaColumna, ganaFila, ganaDiagonal, ganaDiagonalContraria]):
        return 1

    # Gana el jugador X
    ganaFila = 30 in np.sum(tablero, axis=1)
    ganaColumna = 30 in np.sum(tablero, axis=0)
    ganaDiagonal = 30 == np.sum(tablero.diagonal())
    ganaDiagonalContraria = 30 == np.sum(np.fliplr(tablero).diagonal())
    if any([ganaColumna, ganaFila, ganaDiagonal, ganaDiagonalContraria]):
        return 10

    # Empate
    empateIniciandoO = np.sum(tablero) == 45
    empateIniciandoX = np.sum(tablero) == 54
    if any([empateIniciandoO, empateIniciandoX]):
        return 0

    # No se cumple ninguna
    return -1


# Seccion principal (sistema)
# ---------------------------
# Inicializa el juego
tablero = np.zeros((3, 3))
mostrarTablero(tablero)

# Forzar modificaciones para calibrar nuestros jugadores
# print('Modificaciones sobre el tablero')
# tablero[0, 0] = 1
# tablero[2, 2] = 10
# mostrarTablero(tablero)

# # Jugador percibiendo el tablero y afectando el tablero
# jugadorX(tablero)
# mostrarTablero(tablero)
# jugadorO(tablero)
# mostrarTablero(tablero)
# jugadorX(tablero)
# mostrarTablero(tablero)
# jugadorO(tablero)
# mostrarTablero(tablero)
# jugadorX(tablero)
# mostrarTablero(tablero)
# jugadorO(tablero)

# Sistema va a elegir el jugador que inicia
jugadorElegido = 1 if random.randint(0, 1) else 10

# Sistema le da el turno al jugador seleccionado
if jugadorElegido == 1:
    jugadorO(tablero)
    jugadorElegido = 10
else:
    jugadorX(tablero)
    jugdoreElegido = 1
    print(jugadorElegido)

mostrarTablero(tablero)

# Simulacion
while True:
    # Revisar si el tablero aun tiene posiciones
    casillasVacias = np.where(tablero == 0)
    if len(casillasVacias[0]) == 0:
        break

    # Sistema le da el turno al jugador seleccionado
    if jugadorElegido == 1:
        jugadorO(tablero)
        jugadorElegido = 10
    else:
        jugadorX(tablero)
        jugadorElegido = 1

    # Evolucion del tablero con la intervencion de los jugadores bots
    mostrarTablero(tablero)
    # Pausa en la salida
    input()
