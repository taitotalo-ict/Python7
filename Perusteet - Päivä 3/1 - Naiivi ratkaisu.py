# Naive solution

player_1 = 'kivi'
player_2 = 'sakset'

if player_1 == player_2:
    print('Tasapeli')
elif player_1 == 'kivi':
    if player_2 == 'sakset':
        print('Player 1 wins')
    elif player_2 == 'paperi':
        print('Player 2 wins')
    else:
        print('Tasapeli')
elif player_1 == 'sakset':
    if player_2 == 'kivi':
        print('Player 2 wins')
    elif player_2 == 'paperi':
        print('Player 1 wins')
    else:
        print('Tasapeli')
elif player_1 == 'paperi':
    if player_2 == 'kivi':
        print('Player 1 wins')
    elif player_2 == 'sakset':
        print('Player 2 wins')
    else:
        print('Tasapeli')


# Hieman muokattu versio
if player_1 == player_2:
    print('Tasapeli!')
elif player_1 == 'kivi':
    if player_2 == 'sakset':
        print('Player 1 wins')
    else:
        print('Player 2 wins')
elif player_1 == 'sakset':
    if player_2 == 'kivi':
        print('Player 2 wins')
    else:
        print('Player 1 wins')
# Player_1 = 'paperi'
elif player_2 == 'kivi':
    print('Player 1 wins')
else:
    print('Player 2 wins')
