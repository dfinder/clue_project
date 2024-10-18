from enum import Enum

class Notes_Controller:

    suspects = {}
    weapons = {}
    rooms = {}

    class Suspects(Enum):
        COL_MUSTARD = "Col. Mustard"
        PROF_PLUM = "Prof. Plum"
        MR_GREEN = "Mr. Green"
        MRS_PEACOCK = "Mrs. Peacock"
        MISS_SCARLET = "Miss Scarlet"
        MRS_WHITE = "Mrs. White"
    
    class Weapons(Enum):
        KNIFE = "Knife"
        CANDLESTICK = "Candlestick"
        REVOLVER = "Revolver"
        ROPE = "Rope"
        LEAD_PIPE = "Lead Pipe"
        WRENCH = "Wrench"
    
    class Rooms(Enum):
        HALL = "Hall"
        LOUNGE = "Lounge"
        DINING_ROOM = "Dining Room"
        KITCHEN = "Kitchen"
        BALL_ROOM = "Ball Room"
        CONSERVATORY = "Conservatory"
        BILLIARD_ROOM = "Billiard Room"
        LIBRARY = "Library"
        STUDY = "Study"

    def __init__(self):
        self.reset()
    
    def reset(self):
        self.suspects[self.Suspects.COL_MUSTARD] = False
        self.suspects[self.Suspects.PROF_PLUM] = False
        self.suspects[self.Suspects.MR_GREEN] = False
        self.suspects[self.Suspects.MRS_PEACOCK] = False
        self.suspects[self.Suspects.MISS_SCARLET] = False
        self.suspects[self.Suspects.MRS_WHITE] = False

        self.weapons[self.Weapons.KNIFE] = False
        self.weapons[self.Weapons.CANDLESTICK] = False
        self.weapons[self.Weapons.REVOLVER] = False
        self.weapons[self.Weapons.ROPE] = False
        self.weapons[self.Weapons.LEAD_PIPE] = False
        self.weapons[self.Weapons.WRENCH] = False

        self.rooms[self.Rooms.HALL] = False
        self.rooms[self.Rooms.LOUNGE] = False
        self.rooms[self.Rooms.DINING_ROOM] = False
        self.rooms[self.Rooms.KITCHEN] = False
        self.rooms[self.Rooms.BALL_ROOM] = False
        self.rooms[self.Rooms.CONSERVATORY] = False
        self.rooms[self.Rooms.BILLIARD_ROOM] = False
        self.rooms[self.Rooms.LIBRARY] = False
        self.rooms[self.Rooms.STUDY] = False
    
    def crossOffSuspect(self, suspect):
        self.suspects[suspect] = True

    def crossOffWeapon(self, weapon):
        self.weapons[weapon] = True
    
    def crossOffRoom(self, room):
        self.rooms[room] = True
    
    def isSuspectCrossedOff(self, suspect):
        return self.suspects[suspect]
    
    def isWeaponCrossedOff(self, weapon):
        return self.weapons[weapon]
    
    def isRoomCrossedOff(self, room):
        return self.rooms[room]

