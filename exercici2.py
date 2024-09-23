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
            if isinstance(notas, (int, float)) and  notas >= 0 and notas <= 10:
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
            
            return sum(
                [nota for nota in self.notas.values() if isinstance(nota, (int, float))]
            ) / len([nota for nota in self.notas.values() if isinstance(nota, (int, float))])

    @classmethod
    def modificar_assignatures(cls, noves_assignatures):
        #Mètode de classe per modificar la llista d'assignatures
        cls.a = noves_assignatures
        print(f"La llista d'assignatures s'ha actualitzat a: {cls.a}")        
        
        
    def add_nota_np(self,assignatura):
        
        if assignatura not in self.a:
            print("Aquesta assignatura no existeix")
                   
        else:
            self.notas[assignatura] = "NP"

        



