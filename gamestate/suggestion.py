from weapons import Weapon
from character import Character
from player import Player
from rooms import Room
class Suggestion(GameStateObject):
    suggestor: Player
    weapon: Weapon
    accused: Character
    location: Room
    def __init__(player,weapon,accused):
        pass 

