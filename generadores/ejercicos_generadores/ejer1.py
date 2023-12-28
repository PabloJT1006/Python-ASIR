#1.Cargar 10 números naturales entre 0 y 1000 y sacarlos a pantalla
import random
def dieznaturales():
    num = 1
    while num <= 10:
        yield(random.randint(0,1000))
        num = num + 1

def diez_random():
    num = 1
    milista = []
    while num <= 10:
        #agregamos pares a la lista
        milista.append(random.randint(0,1000))
        num = num + 1
    return milista


#generar = dieznaturales()
#for i in generar:
#    print(i)
#print("-----------------------------------------")

milista=diez_random()
#print(milista)