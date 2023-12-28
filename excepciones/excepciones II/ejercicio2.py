#no se ejecuta la excepcion ya que el error de sintaxis es mas importante que la excepcion
try:
    if True
        print ("hola")
except SyntaxError:
    print("Codigo mal escrito")