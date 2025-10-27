# Optimized solution with input and functions

MOVES = ['kivi', 'sakset', 'paperi']
INITIALS = ['k', 's', 'p']
ANSWERS = INITIALS + MOVES

def get_move(name):
    answer = ''
    while answer not in ANSWERS:
        answer = input(f'{name}: [K]ivi, [S]akset tai [P]aperi? ').lower()
    if answer in INITIALS:
        return INITIALS.index(answer)
    else:
        return MOVES.index(answer)

def play(player_1, player_2):
    if player_1 == player_2:
        return 'Tasapeli!'
    elif (player_1 + 1) % 3 == player_2:
        return 'Player 1 wins'
    else:
        return 'Player 2 wins'


player_1 = get_move('Player 1')
player_2 = get_move('Player 2')

print(play(player_1, player_2))

#   K S P
# I 0 1 2
#   A B
#     A B
#   B   A
