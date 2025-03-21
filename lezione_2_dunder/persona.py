#classi ed oggetti programmazione OOP
import datetime as d
class Persona:
    def __init__(self, nome, cognome, annoNascita):
        self.nome = nome
        self.cognome = cognome
        self.annoNascita = annoNascita
    
    def calcolaEta(self):
        annoOggi = d.datetime.now().year
        eta = annoOggi - self.annoNascita
        return eta
    
    def __str__(self):
        riga = "Dati della persona \n"
        riga += "Nome : " + self.nome + "\n"
        riga += "Cognome : " + self.cognome + "\n"
        riga += "Età : " + str(self.calcolaEta()) + "\n"
        return riga
    
    def __add__(self, altraPersona):
        #creo una nuva persona figlio
        nome_figlio = self.nome + ", " + altraPersona.nome
        cognome_figlio = self.cognome + ", " + altraPersona.cognome
        anno_figlio = d.datetime.now().year
        return Persona(nome_figlio, cognome_figlio, anno_figlio)    
#main
persona1 = Persona("Mario", "Rossi", 1997)
print(persona1)

"""
persona2 = Persona("Luisa", "Rossi", 2000)
figlio = persona1 + persona2
print("++++++++dati del babbo+++++++++")
print(persona1)
print("--------dati della mamma-------")
print(persona2)
print("********dati del figlio*******")
print(figlio)
"""