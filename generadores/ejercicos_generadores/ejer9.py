#9.Crear un array y dividirlo en 2 nuevos, uno con las posiciones pares y otro con las 
#impares
from ejer1 import(diez_random)
lista1=diez_random()
lista_par=[]
lista_impar=[]

for i in range(0,len(lista1)):
    if (i%2==0):
        lista_par.append(lista1[i])

for i in range(0,len(lista1)):
    if (i%2!=0):
        lista_impar.append(lista1[i])


print(lista1)
print("---------LISTA DE PARES-----------")
print(lista_par)
print("---------LISTA DE IMPARES-----------")
print(lista_impar)

