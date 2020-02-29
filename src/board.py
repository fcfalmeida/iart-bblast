from src.bubble import Bubble
from src.bubble_types import BubbleTypes
import src.utils as utils

BOARD_WIDTH = 5
BOARD_HEIGHT = 6

class Board:

  def __init__(self):
    self.board = utils.create_empty_board(BOARD_HEIGHT, BOARD_WIDTH)
