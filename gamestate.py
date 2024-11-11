from dataclasses import dataclass
from typing import TypeVar
from player import Player
from ui import Option, menu
import time
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
        isinstance(self,Room)

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
            case Passage(start,self.name,True): Room(start)
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
    prefix = lambda x: Cards.namePrefixMap[x]+" "+x
    namePrefixMap = {"Plum":"Prof.","Mustard":"Col.","Green":"Rev.","Scarlet":"Ms.","White":"Mrs.","Peacock":"Mrs."}
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

class GameState(object):
    players : list[Player]
    win_con: tuple[Weapon, Character, Location] # type: ignore
    turn_order: list[Character]
    previous_action_set: list[str]
    user: Character
    log: list[str]
    def __init__(self,seed,active:list[Character],char:Character):
        self.user = char
        self.turn_order = active 
        self.players = [Player(piece,piece in active) for piece in Cards.CharCards()]
    def action(self,action,*kwargs):
        action(self,*kwargs)
    def char(self)->Player:
        return filter(lambda x: x.piece == self.user, self.players)
    def take_turn(self): #Does the UI work.
        action_set = []
        if self.char().lost:
            return menu(Option("NEXT TURN","Skip Turn"))
    def suggestion_response(self,*kwargs): #This fulfils the guess
        #From player is who made the most recent response
        #Orig player is who made the guess 
        #Suggestion is the original contents of the action
        #Response player is who gives you the card

        #God I need a state diagram to sort this out tomorrow
    
        (from_player,orig_player,suggestion,response_player,card)=kwargs
        (weapon,char,location) = suggestion
        if orig_player == self.user: #User case 

            if card == None:
                print(f"{Cards.prefix(response_player)} Didn")
            else:
                if self.user == orig_player:
                    print(f"{Cards.prefix(response_player)} has informed you that:")
                    print(f"{card} was an invalid part of your guess") 
        if self.turn_order[0] == orig_player and self.turn_order[0] != self.user:
            print(f"It seems that {Cards.prefix(response_player)} has whispered some sweet nothings to ")
        elif self.turn_order[0] == self.user:
            print(f"It is time to respond to a guess from {orig_player}")
            print(f"They have guess that Mr. Body was killed:")
            print(f"(Dramatic pause)")
            time.sleep(1)
            print(f"By {char}!")
            time.sleep(2)
            print(f"*audible gasp*")
            time.sleep(1)
            print(f"With the {weapon}")
            time.sleep(2)
            print(f"*audible gasp*")
            time.sleep(1)
            print(f"in the {location}")
            if len(options:=list(filter(lambda x: x in suggestion,self.char().hand)))>0:
                card = menu(list(map(lambda x: Option(x,str(x)),options)))
            else: 
                menu(Option(None,"You have no cards that fulfill this guess"))
        self.turn_order = Cards.rotate(self.turn_order,1)
    def next_turn(self):
        self.turn_order = Cards.rotate(self.turn_order,1)
        if self.turn_order[0] == self.user:
            self.take_turn()
    def my_turn(self):
        return self.turn_order[0] == self.user
