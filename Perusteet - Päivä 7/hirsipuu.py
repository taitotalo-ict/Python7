hidden_word = 'hirsipuu'
resolved_word = ['_'] * len(hidden_word)
VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyzäö'
used_letters = set()

def ask_user(question: str) -> str:
    while True:
        answer = input(question).lower()
        match answer:
            case '':
                continue
       
            case '0':
                return '0'
            case _:
                for letter in answer:
                    if letter not in VALID_LETTERS:
                        break
                else:
                    return answer

while True:
    print(f"Arvattava sana on {''.join(resolved_word)}")
    user_answer = ask_user('Syötä kirjain tai sana (A-Za-zÄäÖö). 0 -> lopettaa peli\n? ')
    match user_answer:
        case '0':
            print('Kiitos pelaamisesta')
            break
        
        case _ if len(user_answer) == 1:
            if user_answer in used_letters:
                print('Viesti')
                continue

            used_letters.add(user_answer)
            for index, word_letter in enumerate(hidden_word):
                if user_answer == word_letter:
                    resolved_word[index] = user_answer
        
        case _ if user_answer == hidden_word:
           resolved_word = list(hidden_word)
    
    if resolved_word.count('_') == 0:
           print(f'Voitit. Sana oli {hidden_word}')
           break
