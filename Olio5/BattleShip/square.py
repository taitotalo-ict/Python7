from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship import ShipPart, Ship


class Sea:
    def __init__(self, square: 'Square') -> None:
        self.square = square
        self.hit_status = False

    def hit(self) -> None:
        '''Sea receives a hit. Returns None.'''
        self.hit_status = True

    def is_hit(self) -> bool:
        '''Return True if this part of the sea has received a hit. False otherwise.'''
        return self.hit_status

    def __str__(self) -> str:
        '''Returns a character representing the sea: 'o' if hit, '·' if not hit.'''
        return 'o' if self.hit_status else '·'

class Square:
    '''
    A class that represents a square of the map. A square can contain a part of the sea or a part of a ship.
    Default is to contain a part of the sea. A part of a ship can be added later, but once added it can't be changed.
    '''
    def __init__(self) -> None:
        self.content = Sea(self)

    def is_empty(self) -> bool:
        '''Returns True is this square contains a part of the sea. False if there is a ship part in this space.'''
        return isinstance(self.content, Sea)

    def set_ship_part(self, ship_part: 'ShipPart') -> None:
        '''Sets this square to contain the given ship part. Returns None.'''
        if not self.is_empty():
            raise Exception
        self.content = ship_part

    def hit(self) -> 'Ship|None':
        '''Hits the content of this square and returns what that content returns (a ship if a ship part is hit or None if it is sea).'''
        return self.content.hit()

    def is_hit(self) -> bool:
        '''Returns whether this square has been hit already.'''
        return self.content.is_hit()

    def __str__(self) -> str:
        '''
        Returns a character representing the content of this square:
           - '·': Sea that has not been hit.
           - 'o': Sea that has been hit.
           - '#': Ship part that has not been hit.
           - 'X': Ship part that has been hit.
        '''
        return self.content.__str__()
        # return str(self.content)
    
    def __repr__(self) -> str:
        '''Representation of the square.'''
        return f'<Square: {self.content}>'
