#.Dada una fórmula, guardar el resultado final y los dos resultados intermedios en 
#una matriz usando una librería externa
from funcion_ejer7 import EKIS
print("Introduce cuatro numeros para realizar una formula")
n1=float(input("Numero 1: "))
n2=float(input("Numero 2: "))
n3=float(input("Numero 3: "))
n4=float(input("Numero 4: "))

print("Solucion de la formula: ",EKIS(n1,n2,n3,n4))

