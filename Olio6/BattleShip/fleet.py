from ship import Ship
from map import Map

class Fleet:
    _SHIP_QUANTITY = {1: 3, 2: 3, 3: 2, 4: 1, 5: 1}

    def __init__(self, board_size, hidden: bool = False) -> None:
        self._ships = [Ship(ship_size, hidden) for ship_size, ship_count in sorted(self._SHIP_QUANTITY.items(), reverse=True) for _ in range(ship_count)]
        self._map = Map(board_size, board_size)
        self.add_to_map()
    
    def __iter__(self):
        '''Returns an iterator of the ships.'''
        return iter(self._ships)
    
    def is_destroyed(self) -> bool:
        '''Returns True if all ships are destroyed. False otherwise.'''
        return all(map(Ship.is_destroyed, self._ships))     # map is Python map function, not game map!!!

    @property
    def map(self) -> Map:
        '''Returns the map where this fleet resides.'''
        return self._map
    
    def add_to_map(self) -> None:
        '''Add the ships of this fleet to the map. Returns None.'''
        for ship in self:
            self._map.add_ship_random(ship)