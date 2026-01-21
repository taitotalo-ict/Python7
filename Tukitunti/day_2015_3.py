from pathlib import Path

SCRIPTROOT = Path(__file__).parent

pos = 0+0j
house_visits = {pos}
MOVES = {'^': 1j, 'v': -1j, '>': 1, '<': -1}

with open(SCRIPTROOT / 'input_2015_3.txt', 'r', encoding='utf-8') as file:
    data = file.read().strip()

for move in data:
    pos += MOVES[move]
    # match move:
    #     case '^':
    #         pos[1] += 1
    #     case 'v':
    #         pos[1] -= 1
    #     case '>':
    #         pos[0] += 1
    #     case '<':
    #         pos[0] -= 1
    house_visits.add(pos)

print(len(house_visits))

house_visits = {0+0j}
pos_santa = 0+0j
pos_robot = 0+0j
for index, move in enumerate(data):
    if index % 2 == 0:
        pos_santa += MOVES[move]
        house_visits.add(pos_santa)
    else:
        pos_robot += MOVES[move]
        house_visits.add(pos_robot)

print(len(house_visits))
