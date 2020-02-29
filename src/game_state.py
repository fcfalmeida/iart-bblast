from src.game_results import GameResults
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