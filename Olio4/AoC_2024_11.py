from functools import cache

@cache
def blink(stone: str, count: int) -> int:
    if count == 0:
        return 1
    if stone == '0':
        return blink('1', count-1) 
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        part1 = str(int(stone[:middle]))
        part2 = str(int(stone[middle:]))
        return blink(part1, count-1) + blink(part2, count-1)
    else:
        return blink(str(int(stone) * 2024), count-1)

stones = '5688 62084 2 3248809 179 79 0 172169'
print(sum(blink(stone, 25) for stone in stones.split()))
print(sum(blink(stone, 75) for stone in stones.split()))

    