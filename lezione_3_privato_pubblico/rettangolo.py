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
            print("base negativa non ammessa")
        else:
            self.__base = valore
    def getBase(self):
        return self.__base
    
#main
rettangolo1 = Rettangolo(3,7)  #incapsulamento
rettangolo1.setBase(2)
#rettangolo1.base = _2
#print(rettangolo1.__base)
print("la base del rettangolo risulta ", rettangolo1.getBase())
print("Il perimetro del rettangolo risulta ",rettangolo1.calcolaPerimetro())
print("L'area del rettangolo risulta ", rettangolo1.calcolaArea())