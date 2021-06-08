import chess
import chess.engine
import numpy as np
from stockfish import Stockfish

class Stkfish():
  def __init__(self, isWhite= True):
    self.Side = isWhite
    self.stockfish = Stockfish("/content/stockfish/stockfish")

  def MakeMove(self, board):
    self.stockfish.set_fen_position(board.fen())
    return str(self.stockfish.get_best_move())