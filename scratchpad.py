import socket
import requests
from clue import *
from dataclasses import dataclass
# next create a socket object
from typing import Optional, List
@dataclass
class Option(object):
    result:object
    label:str
    response: Optional[str]=None
    def __repr__(self):
        self.label
def menu(options:list[Option])->object:
    for idx,option in enumerate(options):
        print(f"{idx}:{option.label}")
    while not (response:=input("?")).isnumeric():
        print(f"Please input x∈[0,{len(options)-1}]") 
        for idx,option in enumerate(options):
            print(f"{idx}:{option.label}")
    option = options[int(response)]
    (option.response is None) or print(option.response)
    return options[int(response)].result


def select_character(characters:List[Character])->tuple[Character,list[Character]]:
    print("SELECT A CHARACTER:")
    character_options = list(map(lambda x: Option(x,Cards.prefix(str(x)),f"You have selected: {Cards.prefix(str(x))}"),characters))
    my_character:Character = menu(character_options)
    print(my_character)
    characters.remove(my_character)
    print((my_character,characters))
    return (my_character,characters)

def client():
    s = socket.socket()
    ip = input("IP Address?")
    #port = int(input("Port?"))
    #s.bind(('',1493))
    s.connect((ip,1492))
    char_list = s.recv(4096)
    characters = str(char_list,encoding='utf-8').split(",")
    (my_character,remaining) = select_character(characters)
    s.send(bytes(my_character,encoding='utf-8'))
    
    s.bind(('',1492))
 
def server():
    print("Howdy, you're the host!")
    print("Before we go anywhere, we need to select your character!")
    (char,remaining) = select_character(Cards.CharCards)
    s = socket.socket()
    print ("Socket successfully created")

    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    # reserve a port on your computer in our
    # case it is 40674 but it can be anything
    port = 1492
    print(f"Tell people to connect with \n ip:{ip} \n port:{port}")
    s.bind(('', port))
    print ("socket binded to %s" %(port))

    # put the socket into listening mode
    s.listen(6)#We can have a maximum of 6 players in this game.
    print ("socket is listening")
    clients = []
    while True:

        # Establish connection with client.

        c, addr=s.accept()
        print('Got connection from', addr )

        # send a thank you message to the client.
        #c.send(b'Thank you for connecting')
        c.send(bytes(",".join(map(lambda x: str(x), remaining)),encoding='utf-8'))
        selection = c.recv(4096)
        clients.append((ServerPlayerPrimitive(c,addr,Character(str(selection,encoding="utf-8")))))
        c.close()

        # Close the connection with the client
@dataclass
class ServerPlayerPrimitive(object):
    connection:socket
    address:object
    char:Character

menu([Option(client,"Client"),Option(server,"Server")])()