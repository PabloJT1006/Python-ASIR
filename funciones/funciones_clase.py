def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

bucle=True
while (bucle):
    numero1=float(input("Introduce un numero: "))
    numero2=float(input("Introduce otro numero: "))

    print("1-Suma")
    print("2-Resta")
    print("3-Multiplicacion")
    print("4-Division")
    print("5-Salir")

    elecc=int(input("Elige alguna de las 4 cuentas ha realizar: "))

    if (elecc==1):
        print("La suma es:",suma(numero1,numero2))
    elif (elecc==2):
        print("La resta es:",resta(numero1,numero2))
    elif (elecc==3):
        print("La multiplicaion es:",multiplicacion(numero1,numero2))
    elif (elecc==4):
        print("La division es:",division(numero1,numero2))
    elif(elecc==5):
        print("Adios")
        bucle=False
    else:
        print("No has elegido ninguna opcion correcta")



