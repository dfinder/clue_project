#from gamestate import GameStateObject
from weapons import WeaponEnum
from rooms import RoomEnum
from character import CharacterEnum
import random


class Card():
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

#subclasses of class Card. Purpose is to quickly identify the card type so they can easily be put in the envelope
class CharacterCard(Card): 
    def __init__(self, value:str): 
        '''initializes the character card class with a value. 
        The value will be the enum name represented as a string
        Args: None 
        Returns: None'''
        super.__init__(value)
class WeaponCard(Card):
     def __init__(self, value:str): 
        '''initializes the weapon card class with a value. 
        The value will be the enum name represented as a string
        Args: None 
        Returns: None'''
        super.__init__(value)
        
class LocationCard(Card):
      def __init__(self, value:str): 
        '''initializes the location card class with a value. 
        The value will be the enum name represented as a string
        Args: None 
        Returns: None'''
        super.__init__(value)
        
    
class Deck():
    def __init__(self):
        '''
        initializes the cards by iterating through the enums and assigning values
        Args: None 
        Returns: None
        '''
        #The deck will have 3 seperate piles, one for characters, one for rooms, and one for weapon
        self.character_deck: list[CharacterCard] = [] 
        self.room_deck: list[LocationCard] = [] 
        self.weapon_deck: list[WeaponCard] = [] 
        
        for character in CharacterEnum: #creates character deck
            c = CharacterCard(character.name)
            self.character_deck.append(c)
        
        for room in RoomEnum: #creates room deck
            c = LocationCard(room.name)
            self.room_deck.append(c)
        
        for weapon in WeaponEnum: #creates weapon deck
            c = WeaponCard(weapon.name)
            self.weapon_deck.append(c)
    
    def shuffleDecks(self):
        '''shuffles all 3 decks of cards
        Args: None 
        Returns: None'''
        self.weapon_deck = random.shuffle(self.weapon_deck)
        self.character_deck = random.shuffle(self.character_deck)
        self.location_deck = random.shuffle(self.location_deck)

    def removeCardfromCharacterDeck(self) -> CharacterCard:
        '''removes a card from the character deck.
        Args: None 
        Returns: a card object'''
        return self.character_deck.pop()
    
    def addCardtoCharacterDeck(self, card: CharacterCard):
        '''adds a card to the character deck
        Args: object of type Card. 
        Returns: None'''
        if isinstance (card, CharacterCard):
            self.character_deck.append(card)
     
    def removeCardfromWeaponDeck(self) -> WeaponCard:
        '''removes a card from the weapon deck.
        Args: None 
        Returns: a card object'''
        return self.weapon_deck.pop()
    
    def addCardtoWeaponDeck(self, card: WeaponCard):
        '''adds a card to the weapon deck
        Args: object of type WeaponCard. 
        Returns: None'''
        if isinstance (card, WeaponCard):
            self.character_deck.append(card)

    def removeCardfromLocationDeck(self) -> LocationCard:
        '''removes a card from the location deck.
        Args: None 
        Returns: a card object'''
        return self.location_deck.pop()
    
    def addCardtoLocationDeck(self, card: LocationCard):
        '''adds a card to the location deck
        Args: object of type LocationCard. 
        Returns: None'''
        if isinstance (card, LocationCard):
            self.location_deck.append(card)




        
    



