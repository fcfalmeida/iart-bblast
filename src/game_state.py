from src.game_results import GameResults
from src.bubble_types import BubbleTypes
import src.utils as utils

class GameState:
  
  def __init__(self, board, touches_left):
    self.board = board
    self.touches_left = touches_left
    self.score = 0
    self.result = None

  # sets the board for the game state
  def set_board(self, board):
    self.board = board

  # increases the current score
  def increase_score(self, amount):
    self.score += amount

  # decrements the number of touches left in the game
  #
  # if touches_left reaches 0 and the board is empty, then the game result is set as Win
  # if touches_left reaches 0 and the board is not empty, then the gam result is set as Lose
  def decrement_touches(self):
    if self.touches_left > 0:
      self.touches_left -= 1

    if self.touches_left == 0:
      if utils.is_board_empty(board):
        self.result = GameResults.Win
      else:
        self.result = GameResults.Lose

  def update_board(self, touch_row, touch_col):
    new_matrix = self.__update_matrix(self.board.matrix, touch_row, touch_col)
    self.board.matrix = new_matrix

  def __update_matrix(self, matrix, touch_row, touch_col):
    touched_bubble = matrix[touch_row][touch_col]

    if touched_bubble.type == BubbleTypes.Empty:
      return

    touched_bubble.decrement_hp()
    matrix[touch_row][touch_col] = touched_bubble

    if touched_bubble.type == BubbleTypes.Empty:
      # check bubbles on same column
      for row in range(len(matrix)):
        #if matrix[row][touch_col].type == BubbleTypes.Red:
          if utils.are_adjacent(matrix, touch_row, touch_col, row, touch_col):
            self.__update_matrix(matrix, row, touch_col)

      # check bubbles on same row
      for col in range(len(matrix[touch_row])):
        #if matrix[touch_row][col].type == BubbleTypes.Red:
          if utils.are_adjacent(matrix, touch_row, touch_col, touch_row, col):
            self.__update_matrix(matrix, touch_row, col)

    return matrix

