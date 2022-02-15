# Chess AI
Utilizing Tensorflow and Stockfish, we train a Chess AI specific to Black and White through use of neural networks on a dataset of past games. We then apply reinforcement learning methods to improve its performance against Greedy, Minmax, Stockfish AI, and against itself. We discussed which color learns better against different opponents, the rate of learning against multiple difficulties and why that may be the case. We use a consensus of 15 unique deep learning models and utilize Stockfish’s evaluation on the best move and on different moves.  <br />

## Project Report
[project_report.pdf](https://drive.google.com/file/d/1EcXG61i0WE7jQFex4QPA6nCSXAizljgR/view?usp=sharing)

## File Index
**games.csv** is the dataset for the initial training  
**dataload.py** will load the data from the Games into Board states and reactions  
**Model.py** Takes the data from dataload.py and creates the initial models in Folder White Weights and Folder Black Weights  
**Environment.py** is a class that holds the Game information and allows different agents to interact with the board  
**Agent.py** will create a White or Black agent as specified, it will update and store those weights in a folder called RWhite Weights or RBlack Weights  
**Minmax.py** utilizes stockfish lookahead of depth of 3 and chooses the best move  
**Greedy.py** utilizes stockfish lookahead of depth of 1 and chooses the best move  
**stkfish.py** utilizes stockfish's best move function of a given board state and chooses that best move  
**Player.py** Allows the User to interact with the Environment  
**stockfish** folder contains the stockfish engine used  
**Models folder** contains images of all the different models  
**Adversarial Learning** folder contains the learned Weights from playing against itself for 100 games  
**Minmax Learning** folder contains the learned Weights from playing against the Minmax AI for 100 games  
**Greedy Learning** folder contains the learned Weights from playing against the Greedy AI for 100 games  
**Stockfish Learning** folder contains the learned Weights from playing against the Stockfish AI for 100 games  
**ChessDemo** allows the User to play in an environment in a python notebook
