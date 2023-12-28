#10. Calcula la suma de todos los números comprendidos entre dos números introducidos por teclado.
print("Introduce dos numeros enteros para calcular la suma de todos los numeos comprendidos entre estos")

numero1=int(input("Introduce el primer numero: "))
numero2=int(input("Introduce el segundo numero: "))
suma=0

for x in range(numero1,numero2+1):
    suma+=x

print("Resultado de la suma: ",suma)