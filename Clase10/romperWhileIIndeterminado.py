from typing import Tuple


estamosFuncionando = True

while estamosFuncionando:
    print("Todo en orden")
    if input("Desea detenerse? (s/n) ").lower() == 's':
        estamosFuncionando = False
