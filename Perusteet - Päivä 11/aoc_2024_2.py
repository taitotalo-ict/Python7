from pathlib import Path

BASEDIR = Path(__file__).parent

def is_between_1_and_3(num: int) -> bool:
    return 0 < num < 4
    # return 1 <= num <= 3
    # return (num >= 1 and num <= 3)
    # return True if num >= 1 and num <= 3 else False
    # if num >= 1 and num <= 3:
    #     return True
    # else:
    #     return False

def is_negative_between_1_and_3(num: int) -> bool:
    return 0 > num > -4

def is_safe(report: tuple[int, ...]) -> bool:
    diffs = [report[index+1] - report[index] for index in range(len(report)-1)]
    return all(map(is_between_1_and_3, diffs)) or \
           all(map(is_negative_between_1_and_3, diffs))

    # is_negative = diffs[0] < 0
    # for diff in diffs:
    #     if abs(diff) < 1 or abs(diff) > 3:
    #     # if not(0 < abs(diff) < 4):
    #         return False
    #     if is_negative != (diff < 0):
    #         return False
    # return True


with open(BASEDIR / 'input_2024_2.txt', 'r', encoding='utf-8') as file:
    data = [tuple(map(int, line.strip().split())) for line in file]

safe = sum(is_safe(report) for report in data)
print(safe)