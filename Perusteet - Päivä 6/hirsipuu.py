hidden_word = 'hirsipuu'
resolved_word = ['_'] * len(hidden_word)
VALID_LETTERS='abcdefghijklmnopqrstuvwxyzäö'


def ask_user(question: str) -> str:
    while True:
        answer = input(question).lower()
        if answer == '':
            continue
        else:
            for letter in answer:
                if letter not in VALID_LETTERS:
                    break
            else:
                return answer

while resolved_word.count('_') >= 1:
    print(f"Arvattava sana on {''.join(resolved_word)}")
    user_answer = ask_user('Syötä kirjain tai sana (A-Za-zÄäÖö)\n? ')
    
    if len(user_answer) == 1:
        for index, word_letter in enumerate(hidden_word):
            if user_answer == word_letter:
                resolved_word[index] = user_answer
    else:
        if user_answer == hidden_word:
           break 


print(f'Voitit. Sana oli {hidden_word}')


