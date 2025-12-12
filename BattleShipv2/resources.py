from dataclasses import dataclass
from enum import StrEnum
import random
from collections.abc import Generator   # Typing


class Direction(StrEnum):
    UP ='up'
    UPRIGHT = 'upright'
    RIGHT = 'right'
    DOWNRIGHT = 'downright'
    DOWN = 'down'
    DOWNLEFT = 'downleft'
    LEFT = 'left'
    UPLEFT = 'upleft'
    
    def get_same_dir(self) -> Generator['Direction']:
        '''Returns a list of the directions similar to this one.
        For example, for UP, this methods returns UPLEFT, UP and UPRIGHT. For LEFT it returns DOWNLEFT, LEFT and UPLEFT.'''
        dir_list = list(self.__class__)
        self_index = dir_list.index(self)
        return (dir_list[index % len(dir_list)] for index in range(self_index-1, self_index+2))


class Square:
    def __init__(self, column_letter: str, row_number: int) -> None:
        for direction in Direction:
            setattr(self, direction, None)
        self.next: 'Square|None' = None
        self.ship: 'Ship|None' = None
        self.is_hit: bool = False
        self.column_letter = column_letter
        self.row_number = row_number

    @property
    def is_free(self) -> bool:
        '''Return is square is free (there is no ship in the square)'''
        return self.ship is None

    @property
    def neighbors(self) -> Generator['Square']:
        '''Return all existing surrounding squares'''
        return (getattr(self, direction) for direction in Direction if getattr(self, direction) is not None)

    def get_direction_neighbors(self, direction: Direction) -> Generator['Square']:
        '''Get the squares next to this one in the indicated direction if there are any.
        
        For example, for UP, this methods checks UPLEFT, UP and UPRIGHT. For LEFT it checks UPLEFT, LEFT and DOWNLEFT.'''
        return (getattr(self, dir) for dir in direction.get_same_dir() if getattr(self, dir) is not None)
    
    def get_neighbor(self, direction: Direction) -> 'Square':
        '''Get the neighbor square in the indicated direction.'''
        return getattr(self, direction)

    def hit(self) -> 'Ship|None':
        '''Mark the square as hit. If the square contains a ship and the ship is destroyed, mark surrounding squares also as hit.
        Returns the content of the square: a Ship or None'''
        if self.is_hit:
            return self.ship
        self.is_hit = True
        if self.ship:
            if self.ship.is_destroyed:
                for square in self.ship:
                    for neighbor in square.neighbors:
                        neighbor.hit()
            return self.ship
        return None

    def __str__(self) -> str:
        '''
        Returns a character representing the content of this square:
           - '·': Sea that has not been hit.
           - 'o': Sea that has been hit.
           - '#': Ship part that has not been hit.
           - 'X': Ship part that has been hit.
        '''
        if self.ship:
            return 'X' if self.is_hit else ('·' if self.ship.hidden else '#')
        else:
            return 'o' if self.is_hit else '·'

    def __repr__(self):
        '''Returns a developer friendly representation of the Square'''
        return f'<Square {self.column_letter}{self.row_number}>'


@dataclass
class Ship:
    start_square: 'Square'
    direction: Direction
    size: int
    hidden: bool = False

    @property   
    def is_destroyed(self) -> bool:
        '''Return True if all squares of the ship have been hit.'''
        return all(sq.is_hit for sq in self)

    def __len__(self) -> int:
        '''Return the size of the ship.'''
        return self.size

    def __iter__(self):
        '''Ship iterator. Iterator returns ship squares.'''
        current = self.start_square
        while current:
            yield current
            current = current.next


