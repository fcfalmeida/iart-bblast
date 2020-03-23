from src.search_algorithm import SearchAlgorithm
from src.game_results import GameResults
import src.utils as utils

# https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
class BFS(SearchAlgorithm):
  @staticmethod
  def execute(game_state, heuristic):
    queue = utils.get_possible_next_states_path(game_state)
    max_touches = game_state.touches_left

    while queue:
      solution = queue.pop(0)
      state, move = solution[-1]

      if state.result == GameResults.Win: return utils.extract_solution(solution)

      next_possible_states = utils.get_possible_next_states(state)

      for next_state in next_possible_states:
        new_solution = list(solution)
        new_solution.append(next_state)
        queue.append(new_solution)
       
    return []
