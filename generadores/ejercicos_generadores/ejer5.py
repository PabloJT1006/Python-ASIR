#5.Sumar el contenido de las posiciones pares e impares y decir cual es mayor y cual 
#menor
from ejer1 import(milista)
sumapar=0;
sumaimpar=0;
for i in range(0,len(milista)):
    if (i%2==0):
        sumapar+=milista[i]

for i in range(0,len(milista)):
    if (i%2!=0):
        sumaimpar+=milista[i]

print("La suma de las posiciones pares, incliuida la 0 es de: ",sumapar," y la suma de las posiciones impares es de: ",sumaimpar)

if (sumapar>sumaimpar):
    print("La suma de los pares es mayor que los impares")
elif(sumaimpar==sumapar):
    print("Son iguales tanto la suma de los pares como de los impares")
else:
    print("La suma de los impares es mayor que la suma de los pares")