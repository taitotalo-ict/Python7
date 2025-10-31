import random

# Optimized solution with input and functions

MOVES = ['kivi', 'sakset', 'paperi']
INITIALS = ['k', 's', 'p']
ANSWERS = INITIALS + MOVES

def get_move(name: str) -> int:
    """
    Get the player move and returns it in integer form

    This function will ask the user to choose between 'Kivi', 'Sakset' and 'Paperi'.
    The whole word or initials are accepted (case insensitive).
    It will keep asking the user until it gets a valid answer. It can not be cancelled.

    Parameters:
    - name (str): Name of the player that will be presented in the question

    Returns:
    An integer that represents the index in the options.

    """
    answer = ''
    while answer not in ANSWERS:
        answer = input(f'{name}: [K]ivi, [S]akset tai [P]aperi? ').lower()
    if answer in INITIALS:
        return INITIALS.index(answer)
    else:
        return MOVES.index(answer)

def play(player_1: int, player_2: int) -> str:
    """
    Calculate the winner according to the rules of the game and return a string declaring the winner.

    Parameters:
    - player_1 (int): The first player move. It's an index of the list of possible moves.
    - player_2 (int): The second player move. It's an index of the list of possible moves.

    Returns:
    A string containing a message declaring the winner or that the game was a draw.
    """
    if player_1 == player_2:
        return 'Tasapeli!'
    elif (player_1 + 1) % 3 == player_2:
        return 'Pelaaja 1 voittaa'
    else:
        return 'Pelaaja 2 voittaa'


player_1 = get_move('Pelaaja 1')
player_2 = random.randint(0, 2)

print(f'Pelaaja 1 pelaa {MOVES[player_1]}')
print(f'Pelaaja 2 pelaa {MOVES[player_2]}')

print(play(player_1, player_2))

#   K S P
# I 0 1 2
#   A B
#     A B
#   B   A
