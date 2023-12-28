#.Introducir un número y decir si es capicúa
def invertido(numero):
        inv=0
        while(numero != 0):
                inv = inv * 10 + (numero % 10)
                numero //= 10
        return inv

def capicuo(numero):
        if (invertido(numero)==numero):
                return print("El numero es capicuo")
        
        else:
                return print("El numero no es capicuo")


n=float(input("Introduce un numero para comprobar si es capicuo o no: "))

print(capicuo(n))

