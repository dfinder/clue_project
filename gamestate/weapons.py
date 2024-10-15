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
    WeaponID:WeaponEnum
    
