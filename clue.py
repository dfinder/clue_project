<<<<<<< HEAD
from dataclasses import dataclass
from functools import partial
=======
from enum import Enum
>>>>>>> b181545 (adding more content)
import socket
import requests
from clue import *
from dataclasses import dataclass
# next create a socket object
from typing import Optional, List
from ui import *
from gamestate import *
from networking import client,server
menu([Option(client,"Client"),Option(server,"Server")])()