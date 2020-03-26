from src.heuristic import Heuristic
from src.board import BOARD_HEIGHT, BOARD_WIDTH
from src.bubble import Bubble
from src.bubble_types import BubbleTypes
import src.utils as utils

DEFAULT_VALUE = 2
PENALTY = 1


class MoveNotOnExtremeties(Heuristic):
    @staticmethod
    def calculate(game_state):
        board_matrix = game_state[0][0].board.matrix
        move = game_state[0][1]

        value = DEFAULT_VALUE

        if move[0] == len(board_matrix) - 1 or move[0] == 0:
            value -= PENALTY

        if move[1] == len(board_matrix[move[0]]) - 1 or move[1] == 0:
            value -= PENALTY

        return value
