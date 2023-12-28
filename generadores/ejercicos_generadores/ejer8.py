#8.Crear 3 arrays de 10 posiciones, 2 con números al azar y otro donde guardar los 
#resultados de las sumas de las posiciones
from ejer1 import(diez_random)

lista1=diez_random()
lista2=diez_random()
suma1=0
suma2=0
listasuma=[]
for i in lista1:
    suma1+=i

for j in lista2:
    suma2+=j

listasuma.append(suma1)
listasuma.append(suma2)


print ("La suma de todas las posiciones de la lista uno y la dos es: ",listasuma)
