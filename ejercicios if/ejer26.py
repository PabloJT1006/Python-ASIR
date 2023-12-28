#26. Programa que pida dos números por teclado y calcule si el segundo es 
# múltiplo del primero 

numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce un numero para saber si este es multiplo del primero: "))

if numero1%numero2==0:
    print("El ",numero2," es multiplo de ",numero1)
else:
    print("El ",numero2," no es multiplo de ",numero1)
