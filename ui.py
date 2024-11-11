from gamestate import *
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