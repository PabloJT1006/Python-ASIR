#5. Añadir contenido al final de la lista, en este caso si podremos hacerlo pero como ya dijimos anteriormente en las 
#tuplas no porque se inserta aleatoriamente nada más crearla y luego no se pueden insertar datos. 
#a. Insertar datos al final. 
#b. Insertar datos en una posición de memoria. 
meses=["enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"]
meses2={"enero","febrero","marzo","abril","mayo","junio","agosto","septiembre","octubre","noviembre","diciembre"}
meses3={"1":"enero","2":"febrero","3":"marzo","4":"abril","5":"mayo","6":"junio",
        "7":"agosto","8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}
#a
meses.append("diciembre_2")
#b
meses.insert(3,"hola_que_tal")
print(meses)

#a --> en los conjuntos lo añade de forma aleatoria
meses2.add("diciembre_2")
print(meses2)

#a 
meses3["12"]="hola"
print(meses3)
#b --> en diccionarios solo se podra añadir un valor con su indice alfinal, lo unico posible de hacer seria cambiar 
#el valor de algun indice anterior 
