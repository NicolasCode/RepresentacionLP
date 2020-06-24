import funciones_logica as Fun

letras = []
numfilas = 3
numcolumnas = 3
numsignos = 3
numturnos = 2
filas=[0,1,2]
columnas =[0,1,2]
for fila in range(numfilas):
    for columna in range(numcolumnas):
        for signo in range(numsignos):
            for turno in range (numturnos):
                letras.append(Fun.P(fila,columna,signo,turno,numfilas,numcolumnas,numsignos,numturnos))

# Parte E: Evitar columna
inicial=True
E = ""
for c in columnas:
    for f in filas:
        inicial1 = True
        for a in filas:
            if a != f and inicial1:
                E += Fun.P(a,c,1,0,numfilas, numcolumnas, numsignos, numturnos)
                inicial1 = False
            if a != f:
                 E += Fun.P(a,c,1,0,numfilas, numcolumnas, numsignos, numturnos) + 'Y'
        if inicial:
            E += Fun.P(f,c,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>'
            inicial = False
        else:
            E += Fun.P(f,c,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>' + 'Y'

# Parte F: Evitar fila
inicial=True
F = ""
for f in filas:
    for c in columnas:
        inicial1 = True
        for a in columnas:
            if a != c and inicial1:
                F += Fun.P(f,a,1,0,numfilas, numcolumnas, numsignos, numturnos)
                inicial1 = False
            if a != c:
                 F += Fun.P(f,a,1,0,numfilas, numcolumnas, numsignos, numturnos) + 'Y'
        if inicial:
            F += Fun.P(f,c,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>'
            inicial = False
        else:
            F += Fun.P(f,c,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>' + 'Y'

#Parte G: Evitar columna principal
inicial=True
G = ""
for a in columnas:
    inicial1 = True
    for b in columnas:
        if a != b and inicial1:
            G += Fun.P(b,b,1,0,numfilas, numcolumnas, numsignos, numturnos)
        if a != c:
            G += Fun.P(b,b,1,0,numfilas, numcolumnas, numsignos, numturnos) + 'Y'
    if inicial:
        G += Fun.P(a,a,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>'
        inicial = False
    else:
        G += Fun.P(a,a,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>' + 'Y'

#Parte H: Evitar columna secundaria
inicial=True
H = ""
for a in columnas:
    inicial1 = True
    for b in columnas:
        if a != b and inicial1:
            H += Fun.P(b,2-b,1,0,numfilas, numcolumnas, numsignos, numturnos)
        if a != c:
            H += Fun.P(b,2-b,1,0,numfilas, numcolumnas, numsignos, numturnos) + 'Y'
    if inicial:
        H += Fun.P(a,2-a,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>'
        inicial = False
    else:
        H += Fun.P(a,a,2,1,numfilas, numcolumnas, numsignos, numturnos) + '>' + 'Y'



# Regla completa y solucion
regla_ganar = E + F + 'Y' + G + 'Y' + H + 'Y'
arbol = Fun.String2Tree(regla_ganar,letras)
tseitin = Fun.TseitinJL(arbol, letras)
clausal = Fun.forma_clausal(tseitin)
interpretacion = Fun.DPLLResultado(clausal, letras)
print(interpretacion)
