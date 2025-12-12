class Point:
    def __init__(self, param1, param2=None) -> None:
        if param2 is None:
            if isinstance(param1, tuple):
                self.x = param1[0]
                self.y = param1[1]
                return
        elif isinstance(param1, (int, float)) and isinstance(param2, (int, float)):
            self.x = param1
            self.y = param2
            return
        
        raise TypeError('Incorrect param types')

    @classmethod
    def from_tuple(cls, param):
        return Point(param[0], param[1])



p1 = Point(4, 5) # Kaksi parametria: int 4 ja int 5
print(p1.x) # 4
print(p1.y) # 5
p2 = Point((7, 8)) # Yksi parametri: tuple (7, 8)
p2 = Point.from_tuple((7, 8))
print(p2.x) # 7
print(p2.y) # 8
