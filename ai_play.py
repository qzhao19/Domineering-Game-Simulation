import numpy as np
from chess_board import ChessBoard
from playout import Playout
from cnn_model import CNN
from data_generator import ProcessCsvData



class AI:
    def __init__(self, cnn):
        self.cnn=cnn
    
    def CnnVsMonteCarlo(self, nb_iter):
        """player 0 => play game using CNN
           player 1 => play game using random method

        """
        moves=[]
        winner=[]
        print('The number of iteration is %s' %(str(nb_iter)))
        for i in range(nb_iter):
            print(str(i) + " iterations is done")
            player=0
            board=ChessBoard(8).getChessBoard()
            list_best_move=[]
            while len(Playout().getPossibleMove(board, player))>0:
                # make sure which player
                # CNN player
                if player==0:
                    X=np.concatenate((board, 1-board, np.zeros((8,8), dtype=int)+player), axis=0).reshape(1,3,8,8)
                    y=self.cnn.predict(X).reshape(64)
                    # y=y_predict
                    is_finished=False
                                        
                    max_value=-1
                    counter=0
                    while is_finished==False & counter<64:
                        counter+=1
                        for i in range(64):
                            if y[i]>max_value:
                                max_value=y[i]
                                move=i
                        if move in Playout().getPossibleMove(board, player):
                            list_best_move.append(move)
                            board=Playout().play(board, move, player)
                            player=1-player
                            is_finished=True
                        else:
                            y[move]=0
                            max_value=-1
                elif player==1:
                    possible_moves=Playout().getPossibleMove(board, player)
                    
                    list_mean_playout=[]
                    list_move=[]
                    
                    for i in range(len(possible_moves)):
                        copy_board=np.copy(board)
                        copy_board=Playout().play(copy_board, possible_moves[i], player)
                        list_mean_playout.append(Playout().getMeanOfPlayout(copy_board, 1-player, 10))
                        list_move.append(possible_moves[i])
                    
                    best_playout=-1
                    for i in range(len(list_mean_playout)):
                        if list_mean_playout[i]>best_playout:
                            best_playout=list_mean_playout[i]
                            best_move=list_move[i]
                    
                    list_best_move.append(best_move)
                    board=Playout().play(board, best_move, player)
                    player=1-player

            moves.append(list_best_move)
            winner.append(1-player)
            
        return moves, winner
    def output(self, winners):
        cpt1=0
        cpt2=0
        nb_ite=50
        for a in winners:
            if a==0:
                cpt1+=1
            elif a==1:
                cpt2+=1
        print(str(nb_ite) + ' round, player 0 wins ' + 
              str(cpt1) + ' times,  player 1 wins ' + 
              str(cpt2) + ' times.')

        
        