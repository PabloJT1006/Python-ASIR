#15.- Introducir una cadena y decir si es palíndromo
def invertir_cadena(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

caracteres=str(input("Introduce una cadena para comprobar si es palindroma o no: "))

if (invertir_cadena(caracteres)==caracteres):
    print("La cadena es palindroma")
else:
    print("La cadena no es palindroma")
