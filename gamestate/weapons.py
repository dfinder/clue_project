from enum import Enum
from gamestate import GameSateObject

class WeaponEnum(Enum):
    CANDLESTICK = 0 
    DAGGER = 1 
    REVOLVER = 2 
    PVC_PIPE= 3 
    #who the heck uses lead in their plumbing, the roman empire?
    WRENCH = 4 
    ROPE = 4

class Weapon(GameSateObject):

    def __init__(self, weapon_id: WeaponEnum):
        self.weapon_id = weapon_id  

    def __repr__(self):
        # Return a string representation of the weapon 
        return f"{self.weapon_id.name.}"

    def __str__(self):
        return self.__repr__()
