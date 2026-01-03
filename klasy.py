#Klasa = Szablon, Przepis
class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie, wiek):
        # print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        self.wiek = wiek
        # to jest to samo jakbym wpisala adam.imie = "Adam"
        #ewa.imie = "Ewa"
    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imie {self.imie}")

    def przedstaw(self,osoba):
        print(f"Oto {osoba.imie}")
    def podaj_wiek(self):
        print(f"Wiek {self.imie} wynosi {self.wiek}")
# print(Czlowiek)
# print(type(Czlowiek))
# print(dir(Czlowiek))
# #jak mam podloge __ tzn ze juz jest zdefiniowane przez pythona tzw magia pythona
# print(__name__)

#postanie obiektu, Gotowanie z przepisu
adam = Czlowiek("Adam", 23)
ewa = Czlowiek("Ewa", 24)
# print(type(adam))
# print(dir(adam)

# print(adam.gatunek)
# print(ewa.gatunek)
# print(adam.imie)
# print(ewa.imie)

ewa.podaj_wiek()

