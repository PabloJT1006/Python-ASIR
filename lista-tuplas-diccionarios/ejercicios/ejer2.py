#2. Cambiar el valor de una posición en una lista, a diferencia de esto en la tupla no se puede realizar ya que no 
#sabemos en qué posición están los datos, además teóricamente no se pueden añadir datos en las tuplas ya que son 
#estáticas.
meses=["enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses2={"1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}

meses[0]="enerazo"
print (meses)

meses2["2"]="febrerazo"
print(meses2["2"])