from src.search_algorithm import SearchAlgorithm
from src.game_results import GameResults
import src.utils as utils

class UCS(SearchAlgorithm):
    @staticmethod
    def execute(game_state, heuristic = None):
        stack = utils.get_possible_next_states_path(game_state)
        max_touches = game_state.touches_left
        stack.sort(key=utils.helper_sort, reverse=True)
        
        while stack:
            solution = stack.pop()
            state, move = solution[-1]

            if state.result == GameResults.Win: return utils.extract_solution(solution)

            next_possible_states = utils.get_possible_next_states(state)

            for next_state in next_possible_states:

                new_solution = list(solution)
                new_solution.append(next_state)
                stack.append(new_solution)
                stack.sort(key=utils.helper_sort)

        return []

