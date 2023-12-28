#12. Introducir una cadena y sacar el número de vocales y cuántas hay de cada una, el 
#número de consonantes, el número de palabras y la cadena entera en mayúsculas




frase=str(input("Intrduce una frase: "))
vocales="aeiouAEIOU"
consonantes="qwrtypñlkjhgfdszxcvbnmQWRTYPÑLKJHGFDSZXCVBNM"
contador_consonantes=0
contador_palabras=1
vocal=""
conson=""
a=0
e=0
i=0
o=0
u=0
#para sacar algo de una cadena
for i in frase:
    if (i==" "):
        contador_palabras+=1
    elif (i in vocales=="a" or vocales=="A"):
        a+=1
    elif (i in vocales=="e" or vocales=="E"):
        e+=1
    elif (i in vocales=="i" or vocales=="I"):
        i+=1
    elif (i in vocales=="o" or vocales=="O"):
        o+=1
    elif (i in vocales=="u" or vocales=="U"):
        u+=1

    elif (i in consonantes):
        contador_consonantes+=1


print("Numero de palabras introducidos: ",contador_palabras)
print("----------------------------------------------------")
print("Numero de vocales introducidos, a: ",a," e: ",e," i: ",i," o: ",o,"u: ",u)
print("----------------------------------------------------")
print("Numero de consonantes introducidos: ",contador_consonantes)
print("----------------------------------------------------")
print("Frase en mayusculas : ", frase.upper())



