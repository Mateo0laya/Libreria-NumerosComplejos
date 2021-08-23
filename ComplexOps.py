'''Libreria de operaciones con numeros complejos
    Mateo Olaya Garzon
    Agosto 2021 '''

import math

def suma(a, b):
    '''Funcion que suma dos numeros complejos
        (list, list) -> list '''
    real = a[0]+b[0]                        #Suma la parte real del numero complejo
    imag = a[1]+b[1]                        #Suma la parte imaginaria del numero complejo
    return (real, imag)

def producto(a, b):
    '''Funcion que multiplica dos numeros complejos
        (list, list) -> list '''
    real = ((a[0]*b[0])-(a[1]*b[1]))        #Calcula la parte real del producto de acuerdo con la formula conocida
    imag = ((a[0]*b[1])+(a[1]*b[0]))        #Calcula la parte imaginaria del producto de acuerdo con la formula conocida
    return (real, imag)

def resta(a, b):
    '''Funcion que resta dos numeros complejos
        (list, list) -> list '''
    real = a[0]-b[0]                        #Resta la parte real del numero complejo
    imag = a[1]-b[1]                        #Resta la parte imaginaria del numero complejo
    return (real, imag)

def division(a, b):
    '''Funcion que divide dos numeros complejos
        (list, list) -> list '''
    denom = (b[0])**2+(b[1])**2             #Calcula el denominador necesario para realizar la division
    numr = ((a[0]*b[0])+(a[1]*b[1]))        #Calcula el numerador necesario para realizar la division de la parte real
    numi = ((a[1]*b[0])-(a[0]*b[1]))        #Calcula el numerador necesario para realizar la division de la parte real
    real = (numr/denom)                     #Calcula la parte real de la division de acuerdo con la formula conocida
    imag = (numi/denom)                     #Calcula la parte imaginaria de la division de acuerdo con la formula conocida
    return (real, imag)

def modulo(a):
    '''Funcion que calcula el conjugado de un numero complejo
        list -> float '''
    rad = a[0]**2+a[1]**2                   #Calcula el radicando necesario para calcular el modulo
    mod = pow(rad, 0.5)                     #Calcula el modulo de acuerdo con la formula conocida
    return (mod)

def conjugado(a):
    '''Funcion que calcula el conjugado de un numero complejo
        list -> list '''
    x = (a[1])*(-1)                         #Calcula la parte imaginaria del conjugado
    b = (a[0], x)
    return (b)

def conversionac(a):
    '''Funcion que convierte un numero imaginario de forma polar a forma cartesiana
        list -> list '''
    real = a[0]*(math.cos((a[1]*math.pi)/180))            #Calcula la parte real del numero complejo en su forma cartesiana o rectangular
    imag = a[0]*(math.sin((a[1]*math.pi)/180))            #calcula la parte imaginaria del numero complejo en su forma cartesiana o rectangular
    return (real, imag)

def conversionap(a):
    '''Funcion que convierte un numero imaginario de forma cartesiana a forma polar
        list -> list '''
    mod = modulo(a)                         #Calcula el modulo del numero complejo 
    ang = fase(a)                           #Calcula la fase del numero complejo
    return (mod, ang)

def fase(a):
    '''Funcion que calcula la fase de un numero complejo
        list -> float '''
    ang = math.atan(a[1]/a[0])              #Calcula la fase del numero complejo
    ang = (ang*180)/math.pi
    return (ang)

def main():
    print(fase((4,3)))
main()