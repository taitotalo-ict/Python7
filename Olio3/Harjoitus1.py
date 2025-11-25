from typing import Self
import math

class Vector:
    def __init__(self, x: int|float, y:int|float):
        self.x = x
        self.y = y
    
    def __eq__(self, other: 'Vector') -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)
    
    # def __ne__(self, other: 'Vector') -> bool:
    #     if not isinstance(other, Vector):
    #         return NotImplemented
    #     return (self.x != other.x) or (self.y != other.y)
    
    def __ne__(self, other: 'Vector') -> bool:
        return not self.__eq__(other)

    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    # def __sub__(self, other: 'Vector') -> 'Vector':
    #     if not isinstance(other, Vector):
    #         return NotImplemented
    #     return Vector(self.x - other.x, self.y - other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return self + (-other)        

    def __neg__(self) -> 'Vector':
        return Vector(-self.x, -self.y)
    
    def __mul__(self, n: int|float) -> 'Vector':
        # if not isinstance(n, int) and not isinstance(n, float):
        if not isinstance(n, (int, float)):
            return NotImplemented
        return Vector(self.x * n, self.y * n)

    def __rmul__(self, n: int|float) -> 'Vector':
        return self.__mul__(n)
    
    @property
    def length(self) -> float:
        # return math.sqrt(self.x**2 + self.y**2)
        return (self.x**2 + self.y**2) ** (1/2)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(3, 2)
print(v1 == v2) # False
print(v1 != v2) # True
print(v1 + v2) # Vector(5, 5)
print(v2 + v1) # Vector(5, 5)
print(v1 - v2) # Vector(-1, 1)
print(v2 - v1) # Vector(1, -1)
print(-v1) # Vector(-2, -3)
print(-v2) # Vector(-3, -2)
print(v1.length) # 3.605551275463989
print(v2.length) # 3.605551275463989
print(v1 * 3) # Vector(6, 9)
print(3 * v1) # Vector(6, 9)
print(v2 * 5.5) # Vector(16.5, 11.0)
print(5.5 * v2) # Vector(16.5, 11.0)