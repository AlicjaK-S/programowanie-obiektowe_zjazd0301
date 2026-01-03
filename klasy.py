#Klasa = Szablon, Przepis
class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        # to jest to samo jakbym wpisala adam.imie = "Adam"
        #ewa.imie = "Ewa"

# print(Czlowiek)
# print(type(Czlowiek))
# print(dir(Czlowiek))
# #jak mam podloge __ tzn ze juz jest zdefiniowane przez pythona tzw magia pythona
# print(__name__)

#postanie obiektu, Gotowanie z przepisu
adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
# print(type(adam))
# print(dir(adam)

print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)
