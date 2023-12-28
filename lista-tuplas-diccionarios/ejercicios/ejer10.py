#10. Unir dos tablas, con esto lo que podemos hacer es unir dos tablas en una misma.

meses=["Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses1=("Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre")
meses2={"Principio","enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"}
meses3={"0":"Principio","1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}
meses4=["hola","adios"]
meses5=("hola","adios")
meses6={"12":"hola","13":"adios"}



meses.append(meses4)
print (meses)

#Al conjunto se se le podria añadir una tupla
meses2.add(meses5)
print(meses2)

diccionario={**meses3,**meses6}
print(diccionario)


