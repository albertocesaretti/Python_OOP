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
    def __init__(self, ruolo, stipendio, azienda):
        self.ruolo = ruolo
        self.stipendio = stipendio
        self.azienda = azienda
    
    def __str__(self):
        riga = "Dati del lavoratore \n"
        riga += "Ruolo : " + self.ruolo + "\n"
        riga += "Stipendio  : " + str(self.stipendio) + "\n"
        riga += "Azienda : " + self.azienda + "\n"
        return riga
    
class Studente_lavoratore(Persona,Lavoratore):
    def __init__(self, nome, cognome, annoNascita,ruolo, stipendio, azienda, codice_matricola,universita ):
        Persona.__init__(self, nome, cognome, annoNascita)
        Lavoratore.__init__(self, ruolo, stipendio, azienda)
        self.codice_matricola = codice_matricola
        self.universita = universita
    
    def __str__(self):
        print(Persona.__str__(self))
        print(Lavoratore.__str__(self)) 
        riga = "Dati dello studente \n"
        riga += "Codice matricola : " + str(self.codice_matricola) + "\n"
        riga += "Università  : " + self.universita + "\n"
        return riga    
#main
studente_lavotatore_1 =  Studente_lavoratore("Mario","Rossi", 1999,"Oculistica", 1600,"USL Romagna", 123456,"Università di Bologna" )   
print(studente_lavotatore_1)   

#studente_lavoratore_1 = Studente_lavoratore("Mario", "Rossi", 1967, "oculista", 1600, "USL Romagna",112334,"Bologna")
#print(studente_lavoratore_1)
