#pide numero y escribe la tabla de multiplicar de eso 



def multiplicar(n):
    fich=open("tabla.dat","w")
    result=0
    for i in range (10):
        result=(i+1)*n
        fich.write("%d * %d = %d\n"%(i+1,n,result))



num=int(input("Introduce un numero: "))
ola=multiplicar(num)

