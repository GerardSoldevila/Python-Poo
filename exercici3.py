class Animal:

    def __init__(self,nom,color,manso):
        self.nom = nom
        self.color = color
        self.manso = manso

    def parleu(self):
        print(f"{self.nom} està ")
        
    def descripcio(self):
        print(f"El nom de {self.nom} és :")
        print(f"El color de {self.color} és :")
        print(f"El caracter {self.manso} és :")
        
        
    def menja(self):
        print(f"{self.nom} està menjant")

    def dorm(self):
        print(f"{self.nom} està dormint")

class Gos(Animal):
    def parla(self):
        print("guau,guau")
    
class Gat(Animal):
    def parla(self):
        print("miau,miau")
class Cabra(Animal):
    def parla(self):
        print("beee,beeee")
class Vaca(Animal):
    def parla(self):
        print("muuuu,muuu")
    
  
un_gos = Gos("Rex")
un_gos.parla()
#un_gos.descripcio("rex","negre",True)

un_gat = Gat("Funky")
un_gat.parla()

un_cabra = Cabra("Xai")
un_cabra.parla()

un_vaca = Vaca("Joe")
un_vaca.parla()