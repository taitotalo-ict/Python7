file = open(r'J:\Kouluttajat\Christian Finnberg\Ohjelmointi\Python\AoC\2015\input_2015_1.txt', 'r')

instructions = file.read().rstrip('\n')
file.close()



# Osa 1
kerros = 0
for char in instructions:
    kerros += 1 if char == '(' else -1
    # if char == '(':
    #     kerros += 1
    # else:
    #     kerros -= 1

# Osa 1 - vaihtoehto
# up = instructions.count('(')
# down = instructions.count(')')
# kerros = up - down

print(f'Osa 1: Kerros on {kerros}')

# Osa 2
kerros = 0
for index, char in enumerate(instructions):
    kerros += 1 if char == '(' else -1
    if kerros == -1:
        break

print(f'Osa 2: Sijanti on {index+1}')


# Molemmat osat yhdessä
kerros = 0
sijainti = None
for index, char in enumerate(instructions):
    kerros += 1 if char == '(' else -1
    if kerros == -1:
        if not sijainti:
            sijainti = index + 1

print(f'Osa 1: Kerros on {kerros}')
print(f'Osa 2: Sijanti on {sijainti}')
