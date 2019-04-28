import numpy as np
import pandas as pd
import random
from playout import Playout



class PlayDomineeringGame:
    def __init__(self):
        pass
    
    def playGame(self, board, init_player, nb_iter=10):
        """
        """
        list_best_moves=[]
        player=init_player
        is_continue=False
        possible_moves=Playout().getPossibleMove(board, player)
        
        #if the game don't finish, we assigne to is_continue
        if len(possible_moves)>0:
            is_continue=True
        
        #we begin loop
        while is_continue==True:
            print(len(possible_moves))
            # define a list containing average of playout
            # a list containing all possible move 
            list_mean_playout=[]
            list_moves=[]
            
            # we traversal list containing all of possible moves
            for i in range(len(possible_moves)):
                # copy a board as current board
                # play game using every possible move with current board 
                # create a list containing all of mean of playout be played by every possible move
                # a list involve the move related 
                cur_board=np.copy(board)
                cur_board=Playout().play(cur_board,possible_moves[i],player)
                list_mean_playout.append(Playout().getMeanOfPlayout(cur_board,1-player,nb_iter))
                list_moves.append(possible_moves[i])
            
            
            # make sure the player is 0 or 1
            if player==1:
                best_playout=1
                for i in range(len(list_mean_playout)):
                    if list_mean_playout[i]<best_playout:
                        best_playout=list_mean_playout[i]
                        best_move=list_moves[i]
                        
            elif player==0:
                best_playout=-1
                for i in range(len(list_mean_playout)):
                    if list_mean_playout[i]>best_playout:
                        best_playout=list_mean_playout[i]
                        best_move=list_moves[i]
                        
            list_best_moves.append(best_move)          
            print(best_move)
            print(player)
            print('')

            
            board=Playout().play(board,best_move,player)
            player=1-player
            possible_moves=Playout().getPossibleMove(board, player)
            if len(possible_moves)==0:
                is_continue=False
                
        return 1-player, list_best_moves
    
    def outputGame(self, board, player, list_best_moves):
        cur_board=np.copy(board)
        print(cur_board)
        for best_move in list_best_moves:
            print(best_move)
            cur_board=Playout().play(cur_board, best_move, player)
            print(cur_board)
            print('')
            player=1-player
        
