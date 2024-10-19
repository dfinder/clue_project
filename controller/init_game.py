class GameInitializer(Object):
    def __init__(self,controller_controller):
        pass 

    def choose_character(): 
        #allows player to choose a character. A random character is suggested
        #for the player if the player does not choose a character within
        #the allotted amount of time. 
        pass  
    
    def host_init(self, player_mapping:List[(int,Character)]):
        pass
    
    def distribute_cards(self):
        #distributes cards to players
        pass 
    def place_pieces(self):
        pass
    #Note that game initialization occurs somewhat differently for client and host. 
    #The client will copy the hosts initialization while waiting for the main screen to pop up.
    