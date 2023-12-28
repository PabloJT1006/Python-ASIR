import math
n1=int(input("Introduce un numero para calcular su raiz cuadrada: "))
try:
    print (math.pow(n1,0.5))
except ValueError:
    print("No se puede realizar una raiz cuadrada de un mumero negativo")
    