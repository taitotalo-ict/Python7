class Hirsipuu:
    def __init__(self, hidden_word: str) -> None:
        self._hidden_word = hidden_word
        self._resolved_word = ['_'] * len(hidden_word)
    
    def is_resolved(self) -> bool:
        return self._resolved_word.count('_') == 0

        # try:
        #     self._resolved_word.index('_')
        # except ValueError:
        #     return True
        # return False

        # return ''.join(self._resolved_word).find('_') == -1

    @property
    def hidden_word(self) -> str:
        return ''.join(self._resolved_word)
    
    def resolve_letter(self, user_letter: str) -> None:
        for index, word_letter in enumerate(self._hidden_word):
            if user_letter == word_letter:
                self._resolved_word[index] = user_letter


game = Hirsipuu('hirsipuu')

while not game.is_resolved():
    print(game.hidden_word)
    letter = input('Kirjain? ')
    game.resolve_letter(letter)

print(f'Voitit! Sana oli: {game.hidden_word}')
