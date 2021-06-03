from IPython.display import clear_output
import chess

class Player():
  def __init__(self, isWhite = True):
    self.isWhite = isWhite
    pass
  
  def MakeMove(self,board):
    moveMade = False
    while moveMade is False:
      moves = '\nLegal Moves to make:'
      for i in board.legal_moves:
        moves  = moves + ' ' + str(i)
      print(board)
      print(moves)
      Move = input("please Enter a Legal Move: ")
      if chess.Move.from_uci(Move) in board.legal_moves:
        moveMade = True
      else:
        print('"'+ str(Move) + '" is not a legal move.' )
    clear_output()
    return Move
    
