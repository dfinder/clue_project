



from dataclasses import dataclass
from functools import partial
import socket
from typing import TypeVar

TLocation = TypeVar("TLocation", bound="Location")

TStartingLoc = TypeVar("TStartingLoc", bound="StartingLoc")

TLocation = TypeVar("TLocation", bound="Location")
@dataclass
class Card(object):
    name: str
    def get_class(self)->str:
        pass
    def get_name(self):
        return self.name
    def __repr__(self):
        return self.name


class Location(object):
    def get_adjacency()->list[TLocation]:
        [Passage("Study","Kitchen",True),
         Passage("Lounge","Conservatory",True),
         Passage ("Study","Hall", False),
         Passage("Study","Library", False),
         Passage("Hall" "Lounge", False),
         Passage("Hall", "Billard", False),
         Passage("Lounge", "Dining", False),
         Passage("Dining", "Kitchen", False),
         Passage("Dining", "Billard", False),
         Passage("Billard", "Ball", False),
         Passage("Billard", "Library", False),
         Passage("Library", "Conservatory",False),
         Passage("Ball", "Conservatory", False),
         Passage("Ball", "Kitchen", False )]
    def get_adjacent(self)->list[TLocation]:
        pass
    def in_room(self):
        match self:
            case Room(_):
                True
            case _: 
                False
        
@dataclass
class Passage(Location):
    start: Location
    end: Location
    secret: bool
    def get_adjacent(self):
        return [self.start,self.end]
    
class Room(Card,Location):
    def get_class(self)->str:
        "Room"
    def match_passage(self,passage:Passage)->Location|None:
        match passage:
            case Passage(self.name,end,True): Room(end)
            case Passage(self.name,end,False): passage 
            case Passage(start,self.name,True):Room(start)
            case Passage(start,self.name,False):passage 
            case _:None
    def get_adjacent(self):
        list(filter(lambda x: x!=None,map(self.match_passage(),Location.get_adjacency())))
class Weapon(Card):
    def get_class(self)->str:
        "Weapon"
class Character(Card):
    def get_class(self)->str:
        "Character"
@dataclass
class StartingLoc(Location):
    piece:Character
    passage:Passage
    def get_starts()->list[TStartingLoc]:
           [StartingLoc("Scarlet",Passage("Hall","Lounge",False)),
            StartingLoc("Mustard", Passage("Dining","Lounge",False)),
            StartingLoc("White",Passage("Ball","Kitchen",False)),
            StartingLoc("Green",Passage("Ball","Conservatory",False)),
            StartingLoc("Plum",Passage("Study","Library",False)),
            StartingLoc("Peacock",Passage("Library","Conservatory",False))]
    def get_adjacent(self)->list[Location]:
            return [self.passage]
class Cards:
    seed=40
    CharCards= list(map(Character,["Plum","Mustard","Green","Scarlet","White","Peacock"]))
    WeaponCards= list(map(Weapon,["Candlestick","Dagger","Pipe","Revolver","Rope","Wench"]))
    RoomCards =  list(map(Room,["Kitchen","Ball","Conservatory","Billard","Library","Study","Dining","Hall","Lounge"]))
    prefix = lambda x: Cards.namePrefixMap[x]+x
    namePrefixMap = {"Plum":"Prof. ","Mustard":"Col. ","Green":"Rev. ","Scarlet":"Ms. ","White":"Mrs. ","Peacock":"Mrs. "}
    def shuffle(remaining:list[Card])->list[Card]:
        match remaining:
            case []: []
            case [top_card,*deck]: Cards.shuffle(Cards.rotate(deck),(((Cards.seed+1)^2) % len(deck))).append(top_card)
    def rotate(l, n):
        return l[n:] + l[:n]
    def selectWinCon()->tuple[tuple[Character,Weapon,Room],list[Card]]:
        characters = Cards.shuffle(Cards.CharCards)
        weapons = Cards.shuffle(Cards.WeaponCards)
        rooms = Cards.shuffle(Cards.RoomCards)
        (characters.pop(),weapons.pop(),rooms.pop(),Cards.shuffle([]+characters+weapons+rooms))
    def deal(remaining:list[Card],hand_count:int)->list[list[Card]]:
        hands = [[]]*hand_count
        while len(remaining) !=0:
            hands[0].append(remaining.pop())
            hands = Cards.rotate(hands,1)
        return hands

class Player(object):
    hand: list[Card]
    piece: list[Character]
    location: Location 
    telported: bool 
    lost: bool 
    is_player: bool
    def __init__(self):
        self.hand = [] 
        self.piece = None 
        self.knowledge = [] 
        self.location = None 
        self.teleported = False 
        self.lost = False 
        self.is_playing = False
    def perform_action(self,action:callable):
        pass
    def move(self,location):
        self.location = location 
    def teleport(self,location):
        self.location = location 
        self.telported = True 
    def guess(self, weapon:Weapon, target:Location):
        return (self,weapon,target,self.location)
    def accuse(self,weapon,target,location):
        pass

class GameState(object):
    players : list[Player]
    win_con: tuple[Weapon, Character, Location] # type: ignore
    turn_order: list[Character]
    action_set: list[callable]
    def __init__(self,network_addrs):
        players = [] 
    #def 


