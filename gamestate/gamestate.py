from abc import ABC
from subprocess import _FILE
from card import CharacterCard,WeaponCard,LocationCard
from player import Player
from character import Character
from network_info import NetworkConnection
class GameStateObject(ABC):
    def as_json(self):
        pass #I define how this object looks in JSON
    def as_log(self):
        pass #I define 


class GameState(object):
    envelope:tuple[CharacterCard,WeaponCard,LocationCard]
    player_list: list[Player]
    turn_number:int 
    storage: _FILE  
    def __init__(self):
        pass
    def init_players(self,players:list[(NetworkConnection,Character)]):
        pass   
