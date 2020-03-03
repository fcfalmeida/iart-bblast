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

# Prints the board matrix on the console
def print_matrix(matrix):
  for i in range(len(matrix)):
    print('\n')
    for j in range(len(matrix[i])):
      print('[', matrix[i][j], ']', end='')

  print('\n')

# Given a board matrix, checks if the bubbles with the given
# coordinates are adjacent or not
#
# Two bubbles are adjacent if they are on the same row or column
# and if there are only empty bubbles between them
def are_adjacent(matrix, row1, col1, row2, col2):
  if not (row1 == row2 or col1 == col2):
    return False

  if row1 == row2 and col1 == col2:
    return False

  #if matrix[row1][col1].type == BubbleTypes.Empty or matrix[row2][col2].type == BubbleTypes.Empty:
  #  return False

  if row1 == row2:
    col_indexes = []

    if col2 > col1:
      col_indexes = range(col1 + 1, col2)
    else:
      col_indexes = range(col2 + 1, col1)

    for col in col_indexes:
      if matrix[row1][col].type != BubbleTypes.Empty:
        return False

  if col1 == col2:
    row_indexes = []
    
    if row2 > row1:
      row_indexes = range(row1 + 1, row2)
    else:
      row_indexes = range(row2 + 1, row1)

    for row in row_indexes:
      if matrix[row][col1].type != BubbleTypes.Empty:
        return False

  return True

def num_matrix_to_bubble_matrix(num_matrix):
  bubble_matrix = []

  for i in range(len(num_matrix)):
    aux = []

    for j in range(len(num_matrix[i])):
      aux.append(Bubble(BubbleTypes(num_matrix[i][j])))

    bubble_matrix.append(aux)

  return bubble_matrix

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
