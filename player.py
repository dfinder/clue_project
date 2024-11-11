import gamestate
from gamestate import Character, StartingLoc, Weapon,Location
class Player(object):
    hand: list[gamestate.Card]
    piece: list[gamestate.Character]
    location: gamestate.Location 
    telported: bool 
    lost: bool 
    is_player: bool
    def __init__(self,char:Character,is_playing=True):
        self.hand = [] 
        self.piece = char
        self.knowledge = []
        self.location = list(filter(lambda x: x.piece==char,StartingLoc.get_starts()))[0]
        self.teleported = False 
        self.lost = not is_playing
        self.is_playing = is_playing
    def move(self,location):
        self.location = location 
    def teleport(self,location):
        self.location = location 
        self.telported = True 
    def guess(self, weapon:Weapon, target:Location):
        return (self,weapon,target,self.location)
    def accuse(self,weapon,target,location):
        pass
    