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
    def __init__(self, room_name: RoomEnum):
        self.room_name = room_name  # Store the room enum
        self.name = room_name.name.replace("_", " ").title()

    def __repr__(self):
        # print the room 
        return f"Room: {self.name}"


     