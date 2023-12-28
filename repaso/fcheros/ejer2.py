from ast import Num
from inspect import CO_ASYNC_GENERATOR
from mailcap import findmatch


def multiplicar(n):
    fich=open("tabla.dat","w")
    result=0
    for i in range (10):
        result=(i+1)*n
        fich.write("%d * %d = %d\n"%(i+1,n,result))


def leer (m):
    lineas=open("tabla.dat","r").readlines()
    print (lineas[m])



num=int(input("Introuce un numero: "))
linea=int(input("Introduce la linea que quieres leer: "))

cargar=multiplicar(num)
mostrar=leer(linea-1)