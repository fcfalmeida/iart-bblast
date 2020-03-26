from src.search_algorithm import SearchAlgorithm
from src.game_results import GameResults
import src.utils as utils


class IDepth(SearchAlgorithm):
    @staticmethod
    def execute(game_state, heuristic=None):
        max_level_search = game_state.touches_left
        nice_copy = game_state
        for max_numb in range(max_level_search):
            nice_copy.touches_left = max_numb + 1
            stack = utils.get_possible_next_states_path(nice_copy)

            while stack:
                solution = stack.pop()
                state, move = solution[-1]

                if state.result == GameResults.Win: return utils.extract_solution(solution)

                next_possible_states = utils.get_possible_next_states(state)

                for next_state in next_possible_states:
                    new_solution = list(solution)
                    new_solution.append(next_state)
                    stack.append(new_solution)

        return []