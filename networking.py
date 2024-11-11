from enum import Enum
import socket
import requests
from clue import *
from dataclasses import dataclass
# next create a socket object
from typing import Optional, List
from ui import *
from gamestate import *
 
class network_state(Enum):
    UI_WAIT=0
    HOST_WAIT = 1
    CLIENT_WAIT = 2
    GAME_WAIT = 3
    GAME_SYNC = 4
    
class client(object):
    host_ip:str 
    port = 1492
    gamestate:None|GameState = None
    player_token = None 
    network_state = network_state.HOST_WAIT
    client_socket:socket
    def __init__(self):
        self.client_socket = socket.socket()
        ip = input("IP Address?")
        self.client_socket.connect((ip,1492))
        char_list = self.client_socket.recv(4096)
        characters = str(char_list,encoding='utf-8').split(",")
        (self.player_token,remaining) = select_character(characters)
        self.client_socket.send(bytes(self.player_token,encoding='utf-8'))
        self.client_socket.bind(('',1492)) #wait to hear gamestate.
        self.init_gamestate(self)
        self.network_loop()
    def network_loop(self):
        while len(list(filter(lambda x: not x.lost, self.gamestate.players)))>1:
            match self.network_state:
                case network_state.HOST_WAIT:
                    action = self.client_wait_and_process()
                    self.gamestate.action(action[0],action[1])
            self.network_state = network_state.CLIENT_WAIT

    def init_gamestate(self):
        self.client_socket.connect((self.host_ip,1492))
        data_length = self.client_socket.recv(8)
        data = self.client_socket.recv(data_length)
        action = self.format_data(data)
        self.gamestate = GameState(action[0],action[1],self.player_token)
    def client_wait_and_process(self):
        self.client_socket.connect((self.host_ip,1492))
        data_length = self.client_socket.recv(8)
        data = self.client_socket.recv(data_length)
        action = self.format_data(data)



    def format_data(self,data):
        split1 = data.split("|")
        split2 = split1[2].split(",")
        return ()
    #Schema:
    #NETWORK_MSG_TYPE|Move|Player Location
    #Suggestion|Player Suspect Weapon Location
    #Suggestion Response|From|Orig_Player|Guess|Response_Player|Card Type/None| Card
    #Accusation|Player Suspect Weapon Location
    #EndTurn
    #ACK
    #Init_GameState| Seed | [Player]
    def encode_data(data):
        pass
@dataclass
class ServerPlayerPrimitive(object):
    connection:socket
    address:object
    char: Character
class Server(object):
    clients:List[ServerPlayerPrimitive]
    gamestate: GameState
    port = 1492
    def __init__(self):
        print("Howdy, you're the host!")
        print("Before we go anywhere, we need to select your character!")
        (char,remaining) = select_character(Cards.CharCards)
        s = socket.socket()
        print ("Socket successfully created")
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        # reserve a port on your computer in our
        # case it is 40674 but it can be anything
        print(f"Tell people to connect with \n ip:{ip} \n port:{self.port}")
        s.bind(('', self.port))
        print("socket binded to %s" %(self.port))
        # put the socket into listening mode
        s.listen(6)#We can have a maximum of 6 players in this game.
        print("socket is listening")
        clients = []
        while remaining == []:
            c, addr=s.accept()
            print('Got connection from', addr )
            # send a thank you message to the client.
            #c.send(b'Thank you for connecting')
            c.send(bytes(",".join(map(lambda x: str(x), remaining)),encoding='utf-8'))
            selection = c.recv(4096)
            client_char = Character(str(selection,encoding="utf-8"))
            clients.append((ServerPlayerPrimitive(c,addr,client_char)))
            remaining.remove(client_char)
            c.close()
            print("Continue accepting?")
            if menu([Option(False,"Yes"),Option(True,"No.")]):
                break
        self.initialize_game_state(clients)
    def initialize_game_state(self):
        self.gamestate = GameState(action[0],action[1],self.player_token)
        num_clients = len(self.clients)
        for client in self.clients: #finish mes

            self.client_socket.connect((self.host_ip,1492))
            data_length = self.client_socket.recv(8)
            data = self.client_socket.recv(data_length)
            action = self.format_data(data)
      

