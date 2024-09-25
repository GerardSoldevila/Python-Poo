import csv
from abc import ABC, abstractmethod

class Biblioteca: #HA DE SER UNA RELACIO d'agregacio entre llibre i biblioteca, no abstracta ni herencia
    
    #llibres = [] #això ha de ser una llista de diccionaris, on cada diccionari és un llibre.
    
    def __init__(self, nom, adreça):
        
        self.nom = nom
        self.adreça = adreça
        self.llista_llibres = []
           
    def mostra_cataleg(self):
       
        if self.llista_llibres:
            for llibre in self.llista_llibres:
                print(llibre.descripcio())
        else:
            print("no hi ha cap llibre")
        
    
    def add_llibre(self,llibre):
        self.llista_llibres.append(llibre)
      '''
       llibre = {}
       llibre[self.isbn] = {
           "ISBN":self.isbn,
           "Títol":self.titol,
           "Autor":self.autor,
           "Pàgines":self.nombre_pagines,
           "Prestat":self.en_prestec,
       }
       ''' 
        # 
        
    
    def write_to_fitxer(self,nom_fitxer="fitxer.csv"):
             
        with open(nom_fitxer, "r") as f:
            lector = csv.reader(f)
            for dades in lector:
                isbn, titol, autor = dades[0], dades[1], dades[2], 
                
                # llibre = 

                self.write_to_fitxer(llibre)

        pass    
        
    def read_from_fitxer(self):
        pass
        



class LLibre:
    
    isbn_list = []
    llibres_prestats = []
    
    
    def __init__(self, isbn, titol,autor, nombre_pagines, en_prestec):
        
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
        print(f"En prestec:{'SI' if self.en_prestec else 'NO'}")
        print("----------------------")
    
    
    def posa_en_prestec(self,isbn,llibres_prestats):
        
        afegit = False
        isbn_input = int(input( "Introdueix el ISBN de llibre per saber si està en prestec: "))
        
        #AQUI FALTA FER UN BUCLE PER COMPARAR EL INPUT AMB UNA LLISTA DE ISBN QUE ESTAN EN PRESTEC...
        if isbn_input in self.en_prestec:
            print(f"El llibre {self.titol} de {self.autor} amb ISBN {self.isbn} ja està prestat")
            afegit = True
        else:
            self.en_prestec.append(isbn_input)
            print(f"El llibre {self.titol} de {self.autor} amb ISBN {self.isbn} es pot deixar en prestec")
            confirmacio = input(f"Vols agafar-lo en prestec?:(s/n) ")
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
   
         
    def  write_llista_llibres(self,llista):
        pass
    
    
    def read_write_llista(self):
        pass    
        

class FitxerCSV(Fitxer):
         
    def  write_llista_llibres(self,llista):
        f=open("llibres.csv","w")
        for llibre in llista:
            f.write(f"ISBN: {llibre.isbn}, Titol: {llibre.titol}; Autor: {llibre.autor}, Nombre de pàgines: {llibre.nombre_pagines},Prestat: {llibre.en_prestec}")
    pass

class XMLFIle(Fitxer):
    pass

class JSONFile(Fitxer):
    pass





