from enum import Enum
import socket
import requests
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
    READY_WAIT = 4
    
class Client(object):
    host_ip:str 
    port = 1492
    gamestate:None|GameState = None
    player_token = None 
    network_state = network_state.HOST_WAIT
    client_socket:socket
    def __init__(self):
        self.client_socket = socket.socket()
        #ip = input("IP Address?")
        ip="127.0.0.1"
        self.client_socket.connect((ip,1492))
        char_list = self.client_socket.recv(4096)
        characters = str(char_list,encoding='utf-8').split(",")
        print("Please select your character")
        print("If you do not see a character, that's because the character has been selected by another player.")
        (self.player_token,_) = select_character(characters)
        self.client_socket.send(bytes(self.player_token,encoding='utf-8'))
        print("Waiting on other players to join")
        self.init_gamestate()
        self.network_loop()
    def network_loop(self):
        while len(list(filter(lambda x: not x.lost, self.gamestate.players)))>1:
            match self.network_state:
                case network_state.UI_WAIT:
                    self.server_transmit(self.gamestate.show_ui())
                    self.network_state=network_state.HOST_WAIT
                case network_state.HOST_WAIT:
                    action = self.client_wait_and_process()
                    self.network_state = network_state.CLIENT_WAIT
                case network_state.CLIENT_WAIT:
                    self.server_transmit("ACK")
                    self.network_state = network_state.GAME_WAIT
                    self.gamestate.apply_action(action[0],action[1])
                case network_state.GAME_WAIT:
                    self.client_wait_and_process()
                    self.network_state=network_state.READY_WAIT
                case network_state.READY_WAIT:
                    if self.gamestate.my_turn():
                        self.client_wait_and_process()
                        self.network_state=network_state.UI_WAIT
                    else:
                        self.server_transmit("ACK")
                        self.network_state=network_state.HOST_WAIT


    def init_gamestate(self):
        #self.client_socket.connect((self.host_ip,1492))
 
        #data_length = int(str(self.client_socket.recv(4),encoding='utf-8'))
        data = self.client_socket.recv(4096)
        print(data)
        action = self.decode_msg(data)
        print(action)
        self.gamestate = GameState(action[0],action[1],Character(self.player_token))
        self.server_transmit("ACK")
    
    def client_wait_and_process(self):
        #self.client_socket.connect((self.host_ip,1492))
        data = self.client_socket.recv(4096)
        return self.decode_msg(data)

    def decode_msg(self,data):

        data_str = str(data,encoding="utf-8")
        partition = data_str.split("|")
        print(partition)
        args = partition[1].split(",")
        match partition[0]:
            case "SUGG":
                return(GameState.suggestion,args)
            case "SUGG RESP":
                return(GameState.suggestion_response,args)
            case "ACCUSE":
                return(GameState.accusation,args)
            case "END TURN":
                return(GameState.end_turn,())
            case "MOVE":
                return(GameState.move,args)
            case "ACK":
                return "ACK"
            case "INIT":
                return(args[0],list(map(lambda x: Character(x),args[1:])))
    #Schema:
    #Move|Player Location
    #Suggestion|Player Suspect Weapon Location
    #Suggestion Response|Player Card Card Type
    #Accusation|Player Suspect Weapon Location
    #EndTurn
    #ACK
    #Init_GameState| Seed | [Player]
    def server_transmit(self,data):
        encoded = self.encode_data(data)
        self.client_socket.sendall(encoded)
    def encode_data(self,data):
        return bytes("|".join([data[0],",".join(map(lambda x: str(x),data[1]))]),encoding='utf-8')
       
        return(msg,length)
@dataclass
class ServerPlayerPrimitive(object):
    connection:socket
    address:object
    char: Character
