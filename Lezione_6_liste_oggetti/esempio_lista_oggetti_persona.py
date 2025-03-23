#Un esempio di come creare dinamicamente una lista di oggetti "Persona"
#in Python utilizzando un ciclo for:
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return f"{self.nome}  {self.cognome}  {self.eta}"

# Creiamo una lista vuota per contenere gli oggetti Persona
persone = []

# Definiamo i dati delle persone
dati_persone = [
    ("Mario", "Rossi", 30),
    ("Laura", "Verdi", 25),
    ("Giovanni", "Bianchi", 40)
]

# Utilizziamo un ciclo for per creare gli oggetti Persona
#e aggiungerli alla lista
for tupla in dati_persone:
    print(tupla)
    nome = tupla[0]
    cognome = tupla[1]
    eta = tupla[2]
    persona = Persona(nome, cognome, eta)
    persone.append(persona)

# Stampiamo la lista di persone
for persona in persone:
    print(persona)
