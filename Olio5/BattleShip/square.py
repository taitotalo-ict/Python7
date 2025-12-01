from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship import ShipPart, Ship


class Sea:
    def __init__(self, square: 'Square') -> None:
        pass

    def hit(self) -> None:
        '''Sea receives a hit. Returns None.'''
        pass

    def is_hit(self) -> bool:
        '''Return True if this part of the sea has received a hit. False otherwise.'''
        pass

    def __str__(self) -> str:
        '''Returns a character representing the sea: 'o' if hit, '·' if not hit.'''
        pass

class Square:
    '''
    A class that represents a square of the map. A square can contain a part of the sea or a part of a ship.
    Default is to contain a part of the sea. A part of a ship can be added later, but once added it can't be changed.
    '''
    def __init__(self) -> None:
        pass

    def is_empty(self) -> bool:
        '''Returns True is this square contains a part of the sea. False if there is a ship part in this space.'''
        pass

    def set_ship_part(self, ship_part: 'ShipPart') -> None:
        '''Sets this square to contain the given ship part. Returns None.'''
        pass

    def hit(self) -> 'Ship|None':
        '''Hits the content of this square and returns what that content returns (a ship if a ship part is hit or None if it is sea).'''
        pass


    def is_hit(self) -> bool:
        '''Returns whether this square has been hit already.'''
        pass

    def __str__(self) -> str:
        '''
        Returns a character representing the content of this square:
           - '·': Sea that has not been hit.
           - 'o': Sea that has been hit.
           - '#': Ship part that has not been hit.
           - 'X': Ship part that has been hit.
        '''
        pass
    
    def __repr__(self) -> str:
        '''Representation of the square.'''
        pass
