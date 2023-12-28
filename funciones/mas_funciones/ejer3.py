from typing import final
from funciones import media
print("introduce el inicio y el final de un rango de numeros para calcular su media")

principio=int(input("Introduce el inicio: "))
final=int(input("Introduce el final: "))

print("La media seria de: ",media(principio,final))