from enum import Enum
import time
import builtins as __builtin__
class ControllerController(object):
    def __init__(self):
        print("Howdy, I'm the controller controller, I act as a go between for everyone! Spooky!")

        self.network_controller= NetworkController()
        self.ui_controller = UIController()
        self.gamestate_controller = GameStateController()
        self.turn = True
    def main_function(self):
        while True:
            if self.turn:
                self.ui_controller.UI()
                ui_message = self.ui_controller.process_input()
                network_response = self.network_controller.process_networking(ui_message)
                game_state_response = self.gamestate_controller.process_action(network_response)
                self.network_controller.process_networking_sync()
                self.ui_controller.update_ui(game_state_response)
            else: 
                network_response = self.network_controller.wait_networking()
                self.network_controller.process_networking_sync()
                game_state_response = self.gamestate_controller.process_action(network_response)
                self.ui_controller.update_ui(game_state_response)
class NetworkController(object):
    class network_state(Enum):
        UI_WAIT=1 #Wait on the UI
        HOST_WAIT=2 #Wait on the host
        CLIENT_WAIT=3 #Wait on the clients to response that they've synched
        GAME_WAIT=4 #Wait on the game state to sync
        READY_WAIT=5 

    class networking_message(Enum):
        pass
    def __init__(self):
        print("Howdy I'm the network controller, I manage the connections between host/client, and syncing game state")
        self.network_state=self.network_state.UI_WAIT

    def wait_networking(self):
        pass
    def process_networking(self,message)->str:
        print("Howdy I am the Network Controller!")
        print(f"I definitely don't work yet.")
        print(f"\n If I did work, I'd be replicating this message:{message} to everyone along the following steps:")
        print(f"1. Tell the host(ms. white) that am DOING A THING, by using a PLAYER_SYN message.")
        print(" I move from waiting on the UI(UI_WAIT) to waiting on the the host(HOST_WAIT)")
        print(f"2. Wait for her to tell everyone including me about this cool thing({message}) that I'm doing")
        print(f"When she tells everyone(HOST_ACK), she moves from HOST_WAIT to CLIENT_WAIT")
        print("When she tells me about the cool thing I told her I'm doing, I don't complain.")
        print("I just move to CLIENT_WAIT too, and tell her CLIENT_ACK, change my game state.")
        input()
        return message
    def process_networking_sync(self):
        print("Here we just wait for everyone to confirm that they've synched before everyone updates UI")
        print("We move to GAME_WAIT, then the host broadcasts GAME_SYNC until everyone returns READY_SYN")
        print("Then the host replies NEXT ACTION, and we enter UI ")

    
class GameStateController(object): 
    def __init__(self):
        print("Howdy, I'm the game state controller")
        print("I'm supposed to be managing the game state")
    def process_action(self,message)->str:
        print(f"Howdy, I'm the Gamestate controller, and I'm processing with {message}")
        print("I have moved Scarlett to the Library Billards Hallway")
        input()
        return "Scarlett@Library|Billards"
    def update_game_state(self,update):
        print(f"Howdy, I am the GameState Controller, I am updating with {update}")
class UIController(object):
    def __init__(self):
        print("Howdy, I'm the UI controller.")
        self.state=False
    def UI(self):
        if not self.state:
            print("Howdy, I'm the UI, printing itself")
            print("You are MISS SCARLET ")
            print("You are in the LIBRARY")
            print("Pofessor Plum is in the KITCHEN")
            print("Ms White is between the STUDY and the HALL")
            print("Mr Green is in the CONSERVATORY")
            print("Ms. Peacock is at PEACOCK_START")
            print("Col. Mustard is at MUSTARD_START")
        if self.state: 
            print("Howdy, I'm the UI, printing itself")
            print("You are MISS SCARLET")
            print("You are in between the BILLARDS and the LIBRARY")
            print("Pofessor Plum is in the KITCHEN")
            print("Ms White is between the STUDY and the HALL")
            print("Mr Green is in the CONSERVATORY")
            print("Ms. Peacock is at PEACOCK_START")
            print("Col. Mustard is at MUSTARD_START")
            #exit()
    def process_input(self): 
        print("Howdy, I'm processing the input, and I'd like to return the new state")
        print("Where would you like to go?")
        print("LIBRARY-BILLARDS hallway[0]")
        print("LIBRARY-KITCHEN hallway[1]")
        print("LIBRARY-CONSERVATORY hallway[2]")
        print("?")
        ret_value = input()
        self.state=True
        return "MOVE[LIBRARY->LIBRARY|BILLARDS]"

    def update_ui(self,message):

        print(f"Howdy, I'm updating the UI to indicate {message}")


def print(s:str):
    time.sleep(1)
    __builtin__.print(s)

my_controller = ControllerController()
my_controller.main_function()