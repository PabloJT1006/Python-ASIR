#19. Escribe un programa que calcule la multiplicación de dos números introducidos por 
# teclado sin utilizar el operador * (usando sumas sucesivas)


numero1=int(input("Introduce el multiplicando: "))
numero2=int(input("Introduce el multiplicador: "))
resultado=0
for x in range(1,numero2+1):
    resultado+=numero1
    print(resultado)

print("Resultado: ",resultado)
