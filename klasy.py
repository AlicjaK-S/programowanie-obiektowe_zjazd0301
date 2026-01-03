#Klasa = Szablon, Przepis
class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self):
        print("Niech powstanie Czlowiek")



# print(Czlowiek)
# print(type(Czlowiek))
# print(dir(Czlowiek))
#
# #jak mam podloge __ tzn ze juz jest zdefiniowane przez pythona tzw magia pythona
# print(__name__)


#postanie obiegtu, Gotowanie z przepisu
ala = Czlowiek()
# print(type(ala))
# print(dir(ala))

print(ala.gatunek)