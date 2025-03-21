#classi ed oggetti programmazione OOP
class Rettangolo:
    def __init__(self, dimensione1, dimensione2):
        self.base = dimensione1
        self.altezza = dimensione2
    
    def calcolaPerimetro(self):
        return self.base *2 + self.altezza * 2
    
    def calcolaArea(self):
        return self.base * self.altezza
    
#main
rettangolo1 = Rettangolo(3,7)
#rettangolo.base = 2
print("Il perimetro del rettangolo risulta ",rettangolo1.calcolaPerimetro())
print("L'area del rettangolo risulta ", rettangolo1.calcolaArea())