class Server(object):
    clients:List[ServerPlayerPrimitive]
    gamestate: GameState
    port = 1492
    token = None
    network_state = network_state.UI_WAIT
    def __init__(self):
        print("Howdy, you're the host!. That means players will join your game.")
        print("Before we go anywhere, we need to select your character!")
        (self.token,remaining) = select_character(Cards.CharCards())
        s = socket.socket()
        print ("Socket successfully created")
        # reserve a port on your computer in our
        # case it is 40674 but it can be anything
       
        

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', self.port))
        print("socket binded to %s" %(self.port))
        # put the socket into listening mode
        s.listen(5)#We can have a maximum of 6 players in this game.
        print("socket is listening")
        players_that_can_join = 5
        print("The other players can now join the game.")
        print ("Waiting for players. Up to " + str(players_that_can_join) + " more people can join.")
        self.clients = []
        while remaining != []:
            c, addr=s.accept()
            print('Got connection from', addr )
            players_that_can_join -= 1
            # send a thank you message to the client.
            #c.send(b'Thank you for connecting')
            c.sendall(bytes(",".join(map(lambda x: str(x), remaining)),encoding='utf-8'))
            selection = c.recv(4096)
            client_char = Character(str(selection,encoding="utf-8"))
            self.clients.append((ServerPlayerPrimitive(c,addr,client_char)))
            remaining.remove(client_char)
            #c.close()
            if players_that_can_join == 0:
                print("The maximum number of players have joined! Time to start")
                break
            print("Continue accepting players? Up to " + str(players_that_can_join) + " more people can join.")
            if menu([Option(False,"Yes"),Option(True,"No")]):
                break
        self.initialize_game_state()
        self.gamestate.start_turn()
        self.network_loop()
    def initialize_game_state(self):
        init_args = (40,list(map(lambda x: x.char, self.clients))+[self.token],self.token)
        #print(init_args), #We don't need to print this it's not useful for the user
        self.gamestate = GameState(*init_args)
        encoded = [str(40)]+list(map(lambda x: str(x),init_args[1]))
        self.clients_transmit(["INIT",encoded])
    def clients_transmit(self,msg):
        print(self.clients)
        for client_conn in self.clients: #finish me
            print(msg)
            encoded = "|".join([msg[0],",".join(map(lambda x: str(x),msg[1]))])
            client_conn.connection.sendall(bytes(encoded,encoding='utf-8'))
    def ready_syn(self):
          for client_conn in filter(lambda x: x.char != self.gamestate.turn_order[0],self.clients):
              result=client_conn.connection.recv(4096)
              assert(result=="ACK")
    def clients_wait(self):
          for client_conn in self.clients: 
              result = client_conn.connection.recv(4096)
              assert(result=="ACK")
    def player_wait(self):
        player_conn:ServerPlayerPrimitive = filter(lambda x: x.char == self.gamestate.turn_order[0],self.clients)[0]
        data = player_conn.recv(4096)
        return self.decode_msg(data)
    def network_loop(self):
        while len(list(filter(lambda x: not x.lost, self.gamestate.players)))>1:
            match self.network_state:
                case network_state.UI_WAIT:
                    action = self.gamestate.show_ui()
                    self.clients_transmit(action)
                    self.network_state = network_state.CLIENT_WAIT
                case network_state.HOST_WAIT:
                    action = self.player_wait()
                    self.clients_transmit(action)
                    self.network_state=network_state.CLIENT_WAIT
                case network_state.CLIENT_WAIT:
                    self.clients_wait()
                    self.network_state = network_state.GAME_WAIT
                case network_state.GAME_WAIT:
                    self.gamestate.apply_action(action[0],action[1])
                    self.clients_transmit("ACK") #GAME SYNC
                case network_state.READY_WAIT:
                    if self.gamestate.my_turn():
                        self.clients_wait()
                        self.network_state=network_state.UI_WAIT
                    else:
                        self.ready_syn()
                        self.network_state=network_state.HOST_WAIT

    def decode_msg(self,data):
        data_str = str(data,encoding="utf-8")
        partition = data_str.split("|")
        print(partition)
        args = partition[1].split(",")
        match partition[0]:
            case "SUGG":
                return(GameState.suggestion,args)
            case "SUGG RESP":
                return(GameState.suggestion_response,args)
            case "ACCUSE":
                return(GameState.accusation,args)
            case "END TURN":
                return(GameState.end_turn,())
            case "MOVE":
                return(GameState.move,args)
            case "ACK":
                return "ACK"
            case "INIT":
                return(args[0],args[1].split(","))