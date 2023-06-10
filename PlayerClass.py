#
# A Connect Four Player class
#

from BoardClass import Board

class Player:
    """ a data type to represent a player of the Connect Four game
    """ 
    def __init__(self, checker):
        """ constructs a new Player object by initializing checker & num_moves
        """
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a str representing a Player object
        """
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """ returns one-char str representing the chekcer of the
            Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """ returns the col where the player wants to make the next move
            method should ask the user to enter a col # 
            asks repeatedly for a valid col #
            increment the num of moves that the Player object has made
            input: Board object b
        """
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                break
            print('Try again!')
            print()
        
        self.num_moves += 1
        return col
        