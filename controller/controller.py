from messages import messages
class AbstractController(object):
    pass 

def UIActionMessage(Message):
    Button_Clicked = None 

    #Types: 
    #Button push
def NetworkBroadcastMessage(Message):
    
def NetworkUpdateMessage(Message):

def GameStateUpdateMessage(Message):

def GameStateRetrievalMessage(Message):

def UIUpdateMessage(Message):
    pass 
class game_phase(Enum):
    NOT_TURN=()
    MAKING_GUESS:(Character,)

    

class ControllerController(object):
    #This controller sets up and coordinates with all the other controllers, and passes the gamestate to them.
    ui_controller= UIController
    network_controller= NetworkController 
    gs_controller= GameStateController
    game_phase = game_phase
    def __init__(self,networking):
        #Set up controllers for basic systems, like UI, Networking

        pass
    def ui_event(self,UIActionMessage):
        #Unwrap UI

    def ui_update(self,UIUpdateMeessage):
        
        pass
    def network_broadcast(self,NetworkBroadcastMessage):
        pass
    def network_event(self,NetworkUpdateEvent):
        pass 
        #What happens when we get a network event?
        #We update the gamestate
    def gamestate_event(self,GameStateEvent):
        pass 
        #What happens when we get a gamestate event? 
        #Like finishing a turn. Like actually finishing the turn, not just pressing the finish turn button, after we've recorded everything. 
        #We alert everyone!