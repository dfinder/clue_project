from gamestate import GameStateObject
from enum import Enum
from weapons import WeaponEnum
from rooms import RoomEnum
from character import CharacterEnum
import random


class CardType(Enum):
    CHARACTER = 0
    WEAPON = 1 
    LOCATION = 2

class Card(GameStateObject):
    # Cards that will be used in Clue. 
    # A card is more so a wrapper for a character, a weapon, or a room 
    def __init__(self, value:str): 
        '''initializes the card class with a value. 
        The value will be the enum name represented as a string
        Args: None 
        Returns: None'''
        self.value = value

    def getValue(self) -> str: 
        '''Returns the card's value as a string
        Args: None 
        Returns: None'''
        return self.value

#subclasses of cards. Purpose is to quickly identify the card type so they can easily be put in the envelope
class CharacterCard(Card): 
    pass
class WeaponCard(Card):
    pass
class LocationCard(Card):
    pass
    
class Deck(GameStateObject):
    def initializeDeck(self):
        '''
        initializes the cards by iterating through the enums and assigning values
        Args: None 
        Returns: None
        '''
        self.deck: list[Card] = [] #initializes a deck as a list of card objects
        for character in CharacterEnum: #creates character cards
            c = CharacterCard(character.name)
            self.deck.append(c)
        for room in RoomEnum: #creates room cards
            c = LocationCard(room.name)
            self.deck.append(c)
        for weapon in WeaponEnum: #creates weapon cards
            c = WeaponCard(weapon.name)
            self.deck.append(c)
    
    def shuffleDeck(self):
        '''shuffles the deck
        Args: None 
        Returns: None'''
        self.deck = random.shuffle(self.deck)

    def removeCard(self) -> Card:
        '''removes a card from the deck.
        Args: None 
        Returns: a card object'''
        return self.deck.pop()
    
    def addCard(self, card: Card):
        '''adds a card to the deck
        Args: object of type Card. 
        Returns: None'''
        self.deck.append(card)


        
    



