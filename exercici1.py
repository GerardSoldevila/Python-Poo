from persona import Persona

def main():
    persones = []

    num_persones = int(input("Quantes persones vols afegir? "))

    for i in range(num_persones):
        print(f"\nIntrodueix les dades de la persona {i + 1}:")
        name = input("Nom: ")
        surname = input("Cognoms: ")
        age = int(input("Edat: "))
        favoritColor = input("Color preferit: ")

        # Crear persona
        persona = Persona(name, surname, age, favoritColor)
        persones.append(persona)

        # malnoms_input = input("Introdueix els malnoms separats per comes (deixa-ho buit si no vols afegir-ne cap): ")
        # if malnoms_input: 
        #     malnoms = [malnom.strip() for malnom in malnoms_input.split(',')]
        #     for malnom in malnoms:
        #         persona.afegir_malnom(malnom)      

    # Mostrar
    print("\nLlista de persones:")
    suma_edats = 0
    for persona in persones:
        print(persona.description())
        suma_edats += persona.age

    mitjana_edats = suma_edats / num_persones  
    print(f"La mitjana de les edats és: {mitjana_edats}")

    # Calcular la mitjana d'edat
    # suma_edats = sum([persona.edat for persona in persones])
    # mitjana_edat = suma_edats / len(persones)
    # print(f"\nMitjana d'edat: {mitjana_edat:.2f}")

if __name__ == "__main__":
    main()
'''
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

'''