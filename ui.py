import gamestate
from gamepieces import Character,Cards,Passage,Room,Location,Card
from player import Player
from typing import Optional, List
from dataclasses import dataclass
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
    while not (response:=input("?")).isnumeric() and response>=len(options):
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
class UserInterface(object):
    turn_action_set:list[tuple[callable,str]]
    gs:gamestate.GameState
    player:Player
    def __init__(self,gs):
        self.turn_action_set=[]
        self.gs = gs
        self.player = self.gs.player()
        actions = []
        if gs.suggestion_round:
            self.turn_action_set.append((self.guess_response,"Respond to a guess!"))
        elif not self.player.lost:
            print(self.player.location)
            hallway_limit = lambda x: not (isinstance(x, Passage) and any(map(lambda y: x==y.location, self.gs.players)))
            locations = list(filter(hallway_limit, self.player.location.get_adjacent()))
            if len(locations)!=0:
                actions.append((self.move,"Move your piece"))
            self.turn_action_set.append((self.move,"Move your piece"))
                
            if isinstance(self.player.location,Room):
                actions.append((self.suggestion,"Make a suggestion")) #This is a guess AND move

            actions.append((self.accuse,"Make an accusation"))
        else:
            print("You've been a very naughty player, devoured by the rats!")
            actions.append(self.end_turn,"End Turn")
    def move(self):
        hallway_limit = lambda x: not (isinstance(x, Passage) and any(map(lambda y: x==y.location, self.gs.players)))
        locations = filter(hallway_limit, self.player.location.get_adjacent())
        target = menu(list(map(lambda x: Option(x,("Move to "+str(x))),locations)))
        return ("MOVE",(self.player.piece,target))
    def end_turn(self):
        return ("END TURN")
    def main_menu(self):#->tuple[callable,list[object]]:
        actions = []
        actions.extend(self.turn_action_set)
        actions.append((self.check_map,"Check Map"))
        actions.append((self.check_knowledge,"Check Knowledge"))
        actions.append((self.roll_die,"Roll Die"))
        while (ret:=(menu(list(map(lambda x:Option(x[0],x[1]),actions))))()) == None:
            pass 
        print(ret)
        match ret[0]:
            case "MOVE":
                self.turn_action_set.remove((self.move,"Move your piece"))
                if self.player.teleported and not isinstance(ret[1][1],Room): #If you've teleported,moved, and you're not in a room, you can't suggest
                    self.turn_action_set.remove(self.suggestion)
                if not self.player.teleported and isinstance(ret[1][1],Room): #If you've not telported and you've moved, you can suggest now
                    self.turn_action_set.add(self.suggestion)
            case "SUGG": #If you've made a suggestion,
                self.turn_action_set.remove((self.suggestion,"Make a suggestion")) #If you've suggested, you cannot suggest again
                try:
                    self.turn_action_set.remove((self.move,"Move your piece")) #If you've suggested, that ends your turn.
                finally:
                    pass
        return ret 
    
    def suggestion(self):
        print("Select a character:")
        accused = menu(list(map(lambda x: Option(x,Cards.prefix(str(x)),f"You have selected: {Cards.prefix(str(x))}"),Cards.CharCards)))
        print("Select a weapon:")
        weapon = menu(list(map(lambda x: Option(x,x,f"You have selected: {Cards.prefix(x)}"),Cards.WeaponCards)))
        return ("SUGG",(self.player,accused,weapon))
    def accuse(self):
        print("Select a character:")
        accused = menu(list(map(lambda x: Option(x,Cards.prefix(str(x)),f"You have selected: {Cards.prefix(str(x))}"),Cards.CharCards)))
        print("Select a weapon:")
        weapon = menu(list(map(lambda x: Option(x,x,f"You have selected: {Cards.prefix(x)}"),Cards.WeaponCards)))
        print("Select a location:")
        location = menu(list(map(lambda x: Option(x,x,f"You have selected: {x}"),Cards.RoomCards)))
        return ("ACCUSE",(self.player.piece,accused,weapon,location))
    
    def suggestion_response(self):
        print(f"To recap:")
        print(f"{self.gs.current_suggestion[0]} has made the following suggestion:")
        print(f"The tretcherous [{self.gs.current_suggestion[1]}] brutally murdered Mr. Body!")
        print(Cards.WeaponMurderActions(self.gs.current_suggestion[2]))
        print(f"This happened in the comfort of Mr. Body's own {self.gs.current_suggestion[3]}")
        valid_responses = filter(lambda x: x in self.gs.current_suggestion[1:3],self.player.hand)
        if len(valid_responses)==0:
            menu(Option("Pass"))
        card:Card = menu(lambda x: Option(x,str(x)), valid_responses)
        return ("SUGG RESP",(self.player.piece,card,card.get_class()))
    def check_map(self):
        for i in self.gs.players:
            print(f"{i.piece}:{i.location}")
        return (None)
    def check_knowledge(self):
        for i in self.player.knowledge:
            print(i)
        return (None) 
    def roll_die(self):
        print("YOU DIDN'T NEED TO DO THAT!")
        return (None)