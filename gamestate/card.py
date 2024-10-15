from gamestate import GameStateObject
from enum import Enum 
class CardType(Enum):
    CHARACTER = 0
    WEAPON = 1 
    LOCATION = 2

class Card(GameStateObject):
    #A card is more so a wrapper for a character, a weapon, or a room
    pass
class CharacterCard(Card):
    pass
class WeaponCard(Card):
    pass
class LocationCard(Card):
    pass