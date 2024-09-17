class Alumne:
    
    a = ["Mates","Fisica","Angles","Programacio"]
    
    def __init__(self,nom,edat):
        
        self.nom = nom
        self.edat = edat
        self.notas = dict()  #diccionari on guardare les notes d'aquest alumne
       
    def descripcio(self):
        print()
        
        
    def add_nota(self,assignatura,notas):
        if assignatura not in self.a:
            print("Aquesta assignatura no existeix")
                   
        else:
            if (assignatura in Alumne.a and notas >= 0 and notas <= 10):
                self.notas[assignatura] = notas
            elif (notas == "NP"):
                self.notas[assignatura] = notas
            else:
                return ("El valor de la nota no és correcta")
    
    def showNota(self):
        return f"""     
        {self.nom}
        {self.edat}
        {self.notas}
        """
    def average_nota(self):
        
        notmitjana = -1
        if len(self.notas) == 0:
            return " La mitjana és un 0"
        else:
            
            return sum(self.notas.values()) / len(self.notas)

            
    def add_nota_np(self,assignatura):
        
        if assignatura not in self.a:
            print("Aquesta assignatura no existeix")
                   
        else:
            self.notas[assignatura] = "NP"

        


        

a1 = Alumne("Geri","20")

a1.add_nota ("Mates", 7)
a1.add_nota ("Fisica", 12)  #ha de donar error per Patata,ho haig de controlar
a1.add_nota ("Angles", 3) #ha de donar error per 79,ho haig de controlar
a1.add_nota ("Programacio", 5)
a1.add_nota ("Fisica", 8)
print(Alumne.showNota(a1))
print(f"La mitjana de notes es: {Alumne.average_nota(a1)}")


a2 = Alumne("ricard","18")

a2.add_nota ("Mates", 9)
a2.add_nota ("Fisica", 23)  #ha de donar error per Patata,ho haig de controlar
a2.add_nota ("Angles", 6) #ha de donar error per 79,ho haig de controlar
a2.add_nota ("Programacio", 5)
a2.add_nota ("Fisica", 6)
print(Alumne.showNota(a2)) 
print(f"La mitjana de notes es: {Alumne.average_nota(a2)}")

a3 = Alumne("pere","19")

a3.add_nota ("Mates", 9)
a3.add_nota ("Fisica", 23)  #ha de donar error per Patata,ho haig de controlar
a3.add_nota ("Angles", 6) #ha de donar error per 79,ho haig de controlar
a3.add_nota ("Programacio", 5)
a3.add_nota ("Fisica", "NP")
print(Alumne.showNota(a3)) 
print(f"La mitjana de notes es: {Alumne.average_nota(a3)}")