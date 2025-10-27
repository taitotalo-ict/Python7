# Optimized solution

moves = ['kivi', 'sakset', 'paperi']

player_1 = 0
player_2 = 1

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
