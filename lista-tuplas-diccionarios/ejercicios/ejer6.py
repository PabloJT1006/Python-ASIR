#6. Ordenar las listas con sort. 
#a. Alfabéticamente: 
#b. Descendiente

meses=["enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses1=("enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre")
meses2={"enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"}
meses3={"1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}
#a
meses.sort()
print (meses)
#b
meses.sort(reverse=True)
print(meses)

#Solo se podrá hacer sort al arry ya que tanto para conjuntos como diccionarios no sirve




