#Klasa = Szablon, Przepis
from symtable import Class

class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie, wiek, plec):
        # print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        self.wiek = wiek
        self.plec = plec
        # to jest to samo jakbym wpisala adam.imie = "Adam"
        #ewa.imie = "Ewa"
    def __add__(self, other):
        pass
    def przedstaw_sie(self):
        # == to porownanie. Czy plec jest M
        if self.plec == "M":
            print(f"Dzien dobry, mam na imie {self.imie} i jestem Mezczyzna. Mam {self.wiek} lat")

        elif self.plec == "K":
            print(f"Dzien dobry, mam na imie {self.imie} i jestem Kobieta. Mam {self.wiek} lat")

    def przedstaw(self,osoba):
        print(f"Oto {osoba.imie}")
    def podaj_wiek(self):
        print(f"Wiek {self.imie} wynosi {self.wiek}")

class Dziecko(Czlowiek):
    def __str__(self):
        if self.plec == "M":
            return f"Chlopiec {self.imie}"
        else:
            return f"Dziewczynka {self.imie}"

    def baw_sie(self):
        print("Ale zabawa, juhuu!!!!")
    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} i jestem ", end="")
        if self.plec=="M":
            print("chłopcem")
        else:
            print("dziewczynką")

# #jak mam podloge __ tzn ze juz jest zdefiniowane przez pythona tzw magia pythona
# print(__name__)

#postanie obiektu, Gotowanie z przepisu
adam = Czlowiek("Adam", 23, "M")
ewa = Czlowiek("Ewa", 24, "K")
kain = Dziecko("Kain", 1, "M")

# kain.baw_sie()
# kain.przedstaw_sie()

# print(type(adam))
# print(dir(adam)
# print(type(Czlowiek))
# print(adam.gatunek)
# print(ewa.gatunek)
# print(adam.imie)
# print(ewa.imie)
#adam.przedstaw_sie()
print(dir(Czlowiek))
print(dir(adam))
print(dir(kain))
print(Czlowiek)
print(str(kain))