class moto():
    
    def __init__(self):
        self.__ruedas=2
        self.color=""
        self.__motor=49
        self.enmarcha=False



    def arrancar (self):
        self.enmarcha=True

    
    def set_color(self,color):
        self.color=color
        
    def estado(self):
        print ("La moto tiene: ",self.__ruedas," ruedas, con una cilindrada de ",self.__motor,"cc y de color ",self.color)
        if(self.enmarcha):
            print ("La moto está arrancada.")
        else:
            print ("La moto no está arrancada.")


print("############# moto UNO ###########")
primera=moto()
primera.color="fosforita"
primera.__ruedas=200
primera.arrancar()
primera.estado()

print("########### moto DOS ###########")
segunda=moto()
segunda.color="purpura"
segunda.__ruedas=4

segunda.estado()