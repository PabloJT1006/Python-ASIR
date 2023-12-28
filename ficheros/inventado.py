
import random

#FUNCION PARA CAMBIAR VALOR DE X LINEA
def cambia_lineas(fichero, linea, text):
    lines = open(fichero, 'r').readlines()
    lines[linea] = text
    out = open(fichero, 'w')
    out.writelines(lines)
    out.close()




fichero=str(input("Introduce el nonmbre de un fichero a introducir: "))
f=open(fichero,"w")

for x in range(5):
    frase=str(input("Introduce un frase: "))
    f.write("%s\n"%(frase))
    
f.close()

#MACHACAR LA LINEA 2 E INTRODUCIRLE EL DATO
f=open(fichero,"r")
borrar=str(input("Introduce el nuevo valor a escribir: "))
print("Se procedera a machacar el contenido de la segunda linea y cmabiarlo por lo introducido")
cambia_lineas(fichero, 1, borrar+"\n")
print(f.read())
f.close()

#MACHACAR LINEA ALEAOTRIA Y CAMBIARLO POR LO INTRODUCIDO
f=open(fichero,"r")
linea_ran=random.randint(0,5)
print("Se procedera a machacar un a linea aleaotria del fichero")
aniadir=str(input("Introduce un valor para introducirlo en la linea machacada: "))
cambia_lineas(fichero, linea_ran, aniadir+"\n")
print(f.read())
f.close()

#AÑADIR 3 FRASES MAS
f=open(fichero,"a")

for x in range(3):
    frase=str(input("Introduce un frase: "))
    f.write("%s\n"%(frase))
f.close()

f=open(fichero,"r")
print(f.read())
f.close()





