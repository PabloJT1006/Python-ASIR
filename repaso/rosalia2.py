
while (True):
    try:
        inicio=int(input("Introuce un numero: "))
        fin=int(input("Introuce un numero: "))
        if (inicio>=fin):
            print("El inicio debe ser mas pequeño que el fin")
        else:
            break
    except  ValueError:
        print("Los valores introucidos no sonn correctos")

suma=0

for i in range(inicio,fin+1):
    print (i)
    suma+=i

print ("La suma de la serie de nuemeros seria: ",suma)