from src.CuatroEnRaya import completarTableroEnOrden, contenidoColumna, contenidoFila, deteccionError, tableroVacio, todasColumnas, todasFilas

tableroPrueba = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 2, 0, 0],
        [2, 1, 0, 1, 1, 0, 0],
        [1, 2, 1, 2, 2, 0, 0],
    ]
secuenciaPrueba = [1, 2, 3, 4, 4, 5, 5, 5, 5, 5, 2, 1, 1, 1]

def test_tablero_vacio_tiene_6_filas():
    tablero = tableroVacio()

    assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
    tablero = tableroVacio()
    assert len(tablero[0]) == 7

def test_verificaciones_filaycolumna_andan_como_dios_manda():
    assert [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 2, 0, 0],
        [2, 1, 0, 1, 1, 0, 0],
        [1, 2, 1, 2, 2, 0, 0], ] == todasFilas(tableroPrueba)

    assert [[0, 0, 2, 1, 2, 1],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 2],
        [0, 2, 1, 2, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0] ] == todasColumnas(tableroPrueba)
    
    assert contenidoFila(1, tableroPrueba) == [1, 2, 1, 2, 2, 0, 0]
    assert contenidoFila(2, tableroPrueba) == [2, 1, 0, 1, 1, 0, 0]
    assert contenidoFila(3, tableroPrueba) == [1, 0, 0, 0, 2, 0, 0]
    assert contenidoFila(4, tableroPrueba) == [2, 0, 0, 0, 1, 0, 0]
    assert contenidoFila(5, tableroPrueba) == [0, 0, 0, 0, 2, 0, 0]
    assert contenidoFila(6, tableroPrueba) == [0, 0, 0, 0, 0, 0, 0]

    assert contenidoColumna(1, tableroPrueba) == [0, 0, 2, 1, 2, 1]
    assert contenidoColumna(2, tableroPrueba) == [0, 0, 0, 0, 1, 2]
    assert contenidoColumna(3, tableroPrueba) == [0, 0, 0, 0, 0, 1]
    assert contenidoColumna(4, tableroPrueba) == [0, 0, 0, 0, 1, 2]
    assert contenidoColumna(5, tableroPrueba) == [0, 2, 1, 2, 1, 2]
    assert contenidoColumna(6, tableroPrueba) == [0, 0, 0, 0, 0, 0]
    assert contenidoColumna(7, tableroPrueba) == [0, 0, 0, 0, 0, 0]

def test_completarTablero_anda_bien():
    assert tableroPrueba == completarTableroEnOrden(secuenciaPrueba, tableroVacio())

def test_deteccion_error_secuencia_invalida():
    assert deteccionError([1, 2, 3, 10]) == 2