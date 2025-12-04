# Standard modules
from random import choice
from typing import TYPE_CHECKING
from string import ascii_uppercase as LETTERS
# Custom modules
from square import Square
from coordinates import Coordinates
from direction import Direction

if TYPE_CHECKING:
    from ship import Ship

class Map:
    '''
    A map class that contains squares with sea or ship parts. 

    This class exposes the following methods:
    - add_ship_random(ship): To add a ship to a random position of the map.
    - hit(map_coordinates): To hit/attack a certain place of the map.
    - is_hit(map_coordinates): To check if a certain place of the map has been hit.
    - mark_neighbors(ship): To mark the neighbor squares of a ship as hit.

    The map can be printed (or converted to a string) with the __str__ method.
    '''
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.squares = {Coordinates(x, y): Square() for x in range(width) for y in range(height)}
        self.ships = {}


    def __contains__(self, coordinates: 'Coordinates') -> bool:
        '''Returns True if the map contains the given coordinates. False otherwise.'''
        pass

    def _get_square(self, coordinates: 'Coordinates') -> Square:
        '''Returns the square at the given location. Raise an Exception if coordinates are outside the map.'''
        pass

    def _get_neighbor_locations(self, location: 'Coordinates') -> list['Coordinates']:
        '''Returns a list of locations (Coordinates) around a given location. Coordinates outside the map are discarded.'''
        pass

    def _get_neighbor_squares(self, location: 'Coordinates') -> list[Square]:
        '''Returns the list of (valid) squares around a given location.'''
        pass

    def _get_locations_if_valid(self, initial_location: 'Coordinates', facing: 'Direction', length: int) -> None|list[Coordinates]:
        '''Returns a list of locations for a ship in the given direction, with the given length and from the given initial location.
        
        Returns None if it is not possible to place the ship inside the map or with enough separation from other ships.
        '''
        # Get list of locations (coordinates) given the initial location, where the ship is facing and the length of the ship
        ship_locations = [initial_location.get_relative(facing, n) for n in range(length)]
        
        # Are all locations within the map?
        if not all(map(self.__contains__, ship_locations)):
            return None
               
        # Get ship's neighbors' locations
        neighbor_locations = set()
        for location in ship_locations:
            neighbor_locations.update(self._get_neighbor_locations(location))

        # All locations: ship locations + neighbor locations
        locations = neighbor_locations.union(set(ship_locations))

        # Are all squares in those locations empty?
        if not all(map(Square.is_empty, {self._get_square(location) for location in locations})):
            return None
        
        # All locations are empty, so the initial location with the given conditions is valid
        return ship_locations

    def _add_ship(self, ship: 'Ship', initial_location: 'Coordinates', facing: 'Direction') -> bool:
        '''Add a ship to the given location and with the given direction. Returns True if the addition has been possible or False otherwise.'''
        # Get the locations of the ship if they are valid
        if not (ship_locations := self._get_locations_if_valid(initial_location, facing, len(ship))):
            return False

        # Get squares on those locations. 
        squares = [self._get_square(location) for location in ship_locations]

        # Assign ShipPart on those squares        
        for n in range(len(ship)):
            squares[n].set_ship_part(ship[n])

        # Add ship's info to the list of ships
        self.ships[ship] = {
            'ship': ship,
            'location': initial_location,
            'facing': facing,
            'squares': squares
        }

        return True
    
    def add_ship_random(self, ship: 'Ship') -> None:
        '''Adds the ship given as parameter in a random position of the map.'''
        pass

    def _get_random(self) -> 'Coordinates':
        '''Return random coordinates from the map.'''
        pass
    
    def _get_coordinates_from_map_coordinates(self, map_location: str) -> 'Coordinates':
        '''Get the general coordinates (x, y) that correspond to a certain map coordinates (eg. B7).'''
        letter = map_location[0].upper()
        if letter not in LETTERS[:self.width]:
            raise TypeError('First map coordinate must be a letter')
        
        try:
            number = int(map_location[1:])
        except TypeError:
            raise TypeError('Second map coordinate must be an integer number')
        
        coordinates = Coordinates(LETTERS.index(letter), number - 1)
        if coordinates not in self:
            raise ValueError('Map coordinates not in map')

        return coordinates

    def hit(self, map_coordinates:str) -> 'Ship|None':
        '''Hit/attack a certain map coordinates. Returns the result of the hit from the square.'''
        pass

    def is_hit(self, map_coordinates: str) -> bool:
        '''Checks whether a certain map coordinates have been hit before. Returns the result from the square.'''
        pass

    def mark_neighbors(self, ship: 'Ship') -> None:
        '''Mark all neighbors of the given ship as hit. Returns None.'''
        if ship not in self.ships:
            raise ValueError('Ship is not in this map')
        
        ship_info = self.ships[ship]

        for location in [ship_info['location'].get_relative(ship_info['facing'], n) for n in range(len(ship))]:
            for neighbor in self._get_neighbor_squares(location):
                neighbor.hit()

    def __str__(self) -> str:
        '''Return the map.'''
        result = f'   {LETTERS[:self.width]}\n'
        for y in range(self.height):
            result += f'{y+1:>2} '
            for x in range(self.width):
                result += str(self.squares[Coordinates(x, y)])
            result += '\n'
        return result
