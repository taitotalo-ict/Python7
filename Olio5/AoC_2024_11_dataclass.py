from dataclasses import dataclass
from functools import cache

@dataclass(frozen=True)
class Stone:
    value : int

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
    
@cache
def blink(stone: Stone, count: int) -> int:
    if count == 0:
        return 1
    return sum(blink(new_stone, count-1) for new_stone in stone.change())

def blink_cached(stone: Stone, count: int, cache: dict = {}) -> int:
    if count == 0:
        return 1
    if cached_result := cache.get((stone.value, count), None):
        return cached_result
    cached_result = sum(blink_cached(new_stone, count-1, cache) for new_stone in stone.change())
    cache[(stone.value, count)] = cached_result
    return cached_result


stones = '5688 62084 2 3248809 179 79 0 172169'
print(sum(blink_cached(Stone.from_str(value), 25) for value in stones.split()))
print(sum(blink_cached(Stone.from_str(value), 75) for value in stones.split()))