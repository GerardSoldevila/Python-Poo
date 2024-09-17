class Animal:

    def __init__(self, nom):
        self.nom = nom

    def parleu(self):
        print(f"{self.nom} està ")
        
        
        
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

un_gat = Gat("Pel")
un_gat.parla()

un_cabra = Cabra("Xai")
un_cabra.parla()

un_vaca = Vaca("Joe")
un_vaca.parla()