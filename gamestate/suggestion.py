from weapons import Weapon
from character import Character
from player import Player
from rooms import Room
class Suggestion(GameStateObject):
    def __init__(self, suggestor: Player,weapon: Weapon,accused:Character, location: Room):
        self.suggestor = suggestor
        self.weapon = weapon 
        self.accused = accused
        self.location = location
        

