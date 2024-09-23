from exercici2 import Alumne


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



# Modificar la llista d'assignatures
Alumne.modificar_assignatures(["Biologia", "Quimica", "Història"])
a1.add_nota("Biologia", 9)  # Afegir una nota per una assignatura

