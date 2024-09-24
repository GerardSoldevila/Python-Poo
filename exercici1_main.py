class Persona:

    def __init__(self, name, surname, age, favoritColor):
        self.name = name
        self.surname = surname
        self.age = age
        self.favoritColor = favoritColor
        self.malnoms = []

    #change the favorite color
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


