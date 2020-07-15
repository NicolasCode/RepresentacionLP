import json
from DPLL import *
from Codificacion import *
from FNC import *
import numpy as np

Nfilas = 3
Ncolumnas = 3
Nnumeros = 3 # Se asume que E es 0, O es 1, X es 2
Nturnos = 2


def interpreta_tablero(tablero):
    inicial = True

    # for l in tablero:
    #     if inicial:
    #         letra = [[P(*l, 0, Nfilas, Ncolumnas, Nnumeros, Nturnos)]]
    #         inicial = False
    #     else:
    #         letra += [[P(*l, 0, Nfilas, Ncolumnas, Nnumeros, Nturnos)]]

    for i in range(3):
        for j in range(3):
            if inicial:
                letra = [[P(i, j, tablero[i, j], 0, Nfilas, Ncolumnas, Nnumeros, Nturnos)]]
                inicial = False
            else:
                letra += [[P(i, j, tablero[i, j], 0, Nfilas, Ncolumnas, Nnumeros, Nturnos)]]

    return letra

def cargar_reglas(tablero):
    # Cargando reglas
    with open('reglas.json', 'r') as file:
        reglas = json.load(file)

    # rw = list(reglas.keys())
    rw = ['regla0', 'regla1', 'regla3', 'regla4', 'regla5', 'regla2']
    # rw = []
    print("Trabajando con reglas", rw)

    formula = interpreta_tablero(tablero)

    for r in rw:
        formula += reglas[r]

    return formula

def calcular_resultado(formula):

    S, I = DPLL(formula, {})

    print(S)
    # print(I)
    resultado_turno0 = []
    resultado_turno1 = []
    letras = [chr(x) for x in range(256, 311)]
    for i in I.keys():
        if i in letras:
            if I[i] == 1:
                fila = list(Pinv(i, Nfilas, Ncolumnas, Nnumeros, Nturnos))
                if fila[3] == 0:
                    resultado_turno0.append(fila)
                elif fila[3] == 1:
                    resultado_turno1.append(fila)
                else:
                    print("Oops!", i, fila)

    #imprime(resultado_turno0)
    imprime(resultado_turno1)
    resultado = np.matrix([[0]*3]*3)
    for l in resultado_turno1:
        resultado[l[0], l[1]] = l[2]

    print(resultado)

    return resultado

def tablero_inicial():
    # Inicializamos el tablero
    # tablero = [
    # [0, 0, 0],
    # [0, 1, 0],
    # [0, 2, 0],
    # [1, 0, 0],
    # [1, 1, 0],
    # [1, 2, 0],
    # [2, 0, 0],
    # [2, 1, 0],
    # [2, 2, 0]
    # ]
    #
    # return tablero

    return np.matrix([[0]*3]*3)

def jugar(tablero):
    # Pide al computador que haga su jugada dado un tablero
    formula = cargar_reglas(tablero)
    return calcular_resultado(formula)
