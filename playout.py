import numpy as np
import pandas as pd
import random

class Playout:
    def __init__(self):
        pass
    def getPossibleMove(self, board, init_player):
        """player=0 => vertical
           player=1 => horizontal
           parameter: chees boar and player
           return a list containing all possible moves' coordinates
        """
        moves=[]
        if init_player==1:
            for i in range(board.shape[0]):
                for j in range(board.shape[1]):
                    if board[i][j]==0:
                        try:
                            if board[i][j+1]==0:
                                moves.append(i*8+j)
                        except:
                            error=0
        elif init_player==0:
            for i in range(board.shape[0]):
                for j in range(board.shape[1]):
                    if board[i][j]==0:
                        try:
                            if board[i+1][j]==0:
                                moves.append(i*8+j)
                        except:
                            error=0
        return moves 
    
    def play(self, board, move, init_player):
        """parameter: chess board, one move, player
           we define move as 8*i+j, so we have to get i and j 
           i=move//8: get guotient
           j=move%8: get remainder
           return: move shown at board
        """
        i=move//8
        j=move%8
        board[i,j]+=1
        # we fixe up the move direction, which means the player move from left to right
        # if vertical to play, from up to down 
        # if player is 1 => horizontal, player is 0 => vertical
        if init_player==1:
            # horizontal: axis y increment 
            board[i,j+1]+=1
        elif init_player==0:
            # vertical: axis x increment
            board[i+1,j]+=1
        return board
    
    def playout(self, board, init_player):
        """
        
        """
        cur_board=np.copy(board)
        is_continue=False
        cur_player=init_player
        possible_move=self.getPossibleMove(cur_board, cur_player)
        # define a variable to determining if the game is finished
        if len(possible_move)>0:
            is_continue=True
        # here, we initialize is_finished = true
        while is_continue:
            # get a random index between 0 and length of move list 
            index=random.randint(0, len(possible_move)-1)
            # get random move  
            random_move=possible_move[index]
            # we get current board that was palyed by random move 
            cur_board=self.play(cur_board, random_move, cur_player)
            # if current player is 0, the next player is 1 
            # if not, the next one is 0
            # so we get tne next player by 1-cur_player
            cur_player=1-cur_player
            # we refresh all possible moves 
            possible_move=self.getPossibleMove(cur_board, cur_player)
            if len(possible_move)==0:
                is_continue=False
        # to getting the average of playtou, on define 1-cur_player
        return 1-cur_player
    
    def getMeanOfPlayout(self, board, init_player, nb_iter):
        """param: chessboard, starting player, number of iteration
           return the average of playout
        """
        return np.array([[self.playout(board, init_player) for i in range(nb_iter)]]).mean()
 