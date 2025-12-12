class Henkilo:
    def __init__(self):
        self._nimi = 'tuntematon'

    # Getter for 'nimi'
    @property
    def nimi(self):
        return self._nimi

    # Setter for 'nimi'
    @nimi.setter
    def nimi(self, uusi_nimi):
        if isinstance(uusi_nimi, str) and uusi_nimi != '':
            self._nimi = uusi_nimi
        else:
            raise ValueError("Nimen täytyy olla merkkijono")

henkilo = Henkilo()
print(henkilo.nimi) # Tuntematon
henkilo.nimi = ""
print(henkilo.nimi) # Maija