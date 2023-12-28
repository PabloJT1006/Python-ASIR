#introucir el numero por una parte e introducir el exponente por otro

class ejer2():
    def __init__(self):
        self.__matriz=[]
        self.resultado=0
    def ecuacion(self,e):
        suma=0
        for i in range(e):
            suma+=pow(i+1,e)
            self.__matriz.append(pow(i+1,e))
        self.resultado=suma

    def mostrar_cargar(self):
        x=0
        fich=open("datos.dat","w")
        for i in self.__matriz:
            x+=1
            print ("Resultado",x,": ",i)
            fich.write("Serie %d: %d" %(x,i))
        fich.close()




obj1=ejer2()
obj1.ecuacion(4)
obj1.mostrar_cargar()
