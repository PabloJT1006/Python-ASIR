n1=int (input("Intrduce un numero: "))
n2=int (input("Introduce un numero: "))
try:
    print (n1/n2)

except ZeroDivisionError:
    print("No se puede dividir entre 0")