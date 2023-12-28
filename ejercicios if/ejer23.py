#23. Escribe un programa que reciba un número por teclado y una frase. El programa deberá 
# mostrar esa frase por pantalla tantas veces como se le indique en el número
frase=input("Escriba una frase: ")
numero=int(input("Escriba el numero de veces que quieres que se repita la frase: "))

for x in range(1,numero+1):
    print(frase)