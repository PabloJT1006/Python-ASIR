#15. Lee todos los números hasta introducir el cero y calcula el máximo y el mínimo.
contador=0
numero=1
lista_numero=[]
bucle=True
while bucle:
    numero=float(input("Introduzca un numero: "))
    if numero!=0:
        contador+=1
        lista_numero.append(numero)
    else:
        bucle=False

lista_numero.sort()

print("El minimo de esta lista de numeros seria: ",lista_numero[0]," y el maximo seria: ",lista_numero[contador-1])