class Map:
    '''
    A map class that contains squares. Squares can be empty (sea/water) or can contain a ship/ship part. 

    This class exposes the following methods:
    - add_ship_random(size): To create and add a ship of the given size to a random position of the map.
    - hit(coordinates): To hit/attack a certain place of the map.
    - is_hit(coordinates): To check if a certain place of the map has been hit.

    The map can be printed (or converted to a string) with the __str__ method.
    '''

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Class attribute

    def __init__(self, size: int) -> None:
        self.size = size
        self.squares = {}
        self.previous_row = None
        self.previous_column = None
        self.row_count = self.column_count = 0
        self.ships = []
        for _ in range(size*size):
            self._add_square()

    # Private methods

    def _add_square(self) -> None:
        '''Add a single square to the map.
        
        Implementation organize squares in a grid, making sure that when a row is completed column pointer is reset and a new row is started.
        Squares are double linked with all surrounding squares.'''
        # Create new square with current coordinates and add it to the list of squares
        new_square = Square(self.LETTERS[self.column_count], self.row_count+1)
        self.squares[self.LETTERS[self.column_count] + str(self.row_count+1)] = new_square
        
        # As squares are added in order, there is nothing to the right and down of the new square.
        # Only previous squares has to be taken into account. That is: LEFT, UPLEFT, UP and UPRIGHT

        # If not first column of the row
        if self.previous_column:
            # LEFT
            new_square.left = self.previous_column
            new_square.left.right = new_square
            
            # UPLEFT (if not first row)
            if new_square.left.up:
                new_square.upleft = new_square.left.up
                new_square.upleft.downright = new_square
            
            # UP - 1 way link
            new_square.up = self.previous_column.upright
        else:   # This is first column in row
            # If there is a previous row (not first row)
            if self.previous_row:
                # UP - 1 way link
                new_square.up = self.previous_row
            
            # Update row pointer
            self.previous_row = new_square
        
        # If there is a previous row
        if new_square.up:
            # UP - back link
            new_square.up.down = new_square
            
            # UPRIGHT (if not last column)
            if new_square.up.right:
                new_square.upright = new_square.up.right
                new_square.upright.downleft = new_square
        
        # Update counter and pointer attributes
        self.column_count += 1
        if self.column_count == self.size:
            self.column_count = 0
            self.row_count += 1
            self.previous_column = None
        else:
            self.previous_column = new_square

    def _add_ship(self, ship: 'Ship'):
        '''Try to add a ship to the map. If it is not possible to add the ship, returns False. If the ship is successfully added to the map, returns True.'''
        # Check if start_square is touching any other ship
        for neighbor in ship.start_square.neighbors:
            if not neighbor.is_free:
                return False

        count = len(ship)
        current = ship.start_square
        temp_squares = [current]
        while count > 1:
            # Does the ship "fall out" of the map?
            if not (next := current.get_neighbor(ship.direction)):
                return False
            
            # Check possible new neighbors in direction
            for neighbor in next.get_direction_neighbors(ship.direction):
                if not neighbor.is_free:
                    return False

            temp_squares.append(next)
            current = next
            count -= 1

        # Mark squares as occupied
        for square in temp_squares:
            square.ship = ship

        # Link ship squares
        square = temp_squares[0]
        for next in temp_squares[1:]:
            square.next = next
            square = next

        return True

    def _get_random_square(self) -> Square:
        '''Get a random square from the map grid.'''
        return random.choice(list(self.squares.values()))
    
    def _get_random_direction(self) -> Direction:
        '''Get a random direction without diagonals.'''
        return random.choice(list(Direction)[::2])
    
    # Public methods

    def add_random_ship(self, size: int) -> Ship:
        '''Creates and add a ship of the given size to a random location of the map.'''
        while True:
            ship = Ship(self._get_random_square(), self._get_random_direction(), size)
            if self._add_ship(ship):
                return ship
    
    def hit(self, coordinates:str) -> 'Ship|None':
        '''Hit/attack a certain map coordinates. Returns the result of the hit from the square.'''
        return self.squares[coordinates.upper()].hit()

    def is_hit(self, coordinates: str) -> bool:
        '''Checks whether a certain map coordinates have been hit before. Returns the result from the square.'''
        return self.squares[coordinates.upper()].is_hit

    def __str__(self) -> str:
        '''Return the map.'''
        result = f'   {self.LETTERS[:self.size]}\n'
        for y in range(self.size):
            result += f'{y+1:>2} '
            for x in self.LETTERS[:self.size]:
                result += str(self.squares[x+str(y+1)])
            result += '\n'
        return result

class Fleet:
    SIZES = [5, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def __init__(self, map: Map, hidden: bool = False) -> None:
        self.ships = [map.add_random_ship(size) for size in self.SIZES]
        if hidden:
            for ship in self.ships:
                ship.hidden = True

    @property
    def is_destroyed(self):
        return all(ship.is_destroyed for ship in self.ships)
