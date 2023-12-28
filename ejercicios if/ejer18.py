#18. Calcula el cuadrado de todos los números comprendidos entre dos números introducidos 
# por teclado
inicio=int(input("Introduce el inicio de la serie de numeros: "))
fin=int(input("Introduce el fin de la serie de numeros: "))

for x in range(inicio,fin+1):
    print(x*x)    

