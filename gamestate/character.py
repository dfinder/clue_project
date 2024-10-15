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
class CharacterColors():
    #Maps character enums to hex codes, for the purposes of button colors, text highlighting, etc. 
class Character(GameStateObject):
    CharID:CharacterEnum
    CharStartingLocation:StartingRoom
    CharLabel:str #Human readable name
    def __init__(self):
        pass