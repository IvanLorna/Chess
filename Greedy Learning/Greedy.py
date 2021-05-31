import chess
import chess.engine
import numpy as np
from stockfish import Stockfish

class Greedy():
  def __init__(self, isWhite=True, depth=1):
    self.Side = isWhite
    self.depth = depth
    self.stockfish = Stockfish("./stockfish/stockfish")

  def MakeMove(self, board):
    decision = ""
    max = -1000000000
    for move in board.legal_moves:
      TestBoard = chess.Board(board.fen())
      TestBoard.push_uci(str(move))
      if TestBoard.is_checkmate():
        decision = move
        return str(decision)
      else:
        with chess.engine.SimpleEngine.popen_uci('./stockfish/stockfish') as sf:
          result =  sf.analyse(TestBoard, chess.engine.Limit(depth=self.depth))
          if self.Side is True:
            score = result['score'].white().score()
          else:
            score = result['score'].black().score()
        if score is None:
          decision = move
        elif score >= max:
          max = score
          decision = move
    return str(decision)
