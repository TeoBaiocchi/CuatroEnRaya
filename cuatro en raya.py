#NOTA: los comentarios son solamente para poder entender y guiarme con mas facilidad
#Son para referencia personal

def tableroVacio(): #esto es una lista con 6 listas de 7 elementos, que conforman el tablero
    return[ 
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0], #esta es la 1ra, aunque sea la 6ta de la lista de listas
    ]

def todasFilas(tablero):
    orden_filas = []
    for fila in tablero:
        orden_filas.append(fila)
    return orden_filas


def todasColumnas(tablero):
    orden_columnas = []
    for x in range(1, 7):
        orden_columnas.append(contenidoColumna(x, tablero))
    return orden_columnas

def contenidoColumna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda)
    return columna

def contenidoFila(nro_fila, tablero):
    filas = tablero[6 - nro_fila]
    return filas

def completarTableroEnOrden(secuencia, tablero):
    ficha = 1 #(turno)
    for columna in secuencia:
        soltarFichaEnTablero(ficha, columna, tablero)
        if ficha == 1:
            ficha = 2
        else:
            ficha = 1
    return tablero

def dibujarTablero(tablero): #esta funcion solamente va a imprimir el resultado, por lo tanto tengo
    for x in tablero: # que pasarle solamente el resultado xD
        print(x)
    
def soltarFichaEnTablero(ficha, columna, tablero): #esta funcion la va a llamar completar tablero en orden
    for fila in range(6, 0, -1): #fila esta siendo declarado, range va de 6 a 0 (no inclusive) bajando de a 1
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return tablero #el return tiene que estar incluido en el if para que tire una sola ficha por llamado a la funcion
            #porque de no ser así, pasan cosas y revisa 6 veces donde no tiene que hacerlo

def deteccionError(secuencia):
    for x in secuencia:
        if x > 7 or x < 1:
            print("Se ingreso un numero invalido en la secuencia.")
            return 2
    return 1

secuencia = [1, 2, 3, 1]
tablero = []
error = deteccionError(secuencia)
if error == 1:
    tablero = completarTableroEnOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)
    print()
    print("Contenido columna: ", contenidoColumna(1, tablero))
    print("Contenido fila: ", contenidoFila(1, tablero))
    print()
    orden_columnas = todasColumnas(tablero)
    print(orden_columnas)
    print("^Todas columnas^  ///  v Todas filas v")
    orden_filas = todasFilas(tablero)
    print(orden_filas)
#Esta ultima funcion primero define una secuencia
#detecta si es correcta, y despues dibuja el tablero
#para esto lo declara como variable vacia, la llena igualando a completarTableroEnOrden
#y finalmente lo imprime con otra funcion
