from functools import cache

class Stone:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_str(cls, value: str) -> 'Stone':
        return cls(int(value))

    @property
    def len_digits(self) -> int:
        return len(str(self.value))

    @property
    def upper_half(self) -> int:
        return int(str(self.value)[:self.len_digits // 2])
    
    @property
    def lower_half(self) -> int:
        return int(str(self.value)[self.len_digits // 2:])
    
    def change(self) -> tuple['Stone'] | tuple['Stone', 'Stone']:
        match self.value:
            case 0:
                return (Stone(1), )
            case _ if self.len_digits % 2:      # Pariton
                return (Stone(self.value * 2024), )
            case _:                             # Parillinen
                return (Stone(self.upper_half), Stone(self.lower_half))
    
    def __repr__(self) -> str:
        return f'Stone({self.value})'
    
    def __eq__(self, other: 'Stone') -> bool:
        return self.value == other.value
    
    def __hash__(self) -> int:
        return hash(self.value)

@cache
def blink(stone: Stone, count: int) -> int:
    if count == 0:
        return 1
    return sum(blink(new_stone, count-1) for new_stone in stone.change())

stones = '5688 62084 2 3248809 179 79 0 172169'
print(sum(blink(Stone.from_str(value), 25) for value in stones.split()))
print(sum(blink(Stone.from_str(value), 75) for value in stones.split()))