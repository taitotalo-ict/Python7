# Optimized solution with input

moves = ['kivi', 'sakset', 'paperi']
initials = ['k', 's', 'p']
answers = initials + moves
answer_1 = ''
while answer_1 not in answers:
    answer_1 = input('Player 1: [K]ivi, [S]akset tai [P]aperi? ').lower()

answer_2 = ''
while answer_2 not in answers:
    answer_2 = input('Player 2: [K]ivi, [S]akset tai [P]aperi? ').lower()

if answer_1 in initials:
    player_1 = initials.index(answer_1)
else:
    player_1 = moves.index(answer_1)

if answer_2 in initials:
    player_2 = initials.index(answer_2)
else:
    player_2 = moves.index(answer_2)

if player_1 == player_2:
    print('Tasapeli!')
elif (player_1 + 1) % 3 == player_2:
    print('Player 1 wins')
else:
    print('Player 2 wins')

#   K S P
# I 0 1 2
#   A B
#     A B
#   B   A
