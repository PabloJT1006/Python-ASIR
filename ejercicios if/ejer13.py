#13. Lee todos los números hasta introducir el cero y súmalos (prompt).
bucle=True
numero=1
suma=0
while bucle:
    numero=int(input("Introduce un numero: "))
    if numero!=0:
        suma+=numero
    else:
        bucle=False

print ("la suma es : ",suma)
