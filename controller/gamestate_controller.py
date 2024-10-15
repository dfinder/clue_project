
class GameStateController(object):
    accusation_controller: AccusationController
    suggestion_controller: SuggestionController 
    move_controller: MovementControlller
    location_controller: LocationController 
    gamestate: Gamestate
    def __init__(self):
        #Initialize 