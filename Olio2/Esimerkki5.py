class Numero:
    def __init__(self, arvo):
        self.arvo = arvo

    def __add__(self, toinen):
        if isinstance(toinen, Numero):
            return Numero(self.arvo + toinen.arvo)
        elif isinstance(toinen, int):
            return Numero(self.arvo + toinen)
        else:
            return NotImplemented
    
    def __radd__(self, toinen):
        return self.__add__(toinen)
    
    def __sub__(self, toinen):
        return Numero(self.arvo - toinen.arvo)
    
    def __mul__(self, toinen):
        return Numero(self.arvo * toinen.arvo)
    
    def __truediv__(self, toinen):
        return Numero(self.arvo / toinen.arvo)
    
    def __str__(self):
        return str(f'<Numero: {self.arvo}>')
    
    def __repr__(self) -> str:
        return f'Numero({self.arvo})'


num1 = Numero(10)
num2 = Numero(5)
print(num1 + num2) # 15
print(num1 - num2) # 5
print(num1 * num2) # 50
print(num1 / num2) # 2.0
