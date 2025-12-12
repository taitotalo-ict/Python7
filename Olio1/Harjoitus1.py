class Car:
    def __init__(self, brand, colour, speed):
        self.brand = brand
        self.colour = colour
        self.speed = speed

        self.info = f'{self.brand}\nColour: {colour}\nSpeed: {speed}'


audi = Car('Audi', 'Red', 200)
audi.speed = 150

print(audi.info)