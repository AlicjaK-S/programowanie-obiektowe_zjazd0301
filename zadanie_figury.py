# Napisz klasę FiguraGeometryczna, która będzie zawierała
# metody:
# policz_pole()
# policz_obwód()

# Napisz klasy Prostokąt, Kwadrat, Koło i Trojkat
# oraz zaimplementuj metody z interfejsu FiguraGeometryczna

# Stwórz instancje tych klas i sprawdź ich działanie

class FiguraGeometryczna:

    def policz_pole(self):
        pass
    def policz_obwod(self):
        pass

class Prostokat(FiguraGeometryczna):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def policz_pole(self):
        return self.a * self.b

    def policz_obwod(self):
        return 2 * (self.a + self.b)
    pass
class Kwadrat(FiguraGeometryczna):
    def __init__(self, a):
        self.a = a

    def policz_pole(self):
        return self.a * self.a

    def policz_obwod(self):
        return 4 * (self.a)
    pass

class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r

    def policz_pole(self):
        return 3.14 * (self.r) * (self.r)

    def policz_obwod(self):
        return 2 * 3.14 * (self.r)

pass
class Trojkat(FiguraGeometryczna):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def policz_pole(self):
        return self.a * self.h/2

    def policz_obwod(self):
        return self.a + self.b + self.c + self.h

prostokat = Prostokat (4,6)

kwadrat = Kwadrat (3)

kolo = Kolo (5)

trojkat = Trojkat (3,5,2,2)

print(prostokat.policz_pole())
print(prostokat.policz_obwod())
print(kwadrat.policz_obwod())
print(kwadrat.policz_pole())
print(trojkat.policz_pole())
print(trojkat.policz_obwod())
print(kolo.policz_pole())
print(kolo.policz_obwod())
