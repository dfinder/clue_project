from enum import Enum
import socket
from dataclasses import dataclass
# next create a socket object
from ui import menu, Option
from gamestate import *
from networking import Client,Server
print("Welcome to Clue-Less! Select 0 if you are joining a game and 1 if you are hosting a game")
menu([Option(Client,"Client"),Option(Server,"Server")])()