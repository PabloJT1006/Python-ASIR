def suma (numero1,numero2,numero3,numero4,numero5):
    return numero1+numero2+numero3+numero4+numero5




def cilindro (radio,Altura):
    return 3.1416 * radio * radio * Altura 


print("Escribe 5 numeros para sumarlos")

n1=float(input("Numero 1:"))
n2=float(input("Numero 2:"))
n3=float(input("Numero 3:"))
n4=float(input("Numero 4:"))
n5=float(input("Numero 5:"))

print("La suma seria de: ",suma(n1,n2,n3,n4,n5))


print("El resultado de tmp es de : ",suma(2,5,1,8,10))

print ("Introduce el radio y la altura de un cilindro para calcular su volumen")
alt=float(input("Altura: "))
rad=float(input("Radio: "))
print("El volumen del cilindro seria :",cilindro(rad,alt))


