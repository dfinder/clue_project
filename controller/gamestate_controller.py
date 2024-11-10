

class GameStateController(object):
    def __init__(self):
        pass 
        #Initialize the gamestate
        #Initialize the controllers, giving them access to the game state.
class Player(object):
    def __init__(self):
        self.hand = [] 
        self.piece = None 
        self.knowledge = [] 
        self.location = None 
        self.teleported = False 
        self.lost = False 
        self.is_playing = False
    def move(self,location):
        self.location = location 
    def teleport(self,location):
        self.location = location 
        self.telported = True 
    def guess(self, weapon, target):
        return (self,weapon,target,self.location)
    def accuse(self,weapon,target,location)
class GameState(object):
    players = [player]
     
