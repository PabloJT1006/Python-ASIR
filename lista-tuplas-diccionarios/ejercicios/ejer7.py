#7. Borrado de listas. 
#a. De un solo campo.  Borrar de la lista meses el campo “Principio” 
#b. Borrar el último elemento de una lista. 
#c. Borrar lista entera
#d. Vaciado de una lista.
meses=["Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses1=("Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre")
meses2={"Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"}
meses3={"0":"Principio","1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}
#a
print(meses)
meses.remove("Principio")
print(meses)
#b
meses.pop()
print(meses)
#c
meses.clear()

#La unica posibilidad de borrar algo en una tupla seria borrar la tupla entera
print (meses1)
del meses1


#a
print(meses2)
meses2.remove("Principio")
print(meses2)
#b
meses2.pop()
print(meses2)
#c
del meses2

#a
meses3.pop("0")
print(meses3)
#b
meses3.popitem()
print(meses3)
#d
del meses3




