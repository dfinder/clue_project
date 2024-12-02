from dataclasses import dataclass

from typing import TypeVar
TLocation = TypeVar("TLocation", bound="Location")

TStartingLoc = TypeVar("TStartingLoc", bound="StartingLoc")

TLocation = TypeVar("TLocation", bound="Location")

TCard = TypeVar("TCard", bound="Card")
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
        return [Passage("Study","Kitchen",True),
         Passage("Lounge","Conservatory",True),
         Passage("Study","Hall", False),
         Passage("Study","Library", False),
         Passage("Hall","Lounge", False),
         Passage("Hall","Billard", False),
         Passage("Lounge","Dining", False),
         Passage("Dining","Kitchen", False),
         Passage("Dining","Billard", False),
         Passage("Billard","Ball", False),
         Passage("Billard","Library", False),
         Passage("Library","Conservatory",False),
         Passage("Ball","Conservatory",False),
         Passage("Ball","Kitchen",False)]
    def get_adjacent(self)->list[TLocation]:
        pass

@dataclass
class Passage(Location):
    start: Location
    end: Location
    secret: bool
    def get_adjacent(self):
        return [self.start,self.end]
    def __repr__(self):
        return f"Passage from {self.start} to {self.end}"
    def __eq__(self, value):
        return isinstance(value,Passage) and self.start == value.start and self.end == value.end
    def network_repr(self):
        return f"{self.start}-{self.end}"
    def network_unrepr(passage):
        elems = passage.split("-")
        return Passage(elems[0],elems[1],False)
class Room(Card,Location):
    def get_class(self)->str:
        return "Room"
    def match_passage(self,passage:Passage)->Location|None:
        match passage:
            case Passage(self.name,end,True): return Room(end)
            case Passage(self.name,end,False): return passage 
            case Passage(start,self.name,True): return Room(start)
            case Passage(start,self.name,False): return passage 
            case _: return None
    def get_adjacent(self):
        return list(filter(lambda x: x!=None,map(self.match_passage(),Location.get_adjacency())))
    def __eq__(self, value):
        return self.name == value.name
class Weapon(Card):
    def get_class(self)->str:
        return "Weapon"
class Character(Card):
    def get_class(self)->str:
        return "Character"
@dataclass
class StartingLoc(Location):
    piece:Character
    passage:Passage
    def get_starts()->list[TStartingLoc]:
           return [StartingLoc(Character("Scarlet"),Passage("Hall","Lounge",False)),
            StartingLoc(Character("Mustard"), Passage("Dining","Lounge",False)),
            StartingLoc(Character("White"),Passage("Ball","Kitchen",False)),
            StartingLoc(Character("Green"),Passage("Ball","Conservatory",False)),
            StartingLoc(Character("Plum"),Passage("Study","Library",False)),
            StartingLoc(Character("Peacock"),Passage("Library","Conservatory",False))]
    def get_adjacent(self)->list[Location]:
            return [self.passage]
    def __repr__(self):
        return str(self.piece)+" Starting Location"

def shuffle(deck:list[Card],seed:int)->list[Card]:
    if len(deck)==0:
        return deck
    seed = ((seed+3)**2) % len(deck)
    return [deck.pop()]+shuffle(deck[:seed]+deck[seed:],seed)
class Cards:
    seed=40
    @staticmethod
    def CharCards():
        return list(map(Character,["Plum","Mustard","Green","Scarlet","White","Peacock"]))
    @staticmethod
    def WeaponCards():
        return list(map(Weapon,["Candlestick","Dagger","Pipe","Revolver","Rope","Wench"]))
    WeaponMurderActions = lambda x: "He was murdered by being"+[
        "bashed over the head",
        "stabbed in the gut",
        "struck in the chest",
        "shot in the heart",
        "strangled",
        "beaten"
    ][Cards.WeaponCards.index(Weapon(x))]+" with the ["+x+"]!"
    @staticmethod
    def RoomCards():
        return list(map(Room,["Kitchen","Ball","Conservatory","Billard","Library","Study","Dining","Hall","Lounge"]))
    RoomIsRoom = lambda x: x+ ["","room",""," Room","",""," Room","",""][Cards.RoomCards.index(Room(x))]
    prefix = lambda x: Cards.namePrefixMap[str(x)]+" "+x
    namePrefixMap = {"Plum":"Prof.","Mustard":"Col.","Green":"Rev.","Scarlet":"Ms.","White":"Mrs.","Peacock":"Mrs."}
    @staticmethod
    def shuffle(remaining:list[Card],seed:int)->list[Card]:
        if len(remaining)==1:
            return remaining
        return Cards.shuffle(remaining=Cards.rotate(remaining[1:],((seed+1)**2)%len(remaining[1:])),seed=((seed+1)**2)%len(remaining[1:]))+[remaining[0]]
    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]
    @staticmethod
    def selectWinCon()->tuple[tuple[Character,Weapon,Room],list[Card]]:
        characters =Cards.shuffle(remaining=Cards.CharCards(),seed=Cards.seed)
        weapons = Cards.shuffle(Cards.WeaponCards(),Cards.seed)
        rooms = Cards.shuffle(Cards.RoomCards(),Cards.seed)
        return ((characters.pop(),weapons.pop(),rooms.pop()),Cards.shuffle(([]+characters+weapons+rooms),seed=Cards.seed))
    @staticmethod
    def deal(remaining:list[Card],hand_count:int)->list[list[Card]]:
        hands = []
        for i in range(hand_count):
            hands.append([])
        while len(remaining)!=0:
            #print(len(remaining))
            #print(range(hand_count))
            for i in range(hand_count):
                if len(remaining)>0:
                    hands[i].append(remaining.pop())
        return hands
