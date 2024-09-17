class Alumne:

    curs = 2056

    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat


a1 = Alumne("Alfonso", 49);
print(a1.nom)
print(Alumne.curs)
