#9. Copiar lista a otra lista: 
#a. Copiar de una lista a otra todos los datos. 


meses=["Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses1=("Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre")
meses2={"Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"}
meses3={"0":"Principio","1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}

#lista
copia=meses
print(copia)
print(meses)

#tupla
copia1=meses1
print(copia1)

#Conjunto
copia2=meses2
print(copia2)

#diccionario
copia3=meses3.copy()
print(copia3)
