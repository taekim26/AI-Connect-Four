#
# A Connect Four Board class
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        """ constructs a new Board object by initializing an attribute height,
            width, and slots
            (reference to a 2-D list with height rows & width colums)
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         
        for row in range(self.height):
            s += '|'   

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  

        s += '-' * (self.width * 2 + 1)
        s += '\n'
        s += ' '
        for i in range(self.width):
            if i < 10:
                s += str(i) + ' ' 
            else:
                s += str(i % 10) + ' '
            
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row = self.height - 1
        
        while self.slots[row][col] != ' ':
            if row == 0:
                break
            row -= 1
            
        self.slots[row][col] = checker

    def reset(self):
        """ resets the Board object by setting all slots
            to contain a space char
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] != ' ':
                    self.slots[row][col] = ' '    

    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def test():
        b = Board(6, 7)
        print(b)
    
    def can_add_to(self, col):
        """ returns, True if it's valid to place a checker in the column col
            returns False, otherwise
        """
        if 0 <= col < self.width:
            count = 0
            for row in range(self.height):
                if self.slots[row][col] != ' ':
                    count += 1
            if count == self.height:
                return False
            else:
                return True
        else:
            return False
    
    def is_full(self):
        """ returns True, if the called Board object is completely full
            returns False, otherwise
        """
        count = 0
        dimension = self.height * self.width
        
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] != ' ':
                    count += 1        
        if count == dimension:
            return True
        else:
            return False
        
    def remove_checker(self, col):
        """ removes the top checker from column col of the Board object
            if the column is empty, then the method do nothing
        """
        row = 0
        count = 0
        
        for r in range(self.height):
            if self.slots[r][col] == ' ':
                count += 1
        if count != self.height:
            while self.slots[row][col] == ' ':
                row += 1
                if row == self.height:
                    break
                
            self.slots[row][col] = ' '

    def is_horizontal_win(self, checker):
        """ checks for a horizontal win for the specified checker
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True
                   
        return False
    
    def is_vertical_win(self, checker):
        """ checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                       return True
                   
        return False
    
    def is_down_diagonal_win(self, checker):
        """ checks for a down diagonal win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                       return True
                   
        return False

    def is_up_diagonal_win(self, checker):
        """ checks for an up diagonal win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row + 3][col] == checker and \
                   self.slots[row + 2][col + 1] == checker and \
                   self.slots[row + 1][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True
                   
        return False
    
    def is_win_for(self, checker):
        """ returns True, if there are four consecutive slots containing 
            checker on the board
            returns False, otherwise
        """
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
               return True
        else:
            return False
