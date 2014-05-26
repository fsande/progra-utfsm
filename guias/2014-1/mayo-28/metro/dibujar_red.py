from turtle import *
from time import sleep
from metro import coordenadas, estaciones, colores
from figuras import *


def es_estacion_terminal(est):
    for L in estaciones:
        linea = estaciones[L]
        if est == linea[0] or est == linea[-1]:
            return True
    return False

def es_estacion_combinacion(est):
    c = 0
    for L in estaciones:
        linea = estaciones[L]
        if est in linea:
            c += 1
    return c > 1

def misma_linea(est1, est2):
    for L in estaciones:
        linea = estaciones[L]
        if est1 in linea and est2 in linea:
            return True
    return False

def escalar(lat, lon):
    x = 2000 * (lon + 70.6)
    y = 2000 * (lat + 33.5)
    return (x, y)

def dibujar_lineas():
    shape('turtle')
    speed('slowest')
    width(5)

    for L in estaciones:
        linea = estaciones[L]
        print 'Linea', L
        up()
        color(colores[L])
        for est in linea:
            print 'Estacion', est
            #sleep(0.1)
            lat, lon = coordenadas[est]
            x, y = escalar(lat, lon)
            goto(x, y)
            down()

def dibujar_estaciones():
    up()
    color('black')
    speed('fastest')
    width(3)

    for est in coordenadas:
        lat, lon = coordenadas[est]
        x, y = escalar(lat, lon)
        if es_estacion_combinacion(est):
            dibujar_cuadrado(x, y, 8)
        elif es_estacion_terminal(est):
            dibujar_circunferencia(x, y, 7)
        else:
            dibujar_circunferencia(x, y, 5)

def escribir_nombres():
    up()
    speed('slowest')

    for L in ['2', '4']:
        color(colores[L])

        for est in estaciones[L]:
            lat, lon = coordenadas[est]
            x, y = escalar(lat, lon)
            goto(x + 10, y - 5)
            down()
            write(est)
            up()


if __name__ == '__main__':
    dibujar_lineas()
    dibujar_estaciones()
    escribir_nombres()
    color('black')
    up()
    home()
    raw_input()

