from exercici1_main import Persona

def main():
    
    persones = []

    num_persones = int(input("Quantes persones vols afegir? "))

    for i in range(num_persones):
        print(f"\nIntrodueix les dades de la persona {i + 1}:")
        name = input("Nom: ")
        surname = input("Cognoms: ")
        age = int(input("Edat: "))
        favoritColor = input("Color preferit: ")

        # Crear la persona
        persona = Persona(name, surname, age, favoritColor)
        persones.append(persona)

        malnoms_input = input("Introdueix els malnoms separats per comes (deixa-ho buit si no vols afegir-ne cap): ")
        if malnoms_input:
            malnoms = [malnom.strip() for malnom in malnoms_input.split(',')]
            for malnom in malnoms:
                persona.add_malnom(malnom)

    # Mostrar la informació de les persones
    print("\nLlista de persones:")
    suma_edats = 0
    for persona in persones:
        print(persona.description())
        suma_edats += persona.age

    mitjana_edats = suma_edats / num_persones
    print(f"La mitjana de les edats és: {mitjana_edats}")
    #2 especifica que es volen mostrar dues xifres decimals.
    #f indica que és un número en coma flotant (float).      
  

if __name__ == "__main__":
    main()


