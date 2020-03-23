from src.heuristic import Heuristic

class Score(Heuristic):
  @staticmethod
  def calculate(game_state):
    return game_state.score