import numpy as np
import copy

class triqui:

    def estado_inicial(self):
        return np.matrix([[0]*3]*3)

    def pintar_estado(self, estado):
        # Dibuja el tablero correspondiente al estado
        # Input: estado, que es una 3-lista de 3-listas
        fig, axes = plt.subplots()

        # Dibujo el tablero
        step = 1./3
        offset = 0.001
        tangulos = []

        # Borde del tablero
        tangulos.append(patches.Rectangle((0,0),0.998,0.998,\
                                          facecolor='cornsilk',\
                                         edgecolor='black',\
                                         linewidth=2))

        # Creo las líneas del tablero
        for j in range(3):
            locacion = j * step
            # Crea linea horizontal en el rectangulo
            tangulos.append(patches.Rectangle(*[(0, locacion), 1, 0.008],\
                    facecolor='black'))
            # Crea linea vertical en el rectangulo
            tangulos.append(patches.Rectangle(*[(locacion, 0), 0.008, 1],\
                    facecolor='black'))

        for t in tangulos:
            axes.add_patch(t)

        # Cargando imagen de O
        arr_img_O = plt.imread("./imagenes/O.png", format='png')
        image_O = OffsetImage(arr_img_O, zoom=0.14)
        image_O.image.axes = axes

        # Cargando imagen de X
        arr_img_X = plt.imread("./imagenes/X.png", format='png')
        image_X = OffsetImage(arr_img_X, zoom=0.14)
        image_X.image.axes = axes

        offsetX = 0.15
        offsetY = 0.15

        # ASUMO QUE LAS O SE REPRESENTAN CON 1 EN LA MATRIZ
        # Y QUE LAS X SE REPRESENTAN CON 2
        for i in range(3):
            for j in range(3):
                if estado[j, i] == 1:
                    # print("O en (" + str(i) + ", " + str(j) + ")")
                    Y = 2 - j
                    X = i
                    # print("(" + str(X) + ", " + str(Y) + ")")
                    ab = AnnotationBbox(
                        image_O,
                        [(X*step) + offsetX, (Y*step) + offsetY],
                        frameon=False)
                    axes.add_artist(ab)
                if estado[j, i] == 2:
                    # print("X en (" + str(i) + ", " + str(j) + ")")
                    Y = 2 - j
                    X = i
                    # print("(" + str(X) + ", " + str(Y) + ")")
                    ab = AnnotationBbox(
                        image_X,
                        [(X*step) + offsetX, (Y*step) + offsetY],
                        frameon=False)
                    axes.add_artist(ab)

        axes.axis('off')
        return axes

    def jugador(self, estado):
        num_Os = np.count_nonzero(estado==1)
        num_Xs = np.count_nonzero(estado==2)
        # print("Cantidad O:", num_Os, " Cantidad X:", num_Xs)
        if num_Os < num_Xs:
            return 1
        else:
            return 2

    def acciones_aplicables(self, estado):
        # Devuelve una lista de parejas que representan las casillas vacías
        indices = []
        if np.count_nonzero(estado==0)>0:
            for x in range(3):
                for y in range(3):
                    if estado[y, x] == 0:
                        indices.append((x, y))

        return indices

    def transicion(self, estado, indice):
        # Devuelve el tablero incluyendo una O o X en el indice,
        # dependiendo del jugador que tiene el turno
        # Input: estado, que es una np.matrix(3x3)
        #        indice, de la forma (x,y)
        # Output: estado, que es una np.matrix(3x3)

        s = copy.deepcopy(estado)
        x = indice[0]
        y = indice[1]
        s[y, x] = self.jugador(estado)

        return s

    def test_objetivo(self, estado):
        # Devuelve True/False dependiendo si el juego se acabó
        # Input: estado, que es una np.matrix(3x3)
        # Output: True/False
        # print("Determinando si no hay casillas vacías...")
        if np.count_nonzero(estado==0)==0:
            return True
        else:
            # print("Buscando triqui horizontal...")
            for y in range(3):
                num_Os = np.count_nonzero(estado[y,:]==1)
                num_Xs = np.count_nonzero(estado[y,:]==2)
                # print("Cantidad O:", num_Os, " Cantidad X:", num_Xs)
                if (num_Os==3) or (num_Xs==3):
                    return True

            # print("Buscando triqui vertical...")
            for x in range(3):
                num_Os = np.count_nonzero(estado[:,x]==1)
                num_Xs = np.count_nonzero(estado[:,x]==2)
                # print("Cantidad O:", num_Os, " Cantidad X:", num_Xs)
                if (num_Os==3) or (num_Xs==3):
                    return True

            # print("Buscando triqui diagonal...")
            if (estado[0,0]==1) and (estado[1,1]==1) and (estado[2,2]==1):
                return True
            elif (estado[0,0]==2) and (estado[1,1]==2) and (estado[2,2]==2):
                return True

            # print("Buscando triqui transversal...")
            if (estado[2,0]==1) and (estado[1,1]==1) and (estado[0,2]==1):
                return True
            elif (estado[2,0]==2) and (estado[1,1]==2) and (estado[0,2]==2):
                return True

        return None

    def utilidad(self, estado):
        # Devuelve la utilidad del estado donde termina el juego
        # Input: estado, que es una np.matrix(3x3)
        # Output: utilidad, que es un valor -1, 0, 1
        ob = self.test_objetivo(estado)
        if ob:
            if np.count_nonzero(estado==0)==0: # No hay casillas vacías: empate
                return 0
            elif self.jugador(estado)==1: # Jugaron las X y ganaron
                return 1
            else: # Jugaron las O y ganaron
                return -1
        else:
            return None

def min_value(juego, estado):
    if juego.test_objetivo(estado):
        return juego.utilidad(estado)
    else:
        acciones = juego.acciones_aplicables(estado)
#        valores = [
#            (a, max_value(juego, juego.transicion(estado, a)))\
#            for a in acciones
#        ]
#        print("Busca minimo sobre:", valores)
        return min([
            max_value(juego, juego.transicion(estado, a))\
            for a in acciones
        ])

def max_value(juego, estado):
    if juego.test_objetivo(estado):
        return juego.utilidad(estado)
    else:
        acciones = juego.acciones_aplicables(estado)
 #       valores = [
 #           (a, min_value(juego, juego.transicion(estado, a)))\
 #           for a in acciones
 #       ]
 #       print("Busca maximo sobre:", valores)
        return max([
            min_value(juego, juego.transicion(estado, a))\
            for a in acciones
        ])

def minimax_decision(juego, estado):

    # Retorna la acción optima en el estado, para el jugador que lleva el turno
    acciones = juego.acciones_aplicables(estado)

    # Determina qué jugador tiene el turno
    if juego.jugador(estado)==2: # Juegan las X (MAX)
        indice = np.argmax([
            min_value(juego, juego.transicion(estado, a))\
            for a in acciones
        ])
    else: # Juegan las O (MIN)
        indice = np.argmin([
            max_value(juego, juego.transicion(estado, a))\
            for a in acciones
        ])

    print("El computador juega en:", acciones[indice])
    print("Tablero resultado:\n", juego.transicion(estado, acciones[indice]))
    return acciones[indice]

def jugar_minmax(juego, estado):

    return juego.transicion(estado, minimax_decision(juego, estado))
