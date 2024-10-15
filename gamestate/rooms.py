
from enum import Enum 

class RoomEnum(Enum):
    HALL=0
    LOUNGE=1
    DINING_ROOM=2
    KITCHEN=3
    BALLROOM=4
    CONSERVATORY=5
    BILLARD_ROOM=6
    LIBRARY=7
    STUDY=8

class Room(Location):
    room_name:RoomEnum

     