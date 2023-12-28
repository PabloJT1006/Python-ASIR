#14. Lee todos los números hasta introducir el cero y calcula la media (prompt).
bucle=True
numero=1
suma=0
contador=0
while bucle:
    numero=int(input("Introduce un numero: "))
    if numero!=0:
        contador+=1
        suma+=numero
    else:
        bucle=False



print ("la media es : ",suma/contador)
