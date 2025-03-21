#classi ed oggetti programmazione OOP
class Rettangolo:
    def __init__(self, dimensione1, dimensione2):
        self.__base = dimensione1
        self.__altezza = dimensione2
    
    def calcolaPerimetro(self):
        return self.__base *2 + self.__altezza * 2
    
    def calcolaArea(self):
        return self.__base * self.__altezza
    #interfaccia
    def setBase(self, valore):
        if valore < 0:
            print("il valore di base è negativo e non ammesso")
        else:
            self.__base = valore
            
    def getBase(self):
        return self.__base
    
#main
rettangolo1 = Rettangolo(3,7)
rettangolo1.setBase(3)
#print("la base del rettangolo risulta ", rettangolo1.__base)
print("Il perimetro del rettangolo risulta ",rettangolo1.calcolaPerimetro())
print("L'area del rettangolo risulta ", rettangolo1.calcolaArea())