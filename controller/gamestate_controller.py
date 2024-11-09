
class GameStateController(object):
    accusation_controller: AccusationController
    suggestion_controller: SuggestionController 
    move_controller: MovementControlller
    location_controller: LocationController 
    gamestate: Gamestate
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
    def move(self,location):
        self.location = location 
    def teleport(self,location):
        self.location = location 
        self.telported = True 
    def accuse( )