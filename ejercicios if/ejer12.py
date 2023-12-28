#12. Introducir número y exponente y calcular la potencia usando bucles.
print("Introduce un numero y su exponente para calcular la potencia")

numero=int(input("Introduce un numero: "))
exponente=int(input("Introduce un numero: "))
contador=1
potencia=1

while contador<=exponente:
    potencia=potencia*numero
    contador+=1

print("Esta seria la potencia de los numeros introducidos: ",potencia)
