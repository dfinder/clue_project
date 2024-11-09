#I handle the
from enum import Enum 
class AckStateMachine(Enum):
    WAIT #I AM WAITING ON THE UI TO UPDATE GAME STATE
    HOST_ACK #I AM WAITING ON THE HOST ACK, BECAUSE IT IS NOT MY TURN OR I AM A PLAYER WHO JUST MADE A TURN
    CLIENT_ACK # I HAVE HEARD FROM THE HOST, I AM WAITING ON THE OTHER CLIENTS
    GAME_ACK #I AM WAITING ON THE GAMESTATE, EVERYONE CAN UPDATE WITH MY COOL NEW MOVE

#So the player is in wait, the other clients are in host ack
#Then when the player makes a move, they go to host_ack, unless they're the host, in which case they goe into client ack
#The host is in client ack, and retransmits to clients, allowing them to move from host ack to client ack.
#The host waits for the clients to respond, then moves everyone into GAME ACK 
#When you get out of game ack, you move into wait if you're the player, host ack if you're the other clients, and client ack if you're the host. 


class NetworkState(object):
    pass