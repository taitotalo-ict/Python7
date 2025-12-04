from direction import Direction

class Coordinates:
    '''
    A class that represents pairs of integers (x, y) that specify locations on a two-dimensional grid.
    The x values increase towards the right and the y values increase downwards.
    
    A coordinate object is immutable after creation.
    '''

    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        ''' Returns the x coordinate as an integer.'''
        return self._x

    @property
    def y(self) -> int:
        '''Returns the y coordinate as an integer.'''
        return self._y

    def get_neighbor(self, direction: Direction) -> 'Coordinates':
        '''Returns the coordinates of the location next to these one in the given direction.'''
        return self.get_relative(direction, distance=1)

    def get_relative(self, direction: Direction, distance: int) -> 'Coordinates':
        '''Returns the coordinates of the location at a given distance from this location in the given direction.'''
        return Coordinates(self.x + (direction.x * distance), self.y + (direction.y * distance))

    def get_neighbors(self) -> list['Coordinates']:
        '''Return a list of coordinates of the locations next to this one in all directions.'''
        return [self.get_neighbor(direction) for direction in Direction]

    def __repr__(self) -> str:
        '''Representation on the coordinates.'''
        return f'Coordinates({self.x}, {self.y})'

    def __str__(self) -> str:
        '''Returns a string in the form "(X, Y)" of the coordinates.'''
        return f'({self.x}, {self.y})'
