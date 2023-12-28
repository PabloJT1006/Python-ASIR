
print("INtroduce para sumar")


while True:
    try :
        n1=int(input("Introduce un elemento para sumar: "))
        n2=int(input("Introduce un elemento para sumar: "))
        break


    except ValueError :
        print ("Datos incorrectos")
        

print (n1+n2)
