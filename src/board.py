from src.bubble import Bubble
from src.bubble_types import BubbleTypes
import src.utils as utils

BOARD_WIDTH = 5
BOARD_HEIGHT = 6

class Board:

  def __init__(self, matrix = None):
    if matrix is None:
      self.matrix = utils.create_empty_board(BOARD_HEIGHT, BOARD_WIDTH)
    else:
      self.matrix = self.__map_matrix(matrix)

  # checks wether all bubbles have been cleared from the board or not
  #
  # the board is considered empty if all elements are an empty bubble
  def is_empty(self):
    is_empty = True

    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        if self.matrix[i][j].type != BubbleTypes.Empty:
          is_empty = False

    return is_empty

  # private utility function to make it possible for the constructor to receive
  # either a Bubble or int matrix
  def __map_matrix(self, matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if (not isinstance(matrix[i][j], Bubble)):
          matrix[i][j] = Bubble(BubbleTypes(int(matrix[i][j])))

    return matrix

  def __eq__(self, other):
    if not isinstance(other, Board):
      return False

    return self.matrix == other.matrix