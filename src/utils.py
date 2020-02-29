from src.bubble import Bubble
from src.bubble_types import BubbleTypes

# Creates a board with the specified height and width (cells)
# and fills it with empty bubbles
def create_empty_board(height, width):
  board = []

  for i in range (0, height):
    aux = []
    for j in range (0, width):
      aux.append(Bubble(BubbleTypes.Empty))
    board.append(aux)

  return board

# Prints the board on the console
def print_board(board):
  for i in range(len(board)):
    print('\n')
    for j in range(len(board[i])):
      print('[', board[i][j], ']', end='')

  print('\n')