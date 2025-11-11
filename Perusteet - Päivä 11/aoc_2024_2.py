from pathlib import Path

BASEDIR = Path(__file__).parent

def is_safe(report: tuple[int, ...]) -> bool:
    diffs = [report[index+1] - report[index] for index in range(len(report)-1)]
    return all(map(lambda num: 0 < num < 4, diffs)) or \
           all(map(lambda num: 0 > num > -4, diffs))

def is_safe_removing(report: tuple[int, ...]) -> bool:
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))
    # for i in range(len(report)):
    #     if is_safe(report[:i] + report[i+1:]):
    #         return True
    # return False

with open(BASEDIR / 'input_2024_2.txt', 'r', encoding='utf-8') as file:
    data = [tuple(map(int, line.strip().split())) for line in file]

safe = sum(is_safe(report) for report in data)
print(safe)
safe2 = sum(is_safe_removing(report) for report in data)
print(safe2)