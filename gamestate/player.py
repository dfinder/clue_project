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
    def __init__(self, PlayerID, PlayingPiece, Cards):
        self.PlayerID = PlayerID
        self.TurnOrder = 0
        self.PlayingPiece = PlayingPiece
        self.Cards = Cards
        self.AccusationState=False
        self.TeleportFlag=False
        self.Knowledge = []

    
    def set_character(self,char:Character):
        '''
        sets the character for the player
        Args: char: Character as type Character class. Will be passed into PlayingPiece
        Returns: None
        '''
        self.PlayingPiece = char

    @property
    def get_Character(self) -> str:

        return self.PlayingPiece.char.charID.name
    
    def add_initial_cards(self, card: Card):
        '''
        adds a card to the Player's card list
        Args: card that will be passed into the player's list of cards
        Returns: None
        '''
        self.Cards.append(card)
    
    def set_initial_knowledge(self): #Not sure how to implement this
        pass 

    def set_teleport_flag(self, flag_value: bool):
        '''
        sets the player's teleport flag
        Args: flag_value: boolean that will be passed into the TeleportFlag value
        Returns: None
        '''
        self.TeleportFlag = flag_value

    @property
    def get_teleport_flag(self) -> bool:
        return self.TeleportFlag

    @property
    def get_location(self) -> Location:
        return self.location 
    
    @property
    def get_accusation_state(self) -> AccusationState:
        return self.AccusationState
    
    def set_location(self, location: Location):
        '''
        sets the player's location
        Args: location: Location that will get passed to the player's location variable
        Returns: None
        '''
        self.Location = location

    def increase_turn_order(self):
        '''
        increases the player's turn order
        Args: None
        Returns: None
        '''
        self.TurnOrder += 1

    def getCards(self) -> list[str]:
        '''
        Allows players to see their cards
        Args: None
        Returns: list of strings representing the card's value
        '''
        list_of_card_values = []
        for card in self.Cards:
            list_of_card_values.append(card.getValue())
        return list_of_card_values

    


