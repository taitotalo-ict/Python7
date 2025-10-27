# Optimized naive solution

player_1 = 'kivi'
player_2 = 'sakset'

if player_1 == player_2:
    print('Tasapeli!')
elif (player_1 == 'kivi' and player_2 == 'sakset') or (player_1 == 'sakset' and player_2 == 'paperi') or (player_1 == 'paperi' and player_2 == 'kivi'):
    print('Player 1 wins')
else:
    print('Player 2 wins')

