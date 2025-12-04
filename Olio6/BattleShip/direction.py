import random
from enum import Enum

class Direction(Enum):
    '''These constants represent the main directions that can be used to move on a map.'''
    UP = None
    UP_RIGHT = None
    RIGHT = None
    DOWN_RIGHT = None
    DOWN = None
    DOWN_LEFT = None
    LEFT = None
    UP_LEFT = None

    @property
    def x(self) -> int:
        '''Returns x component of the direction as int.'''
        pass
    
    @property
    def y(self) -> int:
        '''Returns y component of the direction as int.'''
        pass

    @classmethod
    def get_values(cls) -> list['Direction']:
        '''Returns a list of directions in a clockwise direction starting from up.'''
        pass

    @classmethod
    def get_random(cls) -> 'Direction':
        '''Return a random direction (not diagonals!).'''
        pass
