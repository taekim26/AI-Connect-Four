#
# Playing the game 
#   

from BoardClass import Board
from PlayerClass import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """ perform all of the steps involved in processing a single move
        by player p on board b
        input: Player object p and Board object b
    """
    print(str(p) + """'s turn""") 
    print()
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    
    if b.is_win_for(p.checker) == True:
        print(str(p) + ' wins in ' + str(p.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print('Its a tie!')
        return True
    else:
        return False

class RandomPlayer(Player):
    """ a sub-class of a class Player """
    def next_move(self, b):
        """ returns the index of the randomly selected column 
            chosen randomly from the cols in the board b that aren't full yet
        """
        ind_list = range(b.width)
        possible_inds = []
        
        for ind in ind_list:
            if b.can_add_to(ind) == True:
                possible_inds += [ind]
        
        self.num_moves += 1
        return random.choice(possible_inds)
