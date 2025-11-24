class Example:
    level: int = 0
    def __init__(self, value):
        self.value = value
        self.level = Example.level
    
    @classmethod
    def update_level(cls, new_value):
        cls.level = new_value


A = Example('A')
B = Example('B')

print(A.level)  # 0
print(B.level)  # 0

Example.update_level(10)
print(Example.level) # 10

print(A.level)  # 10
print(B.level)  # 10
