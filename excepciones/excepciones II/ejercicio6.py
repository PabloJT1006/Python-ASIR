while True:
    try:
        variable=float(input())
        break
    except ValueError:
        print("no has escrito nada en la variable o los datos son incorrectos")