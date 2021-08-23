'''Libreria de operaciones de vectores con numeros complejos
    Mateo Olaya Garzon
    Agosto 2021 '''

from math import prod
import ComplexOps as COps

#   v=((1,2),(0,2))         w=((5,-1),(6,-5))

def suma_v(v,w):
    r = [(0, 0)] * len(v)
    for x in range(len(v)):
        r[x] = COps.suma((v[x]), w[x])
    return r

def inv_ad(v):
    r = [(0, 0)] * len(v)
    for x in range(len(v)):
        r[x] = COps.producto((-1,0), v[x])
    return r

def prod_esc(c, v):
    r = [(0, 0)] * len(v)
    for x in range(len(v)):
        r[x] = COps.producto((c,0), v[x])
    return r

#   v=(((2,3), (0,2), (1,5)), ((7,5), (1,-6), (-1,8)))             w=(((-9,8), (-3,1), (4,8)), ((-5,0), (3,2), (-7,6)))

def suma_m(v, w):
    m = len(v)
    n= len(v[0])
    r = [[(0,0)]*n]*m
    for x in range(m):
        for y in range(n):
            r[x][y] = COps.suma((v[x][y]), (w[x][y]))
    return r


def main():
    v=(((2,3), (0,2), (1,5)), ((7,5), (1,-6), (-1,8)))
    w=(((-9,8), (-3,1), (4,8)), ((-5,0), (3,2), (-7,6)))
    print(suma_m(v, w))
main()