from src.heuristic import Heuristic

class TotalSum(Heuristic):
  @staticmethod
  def calculate(game_state):
    return game_state.score