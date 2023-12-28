def ec_segundogrado(a,b,c):
    radicando=(b*b)-4*a*c
    if (radicando>=0):
        return print("La ecuacion tendria una solucion real")
    else:
        return print("La ecuacion tendria una solucion compleja")

def cuadrado(lado):
    return lado*lado

def triangulo(base,altura):
    return (base*altura)/2

def rectangulo(base,altura):
    return base*altura


def media(inicio,fin):
    suma=0
    contador=0
    for i in range(inicio,fin):
        suma+=i
        contador+=1
    return suma/contador

def potencias (numero1,numero2,numero3,numero4,exponente):
    return print("Potencia 1: ",numero1**exponente,", potencia 2: ",numero2**exponente,", potencia 3: ",numero3**exponente,", potencia 4: ",numero4**exponente)


def descuento(producto,porcentaje):
    decimal=porcentaje/100
    return producto*(1-decimal)