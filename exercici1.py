from persona import Persona


def listPeople():
    
    people = list()
    num_people = int(input("Quantes persones vols afegir?: "))
    
    for i in range(num_people):
        nom = input("Nom: ")
        cognom = input("Cognom: ")
        edat = input ("Edat: ")
        color_preferit = input ("Color preferit: ")
        
        persona = Persona(nom, cognom, edat, color_preferit)
        people.append(persona)
        



# Nombre d'alumnes com a variable de classe
# Llista dels noms alumnes com a variable de classe
# Edat mitjana dels alumnes
