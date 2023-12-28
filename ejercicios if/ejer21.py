#21. Determinar si un número introducido por teclado es primo.
numero=int(input("Introduce un numero: "))
primo=True
for x in range (2,numero):
    if numero%x==0:
        primo=False
    

if primo==True:
    print("El numero es primo")
else:
    print ("El numero no es primo")
    
