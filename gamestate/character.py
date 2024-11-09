from enum import Enum 
from rooms import StartingRoom
from gamestate import GameStateObject
class CharacterEnum(Enum):
    SCARLET=0
    MUSTARD=1
    PEACOCK=2 
    GREEN=3
    WHITE=4
    PLUM=5
#I don't think we need all this stuff
class CharacterColors():
    #Maps character enums to hex codes, for the purposes of button colors, text highlighting, etc. 
    pass
class Character(GameStateObject):
    
    def __init__(self, CharID:CharacterEnum, CharStartingLocation:StartingRoom, CharLabel:str):
        '''
        Initializes the class for character. 
        Args:
            CharID:CharacterEnum
            CharStartingLocation:StartingRoom
            CharLabel:str #Human readable name
        Returns:
            None
        '''
        self.CharID = CharID
        self.CharStartingLocation = CharStartingLocation
        self.CharLabel = CharLabel
        