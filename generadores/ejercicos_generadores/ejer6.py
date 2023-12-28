#6.Indicar qué contenido es el mayor y cual el menor y decir la posicion que ocupa
from ejer1 import(milista)
menor=milista[0]
mayor=milista[0]
for i in milista:
    if (i<menor):
        menor=i

for j in milista:
    if (j>mayor):
        mayor=j

print("El numero mayor de la lista es: ",mayor," y el menor es: ",menor)