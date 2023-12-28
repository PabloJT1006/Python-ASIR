while True:
    try:
        variable=input()
        break
    except EOFError:
        print("El valor introducido no es correcto")