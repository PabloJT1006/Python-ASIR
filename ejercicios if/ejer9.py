#9. Calcula la suma de todos los pares comprendidos entre 1 y 1000 y muéstralo.

print("Se muestran la suma de todos los pares del 1 al 100")
suma=0
for x in range(1,100):
    if x%2==0:
        suma+=x
print(suma)