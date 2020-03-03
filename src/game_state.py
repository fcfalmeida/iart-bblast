from src.game_results import GameResults
from src.bubble_types import BubbleTypes
import src.utils as utils
from copy import deepcopy

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
    print(utils.print_matrix(matrix))
    touched_bubble = matrix[touch_row][touch_col]

    if touched_bubble.type == BubbleTypes.Empty:
      return matrix

    touched_bubble.decrement_hp()
    matrix[touch_row][touch_col] = touched_bubble

    # if bubble has been destroyed
    if touched_bubble.type == BubbleTypes.Empty:
      # we search for all adjacent bubbles
      for row in range(len(matrix)):
        for col in range(len(matrix[row])):
          if utils.are_adjacent(matrix, touch_row, touch_col, row, col):
            # if an adjacent bubble is red, then recursively call the function on it
            if matrix[row][col].type == BubbleTypes.Red:
              matrix = self.__update_matrix(matrix, row, col)
            else:
              # this line may try to decrease the HP of an empty bubble but it does nothing
              # since HP can't go below 0
              matrix[row][col].decrement_hp()
          
    return matrix

