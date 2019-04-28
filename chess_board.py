import numpy as np
import pandas as pd
import random

class ChessBoard:
    """class ChessBoard allows to generate the chess board, we define three functions 
       one constructor initialize board size, one function that we cant get board size
       function getChessBoard return a chess board
    """
    def __init__(self, board_size):
        self.board_size=board_size
    def getChessBoard(self):
        return np.zeros((self.board_size, self.board_size), dtype=int)
    def getBoardSize(self):
        return self.board_size