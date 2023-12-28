#Generar 20 números aleatorios entre 1 y 1000. Se tendrá que mostrar los números pares junto con su media,
#  y los números impares junto con su media.

import random

lista=[]
lista_par=[]
lista_impar=[]
suma_par=0
suma_impar=0
contador_par=0
contador_impar=0

for i in range(0,20):
    numero=random.randint(1,20)
    lista.append(numero)

for i in lista:
    if (i%2==0):
        lista_par.append(i)
        suma_par+=i
        contador_par+=1
    else:
        lista_impar.append(i)
        suma_impar+=i
        contador_impar+=1


print("lista par: ",lista_par)
print("Media de pares: ",suma_par/contador_par)
print("--------------------------------------")
print("lista impar: ",lista_impar)
print("Media de impares: ",suma_impar/contador_impar)







