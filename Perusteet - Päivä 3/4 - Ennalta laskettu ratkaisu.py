# Precompiled solution

player_1 = 'K'
player_2 = 'S'

results = { 'KS': 1, 'SP': 1, 'PK': 1, 'KP': 2, 'SK': 2, 'PS': 2 }
move = player_1 + player_2

if player_1 == player_2:
    print('Tasapeli')
else:
    print(f'Player {results[move]} wins')