#4.Sacar solamente las posiciones impares del array
from ejer1 import(milista)
print("Se van a mostrar las posiciones impares de milista")

for i in range(0,len(milista)):
    if (i%2!=0):
        print (milista[i])