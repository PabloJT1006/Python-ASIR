#Indicando el máximo número deseado a generar, se irá pidiendo confirmación o 
# no de ir generando 3 números aleatorios, en el momento que se indique que se desea salir, 
# se tendrá que mostrar por pantalla la media de todos los números generados, junto con su máximo y su mínimo.

#se introduce el rango del aleatorio, se generan 3 
import random
#def generar(limit):
 #   numero1=random.randint(0,limit)
  #  numero2=random.randint(0,limit)
   # numero3=random.randint(0,limit)
    #return numero1,numero2,numero3

lista=[]
contador=0
suma=0
limite=int(input("Introduce el limite del rango de 3 numeros aleatorios, los cuales se gurdaran en una lista para luego calcular su media"))


while (True):
    numero1=random.randint(0,limite)
    numero2=random.randint(0,limite)
    numero3=random.randint(0,limite)
    lista.append(numero1)
    lista.append(numero2)
    lista.append(numero3)
    proseguir=str(input("¿Desea seguir generando?(s/n)"))
    if (proseguir!= "s"):
        print("Se procedera a calcular la media de los introducidos y su maximo y minimo")
        break
        
    
menor=lista[0]
mayor=lista[0]


for i in lista:
    contador+=1
    suma+=i
    if (i<menor):
        menor=i
    elif (i>mayor):
        mayor=i

print ("La media de los numeros seria: ",suma/contador," maximo: ",mayor," minimo: ",menor)

