#13. Introducir una cadena y meter las consonantes en un array y las vocales en otros, 
#después unirlas en un nuevo array que tenga primero las consonantes y luego las 
#vocales



frase=str(input("Intrduce una frase: "))
vocales="aeiouAEIOU"
consonantes="qwrtypñlkjhgfdszxcvbnmQWRTYPÑLKJHGFDSZXCVBNM"
vocal=[]
conson=[]


for i in frase:
    if (i in vocales):
        vocal.append(i)
    
    if (i in consonantes):
        conson.append(i)

union=vocal+conson
print("Todas las vocales junto con todas las consonantes",union)