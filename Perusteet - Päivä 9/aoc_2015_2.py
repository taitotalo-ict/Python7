with open('input_2015_2.txt') as file:
    content = []
    for line in file.readlines():
        content.append(tuple(map(int, line.rstrip().split('x'))))

total_gift_paper = 0
for length, height, width in content:
    area = 2 * length * width +  2 * width * height + 2 * height * length
    smallest_side = min(length * width, width * height, height * length)
    total_gift_paper += area + smallest_side

print(total_gift_paper)