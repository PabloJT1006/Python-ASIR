
import random


    

def cargar_datos():
    fich=open("datos.dat",'w')
        
    for i in range (100):
        a=random.randint(1,300)
        fich.write("%d\n"%(a))
    fich.close()
        
def par_impar():
    numeros=open("datos.dat",'r').readlines()
    numeros=list(map(lambda l: l.rstrip('\n'),numeros))
    par=open("fichero1.dat",'w')
    impar=open("ficero2.dat",'w')
    print(numeros)
    for i in numeros:
        i=int(i)
        if (i%2==0):
            par.write("%d\n"%(i))
        else:
            impar.write("%d\n"%(i))
   
    par.close()
    impar.close()




cargar=cargar_datos()

separar=par_impar()
