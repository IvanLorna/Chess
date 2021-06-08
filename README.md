# Chess
CS228 deep learning final project
games.csv is the dataset for the initial training
dataload.py will load the data from the Games into Board states and reactions
Model.py Takes the data from dataload.py and creates the initial models in Folder White Weights and Folder Black Weights
Environment.py is a class that holds the Game information and allows different agents to interact with the board
Agent.py will create a White or Black agent as specified, it will update and store those weights in a folder called RWhite Weights or RBlack Weights
Minmax.py utilizes stockfish lookahead of depth of 3 and chooses the best move
Greedy.py utilizes stockfish lookahead of depth of 1 and chooses the best move
stkfish.py utilizes stockfish's best move function of a given board state and chooses that best move
Player.py Allows the User to interact with the Environment
stockfish folder contains the stockfish engine used
Models folder contains images of all the different models
Adversarial Learning folder contains the learned Weights from playing against itself for 100 games
Minmax Learning folder contains the learned Weights from playing against the Minmax AI for 100 games
Greedy Learning folder contains the learned Weights from playing against the Greedy AI for 100 games
Stockfish Learning folder contains the learned Weights from playing against the Stockfish AI for 100 games
ChessDemo_Environment allows the User to play in an environment in a python notebook
