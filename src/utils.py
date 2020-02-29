from src.bubble import Bubble
from src.bubble_types import BubbleTypes

# checks wether all bubbles have been cleared from the board or not
#
# the board is considered empty if all elements equal 0
def is_board_empty(board):
  is_empty = True

  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i] != BubbleTypes.Empty:
        is_empty = False

  return is_empty

def create_empty_board(height, width):
  board = []

  for i in range (0, height):
    aux = []
    for j in range (0, width):
      aux.append(Bubble(BubbleTypes.Empty))
    board.append(aux)

  return board

def print_board(board):
  for i in range(len(board)):
    print('\n')
    for j in range(len(board[i])):
      print('[', board[i][j], ']', end='')

  print('\n')