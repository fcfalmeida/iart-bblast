from src.search_algorithm import SearchAlgorithm
from src.game_results import GameResults
import src.utils as utils
import sys

class Greedy(SearchAlgorithm):
  @staticmethod
  def execute(game_state, heuristic):
    sys.setrecursionlimit(10**6) 

    solution = Greedy.recursive(game_state, [], [], [], heuristic)

    return utils.extract_solution(solution)

  @staticmethod
  def recursive(game_state, prev_state, visited_state, solution, heuristic):
    next_possible_states = utils.get_possible_next_states_path(game_state)
    optimal_value = -1000
    optimal_state = None

    if game_state.result == GameResults.Win: return []

    for next_state in next_possible_states:
      heuristic_value = heuristic.calculate(next_state[0][0])
      if heuristic_value > optimal_value and (next_state[0][0].board not in visited_state):
        optimal_state = next_state[0]
        optimal_value = heuristic_value
    
    if optimal_state != None:
      prev_state.append(game_state)
      solution.append(optimal_state)
      Greedy.recursive(optimal_state[0], prev_state, visited_state, solution, heuristic)
    else:
      visited_state.append(game_state.board)
      prev = prev_state.pop()
      solution.pop()
      Greedy.recursive(prev, prev_state, visited_state, solution, heuristic)

    return solution
