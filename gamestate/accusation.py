import card 
from rooms import Room
from player import Player
from character import Character
from gamestate import GameStateObject
from weapons import Weapon
class accusation(GameStateObject):
    player: Player 
    character: Character 
    weapon: Weapon 
    room: Room
    
    def __init__(self,player:Player,character:Character,weapon:Weapon,location:Location):
        self.player = player 
        self.character = character
        self.weapon = weapon
        self.location=location


