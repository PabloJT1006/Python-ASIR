#Generar números aleatorios entre 1 y 10 que el usuario tendrá que ir acertando. 
# En el momento que acierte cuatro se saldrá del programa, 
# y se indicará qué porcentaje se ha acertado y cuál se ha fallado.
import random

print("Adivina 4 numeros de una lista de numeros aleatorios")
aciertos=0
fallos=0

while (aciertos<4):
    aleatorio=random.randint(0,10)
    numero=int(input("Introduce un numero: "))

    if (aleatorio==numero):
        aciertos+=1
        print("Acertas te un numero")
    else:
        fallos+=1
        

suma=aciertos+fallos

print("¡¡¡¡¡¡¡¡¡¡PORFIN ACERTASTES LOS 4!!!!!!!!")
print("Porcentaje de fallos: ",fallos/(suma/100),"%")
print("Porcentaje de aciertos: ",aciertos/(suma/100)," %")





