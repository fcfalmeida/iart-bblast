from src.heuristic import Heuristic
from src.board import BOARD_HEIGHT, BOARD_WIDTH
from src.bubble import Bubble
from src.bubble_types import BubbleTypes
import src.utils as utils


class BubblesNotOnExtremeties(Heuristic):
    @staticmethod
    def calculate(game_state):
        board_matrix = game_state[0][0].board.matrix
        borders = utils.get_matrix_borders(board_matrix)

        borders = list(
            filter(lambda bubble: bubble != Bubble(BubbleTypes.Empty), borders)
        )

        value = BOARD_WIDTH * BOARD_HEIGHT - len(borders)

        return value

