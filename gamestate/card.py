from gamestate import GameStateObject
from enum import Enum 

class CardType(Enum):
    CHARACTER = 0
    WEAPON = 1 
    LOCATION = 2

class Card(GameStateObject):
    def __init__(self, name: str, card_type: CardType):
        self.name = name          # The name of the card
        self.card_type = card_type  # The type of card (CHARACTER, WEAPON, LOCATION)

    def __repr__(self):
        return f"{self.name} ({self.card_type.name})"

class CharacterCard(Card):
    def __init__(self, name: str):
        # Inherit from Card, with card_type set to CHARACTER
        super().__init__(name, CardType.CHARACTER)

class WeaponCard(Card):
    def __init__(self, name: str):
        # Inherit from Card, with card_type set to WEAPON
        super().__init__(name, CardType.WEAPON)
    
class LocationCard(Card):
    def __init__(self, name: str):
        # Inherit from Card, with card_type set to LOCATION
        super().__init__(name, CardType.LOCATION)
