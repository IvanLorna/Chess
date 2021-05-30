from IPython.display import clear_output

class Player():
  def __init__(self, isWhite = True):
    self.isWhite = isWhite
    self.name = input("Please Enter Player Name: ")
    pass
  
  def MakeMove(self,board):
    clear_output()
    moveMade = False
    while moveMade is False:
      moves = 'Legal Moves to make:'
      for i in board.legal_moves:
        moves  = moves + ' ' + str(i)
      print(board)
      print(moves)
      Move = chess.Move.from_uci(input("please Enter a Legal Move: "))
      if Move in board.legal_moves:
        moveMade = True
      else:
        print('"'+ str(Move) + '" is not a legal move.' )
    return Move
    
