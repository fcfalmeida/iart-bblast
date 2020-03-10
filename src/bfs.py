from src.search_algorithm import SearchAlgorithm
from src.game_results import GameResults
from copy import deepcopy
import src.utils as utils

# https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
class BFS(SearchAlgorithm):
  @staticmethod
  def execute(game_state):
    queue = get_possible_next_states_path(game_state)
    max_touches = game_state.touches_left

    while queue:
      solution = queue.pop(0)
      state, move = solution[-1]

      if state.result == GameResults.Win: return extract_solution(solution)

      next_possible_states = get_possible_next_states(state)

      for next_state in next_possible_states:
        new_solution = list(solution)
        new_solution.append(next_state)
        queue.append(new_solution)
       
    return []

# returns the next possible states of a given game state
# wrapped in a list
def get_possible_next_states_path(game_state):
  next_states = []
  possible_moves = game_state.valid_moves()
  
  for move in possible_moves:
    state = get_next_state(game_state, move)
    next_states.append([(state, move)]) # the state and the move that caused it

  return next_states

# returns the next possible states of a given game state
def get_possible_next_states(game_state):
  next_states = []
  possible_moves = game_state.valid_moves()
  
  for move in possible_moves:
    state = get_next_state(game_state, move)
    next_states.append((state, move)) # the state and the move that caused it

  return next_states

def get_next_state(game_state, move):
  move_row, move_col = move
  game_state_cpy = deepcopy(game_state)

  game_state_cpy.update_board(move_row, move_col)

  return game_state_cpy

def extract_solution(solution):
  moves = []

  for state, move in solution:
    moves.append(move)

  return moves