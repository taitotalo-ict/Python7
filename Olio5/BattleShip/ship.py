class ShipPart:
    def __init__(self, ship: 'Ship', hidden: bool = False) -> None:
        self.ship = ship
        self.hidden = hidden
        self.hit_status = False 

    def is_hit(self) -> bool:
        '''Returns True if ship part has been hit/destroyed. False otherwise.'''
        return self.hit_status

    def hit(self) -> 'Ship':
        '''Ship part receives a hit. Returns the ship receiving the hit.'''
        self.hit_status = True
        return self.ship
    
    def __repr__(self) -> str:
        '''Returns representation of the ship part.'''
        return f'ShipPart(ship={self.ship}, hidden={self.hidden}, hit_status={self.hit_status})'
    
    def __str__(self) -> str:
        '''Returns a character representing the ship part: 'X' if hit, if not hit, '·' or '#' depending on being hidden or not respectively.'''
        return 'X' if self.hit_status else ('·' if self.hidden else '#')


class Ship:
    def __init__(self, size:int, hidden:bool = False) -> None:
        self.parts = [ShipPart(self, hidden) for _ in range(size)]

    def is_destroyed(self):
        '''Returns True if ship have been completely destroyed. False if some part has not been hit.'''
        return all(part.is_hit() for part in self.parts)

    def __getitem__(self, index: int) -> ShipPart:
        '''Returns ship part in position 'index'.'''
        return self.parts[index]

    def __len__(self) -> int:
        '''Returns length of the ship.'''
        return len(self.parts)

    def __contains__(self, part: ShipPart) -> bool:
        '''Returns True if ship contains given ship part. False otherwise.'''
        return part in self.parts

    def __repr__(self) -> str:
        '''Returns representation of the ship.'''
        return f'Ship(size={len(self.parts)})'
