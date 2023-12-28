#Realizar un programa que vaya volteando todas las palabras que el usuario vaya introduciendo. 
# El programa finalizará cuando se introduzca tantas palabras como un número aleatorio generado entre 1 y 20.

import random
print ("Introduce un numero aleatorio de palabras y se le dara la vuelta a cada una de ellas")

limite=random.randint(1,20)
delreves=""

for i in range(0,limite):
    palabra=str(input("Introduce una palabra"))
    palabra+=" "
    for j in palabra:
        delreves=j+delreves
    print(delreves)
    


