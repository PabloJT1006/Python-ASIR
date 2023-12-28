#17. Introducir números por teclado y contar los positivos y los negativos. 
# El programa termina cuando se introduce un cero y muestra los resultados.
contador1=0
contador2=0
bucle=True
while bucle:
    numero=int(input("Introduce un numero: "))
    if numero>0:
        contador1+=1
    elif numero<0:
        contador2+=1
    else:
        print("Adios")
        bucle=False

print ("Has introducido ",contador1," positivos y ",contador2," negativos")
