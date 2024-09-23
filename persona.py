class Persona:

    def __init__(self, name, surname, age, favoritColor):
        self.name = name
        self.surname = surname
        self.age = age
        self.favoritColor = favoritColor
        self.malnoms = []

    #change the favotite color
    def set_favoritColor(self, favoritColor):
        self.favoritColor = favoritColor

    #append malnoms
    def add_malnom(self, malnom):
        afegit = True
        if malnom in self.malnoms:
            print(f"Ja té aquest malnom: {malnom}")
            afegit = False
        else:
            self.malnoms.append(malnom)
        return afegit

    #description
    def description(self):
        malnoms_str = ', '.join(self.malnoms) if self.malnoms else 'No té malnoms'
        return f"Nom: {self.name}, Cognoms: {self.surname}, Edat: {self.age}, Color preferit: {self.favoritColor}, Malnoms: {malnoms_str}"

p1 = Persona("Alfonso", "da Silva", 49, "verd")
print(p1.description())

p1.set_favoritColor("groc")
p1.add_malnom("El màquina")
p1.add_malnom("El màquina")
p1.add_malnom("Assamblador")

print(p1.description())


'''
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
        

a1 = Persona("Peter",20,"Groc","PereRepera")
a2 = Persona("Joan",59,"Blau","Capcigrany")
a3 = Persona("Anna",35,"Vermell","Petita")

a1.descripcio()
a2.descripcio()
a3.descripcio()
'''
