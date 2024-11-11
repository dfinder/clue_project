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
        self.suggestor = suggestor
        self.weapon = weapon
        self.accused = accused
        self.location = location

    def __repr__(self):
        # print the suggestion
        return f"Suggestion by {self.suggestor.name}: {self.accused.name} with {self.weapon.name} in {self.location.name}"

