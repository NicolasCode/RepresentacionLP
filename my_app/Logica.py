import json
from my_app.DPLL import *
from my_app.Codificacion import *
from my_app.FNC import *
import numpy as np

Nfilas = 3
Ncolumnas = 3
Nnumeros = 3 # Se asume que E es 0, O es 1, X es 2
Nturnos = 2

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label

def String2Tree(A):
    letrasProposicionales=[chr(x) for x in range(256, 400)]
    Conectivos = ['O','Y','>','=']
    Pila = []
    for c in A:
        # print("Procesando", c)
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")

    return Pila[-1]

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
    with open('my_app/reglas.json', 'r') as file:
        reglas = json.load(file)

    # rw = list(reglas.keys())
    rw = ['regla0', 'regla1', 'regla3', 'regla4', 'regla5', 'regla2']
    # rw = []
    # print("Trabajando con reglas", rw)

    formula = interpreta_tablero(tablero)

    for r in rw:
        formula += reglas[r]

    return formula

def calcular_resultado(formula):

    S, I = DPLL(formula, {})

    # print(S)
    # print(I)
    if S != 'Insatisfacible':
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
    else:
        resultado = []
    # print(resultado)

    return resultado

def tablero_inicial():

    return np.matrix([[0]*3]*3)

#Esta regla es verdadera si existe algún ganador
def regla_ganador():
    #Parte A: Ganador por fila
    inicial = True
    for f in range(Nfilas):
        for n in range(1,3):
            for t in range(Nturnos):
                if inicial:
                    A = P(f,(f+2)%3,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + P(f,(f+1)%3,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y' + P(f,f%3,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y'
                    inicial = False
                else:
                    A += P(f,(f+2)%3,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + P(f,(f+1)%3,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y' + P(f,f%3,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y' + 'O'

    #Parte B: Ganador por columna
    inicial = True
    for c in range(Ncolumnas):
        for n in range(1,3):
            for t in range(Nturnos):
                if inicial:
                    B = P((c+2)%3,c,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + P((c+1)%3,c,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y' + P(c%3,c,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y'
                    inicial = False
                else:
                    B += P((c+2)%3,c,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + P((c+1)%3,c,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y' + P(c%3,c,n,t,Nfilas,Ncolumnas, Nnumeros, Nturnos) + 'Y' + 'O'

    #Parte C: Ganador por diagonal principal
    inicial = True
    for n in range (1,3):
        for t in range (Nturnos):
            inicial1 = True
            for f in range(Nfilas):
                if inicial1:
                    clau = P(f,f,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos)
                    inicial1 = False
                else:
                    clau += P(f,f,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y'
            if inicial:
                C = clau
                inicial = False
            else:
                C += clau + 'O'

    #Parte D: Ganador por diagonal secundaria
    inicial = True
    for n in range (1,3):
        for t in range (Nturnos):
            if inicial:
                D = P(0,2,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos) + P(1,1,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y' + P(2,0,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y'
                inicial = False
            else:
                D += P(0,2,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos) + P(1,1,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y' + P(2,0,n,t,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y' + 'O'

    return A + B + 'O' + C + 'O' + D + 'O'

def tablero2interpretacion(tablero, turno):
    interps = {}
    for f in range(Nfilas):
        for c in range(Ncolumnas):
            interps[P(f,c,tablero[f,c],turno,Nfilas,Ncolumnas,Nnumeros,Nturnos)] = 1
            interps[P(f,c,tablero[f,c],1-turno,Nfilas,Ncolumnas,Nnumeros,Nturnos)] = 0
            for o in [a for a in range(Nnumeros) if a != tablero[f,c]]:
                #print(f,c,o,turno)
                interps[P(f,c,o,turno,Nfilas,Ncolumnas,Nnumeros,Nturnos)] = 0
                interps[P(f,c,o,1-turno,Nfilas,Ncolumnas,Nnumeros,Nturnos)] = 0
    return interps

def V_I(A, I):
    # Devuelve el valor de verdad de A bajo la interpretación I
    # Input: - A, una fórmula en formato tree
    #        - I, una interpretación en forma de un diccionario
    # Output: 0 o 1
    if A.right == None:
        return I[A.label]
    elif A.label == '-':
        return 1 - V_I(A.right, I)
    elif A.label in ['>', 'Y', 'O']:
        if A.label == 'Y':
            return V_I(A.left, I) * V_I(A.right, I)
        elif A.label == 'O':
            return max(V_I(A.left, I), V_I(A.right, I))
        elif A.label == '>':
            return max(1 - V_I(A.left, I), V_I(A.right, I))
    else:
        print("Creo que no conozco el conectivo " + str(A.label))

def hay_triqui(tablero, turno):
    interpretacion = tablero2interpretacion(tablero, turno)
    formula = String2Tree(regla_ganador())
    return V_I(formula,interpretacion)

def jugar_dpll(tablero):
    # Pide al computador que haga su jugada dado un tablero
    formula = cargar_reglas(tablero)
    return calcular_resultado(formula)

def buscar_jugada(tablero1,tablero2):
    for fila in range(3):
        for columna in range(3):
            if tablero1[fila,columna] != tablero2[fila,columna]:
                return str(fila) + str(columna)
    return ''
