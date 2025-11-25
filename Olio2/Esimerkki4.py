class Person:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä

    def __str__(self):
        return f"<{self.nimi}>"

    def __repr__(self):
        return f"Person('{self.nimi}', {self.ikä})"

    def __len__(self):
        return self.ikä

    def __getitem__(self, index):
        return self.nimi[index]
    
    def __setitem__(self, index, value):
        self.nimi = self.nimi[:index] + value + self.nimi[index+1:]

    def __eq__(self, other):
        return self.nimi == other.nimi
    
    def __ne__(self, other):
        # return self.nimi != other.nimi
        return not self.__eq__(other)
    

christian = Person('Christian', 50)