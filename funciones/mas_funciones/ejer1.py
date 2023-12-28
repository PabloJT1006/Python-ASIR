import funciones
from funciones import ec_segundogrado

print("Introduce los valores a,b y c de una ecuacion de segundo grado para indicar si el resultado es real o no")

n1=float(input("Introduce a: "))
n2=float(input("Introduce b: "))
n3=float(input("Introduce c: "))



print(ec_segundogrado(n1,n2,n3))