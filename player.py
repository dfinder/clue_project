from gamepieces import Character, Card,StartingLoc,Location
class Player(object):
    hand: list[Card]
    piece: Character
    location: Location 
    telported: bool 
    lost: bool 
    active: bool
    def __init__(self,char:Character,is_playing=True):
        self.hand = [] 
        self.piece = char
        self.knowledge = []
        print("STARTING LOC:"+str(list(filter(lambda x: x.piece==char,StartingLoc.get_starts()))[0]))
        self.location = list(filter(lambda x: x.piece==char,StartingLoc.get_starts()))[0]
        self.teleported = False 
        self.lost = not is_playing
        self.is_playing = is_playing
    