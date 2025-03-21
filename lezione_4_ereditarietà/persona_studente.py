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

class Studente(Persona):
    def __init__(self, nome, cognome, annoNascita,    scuola, corso, anno):
        super().__init__(nome, cognome, annoNascita)
        self.scuola = scuola
        self.corso = corso
        self.anno = anno
    
    def __str__(self):
        riga = super().__str__()
        riga = "Dati dello studente \n"
        riga += "Scuola : " + self.scuola + "\n"
        riga += "Corso : " + self.corso + "\n"
        riga += "Anno : " + str(self.anno) + "\n"
        return riga   
        
#main
persona1 = Persona("Mario", "Rossi", 2010)
print(persona1)
studente1 = Studente("Mario", "Rossi", 2010, "Liceo Einstein","scienze applicate", 2025)
print(studente1)