import random
# from string import ascii_uppercase as LETTERS
from fleet import Fleet

class BattleShipGame:
    BOARD_SIZE = 10
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    GAME_LETTERS = LETTERS[:BOARD_SIZE]

    def _get_input(self, question: str) -> str:
        while True:
            answer = input(question + ' ')
            if answer == 'q':
                return answer
            letter = ''
            number = None
            if 1 < len(answer) < 4:
                try:
                    letter = answer[0].upper()
                    number = int(answer[1:])
                except ValueError:
                    pass
            if letter not in self.GAME_LETTERS or number is None:
                print(f'Answer should be a letter (from A to {self.GAME_LETTERS[-1]}) and a number (from 1 to {self.BOARD_SIZE}) together (without spaces) and in that order.')
            else:
                return answer.upper()

    def _hit_map_location(self, location: str, fleet: Fleet) -> str:
        '''Hit/attack a given location by the game coordinates (e.g. "B7"). Returns a string with the result of the hit.'''
        map = fleet.map
        if map.is_hit(location):
            return "ALREADY HIT"
        if ship := map.hit(location):
            if ship.is_destroyed():
                map.mark_neighbors(ship)
                if fleet.is_destroyed():
                    return 'FLEET DESTROYED'
                else:
                    return 'SHIP DESTROYED'
            else:
                return 'HIT'
        else:
            return 'MISS'

    def run(self):
        player_fleet = Fleet(self.BOARD_SIZE)
        computer_fleet = Fleet(self.BOARD_SIZE, hidden=True)

        while not (computer_fleet.is_destroyed() or player_fleet.is_destroyed()):
            print('COMPUTER:')
            print(computer_fleet.map)

            print('\nPLAYER:')
            print(player_fleet.map)

            move = self._get_input('\nMove? (q to quit)')
            print()
            if move == 'q':
                break

            match self._hit_map_location(move, computer_fleet):
                case "HIT":
                    print('Hit! Good move!')
                case "MISS":
                    print('Miss! Attack goes to water.')
                case "SHIP DESTROYED":
                    print('Yeah! You destroyed the ship!')
                    print('You have another shot!\n')
                    continue
                case "FLEET DESTROYED":
                    print("Yeah! You destroyed the last ship and therefore the whole enemy's fleet!")
                case "ALREADY HIT":
                    print('You already attacked that location. You lost your turn!')
            print()

            play = True        
            while play:
                play = False
                move = random.choice(self.GAME_LETTERS) + str(random.randint(1, self.BOARD_SIZE))
                print(f'Computer attacks {move}')
                match self._hit_map_location(move, player_fleet):
                    case "HIT":
                        print('Hit! Your ship is damaged')
                    case "MISS":
                        print('Miss! Attacks goes to water.')
                    case "SHIP DESTROYED":
                        print('Oh no! Computers destroyed the ship!')
                        print('Computer plays again!')
                        play = True
                    case "FLEET DESTROYED":
                        print('Oh no! Computers destroyed your last ship and with that, all your fleet!')
                    case "ALREADY HIT":
                        print('Computer already attacked that location. Computer loses its turn!')
                print()    
        else:   # While ended because one of the fleets is destroyed
            if computer_fleet.is_destroyed() and player_fleet.is_destroyed():
                print(computer_fleet.map)
                print(player_fleet.map)
                print('\nYou both have destroyed mutually! What a game!')
            elif computer_fleet.is_destroyed():
                print(computer_fleet.map)
                print('\nYou win! Good job!')
            else:
                print(player_fleet.map)
                print('\nComputer wins. Best luck next time!')

        print('See you. Thanks for playing!')

if __name__ == '__main__':
    game = BattleShipGame()
    game.run()