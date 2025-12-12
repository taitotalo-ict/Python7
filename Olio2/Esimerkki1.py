class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @staticmethod
    def hp_to_watts(hp: int|float):
        return hp * 745.699872
    

    def test(self):
        self.watts = Car.hp_to_watts(200)
# Kutsutaan staattista metodia
print(Car.hp_to_watts(200))

audi = Car('Audi', '2020')
print(audi.hp_to_watts(200))