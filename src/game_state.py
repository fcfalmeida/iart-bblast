from src.game_results import GameResults
from src.bubble_types import BubbleTypes
import src.utils as utils
import math
from copy import deepcopy

class GameState:

  def __init__(self, board, touches_left):
    self.board = board
    self.touches_left = touches_left
    self.score = 0
    self.result = None

  # receives a move and updates the board, score and touches left accordingly
  def update_board(self, touch_row, touch_col):
    if self.board.matrix[touch_row][touch_col].type == BubbleTypes.Empty:
      return

    old_matrix = deepcopy(self.board.matrix)
    new_matrix = self.__update_matrix(self.board.matrix, touch_row, touch_col)
    self.board.matrix = new_matrix

    self.__calculate_score(old_matrix)
    self.__decrement_touches()

  def __update_matrix(self, matrix, touch_row, touch_col):
    touched_bubble = matrix[touch_row][touch_col]

    if touched_bubble.type == BubbleTypes.Empty:
      return matrix

    touched_bubble.decrement_hp()
    matrix[touch_row][touch_col] = touched_bubble

    # if bubble has been destroyed
    if touched_bubble.type == BubbleTypes.Empty:
      # check each direction for adjacent bubbles and recursively call the function
      # on red ones
      matrix = self.__check_left(matrix, touch_row, touch_col)
      matrix = self.__check_up(matrix, touch_row, touch_col)
      matrix = self.__check_right(matrix, touch_row, touch_col)
      matrix = self.__check_down(matrix, touch_row, touch_col)
          
    return matrix

  def __check_right(self, matrix, touch_row, touch_col):
    if touch_col == len(matrix[touch_row]) - 1: return matrix

    queue = []

    for col in range(touch_col + 1, len(matrix[touch_row])):
      if utils.are_adjacent(matrix, touch_row, touch_col, touch_row, col):
        if matrix[touch_row][col].type == BubbleTypes.Red:
          queue.append([touch_row, col])   
        else:
          matrix[touch_row][col].decrement_hp()

    for pos in queue:
      row = pos[0]
      col = pos[1]
      matrix = self.__update_matrix(matrix, row, col)

    return matrix

  def __check_left(self, matrix, touch_row, touch_col):
    if touch_col == 0: return matrix

    queue = []    

    for col in reversed(range(0, touch_col)):
      if utils.are_adjacent(matrix, touch_row, touch_col, touch_row, col):
        if matrix[touch_row][col].type == BubbleTypes.Red:
          queue.append([touch_row, col])
        else:
          matrix[touch_row][col].decrement_hp()

    for pos in queue:
      row = pos[0]
      col = pos[1]
      matrix = self.__update_matrix(matrix, row, col)

    return matrix

  def __check_up(self, matrix, touch_row, touch_col):
    if touch_row == 0: return matrix

    queue = []

    for row in reversed(range(0, touch_row)):
      if utils.are_adjacent(matrix, touch_row, touch_col, row, touch_col):
        if matrix[row][touch_col].type == BubbleTypes.Red:
          queue.append([row, touch_col])
        else:
          matrix[row][touch_col].decrement_hp()

    for pos in queue:
      row = pos[0]
      col = pos[1]
      matrix = self.__update_matrix(matrix, row, col)

    return matrix

  def __check_down(self, matrix, touch_row, touch_col):
    if touch_row == len(matrix) - 1: return matrix

    queue = []

    for row in range(touch_row, len(matrix)):
      if utils.are_adjacent(matrix, touch_row, touch_col, row, touch_col):
        if matrix[row][touch_col].type == BubbleTypes.Red:
          queue.append([row, touch_col])
        else:
          matrix[row][touch_col].decrement_hp()

    for pos in queue:
      row = pos[0]
      col = pos[1]
      matrix = self.__update_matrix(matrix, row, col)

    return matrix

  # decrements the number of touches left in the game
  #
  # if touches_left reaches 0 and the board is empty, then the game result is set as Win
  # if touches_left reaches 0 and the board is not empty, then the game result is set as Lose
  def __decrement_touches(self):
    if self.touches_left > 0:
      self.touches_left -= 1

    self.__check_result()

  def __calculate_score(self, old_matrix):
    old_num_empty = utils.count_empty_bubbles(old_matrix)
    new_num_empty = utils.count_empty_bubbles(self.board.matrix)

    # number of bubbles destroyed in one move
    delta = new_num_empty - old_num_empty

    # avoid domain error in log function
    if delta == 0: return delta

    self.score += int(delta * 10 + math.log(delta))

  def __check_result(self):
    if self.touches_left == 0:
      if self.board.is_empty():
        self.result = GameResults.Win
      elif self.board.is_empty and self.touches_left == 0:
        self.result = GameResults.Lose