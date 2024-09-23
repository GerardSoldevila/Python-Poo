from abc import ABC,abstractmethod

class Animal(ABC):

    def __init__(self, nom, color, manso):
        self.nom = nom
        self.color = color
        self.manso = manso

    @abstractmethod
    def parla(self):
        pass
       
    def descripcio(self):
        if self.manso:
            manso = True
        else:
            manso = False
            
        return f"Nom: {self.nom}, Color: {self.color}, és manso: {self.manso}"
                 
    def menja(self):
        print(f"{self.nom} està menjant")

    def dorm(self):
        print(f"{self.nom} està dormint")

class Gos(Animal):
    def parla(self):
        return"guau,guau"
    
class Gat(Animal):
    def parla(self):
        return "miau,miau"
class Cabra(Animal):
    def parla(self):
        return "beee,beeee"
class Vaca(Animal):
    def parla(self):
        return "muuuu,muuu"
    
    
class Granja:

    def __init__(self, nom):
        self.nom = nom
        self.llista = []
  
    def afegirAnimal(self, animal):
        self.llista.append(animal)
    
    def queParliTothom(self):
        print(f"{self.nom}")
        
        for animal in self.llista:
            print(f"{animal.nom} diu {animal.parla()}")
   
    def creaFitxer(self):
        f = open("exercici3_animals.txt","w")
        for animal in self.llista:
            f.write(f"{animal.nom},{animal.color},{animal.manso}")
            
        f.close()
    
    def afegirAnimalsGranja(self):
    
        f = open("exercici3_animals.txt","r")
        for linia in f:
            # separa la lineaa per comes
            # miro el primer element i faig un if
            # if [0] == "gos":
            pass
   
granja = Granja("Granja Vella")
   
     
gos = Gos("Rex", "blau", True)
gat = Gat("Funky", "negre", False)
cabra = Cabra("Xai", "groc", True)
vaca = Vaca("Joe", "gris", False)


granja.afegirAnimal(gos)
granja.afegirAnimal(gat)
granja.afegirAnimal(cabra)
granja.afegirAnimal(vaca)


granja.queParliTothom()
print(gos.descripcio())
granja.creaFitxer()

'''
print(gos.parla())
print(gos.descripcio())

print(gat.parla())
print(gat.descripcio())

print(cabra.parla())
print(cabra.descripcio())

print(vaca.parla())

'''



    
# herència multi nivell: afegir classe EsserViu amb mètode Respira
# herència múltiple: afegir classe Mascota amb mètode propietari