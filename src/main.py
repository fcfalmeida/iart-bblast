import src.utils as utils
from src.board import Board
from src.bubble_types import BubbleTypes
from src.bubble import Bubble
from src.game_state import GameState
from copy import deepcopy

#board = utils.read_level_file('lvl1')
#utils.print_board(Board(board))

curr_board = Board([
  [2,4,4,1,1], 
  [2,2,2,0,4], 
  [0,4,2,2,2], 
  [1,1,1,3,1],
  [1,4,0,1,4],
  [4,0,3,2,0]
])

matrix = utils.num_matrix_to_bubble_matrix([
  [1,0,2]
])

matrix2 = matrix
matrix2[0][0] = 2
print(matrix[0][0])

bubble = Bubble(BubbleTypes.Blue)
matrix[0][0] = bubble
print(matrix[0][0])
bubble.decrement_hp()
print(matrix[0][0])

game_state = GameState(curr_board, 2)
game_state.update_board(3, 2)