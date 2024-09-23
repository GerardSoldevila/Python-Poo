import csv
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, nom, color, manso):
        self.nom = nom
        self.color = color
        self.manso = manso

    @abstractmethod
    def parla(self):
        pass

    def descripcio(self):
        return f"Nom: {self.nom}, Color: {self.color}, és manso: {'Sí' if self.manso else 'No'}"

# Millora 3.5
class AnimalComestible(Animal):
    def __init__(self, nom, color, manso, preu):
        super().__init__(nom, color, manso)
        self.preu = preu

    def descripcio(self):
        return f"{super().descripcio()}, Preu: {self.preu}€"

class Gos(Animal):
    def parla(self):
        return "guau, guau"

class Gat(Animal):
    def parla(self):
        return "miau, miau"

class Cabra(AnimalComestible):
    def parla(self):
        return "beee, beeee"

class Vaca(AnimalComestible):
    def parla(self):
        return "muuuu, muuu"

class Granja:

    def __init__(self, nom):
        self.nom = nom
        self.llista = []

    def afegir_animal(self, animal):
        self.llista.append(animal)

    def que_parli_tothom(self):
        print(f"En {self.nom} els animals diuen:")
        for animal in self.llista:
            print(f"{animal.nom} diu: {animal.parla()}")
      #MILLORA 2--> FER ARXIU TXT
    '''
    def crea_fitxer(self):
        with open("exercici3_animals.txt", "w") as f:
            for animal in self.llista:
                f.write(f"{animal.__class__.__name__.lower()},{animal.nom},{animal.color},{animal.manso}\n")

    def afegir_animals_granja(self):
        with open("exercici3_animals.txt", "r") as f:
            for linia in f:
                tipus, nom, color, manso = linia.strip().split(",")
                manso = manso.lower() == 'true'
                if tipus == "gos":
                    animal = Gos(nom, color, manso)
                elif tipus == "gat":
                    animal = Gat(nom, color, manso)
                elif tipus == "cabra":
                    animal = Cabra(nom, color, manso)
                elif tipus == "vaca":
                    animal = Vaca(nom, color, manso)
                self.afegir_animal(animal)
    
    '''
    # Millora 4: ARXIU .CSV
    def afegir_animals_granja(self, nom_fitxer="exercici3.csv"):
        with open(nom_fitxer, "r") as f:
            lector = csv.reader(f)
            for dades in lector:
                tipus, nom, color, manso, preu = dades[0], dades[1], dades[2], dades[3].lower() == 'true', dades[4]
                preu = float(preu) if preu != 'N/A' else None
                
                if tipus == "gos":
                    animal = Gos(nom, color, manso)
                elif tipus == "gat":
                    animal = Gat(nom, color, manso)
                elif tipus == "cabra":
                    animal = Cabra(nom, color, manso, preu)
                elif tipus == "vaca":
                    animal = Vaca(nom, color, manso, preu)

                self.afegir_animal(animal)



#Faig un exmeple d¡'us:
granja = Granja("Granja Vella")

gos = Gos("Rex", "blau", True)
gat = Gat("Funky", "negre", False)
cabra = Cabra("Xai", "groc", True, 120)  # Preu per a la cabra
vaca = Vaca("Joe", "gris", False, 200)    # Preu per a la vaca

granja.afegir_animal(gos)
granja.afegir_animal(gat)
granja.afegir_animal(cabra)
granja.afegir_animal(vaca)

granja.que_parli_tothom()
print(gos.descripcio())

 #Si vull afegir animals des del fitxer csv:
nova_granja = Granja("Nova Granja")
nova_granja.afegir_animals_granja("exercici3.csv")
nova_granja.que_parli_tothom()