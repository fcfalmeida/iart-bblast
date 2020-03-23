from src.heuristic import Heuristic
import src.utils as utils

class BubblesLeft(Heuristic):
  @staticmethod
  def calculate(game_state):
    return utils.count_empty_bubbles(game_state.board.matrix)