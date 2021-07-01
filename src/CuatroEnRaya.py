#NOTA: los comentarios son solamente para poder entender y guiarme con mas facilidad
#Son para referencia personal

#NOTA 2: Correr los test con pytest -s para que tome el inicio

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
    for x in range(1, 8):
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

def dibujarTablero(tablero):  
    for x in tablero:
        print("|", end='')    #for anidado que toma cada lista, y despues imprime cada item de cada lista
        for y in x:           #necesario hacerlo así para que no muestre los corchetes y las comas
            if y == 0:
                print(" ", end='')
            else:
                print(y, end ='')
            print(" ", end='')
        print("|", end='')
        print("")   #Los prints le dan la forma.
    print("----------------")

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

secuencia_texto = input("Ingrese la secuencia de fichas a soltar, \nindicando en orden el numero de columna en el que se soltarán \ny separando con comas: ")
secuencia = []
for items in secuencia_texto.split(','): #esto toma una secuencia por consola
    secuencia.append(int(items)) #separa la secuencia donde encuentra coma y la appendea a un array secuencia

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
