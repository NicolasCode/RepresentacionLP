import funciones_logica as Fun

letras = []
Nfilas = 3
Ncolumnas = 3
Nnumeros = 3
Nturnos = 2
filas=[0,1,2]
columnas =[0,1,2]


for fila in range(Nfilas):
    for columna in range(Ncolumnas):
        for signo in range(Nnumeros):
            for turno in range (Nturnos):
                letras.append(Fun.P(fila,columna,signo,turno,Nfilas,Ncolumnas,Nnumeros,Nturnos))

# Parte E: Evitar columna
inicial=True
E = ""
for c in columnas:
    for f in filas:
        inicial1 = True
        for a in filas:
            if a != f and inicial1:
                E += P(a,c,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos)
                inicial1 = False
            if a != f:
                 E += P(a,c,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y'
        if inicial:
            E += P(f,c,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>'
            inicial = False
        else:
            E += P(f,c,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>' + 'Y'

# Parte F: Evitar fila
inicial=True
F = ""
for f in filas:
    for c in columnas:
        inicial1 = True
        for a in columnas:
            if a != c and inicial1:
                F += Fun.P(f,a,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos)
                inicial1 = False
            if a != c:
                 F += Fun.P(f,a,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y'
        if inicial:
            F += Fun.P(f,c,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>'
            inicial = False
        else:
            F += Fun.P(f,c,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>' + 'Y'

#Parte G: Evitar columna principal
inicial=True
G = ""
for a in columnas:
    inicial1 = True
    for b in columnas:
        if a != b and inicial1:
            G += Fun.P(b,b,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos)
        if a != c:
            G += Fun.P(b,b,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y'
    if inicial:
        G += Fun.P(a,a,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>'
        inicial = False
    else:
        G += Fun.P(a,a,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>' + 'Y'

#Parte H: Evitar columna secundaria
inicial=True
H = ""
for a in columnas:
    inicial1 = True
    for b in columnas:
        if a != b and inicial1:
            H += Fun.P(b,2-b,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos)
        if a != c:
            H += Fun.P(b,2-b,1,0,Nfilas, Ncolumnas, Nnumeros, Nturnos) + 'Y'
    if inicial:
        H += Fun.P(a,2-a,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>'
        inicial = False
    else:
        H += Fun.P(a,a,2,1,Nfilas, Ncolumnas, Nnumeros, Nturnos) + '>' + 'Y'



# Regla completa y solucion
regla_ganar = E + F + 'Y' + G + 'Y' + H + 'Y'
arbol = Fun.String2Tree(regla_ganar,letras)
tseitin = Fun.TseitinJL(arbol, letras)
clausal = Fun.forma_clausal(tseitin)
interpretacion = Fun.DPLLResultado(clausal, letras)
print(interpretacion)
