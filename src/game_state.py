from src.game_results import GameResults
import src.utils as utils

class GameState:
  
  def __init__(self, board, touches_left):
    self.board = board
    self.touches_left = touches_left
    self.score = 0
    self.result = None

  def set_board(self, board):
    self.board = board

  def increase_score(self, amount):
    self.score += amount

  def decrement_touches(self):
    if self.touches_left > 0:
      self.touches_left -= 1

    if self.touches_left == 0:
      if utils.is_board_empty(board):
        self.result = GameResults.Win
      else:
        self.result = GameResults.Lose