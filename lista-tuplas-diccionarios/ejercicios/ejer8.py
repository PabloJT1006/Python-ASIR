#8. Mostrar el contenido de la lista: 
#a. Un rango de posiciones 
#b. Mediante un if, que nos diga si está o no en el rango.
from typing import final


meses=["Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]

print("Solo se puede realizar con listas")

principio=int(input("Introduce el inicio del rango: "))
final=int(input("Introduce el final del rango: "))

if (principio>11 or final>11 or principio<0 or final<0):
    print("te pasaste de rango o no tiene sentido")
else:
    print(meses[principio:final])