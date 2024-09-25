from final import Biblioteca, LLibre, Fitxer 


llibre1 = LLibre("99348977", "El mecanoscrit del 2n origen", "Manuel de Pedrolo", 340, False)
llibre2 = LLibre("78668734", "La Biblia", "San Pedro", 500, True)


# mostro el llibre1 i 2 per pantalla
llibre1.descripcio()
llibre2.descripcio()

biblioteca = Biblioteca("Armand Cardona", "Carrer Major 10")
biblioteca.add_llibre(llibre1)
biblioteca.add_llibre(llibre2)


# mostra el cataleg per pantalla, dos llibres
biblioteca.mostra_cataleg()


# Prova CSV
csv_file = FitxerCSV("./biblio.csv")
biblioteca.write_to_fitxer(csv_file)


nova_biblioteca1 = Biblioteca("Prova", "Sense adreça")
nova_biblioteca1.read_from_fitxer(csv_file)


# Prova JSON
json_file = FitxerJSON("./biblio.json")
biblioteca.write_to_fitxer(json_file)


nova_biblioteca2 = Biblioteca("Prova", "Sense adreça")
nova_biblioteca2.read_from_fitxer(json_file)


# Prova XML... igual


























'''
LLIBRE:


TO_DICT....   com alfons ho visulaitza a l hora d'aplicar-ho


 def to_dict(self);
 
 convertir cada llibre en un diccionari:
 
    d = {}
    d["titol"] = self.titol
    d["ISBN"]self.ISBN
    ...

    return d




BIBLIOTECA

creo una llista de llibres(diccionaris):

def write_file(self,fitxer):

1# recorro la llista de llibres i faig una llista de diccioanris fent servir el metode to_dict de LLIBRE

2# f.write_llista_dicts (llista de diccionaris) => guardo la lista de diccionarios en una lista
'''
