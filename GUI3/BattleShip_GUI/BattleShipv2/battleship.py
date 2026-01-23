from resources import Map, Fleet
import random

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
            if letter not in self.GAME_LETTERS or number not in range(1, self.BOARD_SIZE+1):
                print(f'Answer should be a letter (from A to {self.GAME_LETTERS[-1]}) and a number (from 1 to {self.BOARD_SIZE}) together (without spaces) and in that order.')
            else:
                return answer.upper()

    def _hit_map_location(self, location: str, play_map: Map, fleet: Fleet) -> str:
        '''Hit/attack a given location by the game coordinates (e.g. "B7"). Returns a string with the result of the hit.'''
        if play_map.is_hit(location):
            return "ALREADY HIT"
        if ship := play_map.hit(location):
            if ship.is_destroyed:
                if fleet.is_destroyed:
                    return 'FLEET DESTROYED'
                else:
                    return 'SHIP DESTROYED'
            else:
                return 'HIT'
        else:
            return 'MISS'

    def run(self):
        player_map = Map(self.BOARD_SIZE)
        computer_map = Map(self.BOARD_SIZE)
        player_fleet = Fleet(player_map)
        computer_fleet = Fleet(computer_map, hidden=True)

        while not (computer_fleet.is_destroyed or player_fleet.is_destroyed):
            print('COMPUTER:')
            print(computer_map)

            print('\nPLAYER:')
            print(player_map)

            move = self._get_input('\nMove? (q to quit)')
            print()
            if move == 'q':
                break

            match self._hit_map_location(move, computer_map, computer_fleet):
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
                match self._hit_map_location(move, player_map, player_fleet):
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
            if computer_fleet.is_destroyed and player_fleet.is_destroyed:
                print(computer_map)
                print(player_map)
                print('\nYou both have destroyed mutually! What a game!')
            elif computer_fleet.is_destroyed:
                print(computer_map)
                print('\nYou win! Good job!')
            else:
                print(player_map)
                print('\nComputer wins. Best luck next time!')

        print('See you. Thanks for playing!')

if __name__ == '__main__':
    game = BattleShipGame()
    game.run()
