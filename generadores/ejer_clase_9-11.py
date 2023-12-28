def generaPares(limite):#limite es el número de pares
    num = 1
    milista = []
    while num < limite:
        #agregamos pares a la lista
        milista.append(num * 2)
        num = num + 1
    return milista # nos devuelve la lista completa

print(generaPares(10)) # llamada desde el programa pincipa


# yield construye un objeto iterable
# no trabajamos con listas
def generaPares(limite):
    num = 1
    while num < limite:
        yield(num * 2)
        num = num + 1
devuelvepar = generaPares(10) # devuelve el objeto 


#iterable
for i in devuelvepar:
    print(i)
# devuelve los 9 primeros pares