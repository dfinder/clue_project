from player import Player
from gamestate import GameState
from suggestion import Suggestion

class Turn:
    def __init__(self, game_state: GameState):
        self.game_state = game_state  # The current game state
        self.current_player: Player = None  # The player whose turn it is
        self.is_turn_active = False  # Flag to track if the turn is active
        self.is_accusation_made = False  # Flag to check if the player made an accusation
    
    def start_turn(self, player: Player):
        """
        Start the turn for the specified player.
        """
        self.current_player = player
        self.is_turn_active = True
        self.is_accusation_made = False
        print(f"Player {player.PlayerID}'s turn has started.")
        
    def make_suggestion(self, character, location, weapon):
        """
        Allow the current player to make a suggestion.
        """
        if not self.is_turn_active:
            print("No active turn. Cannot make a suggestion.")
            return
        
        suggestion = Suggestion(character, location, weapon)
        self.current_player.make_suggestion(suggestion)
        print(f"Player {self.current_player.PlayerID} made a suggestion: {suggestion}")
    
    def make_accusation(self, character, location, weapon):
        """
        Allow the current player to make an accusation.
        """
        if not self.is_turn_active:
            print("No active turn. Cannot make an accusation.")
            return
        
        accusation_result = self.game_state.check_accusation(character, location, weapon)
        if accusation_result:
            print(f"Player {self.current_player.PlayerID} made a correct accusation!")
            self.end_game(winner=self.current_player)
        else:
            print(f"Player {self.current_player.PlayerID} made an incorrect accusation.")
            self.current_player.AccusationState = True  # Flag that the player has accused incorrectly
            self.end_turn()

    def end_turn(self):
        """
        End the current player's turn and move to the next player.
        """
        if not self.is_turn_active:
            print("Turn is already inactive.")
            return
        
        print(f"Player {self.current_player.PlayerID}'s turn has ended.")
        self.is_turn_active = False
        self.next_player_turn()

    def next_player_turn(self):
        """
        Transition to the next player's turn in the turn order.
        """
        current_turn_order = self.current_player.TurnOrder
        next_player = None

        # Find the next player by turn order
        for player in self.game_state.player_list:
            if player.TurnOrder == current_turn_order + 1:
                next_player = player
                break
        
        # If we reach the last player, loop back to the first player
        if not next_player:
            next_player = self.game_state.player_list[0]
        
        # Start the next player's turn
        self.start_turn(next_player)
        
    def as_json(self):
        """
        Serialize the Turn object to JSON format.
        """
        return {
            "current_player": self.current_player.PlayerID if self.current_player else None,
            "is_turn_active": self.is_turn_active,
            "is_accusation_made": self.is_accusation_made
        }
    
    def as_log(self):
        """
        Generate a log for the current turn.
        """
        log = f"Turn Status: {'Active' if self.is_turn_active else 'Inactive'}"
        log += f"\nCurrent Player: {self.current_player.PlayerID if self.current_player else 'None'}"
        log += f"\nAccusation Made: {self.is_accusation_made}"
        return log
