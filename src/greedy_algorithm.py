from src.search_algorithm import SearchAlgorithm
from src.game_results import GameResults
import src.utils as utils

class Greedy(SearchAlgorithm):
  @staticmethod
  def execute(game_state, heuristic):
    #solution = Greedy.recursive(game_state, [], [], [], heuristic)
    solution = Greedy.algorithm(game_state, heuristic)

    return utils.extract_solution(solution)

  @staticmethod
  def algorithm(game_state, heuristic):
    stack = utils.get_possible_next_states_path(game_state)
    state = [(game_state, None)]
    solution = []
    visited_states = []

    while(state[-1][0].result != GameResults.Win):
      optimal_value = -1000
      optimal_state = None

      for next_state in stack:
        heuristic_value = heuristic.calculate(next_state[0][0])
        if heuristic_value > optimal_value and (next_state[0][0].board.matrix not in visited_states):
          optimal_state = next_state[0]
          optimal_value = heuristic_value

      if optimal_state != None:
        stack = utils.get_possible_next_states_path(optimal_state[0])
        state.append(optimal_state)
      else:
        visited_states.append(state[-1][0].board.matrix)
        state.pop()
        stack = utils.get_possible_next_states_path(state[-1][0])

    state.pop(0)
    return state
