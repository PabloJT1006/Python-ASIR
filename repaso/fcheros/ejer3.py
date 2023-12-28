#cargar un ficehro con nombres y numeros de telefono(aleatorios)
#crear lista de noombres
#consultar el telefono de un cliente
#añair el telefono uno nuevo 
#y eliminar el telefono de uno 
#METER EL REALINES EN UN DICCIONARIO EN LA QUE EL INDDCE SERA EL NOMBRE Y LOS DATOS EL NUMERO ED TELEFONNO
import random


def cargar():
    fich=open("datos.dat","w")
    nombres=["RODOLOFO","ALBERTO","CARLOS","JAVIER","DANIEL","MARADONA"]
    for i in nombres:
        num=random.randint(66666,99999)
        #se podria coger los nombre aleatorios al crera otra variable entre 1 y el len de la lista y asi hacerlo pero me da pereza
        fich.write("%s, %d\n"%(i,num))



def cambiar_numero(nom,num):
    lineas=open("datos.dat","r").readlines()
    #esto convierte la el radlines en un diccionario separando los valores por lo que  esta dentro del split
    lineas=dict([tuple(line.split(','))for line in lineas])
    
    print (lineas)
    fich=open("datos.dat","w")
    if (nom in lineas):
       lineas[nom]=num
       print (lineas)
    else:
        print("no existe el nombre introucio")
        





ola=cargar()
nombre=str(input("Introduce el cliente que ha cambiao de numero: "))
numero=int(input("Introduce el numero: "))

klk=cambiar_numero(nombre,numero)
