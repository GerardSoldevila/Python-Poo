class Persona:

    curs = 2024
    #alumnes= dict()
    #malnoms = list()

    def __init__(self, nom, edat, color_preferit):
        self.nom = nom
        self.edat = edat
        self.color = color_preferit
        self.malnom = []
    
    def descripcio(self):
        print(f"Nom: {self.nom}")
        print(f"Edat: {self.edat}")
        print(f"Color preferit: {self.color}")
        print(f"Malnoms: {self.malnom}")
        
    def changeColour(self,new_colour):
        self.color = new_colour
        
    def addMalnom(self,malnom):
        self.malnoms.append(malnom)
        

a1 = Persona("Peter","20","Groc","PereRepera")
a2 = Persona("Joan","59","Blau","Capcigrany")
a3 = Persona("Anna","35","Vermell","Petita")

a1.descripcio()
a2.descripcio()
a3.descripcio()