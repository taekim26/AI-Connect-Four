#
# AI Player for use in Connect Four  
#

import random  
from PlayGame import *

class AIPlayer(Player):
    """ a sub-class of a class Player """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or \
               tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ overrides & returns a str representing an AIPlayer object
        """
        s = super().__repr__()
        s += ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        """ returns the index of the col with the max score
            if one or more cols are tied for the max score,
            the method should apply the classed AIPlayer's tiebraking strategy
            input: list scores (scores for each col of the board)
        """
        max_cols = []
        max_score = max(scores)
        
        for i in range(len(scores)):
            if max_score == scores[i]:
                max_cols += [i]
        
        if self.tiebreak == 'LEFT':
            return max_cols[0]
        elif self.tiebreak == 'RIGHT':
            return max_cols[-1]
        else:
            return random.choice(max_cols)
        
    def scores_for(self, b):
        """ returns a list containing one score for each col
            by determining the called AIPlayer's scores for the cols in b
            input: Board object b
        """
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker() \
                                    , self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                else:
                    scores[col] = 50
                b.remove_checker(col)
                
        return scores
    
    def next_move(self, b):
        """ returns the called AIPlayer's judgment of its best possible move
            overrides the next_move moethod in superclass Player
        """
        scores = self.scores_for(b)
        ind = self.max_score_column(scores)
        
        self.num_moves += 1
        
        return ind
        