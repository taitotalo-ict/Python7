word = 'hirsipuu'

# resolved_word = []
# for _ in word:
#     resolved_word.append('_')

# resolved_word = []
# for _ in range(len(word)):
#     resolved_word.append('_')

# resolved_word = []
# resolved_word.extend(['_']*len(word))

# resolved_word = list('_'*len(word))

resolved_word = ['_'] * len(word)

while resolved_word.count('_') >= 1:
    print(''.join(resolved_word))
    user_letter = input('Kirjain? ')
    for index, word_letter in enumerate(word):
        if user_letter == word_letter:
            resolved_word[index] = user_letter

print(f'Voitit. Sana oli {word}')


