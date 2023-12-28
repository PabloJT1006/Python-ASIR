
def divide(n1,n2):
    try:
        return n1/n2

    except ZeroDivisionError:
        print("No se puede dividir entre 0")

while True:
    try:
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        break
    except ValueError:
        print("Los valores introducidos no son correctos")
        


print(divide(numero1,numero2))

