from src.bubble import Bubble
from src.bubble_types import BubbleTypes

# Creates a board with the specified height and width (cells)
# and fills it with empty bubbles
# Returns a matrix instead of a Board object
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
  for i in range(len(board.matrix)):
    print('\n')
    for j in range(len(board.matrix[i])):
      print('[', board.matrix[i][j], ']', end='')

  print('\n')

# Reads the given level file and returns a matrix representation of the board
def read_level_file(file):
  board = []

  f = open(file, 'r')
  lines = f.readlines()

  for line in lines:
    lineArr = line.split()
    aux = []

    for num in lineArr:
      aux.append(Bubble(BubbleTypes(int(num))))
    
    board.append(aux)

  return board
