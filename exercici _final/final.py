import csv
from abc import ABC, abstractmethod

class Biblioteca(ABC):
    
    llibres = [] #això ha de ser una llista de diccionaris, on cada diccionari és un llibre.
    
    
    
    def __init__(self, titol, adreça, llista_llibres):
        
        self.titol = titol
        self.adreça = adreça
        self.llista_llibres = llista_llibres
           
    def mostra_cataleg(self):
        pass
    
    def add_llibre(self):
        pass
    
    def write_to_fitxer(self,nom_fitxer="fitxer.csv"):
        
        
        with open(nom_fitxer, "r") as f:
            lector = csv.reader(f)
            for dades in lector:
                titol, adreça, lli, preu = dades[0], dades[1], dades[2], dades[3].lower() == 'true', dades[4]
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

        pass    
        
    def read_from_fitxer(self):
        pass
        

class Llibre(Biblioteca):
    
    isbn_list = []
    llibres_prestats = []
    
    
    def _init_(self, isbn, titol,autor, nombre_pagines, en_prestec):
        
        self.isbn = isbn
        self.titol = titol
        self.autor = autor
        self.nombre_pagines = nombre_pagines
        self.en_prestec = en_prestec
    
    def descripcio(self):
        print("----------------------")
        print(f"ISBN:{self.isbn}")
        print(f"Títol:{self.titol}")
        print(f"Autor:{self.autor}")
        print(f"Nombre de pàgines:{self.nombre_pagines}")
        # if (self.en_prestec):
        #     print("En prestec:SI")
        # else:
        #     print("En prestec:NO")
        print(f"En prestec:{'SI' if self.en_prestec else 'NO'}")
        print("----------------------")
    
    
    def posa_en_prestec(self,isbn,llibres_prestats):
        
        afegit = False
        isbn_input = int(input( "Introdueix el ISBN de llibre per saber si està en prestec: "))
        
        #AQUI FALTA GFER UN BUCLE PER COMPARAR EL INPUT AMB UNA LLISTA DE ISBN QUE ESTAN EN PRESTEC...
        if isbn_input in self.en_prestec:
            print(f"El llibre {self.titol} de {self.autor} amb ISBN {self.isbn} ja està prestat")
            afegit = True
        else:
            self.en_prestec.append(isbn_input)
            print(f"El llibre {self.titol} de {self.autor} amb ISBN {self.isbn} es pot deixar en prestec")
            confirmacio = input(f"Vols agafar-lo en prestec? :(s/n) ")
            if confirmacio.lower() == "s":
                llibres_prestats.append[self.isbn]
                print("Acabes de demanar el llibre en prestec")
                
            elif confirmacio.lower() == "n":
                print("D'acord, no vols retirar el llibre")
            else:
                print("Entrada incorrecta")
                
        return afegit
        pass
    
    def retornat_de_prestec(self):
        retornat = False
        
        isbn_retornat = int(input("Escriu el ISBN del llibre que vols retornar: "))
        
        pass

    def to_dict(self):
        pass




class Fitxer:
    def __init__(self,path):
        
        self.path = path
        
        
    
    def  write_llista_llibres(self):
        pass
    
    
    def read_write_llista(self):
        pass    
        






