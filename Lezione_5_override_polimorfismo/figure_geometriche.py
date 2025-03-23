import math

class FiguraGeometrica:
    def __init__(self, nome):
        self.nome = nome

    def area(self):
        return "Area non definita per la figura generica."

    def perimetro(self):
        return "Perimetro non definito per la figura generica."

    def descrizione(self):
        return f"Figura geometrica: {self.nome}"

class Cerchio(FiguraGeometrica):
    def __init__(self, raggio):
        super().__init__("Cerchio")
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio**2

    def perimetro(self):
        return 2 * math.pi * self.raggio

    def descrizione(self):
      return f"{super().descrizione()}, raggio: {self.raggio}"

class Rettangolo(FiguraGeometrica):
    def __init__(self, base, altezza):
        super().__init__("Rettangolo")
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

    def descrizione(self):
      return f"{super().descrizione()}, base: {self.base}, altezza: {self.altezza}"

# Esempio di utilizzo
cerchio = Cerchio(5)
rettangolo = Rettangolo(4, 6)

print(cerchio.descrizione())
print(f"Area del cerchio: {cerchio.area()}")
print(f"Perimetro del cerchio: {cerchio.perimetro()}")

print(rettangolo.descrizione())
print(f"Area del rettangolo: {rettangolo.area()}")
print(f"Perimetro del rettangolo: {rettangolo.perimetro()}")
