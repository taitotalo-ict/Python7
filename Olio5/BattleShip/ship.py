class ShipPart:
    def __init__(self, ship: 'Ship', hidden: bool = False) -> None:
        pass

    def is_hit(self) -> bool:
        '''Returns True if ship part has been hit/destroyed. False otherwise.'''
        pass

    def hit(self) -> 'Ship':
        '''Ship part receives a hit. Returns the ship receiving the hit.'''
        pass
    
    def __repr__(self) -> str:
        '''Returns representation of the ship part.'''
        pass
    
    def __str__(self) -> str:
        '''Returns a character representing the ship part: 'X' if hit, if not hit, '·' or '#' depending on being hidden.'''
        pass


class Ship:
    def __init__(self, size:int, hidden:bool = False) -> None:
        pass

    def is_destroyed(self):
        '''Returns True if ship have been completely destroyed. False if some part has not been hit.'''
        pass

    def __getitem__(self, index: int) -> ShipPart:
        '''Returns ship part in position 'index'.'''
        pass

    def __len__(self) -> int:
        '''Returns length of the ship.'''
        pass

    def __contains__(self, part: ShipPart) -> bool:
        '''Returns True if ship contains given ship part. False otherwise.'''
        pass

    def __repr__(self) -> str:
        '''Returns representation of the ship.'''
        pass
