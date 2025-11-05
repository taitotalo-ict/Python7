file = open('input_2015_2.txt')
content = file.readlines()
file.close()

total_gift_paper = 0
for row in content:
    lista = row.strip().split('x')
    # length, height, width = tuple(map(int, row.strip().split('x')))
    length = int(lista[0])
    height = int(lista[1])
    width = int(lista[2])
    area = 2 * length * width +  2 * width * height + 2 * height * length
    smallest_side = min(length * width, width * height, height * length)
    total_gift_paper += area + smallest_side

print(total_gift_paper)
