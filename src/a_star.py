from src.search_algorithm import SearchAlgorithm
from src.game_results import GameResults
from src.score_heuristic import Score
from src.bubbles_left_heuristic import BubblesLeft
import src.utils as utils


class AStar(SearchAlgorithm):
    @staticmethod
    def execute(game_state, heuristic):
        solution = AStar.algorithm(game_state, heuristic)

        return utils.extract_solution(solution)

    @staticmethod
    def algorithm(game_state, heuristic):
        stack = utils.get_possible_next_states_path(game_state)
        state = [(game_state, None)]
        solution = []
        visited_states = []

        while state[-1][0].result != GameResults.Win:
            optimal_value = -1000
            optimal_state = None

            for next_state in stack:
                value = Score.calculate(next_state[0][0]) + heuristic.calculate(
                    next_state
                )
                if value > optimal_value and (
                    next_state[0][0].board.matrix not in visited_states
                ):
                    optimal_state = next_state[0]
                    optimal_value = value

            if optimal_state != None:
                stack = utils.get_possible_next_states_path(optimal_state[0])
                state.append(optimal_state)
            else:
                visited_states.append(state[-1][0].board.matrix)
                state.pop()
                stack = utils.get_possible_next_states_path(state[-1][0])

        state.pop(0)
        return state
