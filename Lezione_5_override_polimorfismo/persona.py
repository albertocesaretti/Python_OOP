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
    
class Lavoratore:
    def __init__(self,ruolo, stipendio, azienda):
        self.ruolo = ruolo
        self.stipendio = stipendio
        self.azienda = azienda
        
    def __str__(self):
        riga = "dati del lavoratore"
        riga += "Ricopre il ruolo di: "+ self.ruolo + "\n"
        riga += "Lo stipendio risulta : "+ self.stipendio + "\n"
        riga += "Lavora presso : "+ self.azienda + "\n"
        return riga    


class Studente_lavoratore(Persona, Lavoratore):
    def __init__(self,nome, cognome, annoNascita  , scuola, corso, anno):
        super().__init__(nome, cognome, annoNascita)
        self.scuola = scuola
        self.corso = corso
        self.anno = anno
        
    def __str__(self):
        riga = super().__str__()
        riga += "La scuola frequentata : "+ self.scuola + "\n"
        riga += "Il corso frequentato : "+ self.corso + "\n"
        riga += "Anno: "+ str(self.anno) + "\n"
        return riga
    


#main
persona1 = Persona("Mario", "Rossi", 2010)
print(persona1)

studente1 = Studente("Mario", "Rossi", 2010, "Liceo Einstein di Rimini","scienze applicate", 2025)
print(studente1)

medico1 = Medico("Luigi", "Neri", 1977, "Ospedale infermi di Rimini","ortopedico")
print(medico1)
