from src.bubble import Bubble
from src.bubble_types import BubbleTypes
import src.utils as utils

BOARD_WIDTH = 5
BOARD_HEIGHT = 6

class Board:

  def __init__(self):
    self.board = utils.create_empty_board(BOARD_HEIGHT, BOARD_WIDTH)

  # checks wether all bubbles have been cleared from the board or not
  #
  # the board is considered empty if all elements are an empty bubble
  def is_empty(self):
    is_empty = True

    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j].type != BubbleTypes.Empty:
          is_empty = False

    return is_empty
