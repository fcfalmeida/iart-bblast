from src.bubbles_not_on_extremeties_heuristic import BubblesNotOnExtremeties
from src.adjacent_bubbles_heuristic import AdjacentBubbles
from src.move_not_on_extremeties_heuristic import MoveNotOnExtremeties

aStarHeuristics = {
    1: ("Number of bubbles on the extremities", BubblesNotOnExtremeties),
    2: ("Number of red adjacent bubbles", AdjacentBubbles),
    3: ("Move on extremity", MoveNotOnExtremeties),
}
