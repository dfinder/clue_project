from enum import Enum
import socket
from dataclasses import dataclass
# next create a socket object
from ui import menu, Option
from gamestate import *
from networking import Client,Server
menu([Option(Client,"Client"),Option(Server,"Server")])()