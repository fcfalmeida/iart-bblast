from src.heuristic import Heuristic
from src.board import BOARD_HEIGHT, BOARD_WIDTH
from src.bubble import Bubble
from src.bubble_types import BubbleTypes
import src.utils as utils


class AdjacentBubbles(Heuristic):
    @staticmethod
    def calculate(game_state):
        matrix = game_state[0][0].board.matrix
        value = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                numberOfRedAdjacentBubbles = 0
                if j > 0 and matrix[i][j - 1].type == BubbleTypes.Red:
                    numberOfRedAdjacentBubbles += 1
                if j < len(matrix[i]) - 1 and matrix[i][j + 1].type == BubbleTypes.Red:
                    numberOfRedAdjacentBubbles += 1
                if i > 0 and matrix[i - 1][j].type == BubbleTypes.Red:
                    numberOfRedAdjacentBubbles += 1
                if i < len(matrix) - 1 and matrix[i + 1][j].type == BubbleTypes.Red:
                    numberOfRedAdjacentBubbles += 1
                if numberOfRedAdjacentBubbles >= matrix[i][j].current_hp():
                    value += 1

        return value
