from pathlib import Path


SCRIPT_ROOT = Path(__file__).parent

with open(SCRIPT_ROOT / 'input_2015_2.txt') as file:
    content = [tuple(map(int, line.rstrip().split('x'))) for line in file.readlines()]
    # content = []
    # for line in file.readlines():
    #     content.append(tuple(map(int, line.rstrip().split('x'))))

total_gift_paper = sum(
    2 * length * width +  2 * width * height + 2 * height * length 
    + min(length * width, width * height, height * length)
    for length, height, width in content
    )

# total_gift_paper = 0
# for length, height, width in content:
#     area = 2 * length * width +  2 * width * height + 2 * height * length
#     smallest_side = min(length * width, width * height, height * length)
#     total_gift_paper += area + smallest_side

print(total_gift_paper)