from player import Player
import ui
import time
from gamepieces import *
class GameState(object):
    players : list[Player]
    win_con: tuple[Weapon, Character, Room] # type: ignore
    turn_order: list[Character]
    user: Character 
    log: list[str]
    current_suggestion: tuple[Character,Character,Weapon,Room]|None
    suggestion_fulfilled = False
    suggestion_round=False
    def __init__(self,seed,active:list[Character],char:Character):
        print(list(map(lambda x: type(x),active)))
        self.user = char
        self.turn_order = active 
        self.players = [Player(piece,piece in active) for piece in Cards.CharCards()]
        self.win_con,deck = Cards.selectWinCon()
        
        hands = Cards.deal(deck,len(active))
        #print(list(map(lambda x: x.piece,self.players)))
        for idx,i in enumerate(active):
            self.player(i).hand=hands[idx]
            self.player(i).knowledge=hands[idx]
        print(f"{type(self.user)}")
        print(f"Your hand of cards is {self.player().hand}")
        print(f"The host will go first.")
    def player(self,char=None)->Player:
        if char == None:
            return list(filter(lambda x: x.piece == self.user, self.players))[0]
        #print(list(map(lambda x: x.piece==char,self.players)))
        #print(char==Character(char))
        return list(filter(lambda x: x.piece == char, self.players))[0]
    def suggestion(self,player,suspect,weapon): #Synced event.
        self.suggestion_round = True
        self.current_suggestion = (player,suspect,weapon,player.location)
        self.player(suspect).location = player.location
        print(f"The honorable {Cards.namePrefixMap(player)} has made a suggestion!") 
        print(f"The suspect, {Cards.namePrefixMap(suspect)}. has been summoned to the alleged murder site, {player.location}.")
        print(f"The suspect, {Cards.namePrefixMap(suspect)}, has been accused of murdering Mr. Body with the {weapon}.")
        self.player(suspect).teleported = True
    def move(self,player,location):
        print(f"{player} has moved to {location}")
        self.player(player).location=location
    def accusation(self,player,suspect,weapon,location):
        print(f"{Cards.namePrefixMap(player)} has guessed that Mr. Body was killed:")
        print(f"(Dramatic pause)")
        time.sleep(1)
        print(f"By {suspect}!")
        time.sleep(2)
        print(f"*audible gasp*")
        time.sleep(1)
        print(f"With the {weapon}")
        time.sleep(2)
        print(f"*audible gasp*")
        time.sleep(1)
        print(f"in the {location}")
        print(f"(an audience member faints)")
        print(f"They will open up the envelope of destiny, and either be destroyed or reign triumphant")
        time.sleep(1)
        ##should consider having this as its own seperate function?
        if (suspect,weapon,location)==self.wincon:
            for i in filter(lambda x: x!=player,self.players):
                i.lost=True
            print(f"{player} was correct! Good Game Everyone!")
            quit()
        else:
            self.player(player).lost=True
            print(f"{player} was incorrect! Rats emerge from the walls and devour {player} alive!")

    def suggestion_response(self,response_player,card,card_type): #This fulfils the guess
        #Suggestion is the original contents of the action
        #Response player is who gives you the card
        if card != None:
            type_mapping = {"Room":Room,"Weapon":Weapon,"Character":Character}
            if self.current_suggestion[0]==self.user:
                print(f"{response_player} has whispered to you that {card} was not involved in the murder of Mr. Body")
            else:
                print(f"It seems {response_player} has whispered to {self.current_suggestion[0]} something concerning the murder of Mr. Body")
            self.suggestion_fulfilled=True
            self.player(self.current_suggestion[0]).knowledge.append(type_mapping[card_type](card))
        else:
            if self.current_suggestion[0]!=self.user:
                print(f"It seems that {response_player} had nothing to say concerning the murder of Mr. Body")
    def end_turn(self):
        self.turn_order = Cards.rotate(self.turn_order,1)
    def my_turn(self):
        return self.turn_order[0] == self.user
    def apply_action(self,action,*args):
        return action(self,*args)
    def show_ui(self):
        return self.UInter.main_menu()
    def start_turn(self):
        if self.suggestion_fulfilled:
            if self.gs.suggestion[0] != self.player():
                print("Someone has already made a response! You don't need to reveal anything")
                return ("SUGG RESP",(self.gs.user,"None","None"))
            else:
                self.gs.suggestion_round=False
        self.UInter=ui.UserInterface(self)