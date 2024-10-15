class AbstractController(Object):
    pass 
class ControllerController(Object):
    #This controller sets up and coordinates with all the other controllers, and passes the gamestate to them.
    ui_controller: UIController
    network_controller: NetworkController 
    gs_controller: GameStatecontroller
    #....
    #You get the idea
    def __init__(self,networking):
        #Set up controllers for basic systems, like UI, Networking

        pass 

    def ui_event(self,UIEvent):
        #What happens when we get a UI event from the UI Controller? 
        #Pass it to the gamestate to figure out what it's context is
        pass 
    def network_event(self,NetworkEvent):
        pass 
        #What happens when we get a network event?
        #We update the gamestate
    def gamestate_event(self,GameStateEvent):
        pass 
        #What happens when we get a gamestate event? 
        #Like finishing a turn. Like actually finishing the turn, not just pressing the finish turn button, after we've recorded everything. 
        #We alert everyone!