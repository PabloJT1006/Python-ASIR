#8. Calcular la suma de todos los múltiplos de cinco comprendidos entre 1 y 100.
print("Se muestran la suma de todos los multiplos de 5 del 1 al 100")
suma=0
for x in range(1,100):
    if x%5==0:
        suma=suma+x

print(suma)