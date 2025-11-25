class Henkilö:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä
    
    def __eq__(self, toinen):
        return (self.nimi == toinen.nimi) and (self.ikä == toinen.ikä)


h1 = Henkilö('Matti', 23)
h2 = Henkilö('Matti', 23)
h3 = Henkilö('Matti', 24)
print(h1 == h2) # True
print(h1 == h3) # False