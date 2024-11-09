from enum import Enum
from gamestate import GameStateObject
class Location(GameStateObject):
    def __init__(self, location_name:str, adjacency:list):
        self.location_name = location_name
        self.adjacency = []
    def get_players_at(self):
        pass
    def adjacenency_list(self): 
        pass 
class LocationAdjacency():
    def __init__(self, start_room: Location, end_room: Location):
        '''
        Initializes class for location adjacency map
        Args: 
            start_room: Location Class. Initializes the starting room of the location
            end_room: Location Class. Initializes the ending room of the location. 
        Returns:
            None
        '''
        self.start_room = start_room
        self.end_room = end_room


class Hallway(Location):
   def __init__(self, start_room: Location, end_room: Location):
        '''
        Initializes class for Hallway
        Args: 
            start_room: Location Class. Initializes the starting room of the hallway
            end_room: Location Class. Initializes the ending room of the hallway 
        Returns:
            None
        '''
        self.start_room = start_room
        self.end_room = end_room
