from gamestate import GameStateObject
from card import Card,Deck
from character import Character
from location import Location
from suggestion import Suggestion
ID = int
class Player(GameStateObject):
    PlayerID:ID
    TurnOrder: int 
    PlayingPiece: Character
    Cards: list[Card]
    Knowledge: list[(Card,ID)] #ID 
    Suggestions: list[Suggestion]
    TeleportFlag: bool 
    Location: Location
    AccusationState: bool
    #NetworkInfo: NetworkInfo
    def __init__(self):
        self.AccusationState=False
        self.TeleportFlag=False
    def set_character(self,char:Character):
        #Set Playing Piece, Set Location
        # Set turn order?
        pass 
    def add_initial_cards(self,card: Card):
        pass 
    def set_initial_knowledge(self):
        pass 
    


